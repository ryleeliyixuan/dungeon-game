from PIL import Image, ImageOps
import sys
import time
import subprocess
import qwiic_button
import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import adafruit_ssd1306
import os
import adafruit_mpr121
import random

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
i2c = board.I2C()

# set up the red button
redButton = qwiic_button.QwiicButton(address=0x6f)
redButton.begin()
redButton.LED_off()

if not redButton.begin():
    print("\nThe Red Qwiic Button isn't connected to the system. Please check your connection")

def handle_speak(val):
    subprocess.run(["sh", "speak.sh", val])
    time.sleep(1)

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)

# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()

# play the dungeon game
def die():
  print('You died')
  redButton.LED_on(155)
  # start with a blank screen
  oled.fill(0)
  # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
  oled.show()
  # Create blank image for drawing.
  image = Image.new("1", (oled.width, oled.height))
  draw = ImageDraw.Draw(image)
  draw.text((0, 0), "You died", font=font, fill=255)
  # Display image
  oled.image(image)
  oled.show()
  handle_speak("You died")

def save(blood):
  print('You save the princess')
  redButton.LED_off()
  # start with a blank screen
  oled.fill(0)
  # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
  oled.show()
  # Create blank image for drawing.
  image = Image.new("1", (oled.width, oled.height))
  draw = ImageDraw.Draw(image)
  draw.text((0, 0), "Saved the princess!", font=font2, fill=255)
  # Display image
  oled.image(image)
  oled.show()
  handle_speak('Your blood is ' + str(blood) + "You save the princess!")

def onTheWay(blood):
  print('On the way')
  redButton.LED_off()
  # start with a blank screen
  oled.fill(0)
  # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
  oled.show()
  # Create blank image for drawing.
  image = Image.new("1", (oled.width, oled.height))
  draw = ImageDraw.Draw(image)
  draw.text((0, 0), "On the way", font=font, fill=255)
  # Display image
  oled.image(image)
  oled.show()
  handle_speak("On the way"  + 'Your blood is ' + str(blood))


# sets of matrix to be solved
problem = [[-2, 3, -10, 0, 3, 1, -10, 0, 0, 30, 10, -5],
            [7, 8, -20, 0, -10, -15, 2, 0, 0, 30, 10, -5], 
            [2, 8, 15, 0, -10, -15, 2, 0, 0, 1, -8, -7],
            [-8, 8, 2, 0, -10, 2, 2, 0, 0, 6, 10, -5],
            [-10, 8, 2, 0, -10, 2, 2, 0, 0, -10, 10, -5],
            [-3, 3, 2, 0, -10, 2, 2, 0, 0, -10, -10, -5],
            [-3, -3, 2, 0, -10, 2, 2, 0, 0, -10, -10, -5],
            [0, 8, 2, 0, -10, 2, -11, 0, 0, 8, -1, -5],]
# randomly choose one matrix to solve
index = random.randint(0, len(problem) - 1)
ls = problem[1]
# map the room to the key on sensor
keyToRoom = {0: 0, 1: 1, 4: 2, 11: 3, 2: 4, 5: 5, 10: 6, 9: 7, 6: 8}

def playGame(curRound, keyToRoom):
  blood = 15
  handle_speak('Round' + str(curRound))
  handle_speak('Your initial blood level is 15, please start your tour to save the princess!')
  lastRoom = -1
  while blood > 0:
      for i in range(12):
          if mpr121[i].value:
              # make sure that the chess is only moved to the rightward or downward room
              curRoom = keyToRoom.get(i)
              print("Room" + str(curRoom) + " i:" + str(i))
              if curRoom == lastRoom:
                break
              if curRoom != lastRoom + 1 and curRoom != lastRoom + 3:
                handle_speak('You can only move rightward or downward!')
                break
              lastRoom = curRoom

              blood += ls[i]
              # IN THE LAST ROOM WHERE THE PRINCESS LOCATED
              if i == 6:
                  if blood > 0:
                      save(blood)
                      return True
                  else:
                      die()
                      return False
              else:
                  if blood > 0:
                      onTheWay(blood)
                      break
                  else:
                      die()
                      return False

      time.sleep(0.1)

# Main: start the game
# pre-game alert
handle_speak('You have 3 chances to save the princess.')

end = False
curRound = 1
while end == False and curRound <= 3:
  # start with a blank screen
  oled.fill(0)
  # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
  oled.show()
  # turn off the light
  redButton.LED_off()
  end = playGame(curRound, keyToRoom)
  if end == True:
    break
  handle_speak('The next round will start in 10 seconds.')
  time.sleep(10)
  curRound += 1

if end:
  handle_speak('Congratulations. You win the game.')
else:
  handle_speak('Sorry. You Failed!')
