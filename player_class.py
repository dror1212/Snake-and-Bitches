import pygame
import socket
import select
from Tkinter import *
import easygui
import random
import time

class Player:

    def __init__(self):
        pygame.init()
        self.Username = ""
        self.Players = {}
        self.master = Tk()
        self.entry = None
        self.screen = None
        self.white = (255, 255, 255)
        self.s = None
        self.blue=(0,0,255)
        self.green=(0,255,0)
        self.yellow=(255,255,0)
        self.red=(255,0,0)
        self.black=(0,0,0)
        self.grey=(47,79,79)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 40)
        self.myfont2 = pygame.font.SysFont('Comic Sans MS', 28)
        self.ready = False #check if ready
        #self.distance =  (pygame.display.get_surface().get_size()[1]/36*31/10)-1
        self.place = 0

    def closeConnection(self):
        self.s.send("disconnecttt")
        self.s.close()


    def return_entry(self,en):
        """Gets and prints the content of the entry"""
        self.Username = self.entry.get()
        self.master.destroy()

        
    def main_screen(self):
        pygame.init()
        img = pygame.image.load('Super-Smash-Bros.jpg')
        img2 = pygame.image.load('snakes_ladders.png')
        #pygame.mixer.music.load('start.ogg')
        #pygame.mixer.music.play(-1)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 40)
        
        play_ = self.myfont.render('PLAY', False, self.white)
        options_ = self.myfont.render('OPTIONS', False, self.white)
        quit_ = self.myfont.render('QUIT', False, self.white)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        img = pygame.transform.scale(img, pygame.display.get_surface().get_size())
        img2 = pygame.transform.scale(img2, (pygame.display.get_surface().get_size()[0]/2,pygame.display.get_surface().get_size()[1]/5*2))
        self.screen.fill((self.white))
        self.screen.blit(img,(0,0))
        self.screen.blit(img2,(pygame.display.get_surface().get_size()[0]/4,0))
        pygame.draw.rect(self.screen,self.blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/2,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        pygame.draw.rect(self.screen,self.blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/1.6,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        pygame.draw.rect(self.screen,self.blue,(pygame.display.get_surface().get_size()[0]*3/8,pygame.display.get_surface().get_size()[1]/1.34,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        button_play = self.screen.blit(play_,(pygame.display.get_surface().get_size()[0]*30/64,pygame.display.get_surface().get_size()[1]/2))
        button_options = self.screen.blit(options_,(pygame.display.get_surface().get_size()[0]*28/64,pygame.display.get_surface().get_size()[1]/1.6))
        button_quit = self.screen.blit(quit_,(pygame.display.get_surface().get_size()[0]*30/64,pygame.display.get_surface().get_size()[1]/1.34))
        running = True
        disconnect = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    disconnect = True
                elif event.type == pygame.KEYDOWN:
                    #if esc clicked, quit
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        disconnect = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    #if quit button clicked, quit
                    if button_quit.collidepoint(pos):
                        running = False
                        disconnect = True
                    elif button_play.collidepoint(pos):
                        running = False
            pygame.display.flip()
        return disconnect


       
    def Login(self):
        pygame.init()
        img3 =  pygame.image.load('boared.jpg')
        img3 = pygame.transform.scale(img3, (pygame.display.get_surface().get_size()[1]/36*31,pygame.display.get_surface().get_size()[1]/36*31))       
        img4 = pygame.image.load('oak.jpg')
        img4 = pygame.transform.scale(img4, (pygame.display.get_surface().get_size()[1]*12/10,pygame.display.get_surface().get_size()[1]/36*31))
        self.screen = pygame.display.set_mode((pygame.display.get_surface().get_size()[1]*12/10,pygame.display.get_surface().get_size()[1]/36*31),0)
        self.screen.fill(self.white)
        self.screen.blit(img4,(0,0))
        self.screen.blit(img3,(0,0))
        pygame.draw.rect(self.screen,self.red,(pygame.display.get_surface().get_size()[0]*47/64,pygame.display.get_surface().get_size()[1]/6,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        pygame.draw.rect(self.screen,self.yellow,(pygame.display.get_surface().get_size()[0]*47/64,pygame.display.get_surface().get_size()[1]/3,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        pygame.draw.rect(self.screen,self.green,(pygame.display.get_surface().get_size()[0]*47/64,pygame.display.get_surface().get_size()[1]/2,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        pygame.draw.rect(self.screen,self.blue,(pygame.display.get_surface().get_size()[0]*47/64,pygame.display.get_surface().get_size()[1]/3*2,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/12),0)
        button_ready = pygame.draw.rect(self.screen,self.grey,(pygame.display.get_surface().get_size()[0]*47/64,pygame.display.get_surface().get_size()[1]/60,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/16),0)
        players_ = self.myfont.render('PLAYERS:', False, self.black)
        ready_ = self.myfont2.render('Ready', False, self.white)
        self.screen.blit(players_,(pygame.display.get_surface().get_size()[0]*47/64,pygame.display.get_surface().get_size()[1]/13))
        self.screen.blit(ready_,(pygame.display.get_surface().get_size()[0]*105/128,pygame.display.get_surface().get_size()[1]/60,pygame.display.get_surface().get_size()[0]/4,pygame.display.get_surface().get_size()[1]/16))
        Label(self.master, text="Username: ").grid(row=0, sticky=W)
        self.master.title('Login')
        self.entry = Entry(self.master)
        self.entry.grid(row=0, column=1)
        # Connect the entry with the return button
        self.entry.bind('<Return>',self.return_entry)
        mainloop()
        
        self.game(button_ready)

    def roll(self):
        size = (pygame.display.get_surface().get_size()[1]/43*10,pygame.display.get_surface().get_size()[1]/43*10)
        one = pygame.image.load('1.png')
        one = pygame.transform.scale(one,size)
        two = pygame.image.load('2.png')
        two = pygame.transform.scale(two,size)
        th = pygame.image.load('3.png')
        th = pygame.transform.scale(th,size)
        fo = pygame.image.load('4.png')
        fo = pygame.transform.scale(fo,size)
        fi = pygame.image.load('5.png')
        fi = pygame.transform.scale(fi,size)
        si = pygame.image.load('6.png')
        si = pygame.transform.scale(si,size)
        rr = pygame.image.load('rolling.png')
        rr = pygame.transform.scale(rr,size)
        num = [rr,one,two,th,fo,fi,si]
        pla=0
        #running2 = True
        running2 = 4
        poss = (pygame.display.get_surface().get_size()[0]/1.29,pygame.display.get_surface().get_size()[1]/1.315)
        self.screen.blit(num[pla],poss)
        
        while running2>0:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running2 = False
                elif event.type == pygame.KEYDOWN:
                    #if esc clicked, quit
                    if event.key == pygame.K_ESCAPE:
                        running2 = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    #if quit button clicked, quit
                    if num[pla].get_rect(topleft=poss).collidepoint(pos):
                        while running2>0:
                            running2 = running2 -1 #del
                            pla = random.randint(1, 6)
                            self.screen.blit(num[pla],poss)
                            time.sleep(0.4)
                            pygame.display.flip()
            pygame.display.flip()
        return pla
        
    def game(self,button_ready):
        ######
        size = (pygame.display.get_surface().get_size()[1]/43*10,pygame.display.get_surface().get_size()[1]/43*10)
        rr = pygame.image.load('rolling.png')
        rr = pygame.transform.scale(rr,size)
        poss = (pygame.display.get_surface().get_size()[0]/1.29,pygame.display.get_surface().get_size()[1]/1.315)        
        self.screen.blit(rr,poss)
        ######
        self.s=socket.socket()
        self.s.connect(("127.0.0.1",8783))
        self.s.send("nameeeeeeeeee " + self.Username)
        Da= None
        running = True
        while running:
            rlist,wlist,xlist=select.select([self.s],[self.s],[])
            if len(rlist)!=0:
                DA= self.s.recv(1024)
                print DA
            #if True:
                if DA:
                    if "name" in DA:
                        print "sfgdagsdfgsdfgds"
                        DA2 = DA.split(' ')
                        if "turn" in DA2:
                            DA2.remove("turn")
                        c=1
                        print DA2
                        while c<len(DA2):
                            self.Players[DA2[c]] = DA2[c+1]
                            print self.Players[DA2[c]]
                            c=c+2
                        self.s.send("finish")
                        
                    if "turn" in DA:
                        print "hara"
                        dice = self.roll()
                        print "dfgfgff"
                        turnn = True
                        print "dfx"
                        for key in self.Players:
                            if turnn:
                                print "sfg"
                                self.s.send("move " + key + " " + str(self.place) + " " + str(dice))
                                print "move " + key + " " + str(self.place) + " " + str(dice)
                                turnn = False
                        self.place = self.place + dice
                        print "fh"
  
                    elif "move" in DA:
                        print "sdf"
                        self.s.send("finish")
                    
                #running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    #if esc clicked, quit
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if not self.ready:
                        if button_ready.collidepoint(pos):
                            self.ready = True
                            self.s.send("ready")
                            easygui.msgbox("you are ready to play, please wait for other players to be ready", title="Info")
            pygame.display.flip()             


def main():
    player = Player()
    disconnect = player.main_screen()
    if disconnect: 
        pygame.quit()
    else:    
        player.Login()
        player.closeConnection()
        pygame.quit()

if __name__ == "__main__":
    main()
