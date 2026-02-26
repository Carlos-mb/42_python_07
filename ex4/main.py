from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    print()
    platform = TournamentPlatform()

    card_dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        defense=3,
        health=20
    )

    card_warrior = TournamentCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Epic",
        attack=5,
        defense=4,
        health=18
    )

    card_goblin = TournamentCard(
        name="Goblin Raider",
        cost=2,
        rarity="Common",
        attack=3,
        defense=1,
        health=10
    )

    dragon_id = platform.register_card(card_dragon)
    warrior_id = platform.register_card(card_warrior)
    goblin_id = platform.register_card(card_goblin)

    print("Registered Cards:")
    print(dragon_id, card_dragon.get_card_info())
    print(warrior_id, card_warrior.get_card_info())
    print(goblin_id, card_goblin.get_card_info())
    print()

    print("--- Match 1 ---")
    result1 = platform.create_match(dragon_id, warrior_id)
    print(result1)

    print("\n--- Match 2 ---")
    result2 = platform.create_match(warrior_id, goblin_id)
    print(result2)

    print("\n--- Match 3 ---")
    result3 = platform.create_match(dragon_id, goblin_id)
    print(result3)

    # Leaderboard
    print("\n=== Leaderboard ===")
    leaderboard = platform.get_leaderboard()
    for position, entry in enumerate(leaderboard, start=1):
        print(
            f"{position}. {entry['name']} "
            f"(Rating: {entry['rating']}, Record: {entry['record']})"
        )

    # Tournament Report
    print("\n=== Tournament Report ===")
    report = platform.generate_tournament_report()
    print(report)

    print("\nTournament system fully operational.")


if __name__ == "__main__":
    main()
