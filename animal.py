"""Средняя сложность, задание 5: наследование Animal → Dog."""


class Animal:
    """Описывает животное с именем и общим поведением."""

    def __init__(self, name: str) -> None:
        """Сохраняет имя животного."""
        self.name = name

    def speak(self) -> str:
        """Возвращает общее описание звука животного."""
        return f"{self.name} издаёт звук."


class Dog(Animal):
    """Наследует имя животного и переопределяет его голос."""

    def speak(self) -> str:
        """Возвращает описание лая собаки."""
        return f"{self.name} говорит: Гав!"


def main() -> None:
    """Показывает вызов одного метода для разных типов животных."""
    animals = [Animal("Животное"), Dog("Шарик")]
    for animal in animals:
        print(animal.speak())


if __name__ == "__main__":
    main()
