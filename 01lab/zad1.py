from mimetypes import init


class Animal:
    def __init__(self, genus, gender='Female'):
        self.isAlive = True
        self.gender = gender
        self.genus = genus

    def breed(self, partner):
        if self.gender == 'Female' and \
           partner.gender == 'Male' and \
           self.genus == partner.genus:
            try:
                return self.__class__('Female')
            except AttributeError:
                print("attribute not found")


class Dog(Animal):
    def __init__(self, gender):
        self.genus='Canis'
        super().__init__(self.genus, gender)
    
    
    def woof(self):
        return 'woof woof'


class Cat(Animal):
    def __init__(self, gender):
        self.genus = 'Felis'
        super().__init__(self.genus, gender)
    
    
    def purr(self):
        return 'purr'


dog1 = Dog('Female')
dog2 = Dog('Male')
dog3 = dog1.breed(dog2)
print(dog3.woof())

cat1 = Cat('Male')
cat2 = Cat('Female')
cat3 = cat1.breed(cat2)  # obiekt nie zostanie utworzony
# print(cat3.purr()) - wiec to nie zadziala

dog4 = dog1.breed(cat1)  # tutaj rowniez
# print(dog4.woof())

cat4 = Animal('Felis')
# cat5 = cat1.breed(cat4)
