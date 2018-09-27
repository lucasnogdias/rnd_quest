import math
from random import randint

from skill import Skill

class Hero:
    def __init__(self, level=1):
        charPoints = 15+level
        #Generate Hero Strength
        self.str = randint(1, charPoints)
        charPoints = charPoints - self.str
        #Generate Hero Dexterity
        self.dex = randint(1, charPoints)
        charPoints = charPoints - self.dex
        #Generate Hero Magic
        self.mag = charPoints
        charPoints = charPoints - self.mag
        #Get Character HP, based on Strength
        self.hp = 10+math.ceil(self.str/2)
        #Get Character SPEED, based on Dexterity
        self.speed = 1+math.ceil(2*(self.dex/3))
        #Get Character HEAL, based on Magic
        self.heal = 1+math.ceil(self.mag/3)
        #Get Character Resistence based on Strength
        self.res = 10+math.ceil(1.7*self.str)
        #Get Character Dodge based on Dexterity
        self.dodge = 10+math.ceil(1.7*self.dex)
        #Get Character CRIT, based on Magic
        self.crit = 10+math.ceil(1.75*self.mag)
        print("STR: ", self.str)
        print("DEX: ", self.dex)
        print("MAG: ", self.mag)
        print("HP: ", self.hp)
        print("SPEED: ", self.speed)
        print("HEAL: ", self.heal)
        print("RESIST: ", self.res)
        print("DODGE: ", self.dodge)
        print("CRIT: ", self.crit)

    def setSkill(self, skill, i):
        this.skills[i] = skill;
