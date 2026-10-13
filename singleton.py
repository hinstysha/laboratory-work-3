"""Повышенная сложность, задание 1: Singleton для настроек программы."""

from typing import Optional


class AppSettings:
    """Предоставляет один объект настроек в однопоточной программе."""

    _instance: Optional["AppSettings"] = None

    def __new__(cls) -> "AppSettings":
        """Создаёт объект один раз и возвращает его при следующих вызовах."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {}
        return cls._instance

    def set_setting(self, key: str, value: str) -> None:
        """Сохраняет строковое значение настройки по строковому ключу."""
        self._settings[key] = value

    def get_setting(self, key: str, default: str = "") -> str:
        """Возвращает настройку или значение по умолчанию."""
        return self._settings.get(key, default)


def main() -> None:
    """Демонстрирует идентичность объектов и общее состояние."""
    first = AppSettings()
    first.set_setting("theme", "dark")
    second = AppSettings()
    print(f"Один и тот же объект: {first is second}")
    print(f"Тема через второй объект: {second.get_setting('theme')}")
    second.set_setting("theme", "light")
    print(f"Тема через первый объект: {first.get_setting('theme')}")


if __name__ == "__main__":
    main()
