import pygame
from pygame.locals import *
from random import randint
import os
from prettytable import PrettyTable

#Game Classes
from hero import Hero
from enemy import Enemy
from skill import SkillCreator
from hero_class import ClassCreator
from combat import Combat
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

        self.hero = None;
        self.gameSkills = [];
        self.enemy = None;
        self.ready = False;
        self.onUserAction = False;

        self.contTxt = "Pressione qualquer tecla para continuar..."
        
 
    def on_init(self):
        pygame.init()
        #self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.combat = Combat()
        os.system('clear') 
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
    
        while (self.hero!= None):
            if (self.enemy == None):
                print("Surgiu um novo inimigo!");
                self.enemy = Enemy(0, self.gameSkills)
            else:
                print("Informe qual habilidade você deseja utilizar")
                print("1 - "+self.hero.skills[0].name)
                print("2 - "+self.hero.skills[1].name)
                print("3 - "+self.hero.skills[2].name)
                skUse = input();
                try:
                    skUse = int(skUse)
                    skUse = skUse-1
                    if (skUse<0 or skUse>2):
                        raise ValueError
                    self.combat.combatTurn(self.hero, self.enemy, self.hero.skills[skUse], self)
                    wait = input(self.contTxt)
                    os.system('clear') 
    
                except ValueError:
                    print("Informe um numero de 1 a 3")
            pass
        self.createHero()

    def createHero(self):
        self.hero = Hero();

        skCreator = SkillCreator();
        self.gameSkills = skCreator.generateSkillList(self.hero.str, self.hero.dex, self.hero.mag)

        #TODO: print all skills so user know what he's choosing
        self.listSkills(self.gameSkills)
        cSk1 = input("Selecione sua primeira Skill: ")
        cSk2 = input("Selecione sua segunda Skill: ")
        cSk3 = input("Selecione sua terceira Skill: ")
        cSk1 = int(cSk1)-1
        cSk2 = int(cSk2)-1
        cSk3 = int(cSk3)-1
        self.hero.setSkill(self.gameSkills[cSk1], 0)
        self.hero.setSkill(self.gameSkills[cSk2], 1)
        self.hero.setSkill(self.gameSkills[cSk3], 2)

        clCreator = ClassCreator()
        self.hero.setClass(clCreator.getClass(self.hero.skills[0],
            self.hero.skills[1],
            self.hero.skills[2]))

    def listSkills(self, gameSkills):
        table = PrettyTable()

        table.field_names = ["Id", "Nome", "Tipo", "Descrição", "Dano", "Efeitos", "Alcance"]

        for sk in gameSkills:
            table.add_row([str(sk.id+1), sk.name, sk.type, sk.description, "{0:.2f}".format(sk.damage), str(sk.ef_desc), "Corpo-a-corpo" if sk.reach==0 else "À Distância"])
            skT = str(sk.id+1)+" - "+sk.name+" - "+sk.type+" - "+sk.description+" - "+str(sk.damage)+" - "+str(sk.effects)
            #print(skT);

        print("Escolha três habilidades:")
        print(table)

    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            #self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
