import math
from random import randint

from skill import SkillCreator

class Enemy:
    def __init__(self, level, gameSkills):

        skCreator = SkillCreator();

        charPoints = 14+level
        #TODO: replicate hero generation process
        self.str = 10
        self.dex = 10
        self.mag = 10
        self.hp = 10
        self.speed = 2
        self.heal = 1
        self.res = 1
        self.dodge = 2
        self.crit = 10
        self.skills =[]
        self.skills.append(gameSkills[0])
        self.skills.append(gameSkills[1])

        self.stun = False

    def getRndSkill(self):
        rndSkill = randint(0, len(self.skills)-1)
        return self.skills[rndSkill]
