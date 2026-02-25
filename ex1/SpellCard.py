from ex0.Card import Card


class SpellCard(Card):

    card_type: str = "spell"

    effect_types: dict[str, str] = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health",
            "buff": "Increase attack by 2",
            "debuff": "Reduce enemy attack by 2"}

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name=name, cost=cost, rarity=rarity)

        if effect_type not in self.effect_types:
            raise ValueError("ERROR: Wrong effect_type")
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            result = self.resolve_effect(game_state["targets"])
            result["card_played"] = self.name
            result["mana_used"] = self.cost
            game_state["available_mana"] -= self.cost
        else:
            result = {"error": "Not enough mana."}
        return result

    def resolve_effect(self, targets: list) -> dict:
        return {
                "effect_type": self.effect_type,
                "targets": targets,
                "effect": self.effect_types[self.effect_type]}
