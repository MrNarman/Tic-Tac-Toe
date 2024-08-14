# Tic-Tac-Toe Game

Welcome to our Python implementation of the classic Tic-Tac-Toe game! This project was a collaborative effort between [MrNarman](https://github.com/MrNarman) and [BackendSid22](https://github.com/BackendSid22). We aimed to create a simple, yet fully functional command-line version of the game that anyone can play right from their terminal.

## Game Overview

Tic-Tac-Toe, also known as Noughts and Crosses, is a popular 2-player game where players take turns marking a 3x3 grid with their symbol (either 'X' or 'O'). The objective is to be the first to align three of your symbols either horizontally, vertically, or diagonally. It's a game of strategy and foresight, where every move counts.

### Key Features
- **Interactive Gameplay:** Players can interact with the game by simply entering the position where they want to place their symbol.
- **Real-time Feedback:** The game provides real-time feedback on the board, showing the updated state after each move.
- **Win/Loss/Draw Detection:** The game automatically detects when a player has won, or if the game has ended in a draw.
- **Replay Option:** After each game, players have the option to start a new game or exit.

## How to Play

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/tictactoe.git
   cd tictactoe
   ```

2. **Run the Game:**
   ```
   python tictactoe.py
   ```

3. **Instructions:**
   - Players are prompted to enter their move by specifying a number between 1 and 9, which corresponds to a position on the board as shown below:
     ```
     1 | 2 | 3
     ---------
     4 | 5 | 6
     ---------
     7 | 8 | 9
     ```
   - The first player to align three of their symbols (either 'X' or 'O') wins the game.
   - If all positions are filled without a winning combination, the game ends in a draw.

## Project Structure

- **`tictactoe.py`:** The main game script. This file contains all the logic for the game, including the board setup, player input, win/loss/draw detection, and the replay option.
- **`README.md`:** This file. It provides an overview of the project, instructions on how to play, and information about the authors.

## Authors

- **Godrick Narman:** [GitHub Profile](https://github.com/MrNarman)
- **Sydney Muriuki** [GitHub Profile](https://github.com/BackendSid22)

## Future Enhancements

While this version of Tic-Tac-Toe is complete and functional, we have a few ideas for future improvements:
- **GUI Version:** Developing a graphical user interface (GUI) for the game to make it more visually appealing and user-friendly.
- **Score Tracking:** Adding a feature to keep track of player scores over multiple games.

## Contributions

If you have any ideas, suggestions, or improvements, feel free to fork the repository and submit a pull request. We welcome contributions from the community!
---

Feel free to modify this README to better fit your project's needs!
