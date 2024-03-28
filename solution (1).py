from __future__ import annotations

from itertools import chain
from typing import cast

from model import Menu
from common.repository import Repository
from queries import Queries


class Solution(Repository, Queries):

    @staticmethod
    def type_mapper(values: dict[str, any]) -> Menu | Menu.Meal:
        match values:
            case {"number": _}:
                menu = Menu(**values)
                menu.type = next(
                    Menu.Type[entry.name]
                    for entry in Menu.Type
                    if entry.value == menu.type
                )
                return menu
            case {"menu_id": _}:
                return Menu.Meal(**values)

    @property
    def entities(self) -> list[Menu]:
        return cast(list[Menu], super().entities)

    def count_of_type(self, type: Menu.Type) -> int:
        return len([menu for menu in self.entities
                    if menu.type == type])

    def order(self) -> list[Menu]:
        return sorted(self.entities,
                      key=lambda menu: (-len(menu.meal), menu.name))

    def group_by_type(self) -> dict[Menu.Type, list[Menu]]:
        return {menu: [i for i in self.entities]
                for menu in (i.type for i in self.entities)}

    def distinct_menu_ids(self) -> set[str]:
        return {
            menu.menu_id
            for menu in chain.from_iterable([
                menus.meal
                for menus in self.entities
            ])
        }

    def minimum_meal_in_the_menu(self) -> Menu:
        return next(
            menu for menu in self.entities
            if len(menu.meal) == min([
                len(menu.meal) for menu in self.entities
            ])
        )


def main() -> None:
    repi = Solution(r"../data/menu.json")
    print("A legksiebb meal-vel rendelkező étel: ")
    print(repi.minimum_meal_in_the_menu())
    print("Az elemek sorbarendezése (a meal szerint csökkenő és name szerint növekvő sorrendbe): ")
    print(repi.order())
    print("Visszaadja az összes menu_id-t: ")
    print(repi.distinct_menu_ids())
    print("Az adott típusnak megfelelően összeszámolja az elemeket: ")
    print(repi.count_of_type(Menu.Type.CAKE))
    print("Az összes elemet csoportosítja típusok szerint: ")
    print(repi.group_by_type())


if __name__ == "__main__":
    main()
