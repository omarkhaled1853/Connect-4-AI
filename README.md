# Connect Four

## Overview

This Connect Four game features an AI agent as the opponent, designed to challenge the human player using various heuristic-based algorithms. The AI aims to maximize its score by increasing the human player's losses. The difficulty of the AI is controlled by the number of maximum levels in its decision tree.

## Game Features

- The AI opponent uses different algorithms to determine the best move.
- The AI aims to optimize its strategy by maximizing its advantage over the human player.
- The game is developed using **Python**, **Pygame** for visualization, **Tkinter** for UI interactions, and file-based outputs for printing the decision tree.

## AI Algorithms

### 1. MinMax Algorithm

- The agent tries to maximize its profit at **level 1**.
- At **level 2**, the human tries to minimize their loss.
- This back-and-forth strategy continues up to the set maximum levels.

### 2. ExpectiMinMax Algorithm

- The agent chooses a column to play with **60% probability**.
- The agent can also play in the **left or right adjacent columns with 40% probability**.
- This adds randomness to the AI's decision-making process.

### 3. Alpha-Beta MinMax Algorithm

- An optimized version of the **MinMax** algorithm.
- It speeds up decision-making by **pruning unnecessary branches** in the decision tree.
- The agent can quickly decide the best column to play without excessive computation time.

## How to Play

1. Start the game and select a **difficulty level** based on the maximum AI search depth.
2. Choose which **algorithm** the AI should use (MinMax, ExpectiMinMax, or Alpha-Beta MinMax).
3. Play against the AI by dropping tokens into the grid.
4. The AI will make strategic moves based on the selected algorithm.
5. The game ends when the board is being full.

## Technologies Used

- **Python**: Core language for game logic.
- **Pygame**: For graphical visualization.
- **Tkinter**: For UI components and interaction.
- **File Handling**: To print and visualize the AI’s decision tree.

Enjoy playing Connect Four against an intelligent AI opponent!
