from dataclasses import dataclass


@dataclass
class UnitClass:
    """Базовый класс героя"""
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(...)  # Создаём экземпляр Воин
ThiefClass = UnitClass(...)  # Создаём экземпляр Вор

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}