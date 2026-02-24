from  ex0.Card import Card

class Spellcard(Card):

    effect_types:list [str] = ["damage", "heal", "buff", "debuff"]

    def __int__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name = name, cost=cost, rarity=rarity)
        if effect_type not in Spellcard.effect_types:
            print("ERROR: Wrong effect_type")

        self.effect_type: str = effect_type  #damage, heal, buff, debuf

    
    def play(self, game_state: dict) -> dict:
        result:dict = {
            "effect_type": "spell",
            "consumeble": True,
            }

    def resolve_effect(self, targets: list) -> dict:

Método play(game_state):
    crear diccionario resultado
    indicar que es un spell
    indicar que se consume
    devolver resultado

Método resolve_effect(targets):
    según effect_type:
        si damage → aplicar daño
        si heal → aplicar curación
        si buff → aplicar mejora
        si debuff → aplicar penalización
    devolver diccionario con resultado