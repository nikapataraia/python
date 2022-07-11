#start manu,audio,advanced scoreboard,ending screen,scoreboard,forbiding 180 turns (everything but the visuals(pictures for snake and apples))
from ast import Break
from pickle import TRUE
import random
from tarfile import TarInfo
from tkinter import CENTER, Y
from tokenize import Special
from turtle import Screen
import pygame
class App:
    apples_eaten = 0
    ##################fruit#################################
    class fruit :
        onmap = False
        special = False
        def __init__(self,x = 0,y = 0,rando = 0):
            self.x = x*20
            self.y = y*20
            self.rando = rando
        def draw_fruit(self,screen):
            fruit = pygame.Rect(self.x,self.y,20,20)
            if (self.rando==5):
                App.fruit.special = True
                pygame.draw.circle(screen,(238,190,0),(self.x + 10, self.y  +10),10)
            else : pygame.draw.circle(screen,(156,3,3),(self.x + 10, self.y  +10),10)

            App.fruit.onmap = True
        @ classmethod
        def consume(cls):
            if(App.fruit.special):
                 App.apples_eaten = App.apples_eaten + 3
            else :
                 App.apples_eaten = App.apples_eaten + 1
            cls.onmap = False
            App.fruit.special = False
       
    ################snake###################################
    class snake :
        def __init__(self,x = 0, y = 0, difficulty = 0):
            self.body = [(x*20,y*20),(x*20,(y+1)*20)]
            self.direction = 1
            self.difficulty = difficulty
        def drawsnake(self,screen):
            for blk in self.body:
                body = pygame.Rect(blk[0],blk[1],20,20)
                pygame.draw.rect(screen,(20,27,21),body)
        def grow(self,x,y):
            self.body.append((x*20,y*20))
        def changedirection(self,To):
            if(self.direction%2 == To%2):pass
            else: self.direction = To
        def move(self,fruitcords):
            # savedcords = self.body[0]
            cord = self.body[0]
            if(self.direction == 0): cord = ((self.body[0])[0]-20,(self.body[0])[1])
            if(self.direction == 1): cord = ((self.body[0])[0],(self.body[0])[1] -20)
            if(self.direction == 2): cord = ((self.body[0])[0]+20,(self.body[0])[1])
            if(self.direction == 3): cord = ((self.body[0])[0],(self.body[0])[1]+20)
            self.body.insert(0,cord)
            tail = self.body.pop()
            if(fruitcords == self.body[0]):
                self.body.append(tail)
                App.fruit.consume()
                crunchsound = pygame.mixer.Sound('sounds/Sound_crunch.wav')
                crunchsound.play()
            # temp = self.body[0]
            # for index in range(1,self.body):
            #     temp = self.body[index]
            #     self.body[index] = savedcords
            #     savedcords = temp
    ####################buttons##############################
    class buttons:
        def __init__(self,x,y) :
         self.x = x
         self.y = y
        def draw(self,screen):
            button = pygame.Rect(self.x,self.y,200,100)
            pygame.draw.rect(screen,(153,0,0),button)
            posofmouse = pygame.mouse.get_pos()
            if button.collidepoint(posofmouse):
                if pygame.mouse.get_pressed()[0] == 1:
                    return True
            return False
    

    ###################constructor################################
    def __init__(self):
        self.difficulty = 0
        self.running = False
        self.clock = None
        self.screen = None
        self.snake = App.snake(29,17)
        self.fruit = App.fruit()

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()
    
    def rerun(self):
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        pygame.init()
        pygame.mixer.music.load('sounds/background.mp3')
        pygame.mixer.music.play(-1)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((700, 700))
        start_but = App.buttons(250,150)
        self.clientfont = pygame.font.Font(None,30)
        start = False
        self.screen.fill((202,228,241))
        self.pressingstart = pygame.USEREVENT
        starttxt = self.clientfont.render("START:",True,(51,0,0))
        self.screen.blit(starttxt,starttxt.get_rect(center = (350,120)))


        warning = self.clientfont.render("press 'm' to mute/unmute music",True,(51,0,0))
        self.screen.blit(warning,warning.get_rect(center = (350,420)))


        while(not start):
         start = start_but.draw(self.screen)
         pygame.display.update()
         self.clock.tick(60)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_m):
                    if(pygame.mixer.music.get_busy()):
                     pygame.mixer.music.pause()
                    else :pygame.mixer.music.unpause()
        pygame.display.update()
        
        ###########################################
        self.screen = pygame.display.set_mode((1200, 700))
        self.screen.fill((202,228,241))
        pygame.display.set_caption("Snake")
        self.running = True
        self.Timer_up = pygame.USEREVENT
        pygame.time.set_timer(self.Timer_up,150)
        pygame.display.update()

    def update(self):
        self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == self.Timer_up:
                self.snake.move((self.fruit.x,self.fruit.y))
                if(self.snake.body[0] in self.snake.body[1:len(self.snake.body)]):
                    self.running = False
                    pygame.mixer.Sound('sounds/bonk-sound-effect.mp3').play()
                if(self.snake.body[0][0] < 0 or self.snake.body[0][1] <= 20 or self.snake.body[0][0] > 1180 or self.snake.body[0][1] > 680):
                    self.running = False
                    pygame.mixer.Sound('sounds/bonk-sound-effect.mp3').play()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_w or event.key == pygame.K_UP):
                    self.snake.changedirection(1)
                if (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    self.snake.changedirection(0)
                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                    self.snake.changedirection(2)
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                    self.snake.changedirection(3)
                if (event.key == pygame.K_m):
                    if(pygame.mixer.music.get_busy()):
                     pygame.mixer.music.pause()
                    else :pygame.mixer.music.unpause()
                    
            # if event.type == self.Timerforbackground:
            #     self.backgroundmusic.play()


    def render(self):
        self.screen.fill((42,179,56))
        ###music

        ####fruit
        if (not App.fruit.onmap):
         x = random.randint(0,59)
         y = random.randint(2,34)
         while((x*20,y*20) in self.snake.body):
            x = random.randint(2,59)
            y = random.randint(0,34)
         self.fruit = App.fruit(x,y,x%10)
         self.fruit.draw_fruit(self.screen)
        ###
        else: self.fruit.draw_fruit(self.screen)
        self.snake.drawsnake(self.screen)
        score_sur = self.clientfont.render("current score -> " + str(App.apples_eaten),True,(242,240,231))
        self.screen.blit(score_sur,score_sur.get_rect(center = (1200-160,20)))
        pygame.draw.line(self.screen,(17,14,4),(0,40),(1200,40),5)
        pygame.display.update()
        self.clock.tick(60)
    
#############################################
    def cleanUp(self):
        exit = False
        endscreen = pygame.display.set_mode((550, 500))
        end_but = App.buttons(150,120)
        replay_but = App.buttons(150,320)
        EXITbut = self.clientfont.render("EXIT",True,(255,255,255))
        endscreen.blit(EXITbut,EXITbut.get_rect(center = (250,110))) 
        REPLAYbut = self.clientfont.render("REPLAY",True,(255,255,255))
        endscreen.blit(REPLAYbut ,REPLAYbut .get_rect(center = (250,310))) 
        top_scores = self.clientfont.render("TOP SCORES",True,(255,255,255))
        endscreen.blit(top_scores,top_scores.get_rect(center = (450,20)))
        myscore = self.clientfont.render("Your score was : " + str(App.apples_eaten),True,(255,255,255))
        endscreen.blit(myscore ,myscore .get_rect(center = (250,40))) 
        pygame.display.set_caption("You lost")
        scoreslst = []
        with open("snake_scores.txt") as topscores:
            for line in topscores:
                scoreslst.append(int(line.rstrip()))
            if(len(scoreslst) < 10):
                scoreslst.append(App.apples_eaten)
            else :
                getlowest = min(scoreslst)
                if(getlowest < App.apples_eaten):
                 scoreslst.remove(getlowest)
                 scoreslst.append(App.apples_eaten)
            scoreslst.sort()
            with open("snake_scores.txt","w") as writescores:
             for el in scoreslst:
                 writescores.write(str(el) + "\n")
        playagain = False
        while (not exit):
             exit = end_but.draw(endscreen)
             pygame.display.update()
             x = 0
             for el in scoreslst:
                x=x+20
                top_board = self.clientfont.render(str(el),True,(255,255,255))
                endscreen.blit(top_board,top_board.get_rect(center = (450,20 + x)))
             if (replay_but.draw(screen=endscreen)):
                playagain = True
                exit = True
             pygame.display.update()
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     self.running = False
                 if event.type == pygame.KEYDOWN:
                   if (event.key == pygame.K_m):
                    if(pygame.mixer.music.get_busy()):
                     pygame.mixer.music.pause()
                    else :pygame.mixer.music.unpause()
                    

            
        App.apples_eaten = 0
        if(playagain): 
            App.fruit.onmap = False
            App.fruit.special = False
            app = App()
            app.run()


if __name__ == "__main__":
    app = App()
    app.run()