# Tic-Tac-Toe Game

This project implements a simple command-line Tic-Tac-Toe game for two players. The game allows players to take turns and place their marks ('x' or 'o') on a 3x3 grid. The game checks for a win or a draw after each move.

## Features

The game provides the following features:

- Displaying the playing field.
- Allowing players to take turns and place their marks.
- Checking for a win or a draw after each move.
- Handling invalid inputs and occupied cells.

## Technologies

- **Python** – Programming language used for the game.

## How to Play

1. Run the game script:
    ```sh
    python game.py
    ```

2. Follow the on-screen instructions to enter the row and column numbers for your move.

3. The game will display the updated playing field after each move and announce the winner or a draw when the game ends.

## Game Logic

- The game uses a 3x3 grid represented by a list of lists.
- Players take turns to place their marks ('x' or 'o') on the grid.
- The game checks for a win by evaluating rows, columns, and diagonals.
- The game ends when a player wins or when all cells are occupied, resulting in a draw.

## Example

```sh
   0  1  2
0  -  -  - 
1  -  -  - 
2  -  -  - 
Enter the row number for player x (from 0 to 2): 0
Enter the column number for player x (from 0 to 2): 0
   0  1  2
0  x  -  - 
1  -  -  - 
2  -  -  - 

## Error Handling

- **Invalid Input**: If the player enters an invalid row or column number, the game will prompt the player to try again.
- **Occupied Cell**: If the player tries to place a mark on an occupied cell, the game will inform the player and prompt them to choose another cell.

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch to your fork.
4. Create a pull request with a description of your changes.
