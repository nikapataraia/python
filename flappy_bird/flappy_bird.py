#[better visual,end screen, infinite game,menu,audio,start manu] (everything)
from asyncio.windows_utils import pipe
from random import randint, random
from socketserver import DatagramRequestHandler
import pygame

class App:
    coinscollected = 0
    mapsize = 5000
    checkdistance = 0
    onlvl = 0
    difficulty = 0
    ###########buttons###########
    class buttons:
        def __init__(self,x,y,color = (153,0,0)) :
         self.x = x
         self.y = y
         self.color = color
        def draw(self,screen):
            button = pygame.Rect(self.x,self.y,200,100)
            pygame.draw.rect(screen,self.color,button)
            posofmouse = pygame.mouse.get_pos()
            if button.collidepoint(posofmouse):
                if pygame.mouse.get_pressed()[0] == 1:
                    return True
            return False
    ###############bird#################
    class bird(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.images = [pygame.image.load('flappy_designs/bird1.png'),pygame.image.load('flappy_designs/bird2.png'),pygame.image.load('flappy_designs/bird3.png')]
            self.anidexs = 2
            self.cooldown = 0
            self.image = self.images[self.anidexs]
            self.rect = self.image.get_rect()
            self.rect.center = [x,y]
            self.velocity = 0
            self.pressed = False

        def update(self): ##override
            if(self.velocity == 10):
                self.velocity = 10
            else : self.velocity += 0.5
            self.rect.y = self.rect.y + int(self.velocity)
            self.cooldown += 1
            if self.cooldown == 10:
                self.cooldown = 0
                if (self.anidexs == 2):
                    self.anidexs = 0
                else:
                    self.anidexs += 1
            self.image = self.images[self.anidexs]
            self.image = pygame.transform.rotate(self.images[self.anidexs], -self.velocity * 1.5)
            if (pygame.mouse.get_pressed()[0] == 1 and not self.pressed):
                self.velocity = -10
                self.pressed = True
            if (pygame.mouse.get_pressed()[0] == 0):
                self.pressed = False
        def startmovingright(self):
            self.rect.x = self.rect.x + 6
    ###coins
    class coins(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.image = pygame.image.load('flappy_designs/coin2.png')
            self.rect = self.image.get_rect()
            self.rect.bottomleft = [x,y]
        def update(self):
            if(App.difficulty == 0):
             self.rect.x = self.rect.x - 4
            if(App.difficulty == 1 or App.difficulty == 2):
                self.rect.x = self.rect.x - 6
            if(self.rect.x<-100):
                self.kill()

            
    ####################pipe########
    class pipe(pygame.sprite.Sprite):
        def __init__(self,x,y,top):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('flappy_designs/pipe.png')
            self.rect = self.image.get_rect()
            self.rect.topleft = [x,y]
            if(top):
                self.image = pygame.transform.flip(self.image,False,True)
                self.rect.bottomleft = [x,y]
        def update(self):
            if(App.difficulty == 0):
             self.rect.x = self.rect.x - 4
            if(App.difficulty == 1 or App.difficulty == 2):
                self.rect.x = self.rect.x - 6
            if(self.rect.x<-100):
                self.kill()

            
    ############constr###################
    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.screen_width = 864
        self.screen_height = 986
        self.gap = 250
        self.pipe_frequency = 1500
        self.last = pygame.time.get_ticks()
        self.coinsonmap = []
        self.won = False
    ###########################
    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        #########start#################
        pygame.init()
        pygame.mixer.music.load('sounds/background.mp3')
        pygame.mixer.music.play(-1)
        self.clock = pygame.time.Clock()
        self.running = True
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
        self.screen.blit(warning,warning.get_rect(center = (610,680)))

        diff = self.clientfont.render("press button to chose difficulty",True,(51,0,0))
        self.screen.blit(diff,diff.get_rect(center = (350,350)))

        clrs = self.clientfont.render("green -> eazy, yellow -> normal, red -> hard",True,(51,0,0))
        self.screen.blit(clrs,clrs.get_rect(center = (350,400)))
        green_but = App.buttons(50,450,(42,179,56))
        yellow_but = App.buttons(250,450,(250,208,21))
        red_button = App.buttons(450,450,(255,0,0))
        while(not start):
         start = start_but.draw(self.screen)
         if(green_but.draw(self.screen)):
            App.difficulty = 0
         if(yellow_but.draw(self.screen)):
            App.difficulty = 1
         if(red_button.draw(self.screen)):
            App.difficulty = 2
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
        self.birds = pygame.sprite.Group()
        self.birdmvp = App.bird(100,self.screen_height/2)
        self.pipes = pygame.sprite.Group()
        self.coinsonmap = pygame.sprite.Group()
        self.birds.add(self.birdmvp)
        pygame.display.update()
#########################
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background_img =pygame.image.load('flappy_designs/bg.png')
        self.ground_img = pygame.image.load('flappy_designs/ground.png')
        pygame.display.set_caption("OMG BIIIIRDS")
        self.birds.draw(self.screen)
        self.birdspeed = 5
        self.xcordforground = 0
        self.running = True
        self.pipe_frequency = 1500 - App.difficulty*300 #for difficulty
        pygame.display.update()


    def update(self):
        self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_m):
                    if(pygame.mixer.music.get_busy()):
                     pygame.mixer.music.pause()
                    else :pygame.mixer.music.unpause()
                if event.key == pygame.K_SPACE:
                        self.birdmvp.velocity = -10
                    

    def render(self):
        ###background##
        self.xcordforground = self.xcordforground - self.birdspeed
        if (self.xcordforground <= -35):
            self.xcordforground = 0
        self.screen.blit(self.background_img,(0,50))
        self.screen.blit(self.ground_img,(self.xcordforground,818))

        ########pipes/coins########
        if(App.checkdistance + 400 < App.mapsize):
         time = pygame.time.get_ticks()
         if time - self.last > self.pipe_frequency:
            x = randint(-200,200)
            botpipe = App.pipe(self.screen_width,self.screen_height/2 +x +self.gap/2,False)
            toppipe = App.pipe(self.screen_width,self.screen_height/2 +x - self.gap/2,True)
            self.pipes.add(botpipe,toppipe)
            self.last = time
            if(x%3 == 0):
                newcoin = App.coins(self.screen_width + 30,self.screen_height/2 +x +self.gap/2 - 100)
                self.coinsonmap.add(newcoin)
        self.pipes.draw(self.screen)
        self.coinsonmap.draw(self.screen)
        self.pipes.update()
        self.coinsonmap.update()
        ###bird###
        self.birds.draw(self.screen)
        if(App.checkdistance > App.mapsize):
            self.birdmvp.startmovingright()
        self.birds.update()
        for el in self.birds:
            if(pygame.sprite.spritecollide(el,self.coinsonmap,True,False)):
                App.coinscollected = App.coinscollected + 1
        if (self.birdmvp.rect.bottom > 858 or self.birdmvp.rect.top < 50):
            self.running = False
            self.won = False
            pygame.mixer.Sound('sounds/bonk-sound-effect.mp3').play()
        if (self.birdmvp.rect.right >= self.screen_width):
            self.won = True
            App.checkdistance = 0
            self.birdmvp.rect.x = 100
            App.onlvl = App.onlvl + 1
        if(pygame.sprite.groupcollide(self.birds,self.pipes,False,False)):
            self.running = False
            self.won = False
            pygame.mixer.Sound('sounds/bonk-sound-effect.mp3').play()
        ###########
        score_sur = self.clientfont.render("coins collected -> " + str(App.coinscollected),True,(242,240,231))
        self.screen.blit(score_sur,score_sur.get_rect(center = (self.screen_width - 200 , 25)))

        onlvl = self.clientfont.render("On level -> " + str(App.onlvl),True,(242,240,231))
        self.screen.blit(onlvl,onlvl.get_rect(center = (100 , 25)))
        self.clock.tick(60)
        App.checkdistance = App.checkdistance + 4
        pygame.display.update()





 ###############################end client#############
    def cleanUp(self):
        exit = False
        endscreen = pygame.display.set_mode((550, 600))
        end_but = App.buttons(150,220)
        replay_but = App.buttons(150,420)
        EXITbut = self.clientfont.render("EXIT",True,(255,255,255))
        endscreen.blit(EXITbut,EXITbut.get_rect(center = (250,210))) 
        REPLAYbut = self.clientfont.render("REPLAY",True,(255,255,255))
        endscreen.blit(REPLAYbut ,REPLAYbut .get_rect(center = (250,410))) 
        top_scores = self.clientfont.render("TOP SCORES",True,(255,255,255))
        endscreen.blit(top_scores,top_scores.get_rect(center = (450,20)))
        myscore = self.clientfont.render("coins collected : " + str(App.coinscollected),True,(255,255,255))
        endscreen.blit(myscore ,myscore .get_rect(center = (250,100))) 

        winlose = self.clientfont.render("congrats you " + str(self.won),True,(255,255,255))
        endscreen.blit(winlose ,winlose .get_rect(center = (250,50)))
        scoreslst = []
        with open("flappy_scores.txt") as topscores:
            for line in topscores:
                scoreslst.append(int(line.rstrip()))
            if(len(scoreslst) < 10):
                scoreslst.append(App.onlvl)
            else :
                getlowest = min(scoreslst)
                if(getlowest < App.onlvl):
                 scoreslst.remove(getlowest)
                 scoreslst.append(App.onlvl)
            scoreslst = sorted(scoreslst,key=None,reverse=True)
            with open("flappy_scores.txt","w") as writescores:
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
                    
        App.onlvl = 0
        App.checkdistance = 0
        App.coinscollected = 0
        if(playagain): 
            app = App()
            app.run()

if __name__ == "__main__":
    app = App()
    app.run()