# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import json
import os

import os
import json

from util import manhattanDistance
from game import Directions
import random, util, time, statistics

from game import Agent
from pacman import GameState



class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        

        """ On https://pacman.fandom.com/wiki/Point_Configurations we can see the following
        point distribution which I'm gonna use to make my evaluationFunction.
        Pac-Dot = 10 Pts
        1st Ghost = 200 Pts
        2nd Ghost = 400 Pts
        3rd Ghost = 800 Pts
        4th Ghost = 1600 Pts"""

        dead_ghosts = 0
        total_score = 0
        # If the next state is a win state then return infinity in order to "show" that is a good move.
        if successorGameState.isWin():
            return float("inf")
        # If the next state is a win state then return -infinity in order to "show" that is a bad move.
        if successorGameState.isLose():
            return float("-inf")
        # Calculates the manhattanDistance from next pacman's position to all foods and take the minimum one.
        # Divide 10 by that distance and then add it to total_score.
        food_distances = {food: util.manhattanDistance(newPos, food) for food in newFood.asList()}
        food, min_food_dist = min(food_distances.items(), key=lambda data: data[1])
        total_score += 10 / (min_food_dist + 1e-10)  # Add a small epsilon to avoid division by zero
        
        # For every ghost in the next game state calculates the distance from pacman.
        # Ιf there is a ghost whose distance is less than 2 so it is close to the pacman then it checks if it is scared 
        # Αnd acts accordingly by returning -infinity if it is not to "show" that he will die or 200*2^number of dead ghosts.
        for i in range(len(successorGameState.getGhostPositions())):
            if util.manhattanDistance(newPos, successorGameState.getGhostPositions()[i]) < 2:
                if newScaredTimes[i] != 0:
                    total_score += 200 * (2 ** dead_ghosts)
                    dead_ghosts += 1
                else:
                    return float("-inf")
        # Return the result.
        return successorGameState.getScore() + total_score


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):  # penjelasan sudah ada dalam Agent_explanation.txt
    """
    Your minimax agent (question 2)
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        super().__init__(evalFn, depth)
        self.survival_steps = 0
        self.nodes_expanded = 0
        self.total_nodes_expanded = 0
        self.total_decision_time_ms = 0.0
        self.episode_survival_steps = []
        self.episode_total_nodes = []
        self.episode_avg_nodes = []
        self.episode_avg_time_ms = []
        self.current_game_nodes = 0
        self.current_game_time_ms = 0.0
        self.episode_active = False

    def minimax_decision(self, depth, agentIndex, gameState: GameState):
        self.nodes_expanded += 1
        # If all agents has play increase depth and return to pacman.
        if agentIndex == gameState.getNumAgents():
            depth += 1
            agentIndex = 0
        # Check if the resursion has come to an end.
        if self.depth == depth or gameState.isWin() or gameState.isLose():
            return [self.evaluationFunction(gameState), None]
        # If the agent is the pacman.
        if agentIndex == 0:
            # Initialize the value and the action
            v, v_action = float("-inf"), None
            for action in gameState.getLegalActions(agentIndex):
                # Take the new value.
                v_new = self.minimax_decision(depth, agentIndex + 1, gameState.generateSuccessor(agentIndex, action))[0]
                # Change the new value and the action only if the new value is greater.
                if v_new > v or v_action is None:
                    v = v_new
                    v_action = action
            # Return the result.
            return [v, v_action]
        # If the agent is a ghost.
        else:
            # Initialize the value and the action.
            v, v_action = float("inf"), None
            for action in gameState.getLegalActions(agentIndex):
                # Take the new value.
                v_new = self.minimax_decision(depth, agentIndex + 1, gameState.generateSuccessor(agentIndex, action))[0]
                # Change the new value and the action only if the new value is smaller.
                if v_new < v or v_action is None:
                    v = v_new
                    v_action = action
            # Return the result.
            return [v, v_action]

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        if not self.episode_active:
            self.survival_steps = 0
            self.current_game_nodes = 0
            self.current_game_time_ms = 0.0
            self.episode_active = True

        self.nodes_expanded = 0
        start_time = time.time()
        action = self.minimax_decision(0, 0, gameState)[1]
        elapsed_ms = (time.time() - start_time) * 1000.0
        self.current_game_nodes += self.nodes_expanded
        self.current_game_time_ms += elapsed_ms
        self.survival_steps += 1
        return action

    def final(self, state):
        episode_steps = self.survival_steps
        episode_nodes = self.current_game_nodes
        episode_avg_nodes = episode_nodes / episode_steps if episode_steps else 0.0
        episode_avg_time = self.current_game_time_ms / episode_steps if episode_steps else 0.0

        self.episode_survival_steps.append(episode_steps)
        self.episode_total_nodes.append(episode_nodes)
        self.episode_avg_nodes.append(episode_avg_nodes)
        self.episode_avg_time_ms.append(episode_avg_time)

        self.total_nodes_expanded += episode_nodes
        self.total_decision_time_ms += self.current_game_time_ms

        mean_steps = statistics.mean(self.episode_survival_steps)
        stdev_steps = statistics.stdev(self.episode_survival_steps) if len(self.episode_survival_steps) > 1 else 0.0
        mean_nodes = statistics.mean(self.episode_total_nodes)
        stdev_nodes = statistics.stdev(self.episode_total_nodes) if len(self.episode_total_nodes) > 1 else 0.0
        mean_avg_nodes = statistics.mean(self.episode_avg_nodes)
        stdev_avg_nodes = statistics.stdev(self.episode_avg_nodes) if len(self.episode_avg_nodes) > 1 else 0.0
        mean_avg_time = statistics.mean(self.episode_avg_time_ms)
        stdev_avg_time = statistics.stdev(self.episode_avg_time_ms) if len(self.episode_avg_time_ms) > 1 else 0.0

        print(f"SUMMARY {self.__class__.__name__} EpisodeSurvivalSteps={episode_steps} EpisodeTotalNodesExpanded={episode_nodes} EpisodeAvgNodesExpandedPerStep={episode_avg_nodes:.2f} EpisodeAvgComputationTimeMs={episode_avg_time:.2f}")
        print(f"AGGREGATE {self.__class__.__name__} Episodes={len(self.episode_survival_steps)} MeanSurvivalSteps={mean_steps:.2f} StdDevSurvivalSteps={stdev_steps:.2f} MeanTotalNodesExpanded={mean_nodes:.2f} StdDevTotalNodesExpanded={stdev_nodes:.2f} MeanAvgNodesExpandedPerStep={mean_avg_nodes:.2f} StdDevAvgNodesExpandedPerStep={stdev_avg_nodes:.2f} MeanAvgComputationTimeMs={mean_avg_time:.2f} StdDevAvgComputationTimeMs={stdev_avg_time:.2f}")

        # Reset per-game counters for the next episode
        self.survival_steps = 0
        self.current_game_nodes = 0
        self.current_game_time_ms = 0.0
        self.episode_active = False


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        super().__init__(evalFn, depth)
        self.survival_steps = 0
        self.nodes_expanded = 0
        self.total_nodes_expanded = 0
        self.total_decision_time_ms = 0.0
        self.episode_survival_steps = []
        self.episode_total_nodes = []
        self.episode_avg_nodes = []
        self.episode_avg_time_ms = []
        self.current_game_nodes = 0
        self.current_game_time_ms = 0.0
        self.episode_active = False

    def alpha_beta_search(self, alpha, beta, depth, agentIndex, gameState: GameState):
        self.nodes_expanded += 1
        # If all agents has play increase depth and return to pacman.
        if agentIndex == gameState.getNumAgents():
            depth += 1
            agentIndex = 0
        # Check if the resursion has come to an end.
        if self.depth == depth or gameState.isWin() or gameState.isLose():
            return [self.evaluationFunction(gameState), None]
        # If the agent is the pacman.
        if agentIndex == 0:
            # Initialize the value and the action
            v, v_action = float("-inf"), None
            for action in gameState.getLegalActions(agentIndex):
                # Take the new value.
                v_new = self.alpha_beta_search(alpha, beta, depth, agentIndex + 1,
                                               gameState.generateSuccessor(agentIndex, action))[0]
                # Change the new value and the action only if the new value is greater.
                if v_new > v or v_action is None:
                    v = v_new
                    v_action = action
                # Checks if it needs to stop and return.
                if v > beta:
                    return [v, v_action]
                # Find new alpha
                alpha = max(alpha, v)
            # Return the result.
            return [v, v_action]
        else:
            # Initialize the value and the action
            v, v_action = float("inf"), None
            for action in gameState.getLegalActions(agentIndex):
                # Take the new value.
                v_new = self.alpha_beta_search(alpha, beta, depth, agentIndex + 1,
                                               gameState.generateSuccessor(agentIndex, action))[0]
                # Change the new value and the action only if the new value is smaller.
                if v_new < v or v_action is None:
                    v = v_new
                    v_action = action
                # Checks if it needs to stop and return.
                if v < alpha:
                    return [v, v_action]
                # Find new beta
                beta = min(beta, v)
            # Return the result.
            return [v, v_action]

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        if not self.episode_active:
            self.survival_steps = 0
            self.current_game_nodes = 0
            self.current_game_time_ms = 0.0
            self.episode_active = True

        self.nodes_expanded = 0
        start_time = time.time()
        action = self.alpha_beta_search(float("-inf"), float("inf"), 0, 0, gameState)[1]
        elapsed_ms = (time.time() - start_time) * 1000.0
        self.current_game_nodes += self.nodes_expanded
        self.current_game_time_ms += elapsed_ms
        self.survival_steps += 1
        return action

    def final(self, state):
        episode_steps = self.survival_steps
        episode_nodes = self.current_game_nodes
        episode_avg_nodes = episode_nodes / episode_steps if episode_steps else 0.0
        episode_avg_time = self.current_game_time_ms / episode_steps if episode_steps else 0.0

        self.episode_survival_steps.append(episode_steps)
        self.episode_total_nodes.append(episode_nodes)
        self.episode_avg_nodes.append(episode_avg_nodes)
        self.episode_avg_time_ms.append(episode_avg_time)

        mean_steps = statistics.mean(self.episode_survival_steps)
        stdev_steps = statistics.stdev(self.episode_survival_steps) if len(self.episode_survival_steps) > 1 else 0.0
        mean_nodes = statistics.mean(self.episode_total_nodes)
        stdev_nodes = statistics.stdev(self.episode_total_nodes) if len(self.episode_total_nodes) > 1 else 0.0
        mean_avg_nodes = statistics.mean(self.episode_avg_nodes)
        stdev_avg_nodes = statistics.stdev(self.episode_avg_nodes) if len(self.episode_avg_nodes) > 1 else 0.0
        mean_avg_time = statistics.mean(self.episode_avg_time_ms)
        stdev_avg_time = statistics.stdev(self.episode_avg_time_ms) if len(self.episode_avg_time_ms) > 1 else 0.0

        print(f"SUMMARY {self.__class__.__name__} EpisodeSurvivalSteps={episode_steps} EpisodeTotalNodesExpanded={episode_nodes} EpisodeAvgNodesExpandedPerStep={episode_avg_nodes:.2f} EpisodeAvgComputationTimeMs={episode_avg_time:.2f}")
        print(f"AGGREGATE {self.__class__.__name__} Episodes={len(self.episode_survival_steps)} MeanSurvivalSteps={mean_steps:.2f} StdDevSurvivalSteps={stdev_steps:.2f} MeanTotalNodesExpanded={mean_nodes:.2f} StdDevTotalNodesExpanded={stdev_nodes:.2f} MeanAvgNodesExpandedPerStep={mean_avg_nodes:.2f} StdDevAvgNodesExpandedPerStep={stdev_avg_nodes:.2f} MeanAvgComputationTimeMs={mean_avg_time:.2f} StdDevAvgComputationTimeMs={stdev_avg_time:.2f}")

        # Reset per-game counters for the next episode
        self.survival_steps = 0
        self.current_game_nodes = 0
        self.current_game_time_ms = 0.0
        self.episode_active = False


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        super().__init__(evalFn, depth)
        self.survival_steps = 0
        self.nodes_expanded = 0
        self.total_nodes_expanded = 0
        self.total_decision_time_ms = 0.0
        self.episode_survival_steps = []
        self.episode_total_nodes = []
        self.episode_avg_nodes = []
        self.episode_avg_time_ms = []
        self.current_game_nodes = 0
        self.current_game_time_ms = 0.0
        self.episode_active = False

    def expectimax_decision(self, depth, agentIndex, gameState: GameState):
        self.nodes_expanded += 1
        # If all agents has play increase depth and return to pacman.
        if agentIndex == gameState.getNumAgents():
            depth += 1
            agentIndex = 0
        # Check if the resursion has come to an end.
        if self.depth == depth or gameState.isWin() or gameState.isLose():
            return [self.evaluationFunction(gameState), None]
        # If the agent is the pacman.
        if agentIndex == 0:
            # Initialize the value and the action
            v, v_action = float("-inf"), None
            for action in gameState.getLegalActions(agentIndex):
                # Take the new value.
                v_new = \
                    self.expectimax_decision(depth, agentIndex + 1, gameState.generateSuccessor(agentIndex, action))[0]
                # Change the new value and the action only if the new value is greater.
                if v_new > v or v_action is None:
                    v = v_new
                    v_action = action
            # Return the result.
            return [v, v_action]
        # If the agent is a ghost.
        else:
            # Initialize sum.
            v = 0
            for action in gameState.getLegalActions(agentIndex):
                # Increase the sum.
                v += self.expectimax_decision(depth, agentIndex + 1, gameState.generateSuccessor(agentIndex, action))[0]
            # Return the result as the average of the sum.
            return [v / len(gameState.getLegalActions(agentIndex)), None]

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        if not self.episode_active:
            self.survival_steps = 0
            self.current_game_nodes = 0
            self.current_game_time_ms = 0.0
            self.episode_active = True

        self.nodes_expanded = 0
        start_time = time.time()
        action = self.expectimax_decision(0, 0, gameState)[1]
        elapsed_ms = (time.time() - start_time) * 1000.0
        self.current_game_nodes += self.nodes_expanded
        self.current_game_time_ms += elapsed_ms
        self.survival_steps += 1
        return action

    def final(self, state):
        episode_steps = self.survival_steps
        episode_nodes = self.current_game_nodes
        episode_avg_nodes = episode_nodes / episode_steps if episode_steps else 0.0
        episode_avg_time = self.current_game_time_ms / episode_steps if episode_steps else 0.0

        self.episode_survival_steps.append(episode_steps)
        self.episode_total_nodes.append(episode_nodes)
        self.episode_avg_nodes.append(episode_avg_nodes)
        self.episode_avg_time_ms.append(episode_avg_time)

        mean_steps = statistics.mean(self.episode_survival_steps)
        stdev_steps = statistics.stdev(self.episode_survival_steps) if len(self.episode_survival_steps) > 1 else 0.0
        mean_nodes = statistics.mean(self.episode_total_nodes)
        stdev_nodes = statistics.stdev(self.episode_total_nodes) if len(self.episode_total_nodes) > 1 else 0.0
        mean_avg_nodes = statistics.mean(self.episode_avg_nodes)
        stdev_avg_nodes = statistics.stdev(self.episode_avg_nodes) if len(self.episode_avg_nodes) > 1 else 0.0
        mean_avg_time = statistics.mean(self.episode_avg_time_ms)
        stdev_avg_time = statistics.stdev(self.episode_avg_time_ms) if len(self.episode_avg_time_ms) > 1 else 0.0

        print(f"SUMMARY {self.__class__.__name__} EpisodeSurvivalSteps={episode_steps} EpisodeTotalNodesExpanded={episode_nodes} EpisodeAvgNodesExpandedPerStep={episode_avg_nodes:.2f} EpisodeAvgComputationTimeMs={episode_avg_time:.2f}")
        print(f"AGGREGATE {self.__class__.__name__} Episodes={len(self.episode_survival_steps)} MeanSurvivalSteps={mean_steps:.2f} StdDevSurvivalSteps={stdev_steps:.2f} MeanTotalNodesExpanded={mean_nodes:.2f} StdDevTotalNodesExpanded={stdev_nodes:.2f} MeanAvgNodesExpandedPerStep={mean_avg_nodes:.2f} StdDevAvgNodesExpandedPerStep={stdev_avg_nodes:.2f} MeanAvgComputationTimeMs={mean_avg_time:.2f} StdDevAvgComputationTimeMs={stdev_avg_time:.2f}")

        # Reset per-game counters for the next episode
        self.survival_steps = 0
        self.current_game_nodes = 0
        self.current_game_time_ms = 0.0
        self.episode_active = False


def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    kita ganti angka 50 dengan 5 (power pellet) dan 10 menjadi 1 (food) pada fungsi heuristic bagian deterominator untuk mencegah stuck karena agen bimbang.
    """
    

    """ On https://pacman.fandom.com/wiki/Point_Configurations we can see the following
    point distribution which im gonna use to make my evaluationFunction and the betterEvaluationFunction.
    Pac-Dot = 10 Pts
    Power Pellet = 50 Pts
    1st Ghost = 200 Pts
    2nd Ghost = 400 Pts
    3rd Ghost = 800 Pts
    4th Ghost = 1600 Pts
    I'm also gonna add a -1 pts for every second the pacman does not move. The idea was taken by the current pacman implementation
    where i spotted this when i was playing the game with the command python3 pacman.py (DIBATALKAN)
    'Stop' = -1 Pts """

    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    dead_ghosts = 0
    total_score = 0
    # If the next state is a win state then return infinity in order to "show" that is a good move.
    if currentGameState.isWin():
        return float("inf")
    # If the next state is a win state then return -infinity in order to "show" that is a bad move.
    if currentGameState.isLose():
        return float("-inf")
    # Calculates the manhattanDistance from next pacman's position to all foods and take the minimum one.
    # If there is no food left, skip the food-based contribution.
    food_list = newFood.asList()
    if food_list:
        food_distances = {food: util.manhattanDistance(newPos, food) for food in food_list}
        _, min_food_dist = min(food_distances.items(), key=lambda data: data[1])
        total_score += 1.0 / (min_food_dist + 1e-10)
    # Decreasing the total score by -1 for every Stop action it finds.
    # total_score -= (-1) * currentGameState.getLegalActions().count('Stop')
    # Get the list with pellet.
    pellet_list = currentGameState.getCapsules()
    # Checks if the pellet list has at least one pellet.
    if pellet_list:
        # Calculates the manhattanDistance from next pacman's position to all pellets and take the minimum one.
        # Divide 50 by that distance and then add it to total_score.
        pellet_distances = {pellet: util.manhattanDistance(newPos, pellet) for pellet in pellet_list}
        pellet, min_pellet_dist = min(pellet_distances.items(), key=lambda data: data[1])
        total_score += 5.0 / min_pellet_dist
    # For every ghost in the next game state calculates the distance from pacman.
    # Ιf there is a ghost whose distance is less than 2 so it is close to the pacman then it checks if it is scared. 
    # Αnd acts accordingly by dividing the total score in half if it is not to "show" that he will die.
    # Or 200*2^number of dead ghosts.
    # Evaluasi Hantu dengan Gradien Kontinu
    for i in range(len(currentGameState.getGhostPositions())):
        ghost_dist = util.manhattanDistance(newPos, currentGameState.getGhostPositions()[i])
        
        # Jika hantu sedang takut (scared)
        if newScaredTimes[i] > 0:
            # GRADIEN BERBURU: Tidak ada lagi batasan < 2.
            # Dari jarak 10 petak pun, Pac-Man sudah merasakan "tarikan magnet" +200 ini.
            total_score += 200.0 / (ghost_dist + 1)
        else:
            # Jika hantu normal dan jaraknya mematikan (< 2)
            if ghost_dist < 2:
                return float("-inf") # Insting mutlak: LARI!
    # Return the result.
    return currentGameState.getScore() + total_score




