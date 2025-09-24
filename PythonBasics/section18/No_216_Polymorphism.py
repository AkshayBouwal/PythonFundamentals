class Duck:

    def talk(self):
        print("Duck is Talking !!")

    def walk(self):
        print("Duck is Walking !!")


class Dog:

    def talk(self):
        print("Dog is Talking !!")

    def walk(self):
        print("Dog is Walking !!")


if __name__ == '__main__':

    def person(pet):
        pet.talk()
        pet.walk()

    dog = Dog()
    person(dog)






    # def person(pet):
    #     pet.talk()
    #
    #     if hasattr(pet, 'walk'):
    #         pet.walk()



    # duck = Duck()
    # person(duck)

    # dog = Dog()
    # person(dog)