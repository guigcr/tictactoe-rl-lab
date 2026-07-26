# Game AI Training Project

This project is a collection of AIs trained to play different games using Reinforcement Learning. Each game lives in its own folder/module and has its own agent, environment and neural network, but they all follow the same general approach: the AI plays thousands of matches, learns from its own experience, and gradually improves its decision making.

Currently, the project includes one game:

- **Snake** (see below)

More games/AIs will be added to this same structure over time.

---

## Snake

An AI that learns to play Snake on its own, using Deep Q-Learning (DQN) with PyTorch. This version runs **headless** (no game window) so training happens purely in the terminal, which makes it much faster than watching it play in real time.

### Structure

```
.
├── agent.py    # RL agent: state, memory, training, main loop
├── game.py     # Snake game logic, rules and rewards (no rendering)
└── model.py    # Neural network (Linear_QNet) and training logic (QTrainer)
```

### How the training works

The project uses **Deep Q-Learning**: a neural network learns to estimate the value of each possible action (go straight, turn right, turn left) based on the current state of the game.

#### State (what the AI "sees")

On every frame, the agent builds a vector of 11 binary pieces of information about the snake:

- Immediate danger (1 block ahead) in three directions: straight, right and left
- Current movement direction (left, right, up, down)
- Relative position of the food (left/right/above/below the head)

#### Rewards

- **+10** for eating food
- **-10** for dying (collision with a wall or with its own body, or if it takes too long without eating)
- **0** for a regular step that doesn't eat and doesn't die

#### Neural network

A simple fully connected network (`Linear_QNet`):

- Input: 11 neurons (the state described above)
- Hidden layer: 256 neurons, ReLU activation
- Output: 3 neurons (a score for each action: straight, right, left)

Training uses the Adam optimizer (learning rate 0.001) and mean squared error (MSE) between the predicted Q-value and the target Q-value, calculated with the Bellman equation using a discount factor (gamma) of 0.9.

#### Exploration vs. exploitation (epsilon-greedy)

The exploration rate is tied directly to the number of games played: `epsilon = 80 - n_games`. Early on, this makes the AI move almost randomly to explore the game; as `n_games` grows, epsilon drops (and eventually goes negative, meaning the AI always uses the network's prediction instead of a random move).

#### Experience memory

Every move (state, action, reward, next state, whether it died) is stored in a memory of up to 100,000 records. This is used in two ways:

- **Short-term training**: trains immediately on that move at every step
- **Long-term training (experience replay)**: at the end of each match, samples a batch of up to 1,000 past moves and trains on them again, which helps stabilize learning

### How to run it on your machine

#### Requirements

- Python 3.8 or higher

#### Installation

```bash
pip install torch numpy
```

#### Running the training

```bash
python agent.py
```

No window will open. The AI plays automatically in the background, match after match, and progress is printed straight to the terminal:

```
Game: 1 | Score: 0 | High Score: 0
Game: 2 | Score: 1 | High Score: 1
...
```

Training runs indefinitely (infinite loop) until you stop the process (Ctrl+C in the terminal). There's no fixed number of matches: the longer you let it run, the more experience the AI accumulates.

#### Notes

- This version does not save the trained model to disk. If you stop the process, the learned weights are lost. If you want to keep a trained model between runs, `model.py` needs a `save()` method (using `torch.save(model.state_dict(), ...)`) called whenever a new high score is reached.
- Since training depends on randomness (initial exploration and memory sampling), two runs can produce AIs with different performance even using the same code.

---

## Roadmap

- [ ] Add new games/AIs to this project
- [ ] Add a section here for each new game as it's trained
