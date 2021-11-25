# dungeon-game
This is the final project for the course Interactive Device Design at Cornell Tech. We will use Raspberry Pi to build a machine that executes the dungeon game.

# Project Plan
## Big idea
### Background
Dungeon game is a popular board game among kids. Players, as the knights, try to save the princess who is captured by the demons in the dungeon. We will build a game machine that implements this dungeon game with Raspberry Pi. Rules are detailed below. 

### Rule
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of 3 x 3 rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
* The knight has an initial health point represented by a positive integer (eg. 100). If at any point his health drops to 0 or below, he dies immediately.
* Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).
* To reach the princess as quickly as possible, the knight decides to move *only rightward or downward* in each step.
* Players won’t know whether a room has demons or magic orbs before they enter the room. 
* Note: The order will affect the game results. 

#### Example
With an initial health point of 15, the player successfully rescues the princess by following the path indicated on the matrix.  
![example-dungeon-grid](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/dungeon-grid-1.jpeg)

### Logistic
* __Pre-game:__ Users can input the number of players at the beginning. 
* __During the game:__ Each player has one chance to play the game. They all play the game in the same setting with the same amount of initial health points. 
  * The system will keep track of the healthy points and display them on the OLED screen. 
  * The system will notify the players whether their moves increase or decrease their health points (ie. encounter demons or magic orbs). And they will be alerted with “game over” once their health drops to 0 or below.
  * The system will record the score of each player.  
* __Post-game:__ The one who successfully saves the princess with the largest amount of health points (above 0) wins the game. 
  * The system will notify them about the winner.

### Design
![project-plan-desing](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/project-plan-design.jpg)

## Timeline
* 11/22: Project Plan submitted.
* 11/30: Functional check-off submitted. Finish our first version of the prototype(simply use the cardboard and draw a matrix on the board for initial tests).
* 12/7: Use materials in MakerLab to build our board and finish our final prototype.
* 12/13: Submit write-up and documentation.


## Parts needed
* Raspberry Pi
* Capacitive Sensor
* Copper tape
* QWIIC connector
* Wood Board/Cardboard
* OLED screen
* Speaker
* Red light button for death, green light button for alive
* Joystick for instruction and the number of players

## Risks/Contingencies
* 3d printing being too complicated

## Fall-back plan
The algorithms used in this project are clear and simple. The main concern is whether the hardware parts can be used appropriately to build the functions in our expectations. For instance, if the outer part of our game board prototype is not built properly with the 3D printer, a prototype with a hand-crafted part has to be used instead. 

# Feedback
We received the following feedback:
* This sounds like a cool project that would create a fun game! Perhaps you could enable to player to move up and to the left as well. I also think making it less completely unknown to the user what the next room might be would also be cool. For example, you could have each neighboring square tell you whether there is a high/medium/low chance of danger/health orb and a high/medium/low quantity of damage/health added in that room, so they can make a more strategic decision whether or not they should take that square or not given their health. You could also implement a total move quantity, so that the player cannot make more moves than this quantity (this would make the ability to move in any direction more fair). [Donal Michael Thomas Lowsley-Williams]
* Nice plan and documentation. What are you planning to add beyond the existing dungeon game? It looks reasonable for two people. Consider how you can add to the interaction and make the game fun considering things like what happens after winning, etc. [Alexandra Walburgis Dongfangchen Bremers]
* It is an interesting implementation of the dungeon game on Raspberry pi. I like the design illustration of the system as it explains clearly the components. One thing I am am not sure is how you track the movement of the "knight" in each step. It would be great if you can mention it in your document. [Yehao Zhang]