class FeatureExtractor:
    """
    
    Modul ekstraksi fitur ini mentransformasikan ruang state yang berdimensi tinggi
    menjadi representasi vektor berdimensi rendah. Sesuai kesepakatan desain,
    kita mengimplementasikan fitur berbobot jarak dengan normalisasi invers.
    
    Trade-off: Ekstraksi ini memanggil `state.generateSuccessor(0, action)`. Secara teoritis, 
    pada RL model-free murni, agen tidak boleh memiliki fungsi prediksi state. 
    Namun untuk stabilitas kalkulasi jarak di framework ini, simulasi 1-langkah diizinkan.
    """
    def bfs_closest_distance(self, start_pos, target_positions, walls):
        """
        
        Fungsi pencarian jarak terpendek menggunakan algoritma pencarian melebar (BFS).
        Alih-alih mencari rute ke setiap target (yang berbiaya besar), 
        kita menyebar dari posisi awal dan berhenti pada target pertama yang ditemukan.
        
        Asumsi: Titik koordinat harus berupa integer agar sepadan dengan indeks matriks dinding.
        """
        if not target_positions:
            return None
        
        # Konversi struktur data ke Set untuk lookup O(1)
        target_set = set(target_positions)
        
        if start_pos in target_set:
            return 0.0

        # Antrean untuk menampung (koordinat_x, koordinat_y, jarak_kumulatif)
        queue = util.Queue()
        queue.push((start_pos, 0.0))
        visited = set()
        visited.add(start_pos)

        while not queue.isEmpty():
            current_pos, dist = queue.pop()
            x, y = current_pos

            # Ekspansi ke 4 arah mata angin (Utara, Selatan, Timur, Barat)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = int(x + dx), int(y + dy)
                next_pos = (next_x, next_y)

                # Syarat ekspansi: bukan tembok dan belum pernah dikunjungi
                if not walls[next_x][next_y] and next_pos not in visited:
                    if next_pos in target_set:
                        return dist + 1.0 # Target terdekat ditemukan!
                    
                    visited.add(next_pos)
                    queue.push((next_pos, dist + 1.0))
        
        # Skenario ekstrim: target sepenuhnya tertutup tembok (unreachable)
        return None
    
    def get_features(self, state, action):
        features = util.Counter()
        # Menggunakan index 0 untuk Pac-Man
        successor = state.generateSuccessor(0, action)
        new_pos = successor.getPacmanPosition()

        # 1. Fitur f1: Jarak ke makanan kecil terdekat
        new_food = successor.getFood().asList()
        if len(new_food) > 0:
            min_food_dist = min([util.manhattanDistance(new_pos, food) for food in new_food])
            # Normalisasi menggunakan invers: 1 / (d + 1)
            features["f1_closest_food"] = 1.0 / (min_food_dist + 1.0)
        else:
            features["f1_closest_food"] = 0.0

        # Evaluasi Pemisahan Status Hantu (Menggabungkan f2, f4, f5)
        # Logika Non-Linear: Mencegah agen mati konyol saat waktu scared habis.
        ghost_states = successor.getGhostStates()
        active_ghosts = []
        scared_ghosts = []

        for ghost in ghost_states:
            # Normalisasi koordinat: Posisi hantu bisa berupa float jika sedang melayang
            # di antara blok. Kita wajib membulatkannya ke integer terdekat.
            gx, gy = ghost.getPosition()
            ghost_grid_pos = (int(gx + 0.5), int(gy + 0.5))

            if ghost.scaredTimer < 2:
                active_ghosts.append(ghost_grid_pos)
            else:
                scared_ghosts.append(ghost_grid_pos)

        # 2. Fitur f2: Jarak ke hantu aktif / berbahaya
        if active_ghosts:
            min_active_ghost_dist = min([util.manhattanDistance(new_pos, g_pos) for g_pos in active_ghosts])
            features["f2_active_ghost"] = 1.0 / (min_active_ghost_dist + 1.0)
        else:
            features["f2_active_ghost"] = 0.0

        # 3. Fitur f3: Indikator Jalan Buntu
        # Aproksimasi heuristik: Jika jumlah langkah legal di state berikutnya <= 1, 
        # artinya Pac-Man hanya bisa mundur (terjebak).
        next_legal_actions = successor.getLegalActions(0)
        if len(next_legal_actions) <= 1:
            features["f3_dead_end"] = 1.0
        else:
            features["f3_dead_end"] = 0.0

        # 4. Fitur f4: Jarak ke hantu yang sedang takut (Peluang makan)
        if scared_ghosts:
            min_scared_ghost_dist = min([util.manhattanDistance(new_pos, g_pos) for g_pos in scared_ghosts])
            features["f4_scared_ghost"] = 1.0 / (min_scared_ghost_dist + 1.0)
        else:
            features["f4_scared_ghost"] = 0.0

        # 5. Fitur f6: Jarak ke Power Pellet (Kapsul) terdekat
        capsules = successor.getCapsules()
        if len(capsules) > 0:
            min_capsule_dist = min([util.manhattanDistance(new_pos, cap) for cap in capsules])
            features["f6_capsule"] = 1.0 / (min_capsule_dist + 1.0)
        else:
            features["f6_capsule"] = 0.0

        # Bias Feature: Berfungsi selayaknya nilai intersep pada regresi linear.
        # Membantu menstabilkan perhitungan ketika semua fitur lain bernilai 0.
        features["bias"] = 1.0

        return features


