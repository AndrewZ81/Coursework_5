from dataclasses import dataclass
from typing import List, Optional
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    """
    Класс Броня
    """
    id: str  # Порядковый номер брони
    name: str  # Название брони
    defence: float  # Очки защиты
    stamina_per_turn: float  # Количество затрачиваемой выносливости за ход


@dataclass
class Weapon:
    """
    Класс Оружие
    """
    id: str  # Порядковый номер оружия
    name: str  # Название оружия
    min_damage: float  # Минимальный урон
    max_damage: float  # Максимальный урон
    stamina_per_hit: float  # Количество затрачиваемой выносливости за удар

    @property
    def damage(self) -> float:
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    """
    Класс Набор экипировки
    """
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment:
    """
    Интерфейсный класс Экипировка
    """

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Optional[Weapon]:
        """
        Возвращает объект оружия по имени
        """
        for i in self.equipment.weapons:
            if i.name == weapon_name:
                return i
        return None

    def get_armor(self, armor_name) -> Optional[Armor]:
        """
        Возвращает объект брони по имени
        """
        for i in self.equipment.armors:
            if i.name == armor_name:
                return i
        return None

    def get_weapons_names(self) -> list[str]:
        """
        Возвращаем список с оружием
        """
        return [i.name for i in self.equipment.weapons]

    def get_armors_names(self) -> list[str]:
        """
        Возвращаем список с броней
        """
        return [i.name for i in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        with open("./data/equipment.json") as file:
            equipment_file = file.read()
            data = json.loads(equipment_file)
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
