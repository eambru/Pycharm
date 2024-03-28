from __future__ import annotations

from enum import Enum
from dataclasses import dataclass, field


@dataclass
class Menu:
    number: str = field(hash=True)
    name: str = field(compare=False)
    type: Type = field(compare=False)
    texture: str = field(compare=False)
    meal: list[Meal] = field(compare=False, repr=False, default_factory=lambda: [])

    class Type(Enum):
        MEAT = "Meat"
        SOUP = "Soup"
        CAKE = "Cake"
        NOODLES = "Noodles"

    @dataclass
    class Meal:
        menu_id: int = field(hash=True)
        time: str = field(compare=False)
        cutlery: str = field(compare=False)