class ApproximateQAgent(Agent):
    """
    
    Agen Approximate Q-Learning. 
    Nilai Q dihitung secara linear: Q(s,a) = sum_i(w_i * f_i(s,a))
    Pembaruan bobot (w) menggunakan metode Temporal Difference (TD) learning.
    """
    def __init__(self, alpha=0.2, discount=0.8, epsilon=0.05, **kwargs):
        super().__init__()
        self.index = 0 
        self.alpha = float(alpha)
        self.discount = float(discount)
        self.epsilon = float(epsilon)
        
        # [EDIT] Tangkap batasan training dari terminal
        self.numTraining = int(kwargs.get('numTraining', 0))
        self.episodesSoFar = 0 
        
        self.weights = util.Counter() 
        self.extractor = FeatureExtractor() 
        self.lastState = None
        self.lastAction = None

        # util.Counter() memungkinkan manipulasi aljabar linear sederhana
        # self.weights = util.Counter() 
        # self.extractor = FeatureExtractor() 

        # [MODIFIKASI] Memori jangka pendek untuk menghitung Temporal Difference
        self.lastState = None
        self.lastAction = None

        # [MODIFIKASI] Memuat memori saat agen dilahirkan
        self.model_path = "pacman_weights.json"
        self.load_weights()

    def load_weights(self):
        """
        
        Membaca matriks bobot dari sistem berkas.
        Fungsi ini memungkinkan transfer learning: jika agen pernah dilatih, 
        ia akan memuat pengalamannya. Jika belum, ia mulai dari nol.
        """
        if os.path.exists(self.model_path):
            with open(self.model_path, "r") as file:
                loaded_dict = json.load(file)
                # Rekonstruksi dictionary standar kembali ke util.Counter
                for key, value in loaded_dict.items():
                    self.weights[key] = float(value)
            print(f"Model berhasil dimuat dari {self.model_path}.")
            
            # Asumsi logis: Jika model sudah ada, agen diasumsikan sudah cukup pintar.
            # Kita secara otomatis menekan epsilon agar agen lebih fokus eksploitasi
            # daripada melakukan eksplorasi acak seperti agen baru.
            self.epsilon = max(0.01, self.epsilon * 0.5) 
        else:
            print("model_weights.json tidak ditemukan. Agen memulai dengan bobot nol dan epsilon default.")
    def save_weights(self):
        """
        
        Serialisasi matriks bobot ke format JSON.
        Disimpan dalam bentuk hirarki agar mudah diaudit secara visual
        oleh peneliti data sains.
        """
        weights_dict = dict(self.weights)
        with open(self.model_path, "w") as file:
            json.dump(weights_dict, file, indent=4)


    def registerInitialState(self, state):
        """
        
        Fungsi bawaan Agent yang pasti dipanggil di awal setiap episode.
        Kita menggunakan ini sebagai 'garbage collector' untuk memproses
        terminal state (kematian) dari episode sebelumnya yang tertelan oleh 
        pemutusan paksa framework.
        """
        if self.lastState is not None:
            # Karena ini mode endless (kematian adalah satu-satunya jalan keluar),
            # kita asumsikan mutlak bahwa transisi terakhir adalah kematian.
            terminal_reward = -500.0
            
            # Kalkulasi Temporal Difference Error khusus terminal state.
            # Nilai masa depan (discount * max_Q) adalah 0 karena agen mati.
            q_val = self.get_q_value(self.lastState, self.lastAction)
            difference = terminal_reward - q_val
            
            # Pembaruan bobot retroaktif
            features = self.extractor.get_features(self.lastState, self.lastAction)
            for feature_name, feature_value in features.items():
                self.weights[feature_name] += self.alpha * difference * feature_value
                
        # Reset memori jangka pendek untuk mulai episode baru
        self.lastState = None
        self.lastAction = None
        
        # [EDIT] Transisi dari Fase Belajar ke Fase Ujian
        self.episodesSoFar += 1
        
        # Jika jumlah game sudah melampaui batas training (contoh: masuk game ke-101)
        if self.episodesSoFar > self.numTraining:
            # Matikan sifat acak! Agen 100% menggunakan ilmunya (Eksploitasi Mutlak)
            self.epsilon = 0.0 
            # Kunci otaknya! Agen tidak lagi memodifikasi bobot (Berhenti Belajar)
            self.alpha = 0.0

        # [PENTING] Decaying Epsilon
        # Menurunkan tingkat eksplorasi secara bertahap setiap episode baru.
        # Ini menjawab masalah mengapa di -n 100 agen tidak tambah pintar.
        # Agen harus beralih dari fase 'coba-coba' menjadi 'eksploitasi ilmu'.
        if self.epsilon > 0.01:
            self.epsilon *= 0.95

        self.save_weights()        
        
    def observationFunction(self, state):
        """
        
        Fungsi ini dipanggil oleh framework setiap kali agen menerima state baru, 
        TETAPI SEBELUM agen diminta mengambil tindakan (getAction).
        Di sinilah kita memiliki s (lastState), a (lastAction), dan s' (state saat ini).
        """
        # Jika ini bukan langkah pertama permainan
        if self.lastState is not None:
            # Kalkulasi reward: Selisih skor saat ini dengan skor masa lalu
            reward = state.getScore() - self.lastState.getScore()
            # Picu pembelajaran!
            self.update(self.lastState, self.lastAction, state, reward)
        return state

    def getAction(self, state):
        """
        
        Kebijakan epsilon-greedy yang kini diperbarui untuk merekam tindakan ke memori.
        """
        legal_actions = state.getLegalActions(self.index)
        if not legal_actions:
            return None

        # Tentukan tindakan (Eksplorasi vs Eksploitasi)
        if util.flipCoin(self.epsilon):
            action = random.choice(legal_actions)
        else:
            action = self.compute_action_from_q_values(state)

        # [MODIFIKASI] Simpan state dan tindakan saat ini untuk observasi di langkah berikutnya
        self.lastState = state
        self.lastAction = action
        return action

    def final(self, state):
        """
        
        Dipanggil oleh framework saat permainan berakhir (Pac-Man mati atau menang).
        Ini sangat krusial karena transisi terakhir menuju kematian memuat penalti terbesar (-500).
        """
        if self.lastState is not None:
            reward = state.getScore() - self.lastState.getScore()
            self.update(self.lastState, self.lastAction, state, reward)
            
        # Reset memori untuk episode / permainan berikutnya
        self.lastState = None
        self.lastAction = None
        

    def get_q_value(self, state, action):
        """
        Kalkulasi nilai Q menggunakan perkalian titik (dot product).
        Operasi `features * self.weights` secara otomatis memetakan key yang sama
        lalu menjumlahkan hasil kalinya berkat util.Counter.
        """
        features = self.extractor.get_features(state, action)
        return features * self.weights 

    def compute_value_from_q_values(self, state):
        """
        Menghitung V(s), yaitu ekspektasi nilai Q terbaik dari sebuah state:
        V(s) = max_a Q(s, a)
        """
        legal_actions = state.getLegalActions(self.index)
        if not legal_actions:
            return 0.0
        return max([self.get_q_value(state, action) for action in legal_actions])

    def compute_action_from_q_values(self, state):
        """
        
        Mencari tindakan terbaik berdasarkan bobot saat ini: argmax_a Q(s, a).
        Jika ada lebih dari satu aksi dengan nilai Q maksimal (seri),
        kita wajib memecahnya secara acak (tie-breaking) agar agen tidak terjebak loop.
        """
        legal_actions = state.getLegalActions(self.index)
        if not legal_actions:
            return None

        max_q = self.compute_value_from_q_values(state)
        # Identifikasi semua aksi yang menghasilkan max_q
        best_actions = [a for a in legal_actions if self.get_q_value(state, a) == max_q]
        return random.choice(best_actions)

    # def getAction(self, state):
    #     """
        
    #     Menerapkan kebijakan epsilon-greedy untuk Dilema Eksplorasi vs Eksploitasi.
    #     """
    #     legal_actions = state.getLegalActions(self.index)
    #     if not legal_actions:
    #         return None

    #     # Eksplorasi
    #     if util.flipCoin(self.epsilon):
    #         return random.choice(legal_actions)

    #     # Eksploitasi
    #     return self.compute_action_from_q_values(state)

    def update(self, state, action, next_state, reward):
        """
        
        Inti dari pembelajaran mesin agen. Dipanggil setelah agen melakukan observasi transisi.
        Formula update bobot: w_i = w_i + alpha * (TD_Error) * f_i(s, a)
        """
        # 1. Hitung target empiris (Realitas + Estimasi Masa Depan)
        target = reward + (self.discount * self.compute_value_from_q_values(next_state))
        
        # 2. Hitung Kesalahan Prediksi (TD Error)
        q_val = self.get_q_value(state, action)
        difference = target - q_val

        # 3. Distribusikan perbaikan pada masing-masing bobot berdasarkan kontribusi fiturnya
        features = self.extractor.get_features(state, action)
        for feature_name, feature_value in features.items():
            self.weights[feature_name] += self.alpha * difference * feature_value

# Abbreviation
better = betterEvaluationFunction
