from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Elite Combat System ===")

    # Create an elite card
    warrior = EliteCard(
        name="Arcane Warrior",
        cost=6,
        rarity="Epic",
        attack=5,
        defense=3,
        health=20,
        mana=10,
        spell_power=7
    )

    print("\nCombat Stats:")
    print(warrior.get_combat_stats())

    print("\nMagic Stats:")
    print(warrior.get_magic_stats())

    # Simulated enemy (another EliteCard for simplicity)
    enemy = EliteCard(
        name="Enemy",
        cost=4,
        rarity="Common",
        attack=4,
        defense=2,
        health=15,
        mana=5,
        spell_power=4
    )

    print("\n--- Combat Phase ---")

    attack_result = warrior.attack(enemy)
    print("Attack result:", attack_result)

    defense_result = warrior.defend(5)
    print("Defense result:", defense_result)

    print("\n--- Magic Phase ---")

    spell_result = warrior.cast_spell("Fireball", ["Enemy"])
    print("Spell cast result:", spell_result)

    channel_result = warrior.channel_mana(5)
    print("Mana channel result:", channel_result)

    print("\nFinal Magic Stats:")
    print(warrior.get_magic_stats())


if __name__ == "__main__":
    main()