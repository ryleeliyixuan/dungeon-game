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

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

i2c = board.I2C()

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
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)

# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()

ls = [-2, 3, 3, -5, -10, 1, 10, 30, -5]
blood = 15
handle_speak('Your blood is 15, please start your tour to save the princess')
while blood > 0:
    for i in range(9):
        if mpr121[i].value:
             blood += ls[i]
             if i == 8:
                 if blood > 0:
                     print('You save the princess')
                     redButton.LED_off()
                     # start with a blank screen
                     oled.fill(0)
                     # we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
                     oled.show()
                     # Create blank image for drawing.
                     image = Image.new("1", (oled.width, oled.height))
                     draw = ImageDraw.Draw(image)
                     draw.text((0, 0), "You save the princess!", font=font, fill=255)
                     # Display image
                     oled.image(image)
                     oled.show()
                     handle_speak('Your blood is ' + str(blood) + "You save the princess!")
                     break
                 else:
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
                     break

             else:
                 if blood > 0:
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
                 else:
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
                     break







    time.sleep(0.1)
