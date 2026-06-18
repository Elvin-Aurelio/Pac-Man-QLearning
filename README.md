# Pac-Man AI using Q-Learning & Adversarial Search (Endless Survival)


## Project Metadata


| Property       | Value |
|----------------|-------|
| **Version** | 1.1.5 |
| **Language** | Python 3.x |
| **Domain** | Reinforcement Learning, Adversarial Search |
| **Algorithms** | Reflex, Minimax, Alpha-Beta Pruning, Expectimax, Approximate Q-Learning |
| **Framework** | Tkinter (GUI) |



## Project Overview

This project implements various AI algorithms in Pac-Man to explore automated decision-making in dynamic environments.

### Available Algorithms

1. **Reflex Agent**
   - Making decisions based purely on the current state
   - Zero consideration for future moves

2. **Minimax Agent**
   - Using adversarial search
   - Assuming the ghosts are playing optimally

3. **Alpha-Beta Agent**
   - Optimizing Minimax using pruning

4. **Expectimax Agent**
   - Assuming the ghosts move probabilistically

5. **Q-Learning Agent**
   - Reward-based Reinforcement Learning
   - Learning straight from gameplay experience



## Game Objective

Pac-Man's goals are to:
  - Clear out all the food pellets

  - Dodge the ghosts

  - Make the most of power capsules

  - Maximize the score



## Project Architecture

```
+-----------------------+
|      pacman.py        |
+-----------+-----------+
            |
            v
+-----------------------+
|       game.py         |
+-----------+-----------+
            |
            v
+-----------------------+
|   Agent Controller    |
+-----------+-----------+
            |
    +-------+-------+
    |               |
    v               v
Pacman Agent    Ghost Agent
    |               |
    +-------+-------+
            |
            v
    Game Environment
```



## Directory Structure

```
Pac-Man-QLearning/
│
├── agents/
│   ├── __init__.py
│   ├── ghostAgents.py
│   ├── keyboardAgents.py
│   ├── multiAgents.py
│   └──pacmanAgents.py
│ 
├── core/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── board.py
│   ├── engine.py
│   ├── game.py
│   ├── geometry.py
│   ├── layout.py
│   ├── state_data.py
│   └── util.py
│
├── display/
│   ├── capsuleClassic.lay
│   ├── contestClassic.lay
│   ├── mediumClassic.lay
│   ├── minimaxClassic.lay
│   ├── openClassic.lay
│   ├── originalClassic.lay
│   ├── powerClassic.lay
│   ├── testClassic.lay
│   ├── trappedClassic.lay
│   └── trickyClassic.lay
│ 
├── layouts/
│   ├── __init__.py
│   ├── ghostAgents.py
│   ├── keyboardAgents.py
│   ├── multiAgents.py
│   └── pacmanAgents.py
│ 
├── tests/
│   ├── __init__.py
│   ├── multiagentTestClasses.py
│   ├── testClasses.py
│   └── testParser.py
│ 
├── .gitignore
├── Agent_explanation.md
├── README.md
├── autograder.py
├── pacman.py
├── pacman_weights.json
├── projectParams.py
└── requirements.txt
```



## Quick Start

Run the game with default settings:
```bash
python pacman.py
```

Run with a specific layout:
```bash
python pacman.py -l mediumClassic
```

Run without GUI (text mode):
```bash
python pacman.py -q
```

Run with keyboard control:
```bash
python pacman.py -p KeyboardAgent
```



## AI Agent Execution

| Agent | Command |
|-------|---------|
| Reflex Agent | `python pacman.py -p ReflexAgent` |
| Minimax Agent | `python pacman.py -p MinimaxAgent` |
| Minimax (depth 3) | `python pacman.py -p MinimaxAgent -a depth=3` |
| Alpha-Beta Agent | `python pacman.py -p AlphaBetaAgent` |
| Expectimax Agent | `python pacman.py -p ExpectimaxAgent` |



## Performance Evaluation

Run evaluation with multiple games:
```bash
python pacman.py -p ReflexAgent -n 10 -q
```

### Command Flags

| Flag | Description |
|------|-------------|
| `-n 10` | Run 10 games |
| `-q` | Disable GUI (quiet mode) |

### Evaluation Metrics

- Average Score
- Survival Time
- Number of Steps
- Food Collected
- Ghost Encounters



## Debugging

Display help information:
```bash
python pacman.py --help
```

Test with simple layout:
```bash
python pacman.py -l testClassic
```

Test with minimax layout:
```bash
python pacman.py -l minimaxClassic
```


## Reinforcement Learning Concept (ApproximateQAgent)

Approximate Q-Learning implemented in `agents/multiAgents.py` (class `ApproximateQAgent`) uses a linear combination of features to estimate Q-values:

- Q(s, a) = sum_i w_i * f_i(s, a)

Where:
- f_i(s, a) are features extracted by `FeatureExtractor.get_features(state, action)` (see `multiAgents.py`). Features include distance-based normalized features for closest food, active/scared ghosts, capsules, a dead-end indicator, and a bias term.
- w_i are learnable weights stored in a util.Counter and persisted to disk in `pacman_weights.json` (agent loads this file automatically if present).

