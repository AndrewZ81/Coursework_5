from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    """
    Базовый класс героя
    """
    name: str  # Название
    max_health: float  # Максимальное число очков здоровья
    max_stamina: float  # Максимальное число очков выносливости
    attack: float  # Модификатор атаки
    stamina: float  # Модификатор выносливости
    armor: float  # Модификатор защиты
    skill: Skill  # Умение


WarriorClass = UnitClass(  # Экземпляр Воин
    name="Воин",
    max_health=60.0,
    max_stamina=30.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
)

ThiefClass = UnitClass(  # Экземпляр Вор
    name="Вор",
    max_health=50.0,
    max_stamina=25.0,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot()
)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
