import pygame
from pygame.locals import *

#Game Classes
from hero import Hero
from skill import SkillCreator
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.hero = None;
        self.gameSkills = [];
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.hero = Hero();

        skCreator = SkillCreator();
        self.gameSkills = skCreator.generateSkillList(self.hero.str, self.hero.dex, self.hero.mag)
       
        for s in self.gameSkills:
            print(s.name);
            print(s.type);
            print(s.range);
            print(s.description);
            print(s.damage);
            print(s.effects);
            print("----------------");
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
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
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
