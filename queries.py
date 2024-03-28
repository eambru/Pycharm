from abc import abstractmethod, ABC

from model import Menu


class Queries(ABC):

    @abstractmethod
    def count_of_type(self, type: Menu.Type) -> int:
        "Megszámollja az adott típusba tartozó elemeket"

    @abstractmethod
    def order(self) -> list[Menu]:
        "Visszatér a meal szerint csökkenő és a name szerint növekvő sorrendbe"

    @abstractmethod
    def group_by_type(self) -> dict[Menu.Type, list[Menu]]:
        "Visszatér a típusok szerinti csoportosítással"

    @abstractmethod
    def distinct_menu_ids(self) -> set[str]:
        "Visszatér a menu_id-kal"

    @abstractmethod
    def minimum_meal_in_the_menu(self) -> Menu:
        "visszaadja a legkisebb meal-vel rendelkező elem másolatát"
