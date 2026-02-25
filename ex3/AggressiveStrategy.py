from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:

        mana_limit = 5
        mana_used = 0
        cards_played = []
        damage_dealt = 0

        # Play lowest cost first
        sorted_hand = sorted(hand, key=lambda c: c.cost)

        for card in sorted_hand:
            if mana_used + card.cost <= mana_limit:
                cards_played.append(card.name)
                mana_used += card.cost

                # Simple damage logic
                if hasattr(card, "attack"):
                    damage_dealt += getattr(card, "attack", 0)
                else:
                    damage_dealt += 3

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets