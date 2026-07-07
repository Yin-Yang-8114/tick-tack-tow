# tick-tack-tow

## Game Rules - חוקי המשחק
* The game is played on a 3*3 board
* The game is designed for 2 players
* Each player chooses their marker to continue the game X/O
* In turn, places their marker on the board
* The first player to get 3 of their markers in a row (horizontally, vertically or diagonally) wins the game.
* If all 9 squares are filled and no player has accumulated 3 markers in a row, the game ends in a draw.

## Running the game - הרצת המשחק

To start the game, run the main Python script from your terminal:

```bash
python main.py
```

### Game Instructions

1. **Player Names:** Enter the names of two players.
2. **First Turn:** Player 1 always starts the game and is given the `X` marker.
3. **Board Positions:** To place your marker, choose a number from **0 to 8** based on the following board layout:

```text
0 | 1 | 2
---|---|---
3 | 4 | 5
---|---|---
6 | 7 | 8
```

* **0** is the top left corner.
* **1** is the top middle position.
* **2** is the top right corner.
* **3** starts the middle row on the left, and so on. 


## Existing features - תכונות קיימות
* Request player names and display them throughout the game
* Set a marker for each player
* Display board
* Select a slot
* Display an updated board after selection

## Developers - מפתחים
* Chaim
* Gad
* Yisrael Meir
* Yehoshua

## Current Key Tasks - משימות מרכזיות  נוכחיות

* **Chaim** - Team management and general development
* **Gad** - Building the game board
* **Yisrael & Meir** - Requesting player names
* **Yehoshua** - README editing 
