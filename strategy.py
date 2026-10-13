"""Повышенная сложность, задание 4: стратегии расчёта цены."""

from abc import ABC, abstractmethod
from math import isfinite


class PricingStrategy(ABC):
    """Задаёт общий интерфейс стратегий расчёта цены."""

    @abstractmethod
    def calculate(self, price: float) -> float:
        """Рассчитывает итоговую цену по проверенной исходной цене."""
        raise NotImplementedError


class RegularPrice(PricingStrategy):
    """Оставляет цену без изменений."""

    def calculate(self, price: float) -> float:
        """Возвращает исходную цену."""
        return price


class PercentDiscount(PricingStrategy):
    """Применяет скидку от 0 до 100 процентов."""

    def __init__(self, percent: float) -> None:
        """Проверяет и сохраняет процент скидки."""
        if isinstance(percent, bool) or not isinstance(percent, (int, float)):
            raise TypeError("Процент скидки должен быть числом.")
        if not isfinite(percent) or not 0 <= percent <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100.")
        self._percent = percent

    def calculate(self, price: float) -> float:
        """Возвращает цену с учётом сохранённого процента скидки."""
        return price * (1 - self._percent / 100)


class PriceCalculator:
    """Проверяет исходную цену и делегирует расчёт выбранной стратегии."""

    def __init__(self, strategy: PricingStrategy) -> None:
        """Устанавливает начальную стратегию расчёта."""
        self.set_strategy(strategy)

    def set_strategy(self, strategy: PricingStrategy) -> None:
        """Меняет стратегию без изменения кода калькулятора."""
        if not isinstance(strategy, PricingStrategy):
            raise TypeError("Нужен объект стратегии PricingStrategy.")
        self._strategy = strategy

    def calculate(self, price: float) -> float:
        """Проверяет конечную неотрицательную цену и вычисляет результат."""
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if not isfinite(price) or price < 0:
            raise ValueError("Цена должна быть конечной и неотрицательной.")
        return self._strategy.calculate(price)


def main() -> None:
    """Показывает смену стратегии расчёта на одном калькуляторе."""
    price = 1250.50
    calculator = PriceCalculator(RegularPrice())
    print(f"Без скидки: {calculator.calculate(price):.2f} руб.")
    for percent in (10, 20, 50):
        calculator.set_strategy(PercentDiscount(percent))
        print(f"Скидка {percent}%: {calculator.calculate(price):.2f} руб.")


if __name__ == "__main__":
    main()
