
from gamelib import *


game =  Game(900,800, "A Way Home")

#Graphic Set Up
logo = Image("A-Way-Home.png",game)
howtoplay = Image("How-To-Play.png",game)
play = Image("play.png",game)
bk = Image("1.jpg",game)
bk.resizeTo(1000,1000)
mc2 = Animation("mc2.png",8,game,196/4,176/2)
mc2.resizeBy(100)
mc2.moveTo(50,700)
ms = Image("mine_shaft.png",game)
ms.resizeBy(20)
keyboard = Image("keyboard.png",game)
arrow = Image("arrow.png",game)
arrow.resizeBy(-80)
back = Image("Back.png",game)
js = Animation("Jem.png",6,game,90/3,104/2)
js.resizeBy(550)
js.moveTo(830,650)
story = Image("Story.png",game)
bm = Sound("Fantasy Game Loop.wav",1)
sb = Image("Story Bg.png",game)
ssb1 = Image("speechbubble1.gif",game)
ssb1.moveTo(223,420)
ssb2 = Image("speechbubble2.gif",game)
ssb2.moveTo(200,600)
ssb3 = Image("speechbubble3.gif",game)
ssb3.moveTo(200,405)
ssb4 = Image("speechbubble4.gif",game)
ssb4.moveTo(200,405)
arrow2 = Image("ar.png",game)
arrow2.moveTo(830,650)
arrow2.resizeBy(20)


#Falling Rocks
rock = []
for index in range (30):
    rock.append( Image("Rocks.png",game))

for index in range (30):
        x = randint(100,900)
        y = randint(100,900)
        s = randint(1,10)
        rock[index].setSpeed(s,180)
        rock[index].resizeBy(-90)
        rock[index].moveTo(x,-y)
            
#Start Up Screen
while not game.over:
    game.processInput()
    bk.draw()
    logo.draw()
    logo.moveTo(450,300)
    howtoplay.draw()
    howtoplay.moveTo(450,600)
    play.draw()
    play.moveTo(450,500)
    js.draw()
    mc2.draw()
    mc2.stop()
    bm.play()



    if howtoplay.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
        keyboard.draw()
        arrow.draw()
        back.draw()
        back.moveTo(110,60)
        arrow.moveTo(685,650)
    
        game.drawText("To move the character, you have to use the up, down, right, left arrows. To throw, press the spacebar", 100,700)


        
    game.update(30)
game.over = False


#How to play Set up Screen
while not game.over:
    game.processInput()
    game.clearBackground()
    keyboard.draw()
    arrow.draw()
    back.draw()
    back.moveTo(110,60)
    arrow.moveTo(685,650)
    
    game.drawText("To move the character, you have to use the up, down, right, left arrows. To throw, press the spacebar", 100,700)

    if back.collidedWith(mouse) and mouse.LeftClick:
         game.over = True

    game.update(30)
game.over = False

    

#Back to Start Screen
while not game.over:
    game.processInput()
    game.clearBackground()
    bk.draw()
    logo.draw()
    logo.moveTo(450,300)
    howtoplay.draw()
    howtoplay.moveTo(450,700)
    play.draw()
    play.moveTo(450,600)
    js.draw()
    mc2.draw()

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(30)


game.over = False


#Story
timeframe = 0
while not game.over:
    game.processInput()
    game.clearBackground()
    sb.draw()
    mc2.draw()
    mc2.stop()

    timeframe += 0.5
    print(timeframe)

    if timeframe >= 0 and timeframe <= 100:
        ssb1.draw()
    elif timeframe >= 100 and timeframe <= 200:
        ssb2.draw()
    elif timeframe >= 200 and timeframe <= 300:
        ssb3.draw()
    elif timeframe >= 300 and timeframe <= 400:
        ssb4.draw()
    elif timeframe >= 500 and timeframe <= 600:
        arrow2.draw()

    if mouse.LeftClick(arrow2):
        game.over = True
        
    
        
    game.update(30)
game.over = False

#Level 1
while not game.over:
    game.processInput()
    game.clearBackground()
    ms.draw()
    mc2.draw()
    mc2.stop()
    js.draw()

    for index in range(30):
        rock[index].move()
        if rock[index].collidedWith(mc2):
                mc2.health -=10
                rock[index].visible = False

    
    
#Hero Control
    if keys.Pressed[K_LEFT]:
        mc2.prevFrame()
        mc2.x -=5

    if keys.Pressed[K_RIGHT]:
        mc2.nextFrame()
        mc2.x +=5

    if keys.Pressed[K_UP]:
        mc2.prevFrame()
        mc2.y -=5

    if keys.Pressed[K_DOWN]:
        mc2.nextFrame()
        mc2.y +=5

    if mc2.health < 5:
        game.over = True

    game.drawText("Health" + str(mc2.health),mc2.x, mc2.y +80)

    if mc2.collidedWith(js):
        game.over = True

    game.update(30)
game.quit()


    
    

    
