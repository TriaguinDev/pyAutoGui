#My first bot in python lol

#Github automatic login
import pyautogui as pg
from time import sleep

pg.PAUSE = 1

name = input("Enter you name or email ")
password = input ("Enter your password")

pg.press("win")
pg.write("Brave")
pg.press("enter")
pg.click(477,74)
pg.write("https://github.com/")
pg.press("enter")
pg.click(1707 , 196)
pg.write(name)
pg.click(866 , 466)
pg.write(password)
pg.press("enter")


