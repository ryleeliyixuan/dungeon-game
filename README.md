# dungeon-game
This is the final project for the course Interactive Device Design at Cornell Tech. We will use Raspberry Pi to build a machine that executes the dungeon game.

[Project Plan](#project-plan)

[Function Check-off](#function-check-off)

[Product Iteration](#product-iteration)

[Connect All the Things Together](#connect-all-the-things-together)

[User Test](#user-test)

[Final Deliverables](#final-deliverables)

[Project Reflections](#project-reflections)


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
![IDD-DungeonGame-Rule-1](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/IDD-DungeonGame-Rule-1.jpg)
![IDD-DungeonGame-Rule-2](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/IDD-DungeonGame-Rule-3.jpg)
![IDD-DungeonGame-Rule-3](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/IDD-DungeonGame-Rule-2.jpg)

#### Example
With an initial health point of 15, the player successfully rescues the princess by following the path indicated on the matrix.  
![example-dungeon-grid](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/dungeon-grid-1.jpeg)

### Logistic
#### Version 1: 
* __Pre-game:__ Users can input the number of players at the beginning. 
* __During the game:__ Each player has one chance to play the game. They all play the game in the same setting with the same amount of initial health points. 
  * The system will keep track of the healthy points and display them on the OLED screen. 
  * The system will notify the players whether their moves increase or decrease their health points (ie. encounter demons or magic orbs). And they will be alerted with “game over” once their health drops to 0 or below.
  * The system will record the score of each player.  
* __Post-game:__ The one who successfully saves the princess with the largest amount of health points (above 0) wins the game. 
  * The system will notify them about the winner.

#### Version 2 (MOST RECENT): 
* __Pre-game:__ We have one player for this game. He/she have 3 chances (ie. rounds) to save the princess. 
* __During the game:__ Players  play the game in a random generated setting with random generated amount of initial health points. But it's guranteed that there's a path such that they can save the princess out.
  * The system will keep track of the healthy points and display them on the OLED screen. 
  * The system will notify the players whether their moves increase or decrease their health points (ie. encounter demons or magic orbs). And they will be alerted with “game over” once their health drops to 0 or below.
* __Post-game:__ If successfully saving the princess with amount of health points (above 0), the player wins the game. 
  * The system will notify the final results.

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
* Joystick for instruction and the number of players (update: no longer needed)

## Risks/Contingencies
* 3d printing being too complicated

## Fall-back plan
The algorithms used in this project are clear and simple. The main concern is whether the hardware parts can be used appropriately to build the functions in our expectations. For instance, if the outer part of our game board prototype is not built properly with the 3D printer, a prototype with a hand-crafted part has to be used instead. 

## Feedback
We received the following feedback:
* This sounds like a cool project that would create a fun game! Perhaps you could enable to player to move up and to the left as well. I also think making it less completely unknown to the user what the next room might be would also be cool. For example, you could have each neighboring square tell you whether there is a high/medium/low chance of danger/health orb and a high/medium/low quantity of damage/health added in that room, so they can make a more strategic decision whether or not they should take that square or not given their health. You could also implement a total move quantity, so that the player cannot make more moves than this quantity (this would make the ability to move in any direction more fair). [Donal Michael Thomas Lowsley-Williams]
* Nice plan and documentation. What are you planning to add beyond the existing dungeon game? It looks reasonable for two people. Consider how you can add to the interaction and make the game fun considering things like what happens after winning, etc. [Alexandra Walburgis Dongfangchen Bremers]
* It is an interesting implementation of the dungeon game on Raspberry pi. I like the design illustration of the system as it explains clearly the components. One thing I am am not sure is how you track the movement of the "knight" in each step. It would be great if you can mention it in your document. [Yehao Zhang] 

# Function Check-off
* **How we track the movement of the "knight" in each step**: On each cell of the board, there is a copper tape placed on it. And the tape is connected to the capacity sensor underneath. Once the knight moves on a specific cell, the sensor receives the status that the knight is on that cell. And finally our Raspberry Pi stores the coordinate information.
* **Basic Function**: We realized the basic algorithm of this game. From the following video, we can see how sound alerts and text display change according to the status of the knight (die vs. save the princess).
  * [Function Check Off - Case 1: DIE](https://youtu.be/FmcbGyky4Jw) : the knight enters room no.3 (indexed from 0) which have demons. His health points drop below 0 and dies.
  * [Function Check Off - Case 2: SAVE THE PRINCESS](https://youtu.be/gMr6t6nUbvM) : the knight enters room no.8 (indexed from 0; this is the room where the princess is located). He sucessfully saves the princess. 

# Product Iteration
## Iteration 1 - Paper Prototype
This is the scatch of our paper prototype.
![paper-prototype-1](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/paper-prototype-1.jpeg)

## Iteration 2 - CAD Prototype - 2d Draft 1
### Iteration Explained
* **Logistic**: We carefully thought through the case of having multi-players. We think this would not be a fair game if we ask each of the players play the game after/before some others. This is because one playing after the others can observe the previous rounds and see the patterns, thus having higher chance of succeeding in the game. 
  * In response to this, we change the game to "one-player, multiple rounds". We will have one player playing on the same matrix for 3 round. The metric of success is whether he/she can save the princess. And the trick of this game is to learn from the failed round, memorize whether rooms have demons or magic orbs.
  * In this case, we cancel the placement of joystick as players don't have to choose the number of players anymore.  
  * Updated version of the logistic can be found in the BIG IDEA section. 
This is the 2d draft of our CAD prototype (version 1). 

![2d-draft-v1](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/2d-draft-v1.jpg)

## Iteration 3 - CAD Prototype - 2d Draft 2
This is the 2d draft of our CAD prototype (version 2). 

![2d-draft-v2](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/2d-draft-v2.jpg)

### Iteration Explained
*  **Cable:** We leave a space to let the power cable out.
*  **Grid Layout:** We indeed built 3d model based on 2d draft v1. However, we don't think this design can work. Our initial purpose is having one grid layout that 1. can support the chess 2. the chess can have contact with the corresponding copper tape once placed on that cell (this is how we track the movement of the knight). This design makes the grid too thin to support the chess. Thus we further improve the grid layout.

![grid-v1](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/grid-v1.png)
![grid-v1-2](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/grid-v1-2.png)


## Iteration 3 - CAD Prototype - 3d CAD Prototype
![game-box-1](https://github.com/ryleeliyixuan/dungeon-game/blob/main/3d-cad-model/game-box-1.jpeg)
![game-box-2](https://github.com/ryleeliyixuan/dungeon-game/blob/main/3d-cad-model/game-box-2.jpeg)
![game-box-3](https://github.com/ryleeliyixuan/dungeon-game/blob/main/3d-cad-model/game-box-3.jpeg)

* [A video showcases the 3d cad model can be found here](https://youtu.be/jVL9Jbo_lVY)
* [All relavant files can be found here.](https://github.com/ryleeliyixuan/dungeon-game/tree/main/3d-cad-model)

## Iteration 4 - Laser Cutting
### Iteration Explained
* **Why Laser Cutting:** During our function check off, Wendy and Rei suggested that it would be better to apply laser cutting rather than 3d printing to our gamebox. We understand that the 3d printers are pretty occupied during the final week. And we consider that our flat design does not necessarily need use of 3d printer and we don't want to occupy resources when they're already intense. 
* **Game Instruction:** According to KI's feedback, although the game rule is simple once ellaborated clearly, people may find hard to understand it if there's no instruction beforehand. So we decide to add text-form instruction on the gamebox.
* **Voice Alert:** We add voice alerts that guide users and inform them about the status of the game (eg. when the game starts - "Your health point now is 15. Please start your tour to save the princess.").


### The Design
The stroke for those parts that are supposted to be cut is thin. And the stroke for those parts that are supposted to be etched is strong.
![dungeongame](https://github.com/ryleeliyixuan/dungeon-game/blob/main/2d-laser-cut/dungeongame.svg)

### The Process
![laser-cut-1](https://github.com/ryleeliyixuan/dungeon-game/blob/main/2d-laser-cut/laser-cut-1.jpeg)
![laser-cut-2](https://github.com/ryleeliyixuan/dungeon-game/blob/main/2d-laser-cut/laser-cut-2.jpeg)
![laser-cut-3](https://github.com/ryleeliyixuan/dungeon-game/blob/main/2d-laser-cut/laser-cut-3.jpeg)
![laser-cut-4](https://github.com/ryleeliyixuan/dungeon-game/blob/main/2d-laser-cut/laser-cut-4.jpeg)

### Prototype
* [A video showcases the laser cutting model can be found here](https://youtu.be/WVc9eOcwr9I)
* [All relavant files can be found here.](https://github.com/ryleeliyixuan/dungeon-game/tree/main/2d-laser-cut)

# Connect All the Things Together
### The Process
![connect-1](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/connect-1.jpeg)
![connect-2](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/connect-2.jpeg)

### Modification and Improvement
* **Routing of the Copper Tape**: We need to map each cell/room to key on the capacitive sensor. Initially, our map was "room 0 -> 0, room 1 -> 1, ...., room 9 -> 8" as our room was indexed from 0. However, when we implemented the routing of the copper tape, we found out that tape would tangle together if we strictly followed this map. Thus, we changed the map to "room 0 -> 0, room 1 -> 1, room 2 -> 4, room 3 -> 3, room 4 -> 11, room 5 -> 2, room 6 -> 5, room 7 -> 10, room 8 -> 9." In this case, the tape will be spread out.

![connect-3](https://github.com/ryleeliyixuan/dungeon-game/blob/main/img/connect-3.jpeg)

# User Test
Although we collect feedbacks from users along the way, we still invite 3 users to test out our gamebox. 

### Video
[Video of the user test can be found here.](https://youtu.be/AI9DVx5K6qg)

### Problems and Solutions
Below are some corner cases that we should take care of and later take a close examine on that:
* **P1:** If users did not understand the rule, rather than move down the knight rightward or downward, they may move it leftward or upward. However, our gamebox do not have any mechanism to prevent these false moves. 
  * **S1:** If users make false moves, we'll alert them and make that move invalid.
* **P2:** Sometimes, when users placed the knight on the cell, there's no response from our Pi. This is because the there are some cracks on our tape.
  * **S2:** Enhance the tape. 
* **P3:** users donot know which round they are in.
  * **S3:** Add voice alert to notify the current round. 


# Final Deliverables
## Code
 One need to go the circuitpython environment, pip install the requirements file, and run python game.py to run the game.
   ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/game
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/game $ pip install -r requirements.txt
  (circuitpython) pi@ixe00:~/Interactive-Lab-Hub/game $ python game.py
  ```
All code can be found [here.](https://github.com/ryleeliyixuan/dungeon-game/blob/main/game.py) 


## Video
[Final Video can be found here.](https://youtu.be/RljdgDhUrUA) 

[Checkout our showcase on the final presentation day.](https://youtu.be/KSc5hwFQiBk)


# Project Reflections
The interactive device design practice of this semester is over. We have learned a lot when creating our own prototypes in each lab.

* **What we learn from this project**
  * The goal of interactive system design can be analyzed from the two levels of "usability" and "user experience", focusing on people-oriented user needs. From the experience we got from this project, we have a comprehensive understanding of how to design a product that is valuable and easy for users to manipulate. And user experience is the core focus of our design. 
  * In the Dungeon Game board, players act as a knight trying to save the princess and control their action by moving the chess. We use capacitive sensors to track the movement of the chess, mapping the position of the chess to numerical code which is the input of our algorithm. We learned to utilize multiple sensors and buttons to facilitate users’ understanding of the game rules and enhance their experience by engaging them with voice/light instruction. 
  * We learned to iterate products based on pilot tests. Users’ feedback has really driven our product development. We indeed received valuable feedback during the final presentation session. Something more to think about includes: 1. We may extend this game to a multi-players version. 2. We may add more visual indications on the board with laser cutting.


* **Wish to know**
  * We wish we knew about different approaches to build our exterior at the start of the project. We went straight for 3d printing and even built the 3d model as we didn’t know about the option of laser-cutting. However, during the function check off, Wendy and Rei suggested that it would be better to apply laser cutting rather than 3d printing. Then we realized that our flat design did not necessarily need the use of 3d printing.


