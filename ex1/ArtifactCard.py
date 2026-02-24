from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str) -> None:

        super().__init__(name=name, cost=cost, rarity=rarity)
        if durability <= 0:
            raise ValueError("Error: durability must ve positive integer")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            result = {}
            result["card_played"] = self.name
            result["mana_used"] = self.cost
            result["effect"] = f"Permanent: {self.effect}"
            game_state["available_mana"] -= self.cost
        else:
            result = {"error": "Not enough mana."}
        return result

    def activate_ability(self) -> dict:

        if self.durability <= 0:
            return {
                "artifact": self.name,
                "effect": None,
                "durability_remaining": 0,
                "status": "destroyed"
            }

        self.durability -= 1

        status = "active" if self.durability > 0 else "destroyed"

        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_remaining": self.durability,
            "status": status
        }
