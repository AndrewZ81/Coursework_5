from __future__ import annotations
from abc import ABC, abstractmethod
from equipment import Weapon, Armor
from classes import UnitClass
from random import randint
from typing import Optional


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """
    def __init__(self, name: str, unit_class: UnitClass):
        """
        При инициализации класса Unit использует свойства класса UnitClass
        """
        self.name = name  # Имя персонажа
        self.unit_class = unit_class  # Класс персонажа (объект, Воин или Вор),
        self.hp = unit_class.max_health  # Очки здоровья
        self.stamina = unit_class.max_stamina  # Очки выносливости
        self.weapon = None  # Оружие
        self.armor = None  # Броня
        self._is_skill_used = False  # Использовано ли умение в бою

    @property
    def health_points(self) -> float:
        """
        Возвращает аттрибут hp в красивом виде
        """
        return round(self.hp, 1)

    @property
    def stamina_points(self) -> float:
        """
        Возвращает аттрибут stamina в красивом виде
        """
        return round(self.stamina, 1)

    def equip_weapon(self, weapon: Weapon) -> str:
        """
        Присваивает нашему герою новое оружие
        """
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor) -> str:
        """
        Одевает новую броню
        """
        self.armor = armor
        return f"{self.name} экипирован броней {self.armor.name}"

    def _count_damage(self, target: BaseUnit) -> float:
        # TODO Эта функция должна содержать:
        #  логику расчета урона игрока
        #  логику расчета брони цели
        #  здесь же происходит уменьшение выносливости атакующего при ударе
        #  и уменьшение выносливости защищающегося при использовании брони
        #  если у защищающегося не хватает выносливости - его броня игнорируется
        #  после всех расчетов цель получает урон - target.get_damage(damage)
        #  и возвращаем предполагаемый урон для последующего вывода пользователю в текстовом виде

        self.stamina -= self.weapon.stamina_per_hit
        damage = self.weapon.damage * self.unit_class.attack
        target_stamina = target.armor.stamina_per_turn * target.unit_class.stamina

        if target.stamina > target_stamina:
            damage -= target.armor.defence * target.unit_class.armor
            target.stamina -= target_stamina

        damage = round(damage, 1)
        target.get_damage(damage=damage)

        return damage

    def get_damage(self, damage: float) -> Optional[float]:
        """
        Цель получает урон.
        Присваивает новое значение для аттрибута self.hp
        """
        if damage > 0:
            self.hp -= damage
        return None

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        Метод использования умения.
        Если умение уже использовано, возвращаем строку Навык использован
        Если же умение не использовано, тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернет нам строку, которая характеризует выполнение умения
        """
        if self._is_skill_used:
            return "Навык использован."
        self._is_skill_used = True
        return self.unit_class.skill.use(user=self, target=target)


class PlayerUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        Функция удар игрока:
        здесь происходит проверка, достаточно ли выносливости для нанесения удара.
        Вызывается функция self._count_damage(target),
        а также возвращается результат в виде строки
        """
        if self.stamina < self.weapon.stamina_per_hit:
            return f"<p>{self.name} попытался использовать {self.weapon.name}," \
                   f" но у него не хватило выносливости.</p>"

        damage = self._count_damage(target)

        if damage > 0:
            return f"<p>{self.name}, используя {self.weapon.name}, " \
                   f"пробивает {target.armor.name} соперника и наносит {damage} урона.</p>"

        return f"<p>{self.name}, используя {self.weapon.name}, " \
               f"наносит удар, но {target.armor.name} cоперника его останавливает.</p>"


class EnemyUnit(BaseUnit):

    def hit(self, target: BaseUnit) -> str:
        """
        Функция удар соперника:
        должна содержать логику применения соперником умения
        (он должен делать это автоматически и только 1 раз за бой).
        Например, для этих целей можно использовать функцию randint из библиотеки random.
        Если умение не применено, противник наносит простой удар, где также используется
        функция _count_damage(target)
        """
        if not self._is_skill_used and self.stamina > self.unit_class.skill.stamina and randint(0,100) < 10:
            return self.use_skill(target)

        if self.stamina < self.weapon.stamina_per_hit:
            return f"<p>{self.name} попытался использовать {self.weapon.name}," \
                   f" но у него не хватило выносливости.</p>"

        damage = self._count_damage(target)

        if damage > 0:
            return f"<p>{self.name}, используя {self.weapon.name}, " \
                   f"пробивает {target.armor.name} и наносит Вам {damage} урона.</p>"

        return f"<p>{self.name}, используя {self.weapon.name}, " \
               f"наносит удар, но Ваш(а) {target.armor.name} его останавливает.</p>"
