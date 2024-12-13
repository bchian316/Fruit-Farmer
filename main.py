'''DO NOT STOP THE PROGRAM IF YOU WISH TO SAVE YOUR PROGRESS
PRESS THE X ON THE GAME WINDOW INSTEAD
PLEASE USE LINK:
https://replit.com/@bchian316/Fruit-Farmer?lite=1&outputonly=1#main.py'''
game_is_running = True
first_fruit_dropped = False
import pygame
import os
import random
from time import time
from sys import exit
repl_name = os.environ["REPL_OWNER"]
if repl_name == "five-nine":
  print("Log into Replit to play this game!")
  exit()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(repl_name)
icon = pygame.image.load("fruit images/apple.png")
pygame.display.set_icon(icon)
background = pygame.image.load("images/background.png")
farmer_img = pygame.image.load("images/farmer.png")
big_farmer = pygame.transform.scale(farmer_img, (400, 400))
back_arrow = pygame.image.load("images/back arrow.png")
back_arrow = pygame.transform.scale(back_arrow, (48, 48))
left_arrow = pygame.image.load("images/left arrow.png")
right_arrow = pygame.image.load("images/right arrow.png")
money_icon = pygame.image.load("images/money.png")
apple_img = pygame.image.load("fruit images/apple.png")
lemon_img = pygame.image.load("fruit images/lemon.png")
grape_img = pygame.image.load("fruit images/grape.png")
orange_img = pygame.image.load("fruit images/orange.png")
banana_img = pygame.image.load("fruit images/banana.png")
raspberry_img = pygame.image.load("fruit images/raspberry.png")
melon_img = pygame.image.load("fruit images/melon.png")
grapefruit_img = pygame.image.load("fruit images/grapefruit.png")
pear_img = pygame.image.load("fruit images/pear.png")
peach_img = pygame.image.load("fruit images/peach.png")
apricot_img = pygame.image.load("fruit images/apricot.png")
plum_img = pygame.image.load("fruit images/plum.png")
blueberry_img = pygame.image.load("fruit images/blueberry.png")
coconut_img = pygame.image.load("fruit images/coconut.png")
strawberry_img = pygame.image.load("fruit images/strawberry.png")
blackberry_img = pygame.image.load("fruit images/blackberry.png")
cherry_img = pygame.image.load("fruit images/cherry.png")
kiwi_img = pygame.image.load("fruit images/kiwi.png")
guava_img = pygame.image.load("fruit images/guava.png")
pineapple_img = pygame.image.load("fruit images/pineapple.png")
lychee_img = pygame.image.load("fruit images/lychee.png")
watermelon_img = pygame.image.load("fruit images/watermelon.png")
mango_img = pygame.image.load("fruit images/mango.png")
nectarine_img = pygame.image.load("fruit images/nectarine.png")
persimmon_img = pygame.image.load("fruit images/persimmon.png")
dragonfruit_img = pygame.image.load("fruit images/dragon-fruit.png")
kumquat_img = pygame.image.load("fruit images/kumquat.png")
passionfruit_img = pygame.image.load("fruit images/passion-fruit.png")
pomegranate_img = pygame.image.load("fruit images/pomegranate.png")
starfruit_img = pygame.image.load("fruit images/star-fruit.png")
gmo_img = pygame.image.load("gmo.png")
clock = pygame.time.Clock()
FPS = 40
fruit_collection = []
showed_fruit = "Frequent"
showed_fruit_color = (255, 255, 255)
paused = False
home_screen = True
shop = False
playing = False
dictionary_status = False
mouse_clicked = False
mouse_up = True
mouse_down = False
unavailable_btn_color = (145, 145, 145, 145)
available_btn_color = (0, 255, 0)
hover_available_btn_color = (43, 186, 43)
unlock_common_lvl = 10
unlock_uncommon_lvl = 25
unlock_rare_lvl = 50
unlock_epic_lvl = 100
unlock_legendary_lvl = 250
ballx = 508
ball_direction = "right"
#player's stats
try:
  file = open(repl_name, "r")
except FileNotFoundError:
  with open(repl_name, "w") as file:
    file.write("0\n0\n0.5\n64.0\n30\n1")
