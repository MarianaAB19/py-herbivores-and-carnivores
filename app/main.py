class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{" \
               f"Name: {self.name}, " \
               f"Health: {self.health}, " \
               f"Hidden: {self.hidden}" \
               f"}}"

    def beast_die(self) -> None:
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Herbivore) -> int | str:
        if isinstance(animal, Carnivore):
            return animal.health
        if animal.hidden is False:
            animal.health -= 50
            animal.beast_die()
        else:
            return "Carnivore cannot bite hidden herbivore"
            animal.hide()
