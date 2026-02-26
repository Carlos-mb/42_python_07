from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print()
    elite = EliteCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Epic",
        attack=5,
        defense=3,
        health=20,
        mana=10,
        spell_power=7
    )
    print()
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()
    print(f"\nPlaying {elite.name} (Elite Card):")
    print()
    print("Combat phase:")

    # Crazy thing to meet PDF signatures and expected behaviour
    # I don't know if it expect a list of string, cards or a single card
    # Implementation doesn't matter, the exercise objective is the
    # comprehension of OOP concepts.
    class DummyTarget:
        def __init__(self) -> None:
            self.name = "Enemy"

        def defend(self, incoming_damage: int) -> dict:
            return {"damage_taken": incoming_damage}

    dummy = DummyTarget()
    attack_result = elite.attack(dummy)
    print(f"Attack result: {attack_result}")
    defense_result = elite.defend(2)
    print(f"Defense result: {defense_result}")
    print()
    print("Magic phase:")
    spell_result = elite.cast_spell("Fireball", ["Enemy"])
    print(f"Spell cast: {spell_result}")
    mana_result = elite.channel_mana(3)
    print(f"Mana channel: {mana_result}")
    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