finally:
  with open(repl_name, "r") as file:
    file_contents = file.read().split("\n")
highscore = int(file_contents[0])
money = int(file_contents[1])
player_speed = float(file_contents[2])
size = float(file_contents[3])
farmer = pygame.transform.scale(farmer_img, (round(size), round(size)))
level_time = int(file_contents[4])
level = int(file_contents[5])
file_num = 6
while file_num < len(file_contents):
  fruit_collection.append(str(file_contents[file_num]))
  file_num += 1
del(file_num)
del(file_contents)
points = 0
playerX = (SCREEN_WIDTH/2) - (size/2)
playerY = SCREEN_HEIGHT - size
font = "Comic Sans MS"
black = (0, 0, 0)
storage1 = None
storage2 = None
storage3 = None
size_price = 0
player_speed_price = 0
level_time_price = 0
#fruit
apple_stats = ["Apple", 250, 2.5, 32, apple_img]
lemon_stats = ["Lemon", 100, 2, 24, lemon_img]
grape_stats = ["Grape", 50, 4.5, 16, grape_img]
orange_stats = ["Orange", 300, 3, 32, orange_img]
banana_stats = ["Banana", 500, 4, 48, banana_img]
raspberry_stats = ["Raspberry", 500, 3.5, 24, raspberry_img]
melon_stats = ["Melon", 1000, 1.5, 56, melon_img]
grapefruit_stats = ["Grapefruit", 750, 2.5, 48, grapefruit_img]
pear_stats = ["Pear", 600, 3.5, 32, pear_img]
peach_stats = ["Peach", 850, 4, 24, peach_img]
apricot_stats = ["Apricot", 1000, 2, 32, apricot_img]
plum_stats = ["Plum", 1500, 4, 32, plum_img]
blueberry_stats = ["Blueberry", 1000, 5, 12, blueberry_img]
coconut_stats = ["Coconut", 1250, 4, 48, coconut_img]
strawberry_stats = ["Strawberry", 750, 3.5, 24, strawberry_img]
blackberry_stats = ["Blackberry", 2000, 4.5, 16, blackberry_img]
cherry_stats = ["Cherry", 2000, 4, 16, cherry_img]
kiwi_stats = ["Kiwi", 3250, 4, 24, kiwi_img]
guava_stats = ["Guava", 3000, 3, 48, guava_img]
pineapple_stats = ["Pineapple", 2500, 2.5, 56, pineapple_img]
lychee_stats = ["Lychee", 5000, 3, 24, lychee_img]
watermelon_stats = ["Watermelon", 10000, 5, 64, watermelon_img]
mango_stats = ["Mango", 4000, 3.5, 32, mango_img]
nectarine_stats = ["Nectarine", 7500, 4, 32, nectarine_img]
persimmon_stats = ["Persimmon", 8750, 3, 48, persimmon_img]
dragonfruit_stats = ["Dragon fruit", 20000, 3.5, 48, dragonfruit_img]#dragon comes and eats your fruit and drops dragonfruit
kumquat_stats = ["Kumquat", 17500, 4, 32, kumquat_img]
passionfruit_stats = ["Passion fruit", 15000, 3, 32, passionfruit_img]#blinks 1 second
pomegranate_stats = ["Pomegranate", 25000, 1.5, 56, pomegranate_img]#collect 10 seeds first
starfruit_stats = ["Star fruit", 22500, 5, 16, starfruit_img]
GMO = False
GMO_stats = ["GMO", 0, 4, range(32, 57, 8), gmo_img]
dict_list = [apple_stats, lemon_stats, grape_stats, orange_stats, banana_stats]
sprite_stagger = 150
def text(size, font, message, color, textx, texty, align = "left"):
  myfont = pygame.font.SysFont(font, size)
  text_width, text_height = myfont.size(message)
  text_surface = myfont.render(message, True, color)
  if align == "left":
    screen.blit(text_surface, (textx, texty))
  if align == "center":
    screen.blit(text_surface, (textx - (text_width/2), texty))
  if align == "right":
    screen.blit(text_surface, (textx - text_width, texty))
