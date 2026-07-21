# Reinforcement Learning for Tic-Tac-Toe: From Minimax to DQN

> 🚧 **Work in progress** — this project is still under active development. Expect incomplete features, rough edges, and frequent changes.

## Overview

This project is a hands-on lab for building a complete Tic-Tac-Toe reinforcement learning pipeline from scratch. It walks through classic game-playing techniques and modern RL methods, comparing value-based and policy-based approaches in a small, fully observable environment that's easy to reason about and debug end to end.

The goal is to explore core RL concepts — exploration vs. exploitation, bootstrapping, and function approximation — in a simple setting before scaling up to more complex environments.

## What's included

- **Game engine** — a from-scratch implementation of Tic-Tac-Toe as the environment.
- **Minimax baseline** — a classic game-tree search agent used as a benchmark for optimal play.
- **Tabular Q-learning** — a value-based agent trained via self-play, using a lookup table for state-action values.
- **Deep Q-Network (DQN)** — a neural network-based agent that approximates the Q-function, enabling comparison against the tabular approach.
- **Agent comparisons** — evaluating and contrasting value-based and policy-based learners on the same game.

## Project status

This is a difficulty-rated learning project (Hard) built as a multi-step lab. Components are being implemented and refined incrementally:

- [x] Game engine
- [ ] Minimax agent
- [ ] Tabular Q-learning agent
- [ ] Deep Q-Network (DQN) agent
- [ ] Agent evaluation & comparison
- [ ] Documentation & examples

## Motivation

Tic-Tac-Toe is small enough to solve exactly, which makes it an ideal sandbox for understanding how RL agents learn, where they succeed, and where they fall short compared to exact methods like minimax. This project is meant as an educational deep dive into RL fundamentals rather than a production-ready library.

## License

TBD

## Acknowledgments

Project structure inspired by [Deep-ML](https://www.deep-ml.com/projects).
