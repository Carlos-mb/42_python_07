Gestionar:

Registro de cartas

Creación de partidas

Ranking global

Reportes

Atributos:
registered_cards: dict[str, TournamentCard]
matches_played: int = 0

Class TournamentPlatform

    Constructor
        initialize empty registry dict
        matches_played = 0

    Method register_card(card: TournamentCard) -> str
        generate unique ID (ex: name_lower + counter)
        store in registry
        return generated_id

    Method create_match(card1_id: str, card2_id: str) -> dict

        get card1 and card2 from registry

        determine winner:
            simple rule:
                higher attack wins

        winner.update_wins(1)
        loser.update_losses(1)

        winner.calculate_rating()
        loser.calculate_rating()

        matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    Method get_leaderboard() -> list

        sort registry.values by rating descending

        return ordered list of:
            name
            rating
            record

    Method generate_tournament_report() -> dict

        calculate average rating

        return {
            "total_cards": number of registered cards,
            "matches_played": matches_played,
            "avg_rating": computed average,
            "platform_status": "active"
        }