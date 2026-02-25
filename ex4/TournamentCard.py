TournamentCard inherits from:
    Card
    Combatable
    Rankable

Attributes:
    wins: int = 0
    losses: int = 0
    rating: int = 1200   # rating base tipo ELO simple
    attack_power
    defense
    health

Debe implementar TODOS los métodos abstractos de:

Card

Combatable

Rankable

Class TournamentCard(Card, Combatable, Rankable)

    Constructor(...)
        call super().__init__()
        initialize combat stats
        initialize wins = 0
        initialize losses = 0
        initialize rating = 1200

    Method play(game_state) -> dict
        return simple deployment message

    Method attack(target) -> dict
        call target.defend(self.attack_power)
        return combat result dict

    Method defend(incoming_damage) -> dict
        apply defense logic
        update health
        return defense result

    Method get_combat_stats() -> dict
        return attack/defense/health

    Method update_wins(wins: int)
        self.wins += wins

    Method update_losses(losses: int)
        self.losses += losses

    Method calculate_rating() -> int
        rating = 1200 + (wins * 16) - (losses * 16)
        self.rating = rating
        return rating

    Method get_rank_info() -> dict
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    Method get_tournament_stats() -> dict
        combine:
            card info
            combat stats
            ranking stats