
class SkillCreator:
    skillList=[
        {
            "id": 0,
            "name": "Corte Diagonal",
            "type": "Força",
            "range": 0,
            "desc": "Um corte amplo e poderoso.",
            "effects": {"buff":-1},
            "effec_desc": 'Reduz sua velocidade para o proximo turno.',
            "reach": 0,
            "dmgByType": [1.25, 0, 0]
        },
        {
            "id": 1,
            "name": "Pancada",
            "type": "Força",
            "range": 0,
            "desc": "Ataque com escudo ou \n com o pomo da arma.",
            "effects": {"stun": [0.5, 0.2, 0]},
            "effec_desc": 'Chance de atordoar o inimigo.',
            "reach": 0,
            "dmgByType": [0.7, 0, 0]
        },
        {
            "id": 2,
            "name": "Flechada",
            "type": "Destreza",
            "range": 1,
            "desc": "Disparo de flecha ou virote",
            "effects": {"crit":0.35},
            "effec_desc": 'Chance elevada de causar dano crítico.',
            "reach": 1,
            "dmgByType": [0.1, 0.7, 0]
        },
        {
            "id": 3,
            "name": "Estocada",
            "type": "Destreza",
            "range": 0,
            "desc": "Estocada com uma arma perfurante.",
            "effects": {"crit":0.18, "buff":2},
            "effec_desc": 'Aumenta sua velcidade pro proximo turno. \n Chance de crítico',
            "reach": 0,
            "dmgByType": [0.3, 0.6, 0]
        },
        {
            "id": 4,
            "name": "Bola de Fogo",
            "type": "Magia",
            "range": 1,
            "desc": "Um orbe flamejante que \n persegue o inimigo.",
            "effec_desc": 'O inimigo não pode se esquivar.',
            "effects": {"nomiss":True},
            "reach": 1,
            "dmgByType": [0, 0, 0.4]
        },
        {
            "id": 5,
            "name": "Terremoto",
            "type": "Magia",
            "range": 0,
            "desc": "Uso de energia arcana para \n provocar um tremor violento.",
            "effec_desc": 'Chance de atordoar o inimigo e o jogador',
            "effects": {"selfStun":True, "stun":[0, 0, 0.8]},
            "reach": 0,
            "dmgByType": [0, 0, 2]
        }
    ]

    def generateSkillList(self, stren, dex, mag):
        skills = []
        for i in range(len(self.skillList)):
            cs = self.skillList[i]
            dmg = (stren*cs['dmgByType'][0])+(dex*cs['dmgByType'][1])+(mag*cs['dmgByType'][2])
            skills.append(Skill(i, cs['name'], cs['type'], cs['range'], cs['desc'], dmg, cs['effects'], cs['effec_desc'], cs['reach']))
        return skills

class Skill:
    def __init__(self, s_id, name, s_type, s_range, description, damage, effects, ef_desc, reach):
        self.id = s_id
        self.name = name
        self.type = s_type
        self.range = s_range
        self.description = description
        self.damage = damage
        self.effects = effects
        self.ef_desc = ef_desc
        self.reach = reach
    
