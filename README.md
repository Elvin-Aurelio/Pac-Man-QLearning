# Pac-Man AI using Q-Learning & Adversarial Search

## Project Metadata

| Property  | Value |
|-----------|-------|
| Version   | ISI SENDIRI |
| Language  | ISI SENDIRI |
| Category  | ISI SENDIRI |
| Framework | ISI SENDIRI |



## Project Overview

Project ini mengimplementasikan berbagai algoritma Artificial Intelligence pada permainan Pac-Man untuk mempelajari pengambilan keputusan otomatis dalam lingkungan yang dinamis.

### Available Algorithms

1. **Reflex Agent**
   - Mengambil keputusan berdasarkan kondisi saat ini
   - Tidak mempertimbangkan langkah masa depan

2. **Minimax Agent**
   - Menggunakan pencarian adversarial
   - Mengasumsikan ghost bermain optimal

3. **Alpha-Beta Agent**
   - Optimasi Minimax menggunakan pruning

4. **Expectimax Agent**
   - Menganggap ghost bergerak secara probabilistik

5. **Q-Learning Agent**
   - Reinforcement Learning berbasis reward
   - Belajar dari pengalaman bermain



## Game Objective

Tujuan Pac-Man adalah:

- Mengumpulkan seluruh food pellet
- Menghindari ghost
- Memanfaatkan power capsule
- Memaksimalkan score
- Menyelesaikan level dengan jumlah langkah minimum



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
├── assets/
├── docs/
├── src/
│   ├── agents/
│   │   ├── ghostAgents.py
│   │   ├── keyboardAgents.py
│   │   ├── multiAgents.py
│   │   └── pacmanAgents.py
│   │
│   ├── core/
│   │   ├── game.py
│   │   ├── layout.py
│   │   └── util.py
│   │
│   ├── display/
│   │   ├── graphicsDisplay.py
│   │   ├── graphicsUtils.py
│   │   └── textDisplay.py
│   │
│   └── layouts/
│
├── tests/
├── README.md
├── requirements.txt
└── LICENSE
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
- Win Rate
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



## Autograder

Project supports UC Berkeley autograder.

Run all tests:
```bash
python autograder.py
```

Run specific test:
```bash
python autograder.py -q q1
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
- ISI SENDIRI

**Gameplay**
- ISI SENDIRI

**Analytics**
- ISI SENDIRI

**Engineering**
- ISI SENDIRI

## System Requirements

### Minimum Specifications

| Component | Requirement |
|-----------|-------------|
| CPU | ISI SENDIRI |
| RAM | ISI SENDIRI |
| Python | ISI SENDIRI |

### Recommended Specifications

| Component | Requirement |
|-----------|-------------|
| CPU | ISI SENDIRI |
| RAM | ISI SENDIRI |
| Python | ISI SENDIRI |



## References

ISI SENDIRI



## License

ISI SENDIRI



## Author

| Property | Value |
|----------|-------|
| Project | ISI SENDIRI |
| Purpose | ISI SENDIRI |

