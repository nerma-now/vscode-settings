class Person:
    def __init__(self, name: str, username: str, location: str, telegram_username: str):
        self.name: str = name
        self.username: str = username
        self.location: str = location
        self.telegram_username: str = telegram_username

    def __str__(self):
        return f"Hey, it's {self.name} (@{self.username}) from {self.location}! Hit me up on TG: @{self.telegram_username}"


def main() -> None:
    person: Person = Person(
        name="Nikita",
        username="nerma-now",
        location="Republic of Belarus",
        telegram_username="nerma_now",
    )

    print(person)


if __name__ == "__main__":
    main()
