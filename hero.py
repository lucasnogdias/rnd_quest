import math
from random import randint
from prettytable import PrettyTable

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
        table = PrettyTable()
        table.field_names = ["Atributo", "Valor"]
        table.add_row(["Força", self.str])
        table.add_row(["Destreza", self.dex])
        table.add_row(["Magia", self.mag])
        table.add_row(["Pontos de Vida", self.hp])
        table.add_row(["Velocidade", self.speed])
        table.add_row(["Cura", self.heal])
        table.add_row(["Resistência", self.res])
        table.add_row(["Esquiva", self.dodge])
        table.add_row(["Crítico", self.crit])

        print("Seu novo personagem de nível 1:")
        print(table)

        #skills
        self.skills = []

        self.hero_class = {} 

        self.stun = False

    def setSkill(self, skill, i):
        self.skills.append(skill)

    def setClass(self, hclass):
        self.hero_class = hclass;
