"""Средняя сложность, задание 1: книга с названием и автором."""


class Book:
    """Хранит название книги и имя автора."""

    def __init__(self, title: str, author: str) -> None:
        """Создаёт книгу с указанными названием и автором."""
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Возвращает краткое текстовое описание книги."""
        return f'«{self.title}», автор: {self.author}'


def main() -> None:
    """Демонстрирует создание книги и чтение её полей."""
    book = Book("Капитанская дочка", "Александр Пушкин")
    print(f"Название: {book.title}")
    print(f"Автор: {book.author}")
    print(book)


if __name__ == "__main__":
    main()