def button(x, y, width, height, radius = 0, cost = 0):
  global available_btn_color
  global unavailable_btn_color
  global hover_available_btn_color
  global mouse_position
  global mouse_clicked
  global money
  if money >= cost:
    if mouse_position[0] >= x and mouse_position[0] <= x + width and mouse_position[1] >= y and mouse_position[1] <= y + height:
      pygame.draw.rect(screen, hover_available_btn_color, (x, y, width, height), 0, radius)
      if mouse_clicked:
        return True
    else:
      pygame.draw.rect(screen, available_btn_color, (x, y, width, height), 0, radius)
  else:
    pygame.draw.rect(screen, unavailable_btn_color, (x, y, width, height), 0, radius)
  return False
def back_arrow_function():
  global shop, home_screen, dictionary_status, playing
  if button(0, 0, 48, 48, 15):
    home_screen = True
    shop = False
    dictionary_status = False
    playing = False
  screen.blit(back_arrow, (0, 0))
  text(24, font, "\'b\' for back", black, 0, 48)
class Fruit:
  all_fruit_on_screen_points_added_up = 0
  fruit_list = []
  def __init__(self, fruit_stats):
    global fruit_collection
    pygame.sprite.Sprite.__init__(self)
    global points
    global playing
    global sprite_stagger
    global GMO
    self.name = fruit_stats[0]
    self.points = fruit_stats[1]
    Fruit.all_fruit_on_screen_points_added_up += self.points
    self.fall_speed = fruit_stats[2]
    self.size = fruit_stats[3]
    self.image = fruit_stats[4]
    self.offset = random.randrange(-self.fall_speed * 2, self.fall_speed * 2 + 1)
    self.offset /= 2
    self.index_number = len(Fruit.fruit_list) - 1
    if GMO:
      self.points *= 1.5
      self.points = int(self.points)
      self.size *= 1.5
      self.image = pygame.transform.scale(self.image, (round(self.size), round(self.size)))
    self.x = random.randint(0, 800 - self.size)
    self.y = random.randint(-sprite_stagger, 0) - self.size
  def update(self):
    global points
    global level
    global playerX
    global size
    global GMO
    screen.blit(self.image, (self.x, self.y))
    self.y += self.fall_speed
    self.x += self.offset
    if self.x < 0 - self.size:
      self.x = 800 + self.size
    if self.x > 800 + self.size:
      self.x = 0 - self.size
    if self.x >= playerX - self.size and self.x <= playerX + size and self.y > (600 - size) - self.size and self.y <= 600:
      if self.name not in fruit_collection:
        fruit_collection.append(self.name)
      Fruit.all_fruit_on_screen_points_added_up -= self.points
      if GMO:
        Fruit.all_fruit_on_screen_points_added_up -= self.points * 0.5
      points += self.points
      Fruit.fruit_list.pop(self.index_number)
    if self.y > 600:
      Fruit.all_fruit_on_screen_points_added_up -= self.points
      if GMO:
        Fruit.all_fruit_on_screen_points_added_up -= self.points * 0.5
      Fruit.fruit_list.pop(self.index_number)
  def display(self, x, y, color):
    global black
    if self.name in fruit_collection:
      screen.blit(self.image, (x - ((self.size - 32)/2), (y - ((self.size - 32)/2))))
      text(75, font, str(self.name), color, x + 100, y)
      text(75, font, "$" + str(self.points), (255, 255, 0), x + 425, y)
      text(75, font, str(int(self.size/4)), (255, 0, 0), x + 600, y)
      text(75, font, str(int(self.fall_speed*2)), (0, 255, 0), x + 700, y)
    else:
      text(50, font, "???", black, x - 16, y)
      text(50, font, "???", color, x + 100, y)
      text(50, font, "???", (255, 255, 0), x + 425, y)
      text(50, font, "???", (255, 0, 0), x + 600, y)
      text(50, font, "???", (0, 255, 0), x + 700, y)
