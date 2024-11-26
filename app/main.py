from typing import Union


class Animal:
    """stores all alive animals"""
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def beast_die(self) -> None:
        """Removes the animal from Animal.alive list
        if its health is 0 or less"""
        if self.health <= 0:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        """Changes the hidden property of the beast to the opposite value"""
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Herbivore) -> Union[int, str]:
        """Takes a herbivore object and decreases the object's health by 50,
        does not work if it is another сarnivore,
        or the herbivore is currently hiding"""
        if isinstance(animal, Carnivore):
            return animal.health
        if animal.hidden is False:
            animal.health -= 50
            animal.beast_die()
        else:
            animal.hide()
            return "Carnivore cannot bite hidden herbivore"
