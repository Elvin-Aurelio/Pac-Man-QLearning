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


## Reinforcement Learning Concept

Q-Learning uses the following equation:

Q(s,a) = Q(s,a) + α(r + γ max Q(s',a') - Q(s,a))

Where:

| Variable | Description |
|----------|-------------|
| Q(s,a) | Q-value for action a in state s |
| α | Learning rate |
| γ | Discount factor |
| r | Reward |
| s | Current state |
| s' | Next state |



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

Educational License - These projects are free to use or extend for educational purposes. You are free to use or extend these projects provided that (1) you do not distribute or publish solutions, (2) you retain this notice, and (3) you provide clear attribution to UC Berkeley.

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