class Powerup:
  powerup_list = []
  def __init__(self, power_stats):
    global sprite_stagger
    self.name = power_stats[0]
    self.points = power_stats[1]
    self.fall_speed = power_stats[2]
    self.size = random.choice(power_stats[3])
    self.image = power_stats[4]
    self.x = random.randint(0, 800 - self.size)
    self.y = random.randint(-sprite_stagger, 0) - self.size
    self.index_number = len(Fruit.fruit_list) - 1
  def update(self):
    global points
    global level
    global playerX
    global size
    global GMO
    screen.blit(self.image, (self.x, self.y))
    self.y += self.fall_speed
    if self.x >= playerX - self.size and self.x <= playerX + size and self.y > (600 - size) - self.size and self.y <= 600:
      points += self.points
      Powerup.powerup_list.pop(self.index_number)
      if self.name == "GMO":
        GMO = True
    if self.y > 600:
      Powerup.powerup_list.pop(self.index_number)
class Timer:
  _list = []
  def __init__(self, seconds, running = False):
    self.start_time = time()
    self.end_time = time()
    self.time = seconds
    self.running = running
  def update(self):
    if self.running:
      self.end_time = time()
      if self.end_time - self.start_time >= self.time:
        return True
    return False
  def start(self, seconds):
    self.time = seconds
    self.running = True
    self.start_time = time()
    self.end_time = time()
  def stop(self):
    self.running = False
