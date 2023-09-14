# Klondike Solitaire #
![alt text](https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FKlondike_%2528solitaire%2529&psig=AOvVaw3XR0iCsMrJShx59sODyWIB&ust=1694817065255000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCOjO6tqTq4EDFQAAAAAdAAAAABAE)

## Introduction ##
Klondike is one of the most popular solitaire card games. The game is played by one person with a standard 52-card deck of playing cards. The goal of the game is to build four foundations (one for each of the four suits), where all of the cards in each foundation are in order from Ace to King (with the Ace on the bottom).

This program will allow the user to play a simplified version of Klondike, with the program managing the game. 

## Game Rules ##

1. The deck of cards is shuffled and 28 cards are dealt into 7 columns to form the tableau.
The cards are dealt in the following manner:
-One card is placed in each of the 7 columns, from left to right

-A second card is placed in the rightmost 6 columns, from left to right 

-A third card is placed in the rightmost 5 columns, from left to right 

-A fourth card is placed in the rightmost 4 columns, from left to right 

-A fifth card is placed in the rightmost 3 columns, from left to right

-A sixth card is placed in the rightmost 2 columns, from left to right 

-A seventh card is placed in the rightmost column

-The last card placed in each column of the tableau is turned face up.

The four foundations are initially empty. The remaining 24 cards become the stock. The top card in the stock is turned over and placed face up in the waste pile (also known as the talon).

2. Whenever an Ace is face up in the tableau or the waste (talon), it may be moved above the tableau and become the first card in that suit’s foundation. After that, additional cards of that same suit may be moved into the suit’s foundation: the Two on the Ace, the Three on the Two, and so on.

3. The objective of the game is to move all 13 cards of each suit into the appropriate foundation. The top card in the talon (waste) may be moved into a foundation or into the tableau:

a) To be moved into one of the foundations, the card must be the correct suit and rank: it must be the same suit as the other cards in that foundation, and it must have a rank which is exactly one higher than the card that is currently at the top of the foundation (as above, the Two on the Ace, the Three on the Two, and so on).

b) To be moved into one of the columns in the tableau, the top card in the waste (talon) must be either a King (if the destination in the Tableau is empty), or the opposite color and exactly one rank lower than the card which is the last face-up card in that column. For example, a red Seven may be moved onto a black Eight. Hint: a red card will have suits as either 2 or 3. A black card will have suits either 1 or 4.

4. The last card in any of the 7 columns in the tableau may be moved into a foundation or into another column in the tableau:
a) To be moved into one of the foundations, the card must be the correct suit and rank (as above).
b) To be move elsewhere in the tableau, the card must be the opposite color and exactly one rank lower (as above).

5. If all of the cards are moved out of a particular column of the tableau, a King of any suit may be moved into that column. Note: a King is the only card which may be moved into an empty column.
6. At any point, the player may turn over the top card from the stock and place it face up in the talon (waste pile). When the stock becomes empty, the talon is turned over and becomes the stock.

## Commands
The program will recognize the following commands:
SW: move one card from the stock to the waste (talon)

WF N: move one card from the waste to foundation N

WT N: move one card from the waste to column N in the tableau

TF N1 N2: move one card from column N1 of the tableau to foundation N2

TT N1 N2: move one card from column N1 to column N2 of the tableau


H: display the legal commands

R: restart the game (remember to shuffle)

Q:  quit

Valid user inputs for foundation numbers range from 1 to 4, and valid user inputs for column numbers in the tableau range from 1 to 7. Note that the functions will accept as parameters the indices and not the column numbers because Python indices starts from 0 and not 1.

The program will repeatedly display the current state of the game and prompt the user to enter a command (until the user enters “q”).

The program will detect, report and recover from invalid commands. None of the data structures representing the foundations, tableau, stock or waste will be altered by an invalid command.

Enjoy!
