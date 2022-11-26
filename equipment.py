from dataclasses import dataclass
from typing import List
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    """
    Класс Броня
    """
    pass


@dataclass
class Weapon:
    """
    Класс Оружие
    """
    pass

    @property
    def damage(self):
        pass


@dataclass
class EquipmentData:
    """
    Класс Набор экипировки
    """
    # TODO содержит 2 списка - с оружием и с броней
    pass


class Equipment:
    """
    Интерфейсный класс Экипировка
    """

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        # TODO возвращает объект оружия по имени
        pass

    def get_armor(self, armor_name) -> Armor:
        # TODO возвращает объект брони по имени
        pass

    def get_weapons_names(self) -> list:
        # TODO возвращаем список с оружием
        pass

    def get_armors_names(self) -> list:
        # TODO возвращаем список с броней
        pass

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData
        equipment_file = open("./data/equipment.json")
        data = json.load( ... )
        equipment_schema = marshmallow_dataclass.class_schema( ... )
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
