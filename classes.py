from dataclasses import dataclass


@dataclass
class UnitClass:
    """Базовый класс героя"""
    name: str  # Имя героя
    max_health: float  # Максимальное здоровье
    max_stamina: float  # Максимальная выносливость
    attack: float  # Сила атаки
    stamina: float  # Текущая выносливость
    armor: float  # Показатель брони
    skill: Skill  # Способность героя


WarriorClass = UnitClass(...)  # Экземпляр Воин
ThiefClass = UnitClass(...)  # Экземпляр Вор

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}