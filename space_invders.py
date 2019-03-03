# Space Invaders
# Created by Fajar Afriansh

import turtle
import os
from os.path import abspath, dirname
import math
import random

basePath = abspath(dirname(__file__))
imagePath = basePath + "/images/"
soundPath = basePath + "/sounds/"
fontPath = basePath + "/fonts/"

#Set up the screen
windows = turtle.Screen()
windows.bgcolor("black")
windows.title("Space Invaders")
windows.bgpic(imagePath + "background.gif")

enemy_img = imagePath + "enemy.gif"
ship_img = imagePath + "ship.gif"
laser_img = imagePath + "ship-laser.gif"
fonts = fontPath + "space_invaders.ttf"
shoot = soundPath + "shoot.wav"

turtle.register_shape(enemy_img)
turtle.register_shape(ship_img)
turtle.register_shape(laser_img)

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.forward(600)
	border_pen.left(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("Gold")
score_pen.penup()
score_pen.setposition(-290, 270)
scoreString = "Score: %s" %score
score_pen.write(scoreString, False, align="left", font=(fonts, 14, "normal"))
score_pen.hideturtle()

#The player turtle
player = turtle.Turtle()
player.shape(ship_img)
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.shapesize(35, 35)

playerSpeed = 15

#Player move left or right
def move_left():
	x = player.xcor()
	x -= playerSpeed
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerSpeed
	if x > 280:
		x = 280
	player.setx(x)

#The player's bullet
bullet = turtle.Turtle()
bullet.shape(laser_img)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(5, 15)
bullet.hideturtle()

bulletSpeed = 20

#The bullet state
bulletState =  "ready"

def fire_bullet():
	global bulletState
	if bulletState == "ready":
	# os.startfile("D:/Dev/Game/space-invaders/sounds/shoot.wav")
		bulletState = "fire"
		x = player.xcor()
		y = player.ycor() +10
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

#The number of anemies
number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
	#The enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.shape(enemy_img)
	enemy.penup()
	enemy.speed(0)
	enemy.shapesize(30, 30)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemySpeed = 2


#The keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#The main loop
while True:

	for enemy in enemies:
		#Enemy move
		x = enemy.xcor()
		x += enemySpeed
		enemy.setx(x)

		#Enemy move back and down
		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemySpeed *= -1

		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemySpeed *= -1

		# Check for the collition between bullet and anemy
		if isCollision(bullet, enemy):
			bullet.hideturtle()
			bulletState = "ready"
			bullet.setposition(0, -400)
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			# Update the Score
			score += 10
			scoreString = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))

	if isCollision(player, enemy):
		player.hideturtle()
		enemy.hideturtle()
		print("Game Over")
		break

	#The bullet move
	if bulletState == "fire":
		y = bullet.ycor()
		y += bulletSpeed
		bullet.sety(y)

	#The bullet check
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletState ="ready"

delay = input("Press Enter to Finish.")