"""Средняя сложность, задание 3: пополнение и снятие со счёта."""

from decimal import Decimal, InvalidOperation
from typing import Union


Money = Union[int, float, str, Decimal]


class BankAccount:
    """Хранит баланс в Decimal; операции выполняются с точностью до копейки."""

    def __init__(self, initial_balance: Money = 0) -> None:
        """Создаёт счёт с неотрицательным начальным балансом."""
        self._balance = self._validate_amount(initial_balance)

    @staticmethod
    def _validate_amount(amount: Money) -> Decimal:
        """Проверяет тип, конечность, знак и точность денежной суммы."""
        if isinstance(amount, bool) or not isinstance(
            amount, (int, float, str, Decimal)
        ):
            raise TypeError("Сумма должна быть числом или числовой строкой.")
        try:
            value = Decimal(str(amount))
        except InvalidOperation as error:
            raise ValueError("Некорректная денежная сумма.") from error
        if not value.is_finite() or value < 0:
            raise ValueError("Сумма должна быть конечной и неотрицательной.")
        try:
            rounded = value.quantize(Decimal("0.01"))
        except InvalidOperation as error:
            raise ValueError("Сумма слишком велика.") from error
        if value != rounded:
            raise ValueError("Сумма должна быть кратна одной копейке.")
        return rounded

    @property
    def balance(self) -> Decimal:
        """Возвращает баланс без возможности присвоения через это свойство."""
        return self._balance

    def deposit(self, amount: Money) -> Decimal:
        """Пополняет счёт положительной суммой и возвращает новый баланс."""
        value = self._validate_amount(amount)
        if value == 0:
            raise ValueError("Сумма пополнения должна быть больше нуля.")
        self._balance += value
        return self._balance

    def withdraw(self, amount: Money) -> Decimal:
        """Снимает положительную сумму, если средств достаточно."""
        value = self._validate_amount(amount)
        if value == 0:
            raise ValueError("Сумма снятия должна быть больше нуля.")
        if value > self._balance:
            raise ValueError("Недостаточно средств на счёте.")
        self._balance -= value
        return self._balance


def main() -> None:
    """Демонстрирует пополнение, снятие и обработку недостатка средств."""
    account = BankAccount("1000.00")
    print(f"Начальный баланс: {account.balance:.2f} руб.")
    print(f"После пополнения: {account.deposit('250.50'):.2f} руб.")
    print(f"После снятия: {account.withdraw('400.00'):.2f} руб.")
    try:
        account.withdraw("2000.00")
    except ValueError as error:
        print(f"Ошибка: {error}")
    print(f"Итоговый баланс: {account.balance:.2f} руб.")


if __name__ == "__main__":
    main()
