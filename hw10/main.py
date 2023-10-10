from AnimalFabric import AnimalFabric
from Animals import Dog, Bird, Fish


if __name__ == '__main__':
    dog = Dog("Рэкс", 40, 5, "Такса")
    bird = Bird("Гоша", 1, 3, "Попугай", "Чирик")
    fish = Fish("Карп", 10, 5, "Речной")
    print(dog)
    print(bird)
    print(f'{fish}\n')
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("dog", "Рэкс", 40, 5, "Такса")
    animal_from_fabric1 = fabric.make_animal("bird", "Гоша", 1, 3, "Попугай", "Чирик")
    print(animal_from_fabric)
    print(animal_from_fabric1)
    print(fabric.make_animal('Fish', "Карп", 10, 5, "Речной"))
    print()