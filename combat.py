from random import randint

import math

from enemy import Enemy

class Combat:
    def calcInit(self, hero, enemy):
        h_init = hero.speed + hero.bonusSpeed
        h_init += randint(1, 20)
        hero.bonusSpeed = 0
        
        e_init = enemy.speed + enemy.bonusSpeed
        e_init += randint(1, 20)
        enemy.bonusSpeed = 0

        if (h_init>=e_init):
            return "hero"
        else:
            return "enemy"

    def calcAttack(self, target, skill):
        if ("nomiss" in skill.effects):
            return True
        else:
            dodge = target.dodge
            roll = randint(0, 100)
            if (roll<=dodge):
                return False
            else:
                return True

    def calcDamage(self, skill):
        critChance = 10
        if ("crit" in skill.effects):
            critChance = skill.effects['crit']*100
        dmg = math.ceil(skill.damage)
        dmg = dmg+randint(1, 4)
        critRoll = randint(0, 100)
        if (critRoll<=critChance):
            print("Acerto Crítico! Dano dobrado!")
            dmg = dmg*2 
        return (dmg)

    def applyEffects(self, user, target, skill):
        if ("buff" in skill.effects):
            user.bonusSpeed = skill.effects["buff"]
        if ("stun" in skill.effects):
            stun = False
            resist = False
            sRoll = randint(0, 100)
            rRoll = randint(0, 100)
            stunProc = user.str*skill.effects['stun'][0]*10
            stunProc += user.dex*skill.effects['stun'][1]*10
            stunProc += user.mag*skill.effects['stun'][2]*10
            print("stunproc")
            print(stunProc)
            print(sRoll)
            if (sRoll<=stunProc):
                stun = True
            if (rRoll<=target.res):
                resist = True
            if (stun and not resist):
                target.stun = True
                if (type(target) is Enemy):
                    print("Seu ataque atordoou o inimigo!")
                else:
                    print("O ataque inimito te atordoou!")
        if ("selfStun" in skill.effects):
            stun = False
            resist = False
            sRoll = randint(0, 100)
            rRoll = randint(0, 100)
            stunProc = user.str*skill.effects['stun'][0]*10
            stunProc += user.dex*skill.effects['stun'][1]*10
            stunProc += user.mag*skill.effects['stun'][2]*10
            if (sRoll<=stunProc):
                stun = True
            if (rRoll<=user.res):
                resist = True
            if (stun and not resist):
                user.stun = True

    def combatTurn(self, hero, enemy, activeSkill, ref):
        turnHeader = ('\033[92m'+hero.hero_class.name+" lvl:1 "+ "HP: "+str(hero.hp))
        turnHeader = (turnHeader+'\033[93m'+(" -----VS----- "))
        turnHeader = (turnHeader+'\033[91m'+("Inimigo lvl:1 HP: "+str(enemy.hp)))
        print(turnHeader)
        print('\033[37m')
        init = self.calcInit(hero, enemy)
        if (init == "hero"):
            if (hero.hp > 0):
                self.heroTurn(hero, enemy, activeSkill)
            else:
                #TODO:computar pontos de xp
                print("Seu Heroi morreu!")
                ref.hero = None

            if (enemy.hp > 0):
                self.enemyTurn(hero, enemy)
            else:
                print("Você Eliminou o Inimigo!")
                ref.enemy = None
        else:
            if (enemy.hp > 0):
                self.enemyTurn(hero, enemy)
            else:
                print("Você Eliminou o Inimigo!")
                ref.enemy = None

            if (hero.hp > 0):
                self.heroTurn(hero, enemy, activeSkill)
            else:
                #TODO: computar pontos de xp
                print("Seu Heroi morreu!")
                ref.hero = None

    def heroTurn(self, hero, enemy, activeSkill):
        if(hero.stun):
            print("Você está atordoado e não pode agir neste turno!")
            hero.stun = false
        else:
            if (self.calcAttack(enemy, activeSkill)):
                print("Seu ataque "+activeSkill.name+" atingiu o inimigo!")
                dmg = self.calcDamage(activeSkill)
                self.applyEffects(hero, enemy, activeSkill)
                print("Você causou "+str(dmg)+" pontos de dano!")
                enemy.hp -= dmg

    def enemyTurn(self, hero, enemy):
        if (enemy.stun):
            print("O inimigo está atordoado e não pode agir neste turno!")
            enemy.stun = false;
        else:
            enSkill = enemy.getRndSkill()
            if(self.calcAttack(hero, enSkill)):
                print("O oponente te atingiu com um(a) "+enSkill.name);
                dmg = self.calcDamage(enSkill)
                hero.hp -= dmg
                print("Você sofreu "+str(dmg)+" pontos de dano!")
