from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class Skill(ABC):
    """
    Базовый класс умения
    """
    user = None  # Игрок
    target = None  # Противник

    @property
    @abstractmethod
    def name(self):
        """
        Имя
        """
        pass

    @property
    @abstractmethod
    def stamina(self):
        """
        Требуемая выносливость
        """
        pass

    @property
    @abstractmethod
    def damage(self):
        """
        Урон
        """
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        """
        Здесь происходит уменьшение выносливости у игрока, применяющего умение и
        уменьшение здоровья цели.
        """

    def _is_stamina_enough(self):
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class FuryPunch(Skill):
    """
    Класс Свирепый пинок
    """
    name:str = "Свирепый пинок"
    stamina:float = 6.0
    damage:float = 12.0

    def skill_effect(self) -> str:
        self.target.get_damage(self.damage)
        self.user.stamina -= self.stamina
        if self.user.stamina >= self.stamina:
            return f"{self.user.name} использует {self.name} " \
                   f"и наносит {self.damage} урона сопернику"
        else:
            return f"{self.user.name} попытался использовать {self.name}, " \
                   f"но у него не хватило выносливости."


class HardShot(Skill):
    """
    Класс Мощный укол
    """
    name: str = "Мощный укол"
    stamina: float = 5.0
    damage: float = 15.0

    def skill_effect(self):
        self.target.get_damage(self.damage)
        self.user.stamina -= self.stamina
        if self.user.stamina >= self.stamina:
            return f"{self.user.name} использует {self.name} " \
                   f"и наносит {self.damage} урона сопернику"
        else:
            return f"{self.user.name} попытался использовать {self.name}, " \
                   f"но у него не хватило выносливости."
