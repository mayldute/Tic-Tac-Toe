This project is a console version of the classic "Tic-Tac-Toe" game for two players. The game is played on a 3x3 grid and ends with one player winning or a draw.

**How to Play:**

Run the script, and the game board will appear on the screen.

Players take turns entering the coordinates of their move (row number and column number from 0 to 2).

The game continues until:
One player aligns three symbols (X or O) in a row, column, or diagonal — victory!

All cells on the board are filled — draw.

**Code Structure:**

playing_field – The 3x3 game board, initially filled with "-".

field() – Displays the current state of the game board in the console.

win_check() – Checks if any player has won (horizontal, vertical, or diagonal lines).

**Main Game Loop:**

Asks for the move coordinates from the current player (X or O).

Validates the input and checks if the cell is free.

Records the move and updates the board.

Checks for a winner.

Switches to the next player's turn.

**Requirements:**

Python 3.x
