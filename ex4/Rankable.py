Class Rankable inherits from ABC

    Abstract method calculate_rating() -> int
        # Devuelve rating actual basado en wins/losses

    Abstract method update_wins(wins: int) -> None
        # Incrementa contador de victorias

    Abstract method update_losses(losses: int) -> None
        # Incrementa contador de derrotas

    Abstract method get_rank_info() -> dict
        # Devuelve información estructurada del ranking