# Epsilon-Greedy K-Armed Bandit Simulation for Action Value Method

This project simulates a **k-armed bandit problem** using the **epsilon-greedy algorithm**. The objective is to evaluate the performance of the algorithm with different epsilon (\( \epsilon \)) values and analyze its impact on the average reward over time.

---

## Overview

The k-armed bandit problem is a classic reinforcement learning problem where:
- Each "arm" (or action) has an unknown probability of yielding a reward.
- The agent must balance between **exploration** (trying less-tested actions) and **exploitation** (choosing the best-known action) to maximize cumulative rewards.

This implementation focuses on comparing the **incremental averages** of rewards achieved under different epsilon values:
- \( \epsilon = 0.1 \) (moderate exploration)
- \( \epsilon = 0.01 \) (low exploration)
- \( \epsilon = 0 \) (pure exploitation)

---

## Features

- **Customizable Parameters**: Easily modify epsilon values, time steps, and reward probabilities for experimentation.
- **Incremental Update**: Efficient computation of the running average reward without storing all past rewards.
- **Visualization**: Clear comparison of performance under different epsilon values through matplotlib-generated plots.

---

## Algorithm

The epsilon-greedy algorithm works as follows:
1. With probability \( 1 - \epsilon \), choose the action with the highest estimated reward (exploitation).
2. With probability \( \epsilon \), choose a random action (exploration).
3. Use incremental updates to refine the Q-values (estimated action values) for each arm:
   \[
   Q(a) \leftarrow Q(a) + \frac{1}{N(a)} (R - Q(a))
   \]
   where:
   - \( N(a) \): Number of times action \( a \) was chosen.
   - \( R \): Reward received.

---

## Results and Insights

The simulation compares the **average reward over time** for three epsilon values:

### Key Observations:
1. **\( \epsilon = 0.1 \)**:
   - Initially performs better because it explores more, quickly refining the action value estimates.
   - However, its continuous exploration prevents it from fully capitalizing on the best-known actions.

2. **\( \epsilon = 0.01 \)**:
   - Starts slower due to limited exploration, causing slower updates to action value estimates.
   - Eventually surpasses \( \epsilon = 0.1 \) because it shifts to more exploitation of the optimal action as time progresses.

3. **\( \epsilon = 0 \)**:
   - Only exploits the initial estimates, leading to poor performance since it doesn't explore enough to find the optimal actions.

### Graph:
Below is the running average reward for each epsilon value over 50,000 time steps:

![Epsilon-Greedy Performance](https://drive.google.com/uc?export=view&id=12PSoPIrJjlYouhWiV1BGDxxf_zwArq8E)

---

