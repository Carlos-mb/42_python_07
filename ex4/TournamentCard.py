from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class Tournamentcard(Card, Combatable, Rankable):
    
    def __init__(self,  name: str, cost: int, rarity: str) -> None:
        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = 1200

    def play(self, game_state: dict) -> dict:
        return simple deployment message

    def attack(target) -> dict
        call target.defend(self.attack_power)
        return combat result dict

    def defend(incoming_damage) -> dict
        apply defense logic
        update health
        return defense result

    def get_combat_stats() -> dict
        return attack/defense/health

    def update_wins(wins: int)
        self.wins += wins

    def update_losses(losses: int)
        self.losses += losses

    def calculate_rating() -> int
        rating = 1200 + (wins * 16) - (losses * 16)
        self.rating = rating
        return rating

    def get_rank_info() -> dict
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats() -> dict
        combine:
            card info
            combat stats
            ranking stats