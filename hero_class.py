class ClassCreator:
    classList = [
        {
            "id": 0,
            "name": "Guerreiro",
            "hability": {"dmgRedS":0.9, "dmgRedD":0.95},
            "reqSkills": [[0, 1, 2], [0, 1, 3], [0,2,3]]
        },
        {
            "id": 1,
            "name": "Ranger",
            "hability": {"dodgy":10, "bCrit":10},
            "reqSkills": [[2, 3, 1], [0, 2, 4], [2, 3, 4]]
        },
        {
            "id": 2,
            "name":"Mago",
            "hability": {"dmgRedS":1.1, "bMDmg":1.3},
            "reqSkills": [[3, 4, 5], [2, 4, 5], [1, 4, 5]]
        },
        {
            "id": 3,
            "name": "Mago de Guerra",
            "hability": {"buff":-2, "dmgRedS":0.95, "bMDmg":1.17},
            "reqSkills": [[1, 2, 5], [0, 3, 4], [0, 4, 5]]
        },
        {
            "id": 4,
            "name": "Druida",
            "hability": {"regen":2},
            "reqSkills": [[2, 3, 5], [1, 3, 5], [0, 3, 5]]
        },
        {
            "id": 5,
            "name": "Dracônico",
            "hability": {"dmgRedD":0.9, "bSDmg":1.1, "bMDmg": 1.05,},
            "reqSkills": [[0, 1, 4], [0, 1, 5]]
        },
        {
            "id":6,
            "name": "Shaman",
            "hability": {"dmgRedM":0.75, "bMDmg":1.2},
            "reqSkills": [[0, 2, 5], [1, 2, 4], [1, 3, 4]],
        },
    ]

    def getClass(self, sk1, sk2, sk3):
        for cl in self.classList:
            for r in cl["reqSkills"]:
                if ((sk1.id in r) and (sk2.id in r) and (sk3.id in r)):
                    print("A Classe do seu heroi é "+cl["name"])
                    return HClass(cl["id"], cl["name"], cl["hability"]) 

class HClass:
    def __init__(self, c_id, c_name, c_fx={}):
        self.id = c_id
        self.name = c_name
        self.hability = c_fx
