import pgzero
import pgzrun
import pygame
import random
from pgzero.builtins import Actor

WIDTH = 500
HEIGHT = 500

White = (255,255,255)
Blue = (0,0,255)

Ship = Actor("ship2")
Enemy = Actor("ship1")

Ship.pos = (WIDTH // 2, HEIGHT - 50)
BulletSpeed = 5
ShipSpeed = 5
EnemySpeed = 5
Bullets = []
Enemies = []
Enemies.append(Actor("ship1"))
Enemies[-1].x = 10
Enemies[-1].y = -100

Score = 0

for i in range(8):
    Enemies.append(Actor("ship1"))
    Enemies[-1].x = 100 + 90 * i
    Enemies[-1].y =  100 + 90 * i

'''def on_key_down(key):
    if key == keys.SPACE:
        Bullets.append(Actor("bullet"))
        Bullets[-1].x = Ship.x
        Bullets[-1].y = Ship.y - 15
'''

def display_score():
    global Score
    screen.draw.text(str(Score), (50,50))

def update():
    global Score,ShipSpeed,Bullets,BulletSpeed,Enemies,EnemySpeed
    if keyboard.left:
        Ship.x -= ShipSpeed
        if Ship.x <= 0:
            Ship.x = 0

    if keyboard.right:
        Ship.x += ShipSpeed
        if Ship.x >= WIDTH:
            Ship.x = WIDTH
    

    if keyboard.space:
        sounds.eep.play()
        Bullets.append(Actor("bullet"))
        Bullets[-1].x = Ship.x
        Bullets[-1].y = Ship.y - 15


    for bullet in Bullets:
        if bullet.y <= 0:
            Bullets.remove(bullet)
        else:
            bullet.y -= BulletSpeed

    for enemy in Enemies:
        enemy.y += EnemySpeed
        if enemy.y >= HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(50,WIDTH - 50)

        for bullet in Bullets:
            if enemy.colliderect(bullet):
                sounds.eep.play()
                Score += 1
                Bullets.remove(bullet)
                Enemies.remove(enemy)



def draw():
    screen.clear()
    screen.fill(Blue)
    for bullet in Bullets:
        bullet.draw()

    for enemy in Enemies:
        enemy.draw()

    Ship.draw()
    display_score()


pgzrun.go()