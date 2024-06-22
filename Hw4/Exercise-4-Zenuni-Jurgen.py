#Exercise 4
class Animal:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class Elephant(Animal):
    def __init__(self, name, trunk_length):
        super().__init__(name)
        self.trunk_length = trunk_length
        
    def speak(self):
        print("trumpet!")
    
    def get_trunk_length(self):
        return self.trunk_length

class Eagle(Animal):
    def speak(self):
        print("screech")

class Parrot(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.vocabulary = []
    
    def get_vocabulary(self):
        return self.vocabulary
    
    def add_word(self, word):
        self.vocabulary.append(word)
    
    def get_word(self):
        import random
        return random.choice(self.vocabulary)
    
    def speak(self):
        print(self.get_word())

eagle = Eagle("Eddie")
print("Animal:", eagle.get_name())
print("Sound:", end=" ")
eagle.speak()

dumbo = Elephant("Dumbo", 5)
print("Animal:", dumbo.get_name())
print("Trunk is long:", dumbo.get_trunk_length())
print("Sound:", end=" ")
dumbo.speak()

parrot = Parrot("Cocorito")
parrot.add_word("one")
print("Animal:", parrot.get_name())
for i in range(3):
    print("Sound:", end=" ")
    parrot.speak()

cocorito = Parrot("Cocorito")
cocorito.add_word("one")
cocorito.add_word("two")
cocorito.add_word("four")
print("Animal:", cocorito.get_name())
for i in range(4):
    print("Sound:", end=" ")
    cocorito.speak()

