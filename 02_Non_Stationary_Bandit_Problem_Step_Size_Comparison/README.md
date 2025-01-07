# Non-Stationary Bandit Problem: Step Size Comparison

This repository contains the implementation of a **non-stationary multi-armed bandit problem**. The project compares two approaches for updating action-value estimates in reinforcement learning:
1. **Constant Step Size**: Fixed learning rate for updates.
2. **Non-Constant Step Size**: Step size decreases over time as \( 1 / N(a) \).

The goal of this project is to demonstrate how these two methods perform in a non-stationary environment where the reward distribution for actions changes over time.

---

## Key Features
- **Non-Stationary Environment**: Simulated with small random variations in true reward values at each time step.
- **Epsilon-Greedy Policy**: Balances exploration and exploitation during action selection.
- **Performance Comparison**: Plots the average reward over time for both constant and non-constant step size approaches.

---

## Visualizations
The project includes a visualization of the average reward over time for both approaches. Here's a preview of the output:
![image](https://drive.google.com/uc?export=view&id=1-0wMkmE_DEEeCqaGU0MbpSD6ld7hyTBp)

- **Non-Constant Step Size**: Adaptive step size that decreases over time.
- **Constant Step Size**: Fixed step size to handle non-stationary changes effectively.

------

## Conclusion
In non-stationary environments, **constant step size** demonstrates superior adaptability to changing reward distributions due to its fixed learning rate, allowing it to quickly incorporate new information. On the other hand, **non-constant step size**, with its diminishing update rate, struggles to adjust to rapid changes, making it better suited for stationary environments. This highlights the importance of selecting an appropriate step size strategy based on the problem's characteristics.
