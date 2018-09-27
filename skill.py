
class SkillCreator:
    skillList=[
        {
            "id": 0,
            "name": "Corte Diagonal",
            "type": "Força",
            "range": 0,
            "desc": "Um corte amplo e poderoso, mas desiquilibra o usuário",
            "effects": {"debuff":-1},
            "dmgByType": [1.25, 0, 0]
        },
        {
            "id": 1,
            "name": "Pancada",
            "type": "Força",
            "range": 0,
            "desc": "Ataque com escudo ou com o pomo da arma.",
            "effects": {"stun": [0.7, 0.2, 0]},
            "dmgByType": [0.7, 0, 0]
        },
        {
            "id": 2,
            "name": "Flechada",
            "type": "Destreza",
            "range": 1,
            "desc": "Disparo de flecha ou virote. Dano moderado e boa chance de crítico.",
            "effects": {"crit":0.2},
            "dmgByType": [0.1, 0.7, 0]
        },
        {
            "id": 3,
            "name": "Estocada",
            "type": "Destreza",
            "range": 0,
            "desc": "Estocada com uma arma perfurante.",
            "effects": {"crit":0.11},
            "dmgByType": [0.3, 0.7, 0]
        },
        {
            "id": 4,
            "name": "Bola de Fogo",
            "type": "Magia",
            "range": 1,
            "desc": "Um orbe flamejante que persegue o inimigo. Dano moderado-baixo mas nunca erra.",
            "effects": {"nomiss":True},
            "dmgByType": [0, 0, 0.4]
        },
        {
            "id": 5,
            "name": "Terremoto",
            "type": "Magia",
            "range": 0,
            "desc": "Uso de energia arcana para provocar um tremor violento. Muito poderoso, mas pode atordoar até mesmo o usuário.",
            "effects": {"selfStun":True, "stun":[0, 0, 0.3]},
            "dmgByType": [0, 0, 2]
        }
    ]

    def generateSkillList(self, stren, dex, mag):
        skills = []
        for i in range(len(self.skillList)):
            cs = self.skillList[i]
            dmg = (stren*cs['dmgByType'][0])+(dex*cs['dmgByType'][1])+(mag*cs['dmgByType'][2]);
            skills.append(Skill(i, cs['name'], cs['type'], cs['range'], cs['desc'], dmg, cs['effects']));
        return skills;

class Skill:
    def __init__(self, s_id, name, s_type, s_range, description, damage, effects):
        self.id = s_id
        self.name = name
        self.type = s_type
        self.range = s_range
        self.description = description
        self.damage = damage
        self.effects = effects
    
