from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def player_info(self) -> None:
        print(f"Dwarf warrior {self.nickname}. {self.nickname}"
              f" has a hummer of the {self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4
