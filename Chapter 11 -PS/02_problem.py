class Animals:
    pass
class pets(Animals):
    pass
class dogs(pets):
    @staticmethod
    def bark():
        print("Woof!")

d = dogs()
d.bark()