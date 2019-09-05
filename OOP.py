class Cat:
    species = "animal"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def discription(self):
        return "{} is {}".format(self.name , self.age)
gus = Cat("gus", "age")
print(gus.discription())