Key implementation details from `ApproximateQAgent`:
- Parameters: alpha (learning rate), discount (gamma), epsilon (exploration probability).
- The agent uses an epsilon-greedy policy: with probability epsilon it explores (random legal action), otherwise it picks the argmax action of Q(s,a).
- Weights are updated using Temporal Difference (TD) learning:
  w_i <- w_i + alpha * (r + gamma * max_a' Q(s', a') - Q(s, a)) * f_i(s, a)
- The agent automatically loads `pacman_weights.json` on startup if the file exists; when loading weights, it also reduces epsilon (multiplies by 0.5 but keeps a minimum 0.01) to favor exploitation.
- The agent keeps short-term memory (lastState, lastAction) to process transitions and applies a large terminal penalty (-500) when an episode ends unexpectedly.
- Number of training episodes can be controlled; once episodes exceed training limit, the agent sets epsilon=0 and alpha=0 (no more exploration or learning).
- Epsilon decays each episode (multiplicative decay of 0.95 while > 0.05) to anneal exploration during training.


## Using ApproximateQAgent (Terminal commands)

Basic run (use ApproximateQAgent with default parameters):
```bash
python pacman.py -p ApproximateQAgent
```

Run with explicit agent hyperparameters (alpha, discount, epsilon, numTraining):
```bash
python pacman.py -p ApproximateQAgent -a alpha=0.2,discount=0.8,epsilon=0.5,numTraining=100
```

Set number of games / training episodes using `-n` (number of games) and `-x` (numTraining episodes passed by framework):
```bash
# Train for 200 games without GUI (quiet) and save weights
python pacman.py -p ApproximateQAgent -n 200 -x 200 -q
```

Run headless evaluation after training (uses saved weights if present and reduces epsilon automatically):
```bash
python pacman.py -p ApproximateQAgent -n 20 -q
```

Examples combining layout and multiple flags:
```bash
# Train for 100 episodes on mediumClassic layout with custom hyperparams
python pacman.py -l mediumClassic -p ApproximateQAgent -a alpha=0.1,discount=0.9,epsilon=0.6,numTraining=100 -n 100 -q
```

Notes:
- The agent persists weights to `pacman_weights.json` in the repo root. After training, re-running the agent will load these weights and reduce exploration automatically.
- If you want to reset learned weights, delete `pacman_weights.json` before running.
- If you provide `numTraining` via `-a numTraining=...` and also use `-x`, the agent may receive `numTraining` via kwargs depending on the framework; using `-x` is the standard way to set training episodes for the runner.


## Dictionary Commands

Complete list of all available command-line flags:

| Flag | Full Name | Description | Default |
|------|-----------|-------------|---------|
| `-n` | `--numGames` | Number of games to play | 1 |
| `-l` | `--layout` | Layout file to load | mediumClassic |
| `-p` | `--pacman` | Pacman agent type | KeyboardAgent |
| `-t` | `--textGraphics` | Display output as text only | False |
| `-q` | `--quietTextGraphics` | Minimal output, no graphics | False |
| `-g` | `--ghosts` | Ghost agent type | RandomGhost |
| `-k` | `--numghosts` | Maximum number of ghosts | 4 |
| `-z` | `--zoom` | Zoom size of graphics window | 1.0 |
| `-f` | `--fixRandomSeed` | Fix random seed for same game | False |
| `-r` | `--recordActions` | Record game history to file | False |
| `--replay` | `--replay` | Replay a recorded game file | None |
| `-a` | `--agentArgs` | Agent parameters (comma-separated) | - |
| `-x` | `--numTraining` | Number of training episodes | 0 |
| `--frameTime` | `--frameTime` | Delay between frames (seconds) | 0.1 |
| `-c` | `--catchExceptions` | Enable exception handling | False |
| `--timeout` | `--timeout` | Max computation time per game (seconds) | 30 |



## Future Improvements

Recommended improvements for the project:

**AI**
- Implement Deep Q-Learning with neural networks
- Add Policy Gradient algorithms (A3C, PPO)
- Multi-agent coordination and learning

**Gameplay**
- Multiplayer mode (cooperative/competitive)
- Custom map editor
- Dynamic difficulty adjustment
- Power-up mechanics enhancement

**Analytics**
- Real-time performance metrics dashboard
- Training statistics visualization
- Agent behavior analysis tool
- Comparison charts for different agents

**Engineering**
- Comprehensive unit tests (pytest)
- API documentation (Sphinx)
- Performance profiling and optimization
- Code refactoring for modularity

## System Requirements

### Minimum Specifications

| Component | Requirement |
|-----------|-------------|
| CPU | Dual-core processor (2.0 GHz) |
| RAM | 2 GB |
| Python | 3.8+ |
| Storage | 500 MB |

### Recommended Specifications

| Component | Requirement |
|-----------|-------------|
| CPU | Quad-core processor (2.5 GHz+) |
| RAM | 4-8 GB |
| Python | 3.10+ |
| Storage | 1 GB (SSD preferred) |
| GPU | Optional (for neural network training) |



## References

- UC Berkeley AI Pacman Project: http://ai.berkeley.edu



## License

Educational License - These projects are free to use or extend for educational purposes. You are free to use or extend these projects provided that (1) you do not distribute or publish solutions,[...]

For more details, visit: http://ai.berkeley.edu



## Contribution
1. Elvin Aurelio
- Develop betterEvaluationFunction
- Debug Agents Logic
- Implement Q-Learning Agent
- Logging summary: Node expansion tracking, computation time tracking, survival steps tracking

2. Jovanic Manuelo
* Food Respawn
* ReadMe & Use Guide setups
* Change Gameplay to endless mode (no win condition)
