import math
from random import randint

from skill import SkillCreator

class Enemy:
    enemyList=[
        [
            {
                "name":"Goblin",
                "base": [1, 2, 0],
                "hability": {"buff": 10},
                "reach": 0,
                "skills": [2]
            },
            {
                "name": "Slime",
                "base": [2, 0, 3],
                "hability": {"regen": 1, "dmgRedS": 0.9, "dmgRedM":1.6},
                "reach": 0,
                "skills": [1] 
            },
            {
                "name": "Aranha Gigante",
                "base": [2, 3, 0],
                "hability": {"dodgy":3},
                "reach": 0,
                "skills": [1, 3]
            },
        ],
        [
            {
                "name":"Guerreiro Orc",
                "base": [5, 3, 1],
                "hability": {"bSDmg":1.15},
                "reach": 0,
                "skills": [0, 1, 2, 3]
            },
            {
                "name":"Cultista",
                "base": [0, 2, 6],
                "hability":{"bMDmg":1.15},
                "reach":0,
                "skills": [5, 6, 2]
            },
            {
                "name": "Imp",
                "base": {2, 4, 4},
                "hability": {"buff":8, "bMDmg":1.08},
                "reach": 1,
                "skills": [5, 6, 2],
            },
            {
                "name": "Drow",
                "base": {3, 7, 2},
                "hability": {"dodgy":12},
                "reach": 0,
                "skills": [2, 3, 1, 4],
            }
        ],
        [
            {
                "name": "Troll",
                "base": {10, 4, 4},
                "hability": {"regen":4, "buff":-2},
                "reach": 0,
                "skills": [0, 1, 5],
            }
        ],
        [
            {
                "name": "Dragão",
                "base": {15, 12, 16},
                "hability": {"regen": 3, "bMDmg":1.7, "bSDmg": 1.8, "bDDmg": 1.5, "dmgRedS":0.8, "dmgRedD":0.7, "dmgRedM":0.92},
                "reach":1,
                "skills": [0, 1, 2, 3, 4, 5]
            }
        ]
    ]

    def __init__(self, level):

        if level<=4:
            enemyPool = self.enemyList[0]
        elif level<=10:
            enemyPool = self.enemyList[1]
        elif level<=20:
            enemyPool = self.enemyList[2]
        else:
            enemyPool = self.enemyList[3]

        eNum = randint(0, len(enemyPool)-1)
        enemyBase = enemyPool[eNum]

        charPoints = level

        self.level = level
        self.name = enemyBase['name']
        #Generate Strength
        statBonus = randint(0, charPoints)
        self.str = enemyBase['base'][0] + statBonus
        charPoints = charPoints-statBonus
        #Generate Dexterity
        if (charPoints == 0):
            statBonus = 0
        else:
            statBonus = randint(0, charPoints) 
        self.dex = enemyBase['base'][1] + statBonus
        charPoints = charPoints-statBonus
        #Generate Magic
        statBonus = charPoints
        self.mag = enemyBase['base'][2] + statBonus

        self.hp = 5+math.ceil(self.str/2)
        self.maxHP = 5+math.ceil(self.str/2)
        self.speed = 1+math.ceil(2*(self.dex/3))
        self.heal = 1+math.ceil(self.mag/3)
        self.res = 10+math.ceil(2.7*self.str)
        self.dodge = 10+math.ceil(1.7*self.dex)
        self.crit = 10+math.ceil(1.75*self.mag)
        self.reach = enemyBase['reach']

        self.skills =[]

        self.stun = False
        self.bonusSpeed = 0

        skCreator = SkillCreator();
        genSkills = skCreator.generateSkillList(self.str, self.dex, self.mag)

        for x in range(0, len(enemyBase['skills'])):
            sInd = enemyBase['skills'][x]
            self.skills.append(genSkills[sInd])

    def getRndSkill(self):
        rndSkill = randint(0, len(self.skills)-1)
        return self.skills[rndSkill]