level_timer = Timer(level_time, running = False)
os.system("clear")
print("Use recommended link:\nhttps://replit.com/@bchian316/Fruit-Farmer?lite=1&outputonly=1#main.py")
while game_is_running:
  while game_is_running and home_screen:
    screen.blit(background, (0, 0))
    mouse_position = pygame.mouse.get_pos()
    mouse_position = list(mouse_position)
    if not(dictionary_status):
      text(175, font, "Fruit Farmer", black, 400, 0, align = "center")
      screen.blit(big_farmer, (200, 125))
      screen.blit(money_icon, (0, 100))
      text(75, font, "= $" + str(money), (255, 255, 0), 75, 105)
      text(50, font, "Highscore: " + str(highscore), (100, 255, 60), 800, 100, align = "right")
      text(20, "freesanbold.ttf ", "Press \'x\' to save and quit", (255, 0, 0), 800, 0, align = "right")
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_is_running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_s:
            home_screen = False
            shop = True
          if event.key == pygame.K_RETURN:
            home_screen = False
            playing = True
          if event.key == pygame.K_d:
            dictionary_status = True
          if event.key == pygame.K_x:
            game_is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_down = True
          if mouse_up == True:
            mouse_clicked = True
            mouse_up = False
        if event.type == pygame.MOUSEBUTTONUP:
          mouse_up = True
          mouse_down = False
      if button(25, 200, 200, 200, 50):
        home_screen = False
        shop = True
      if button(575, 200, 200, 200, 50):
        dictionary_status = True
      if button(150, 500, 500, 100, 50):
        home_screen = False
        playing = True
      text(75, font, "SHOP", (255, 255, 0), 125, 275, align = "center")
      text(30, font, "Click or press 's'", (0, 0, 0), 125, 325, align = "center")
      text(55, font, "Dictionary", (0, 0, 0), 675, 275, align = "center")
      text(30, font, "Click or press 'd'", (0, 0, 0), 675, 325, align = "center")
      text(100, font, "PLAY", (10, 100, 32), 400, 510, align = "center")
      text(30, font, "Click or press 'ENTER'", (0, 0, 0), 400, 575, align = "center")
    else:
      if showed_fruit == "Frequent":
        showed_fruit_color = (255, 255, 255)
      elif showed_fruit == "Common":
        showed_fruit_color = (51, 255, 255)
      elif showed_fruit == "Uncommon":
        showed_fruit_color = (255, 167, 51)
      elif showed_fruit == "Rare":
        showed_fruit_color = (51, 255, 58)
      elif showed_fruit == "Epic":
        showed_fruit_color = (132, 13, 184)
      else:
        showed_fruit_color = (223, 24, 245)
      text(100, font, "Dictionary", black, 225, 0)
      text(60, font, showed_fruit, black, 400, 60, align = "center")
      text(35, font, "Fruit", black, 40, 75, align = "center")
      text(35, font, "Name", black, 125, 75)
      text(35, font, "Money", black, 450, 75)
      text(35, font, "Size", black, 625, 75)
      text(35, font, "Speed", black, 725, 75)
      text(20, "freesanbold.ttf ", "Press \'x\' to save and quit", (255, 0, 0), 800, 0, align = "right")
      if(showed_fruit == "Frequent"):
        dict_list = [Fruit(apple_stats), Fruit(lemon_stats), Fruit(grape_stats), Fruit(orange_stats), Fruit(banana_stats)]
      if(showed_fruit == "Common"):
        dict_list = [Fruit(raspberry_stats), Fruit(melon_stats), Fruit(grapefruit_stats), Fruit(pear_stats), Fruit(peach_stats)]
      if(showed_fruit == "Uncommon"):
        dict_list = [Fruit(apricot_stats), Fruit(plum_stats), Fruit(blueberry_stats), Fruit(coconut_stats), Fruit(strawberry_stats)]
      if(showed_fruit == "Rare"):
        dict_list = [Fruit(blackberry_stats), Fruit(cherry_stats), Fruit(kiwi_stats), Fruit(guava_stats), Fruit(pineapple_stats)]
      if(showed_fruit == "Epic"):
        dict_list = [Fruit(lychee_stats), Fruit(watermelon_stats), Fruit(mango_stats), Fruit(nectarine_stats), Fruit(persimmon_stats)]
      if(showed_fruit == "Legendary"):
        dict_list = [Fruit(dragonfruit_stats), Fruit(kumquat_stats), Fruit(passionfruit_stats), Fruit(pomegranate_stats), Fruit(starfruit_stats)]
      if showed_fruit != "Frequent":
        screen.blit(left_arrow, (0, 576))
        text(24, font, "Previous", black, 32, 580)
      if showed_fruit != "Legendary":
        screen.blit(right_arrow,(776, 576))
        text(24, font, "Next", black, 732, 580)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_is_running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_x:
            game_is_running = False
          if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            if showed_fruit == "Common":
              showed_fruit = "Frequent"
            if showed_fruit == "Uncommon":
              showed_fruit = "Common"
            if showed_fruit == "Rare":
              showed_fruit = "Uncommon"
            if showed_fruit == "Epic":
              showed_fruit = "Rare"
            if showed_fruit == "Legendary":
              showed_fruit = "Epic"
          if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            if showed_fruit == "Epic":
              showed_fruit = "Legendary"
            if showed_fruit == "Rare":
              showed_fruit = "Epic"
            if showed_fruit == "Uncommon":
              showed_fruit = "Rare"
            if showed_fruit == "Common":
              showed_fruit = "Uncommon"
            if showed_fruit == "Frequent":
              showed_fruit = "Common"
          if event.key == pygame.K_b:
            dictionary_status = False
          if event.key == pygame.K_x:
            game_is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_down = True
          if mouse_up == True:
            mouse_clicked = True
            mouse_up = False
        if event.type == pygame.MOUSEBUTTONUP:
          mouse_up = True
          mouse_down = False
      back_arrow_function()
      for _ in enumerate(dict_list):
        _ = list(_)
        _[1].display(25, _[0] * 100 + 100, showed_fruit_color)
    clock.tick(FPS)
    if mouse_clicked:
      mouse_clicked = False
    pygame.display.update()
  while game_is_running and shop:
    screen.blit(background, (0, 0))
    text(100, font, "Shop", black, 325, 0)
    screen.blit(money_icon, (0, 100))
    text(75, font, "= $" + str(money), (255, 255, 0), 75, 105)
    text(20, "freesanbold.ttf ", "Press \'x\' to save and quit", (255, 0, 0), 800, 0, align = "right")
    mouse_position = pygame.mouse.get_pos()
    mouse_position = list(mouse_position)
    screen.blit(farmer, (184 - ((size - 32)/2), (400 - ((size - 32)/2))))
    pygame.draw.circle(screen, (0, 0, 0), (ballx, 400), 16)
    text(60, font, "Your size", black, 200, 300, align = "center")
    text(60, font, "Your speed", black, 600, 300, align = "center")
    text(60, font, "Your level time", black, 400, 225, align = "center")
    if level_time == 30:
      level_time = 29
      storage3 = 30
    level_time_price = round((30 - level_time) * 50000)
    if storage3 != None:
      level_time = 30
    if size == 64:
      size = 70.4
      storage2 = 64
    player_speed_price = round(player_speed * 100000)
    if player_speed == 0.5:
      player_speed = 0
      storage1 = 0.5
    size_price = round(100000 * ((size - 64)/12.8))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_is_running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_b:
          shop = False
          home_screen = True
        if event.key == pygame.K_x:
          game_is_running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_down = True
        if mouse_up == True:
          mouse_clicked = True
          mouse_up = False
      if event.type == pygame.MOUSEBUTTONUP:
        mouse_up = True
        mouse_down = False
    if storage1 != None:
      player_speed = 0.5
    if storage2 != None:
      size = 64
    storage2 = None
    #for size
    if button(100, 500, 200, 50, 50, size_price):
      if size < 192:
        if money >= size_price:
          size += 12.8
          size = round(size, 1)
          playerY = 600 - size
          money -= size_price
          farmer = pygame.transform.scale(farmer_img, (round(size), round(size)))
    if size == 192:
      pygame.draw.rect(screen, (0, 255, 0), (100, 500, 200, 50), 0, 50)
    if button(500, 500, 200, 50, 50, player_speed_price):
      if player_speed < 10:
        if money >= player_speed_price:
          if storage1 != None:
            player_speed += 0.5
            player_speed = int(player_speed)
            money -= player_speed_price
          else:
            money -= player_speed_price
            player_speed += 1
    if player_speed == 10.0:
      pygame.draw.rect(screen, (0, 255, 0), (500, 500, 200, 50), 0, 50)
    if button(300, 400, 200, 50, 50, level_time_price):
      if level_time > 10:
        if money >= level_time_price:
          level_time -= 2
          money -= level_time_price
    if level_time == 10:
      pygame.draw.rect(screen, (0, 255, 0), (300, 400, 200, 50), 0, 50)
    storage1 = None
    back_arrow_function()
    text(35, font, "Size", black, 200, 500, align = "center")
    if size < 192:
      text(25, font, "Level " + str(round(size_price/100000)), black, 100, 525)
      text(25, font, "$" + str(size_price), (255, 255, 0), 225, 525)
    else:
      text(25, font, "Max Level", (255, 255, 0), 160, 525)
    #for speed
    text(35, font, "Speed", black, 600, 500, align = "center")
    if player_speed < 10:
      text(25, font, "Level " + str(round(player_speed)), black, 500, 525)
      if storage1 != None:
        player_speed = 0.5
      text(25, font, "$" + str(player_speed_price), (255, 255, 0), 625, 525)
    else:
      text(25, font, "Max Level", (255, 255, 0), 550, 525)
    #for level time
    text(35, font, "Level Time", black, 400, 400, align = "center")
    if level_time > 10:
      text(25, font, "Level " + str(round(level_time_price/100000)), black, 300, 425)
      text(25, font, "$" + str(level_time_price), (255, 255, 0), 425, 425)
    else:
      text(25, font, "Max Level", (255, 255, 0), 350, 425)
    if ball_direction == "left":
      ballx -= player_speed
    if ball_direction == "right":
      ballx += player_speed
    if ballx <= 508:
      ball_direction = "right"
    if ballx >= 692:
      ball_direction = "left"
    if storage3 != None:
      level_time_price = 0
    text(75, font, str(30 - (level_time_price / 50000)), (255, 255, 255), 350, 275)
    storage3 = None
    text(75, font, " seconds", (255, 255, 255), 300, 325)
    clock.tick(FPS)
    if mouse_clicked:
      mouse_clicked = False
    pygame.display.update()
  ball_direction = "right"
  ballx = 508
  Fruit.all_fruit_on_screen_points_added_up = 0
  if first_fruit_dropped == False:
    Fruit.fruit_list.append(Fruit(apple_stats))
    Fruit.all_fruit_on_screen_points_added_up += 250
    first_fruit_dropped = True
    #Powerup.powerup_list.append(Powerup(GMO_stats))
  playerX = 400 - (size/2)
  level_timer.start(level_time)
  while game_is_running and playing:
    pressed_keys = pygame.key.get_pressed()
    screen.blit(background, (0, 0))
    mouse_position = pygame.mouse.get_pos()
    mouse_position = list(mouse_position)
    text(100, font, str(points), (255, 255, 0), 0, 50)
    text(20, "freesanbold.ttf ", "Press \'x\' to save and quit", (255, 0, 0), 800, 0, align = "right")
    text(50, font, "Level " + str(level), (255, 255, 0), 0, 550)
    if points > highscore:
      text(40, font, "Achieved New Highscore!", (0, 255, 0), 400, 0, align = "center")
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_is_running = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
          game_is_running = False
          break
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_down = True
        if mouse_up == True:
          mouse_clicked = True
          mouse_up = False
      if event.type == pygame.MOUSEBUTTONUP:
        mouse_up = True
        mouse_down = False
    #This one doesn't work for some reason
    back_arrow_function()
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
      playerX -= player_speed
    if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
      playerX += player_speed
    if pressed_keys[pygame.K_b]:
      playing = False
      home_screen = True
      break
    if playerX < 0 - size:
      playerX = 800 + size
    if playerX > 800 + size:
      playerX = 0 - size
    screen.blit(farmer, (playerX, playerY))
    if level_timer.update():
      level += 1
      level_timer.start(level_time)
    for fruit in Fruit.fruit_list:
      Fruit.all_fruit_on_screen_points_added_up += fruit.points
    while Fruit.all_fruit_on_screen_points_added_up < level * 100:
      random_num = random.randint(0, 1000)
      if random_num <= 500:
        Fruit.fruit_list.append(Fruit(random.choice([lemon_stats, grape_stats, apple_stats, orange_stats, banana_stats])))
      if random_num > 500 and random_num <= 800 and level >= unlock_common_lvl:
        Fruit.fruit_list.append(Fruit(random.choice([raspberry_stats, melon_stats, grapefruit_stats, pear_stats, peach_stats])))
      if random_num > 800 and random_num <= 950 and level >= unlock_uncommon_lvl:
        Fruit.fruit_list.append(Fruit(random.choice([apricot_stats, plum_stats, blueberry_stats, coconut_stats, strawberry_stats])))
      if random_num > 950 and random_num <= 990 and level >= unlock_rare_lvl:
        Fruit.fruit_list.append(Fruit(random.choice([blackberry_stats, cherry_stats, kiwi_stats, guava_stats, pineapple_stats])))
      if random_num > 990 and random_num <= 999 and level >= unlock_epic_lvl:
        Fruit.fruit_list.append(Fruit(random.choice([lychee_stats, watermelon_stats, mango_stats, nectarine_stats, persimmon_stats])))
      if random_num > 999 and level >= unlock_legendary_lvl:
        Fruit.fruit_list.append(Fruit(random.choice([dragonfruit_stats, kumquat_stats, pomegranate_stats, passionfruit_stats, starfruit_stats])))
    for fruit in Fruit.fruit_list:
      fruit.index_number = Fruit.fruit_list.index(fruit)
    for fruit in Fruit.fruit_list[:]:
      fruit.update()
    Fruit.all_fruit_on_screen_points_added_up = 0
    for power in Powerup.powerup_list[:]:
      power.update()
    clock.tick(FPS)
    if mouse_clicked:
      mouse_clicked = False
    pygame.display.update()
  level_timer.stop()
  first_fruit_dropped = False
  Fruit.fruit_list = []
  Powerup.powerup_list = []
  GMO = False
  money += points
  if points > highscore:
    highscore = points
  points = 0
  Fruit.all_fruit_on_screen_points_added_up = 0
  continue
file = open(repl_name, "w")
file.write(str(highscore) + "\n" + str(money) + "\n" + str(player_speed) + "\n" + str(size) + "\n" + str(level_time) + "\n" + str(level))
for _ in fruit_collection:
  file.write("\n" + str(_))
file.close()
pygame.quit()
print("Progress saved!")
 
 