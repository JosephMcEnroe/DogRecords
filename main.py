from dog import Dog
from kennel import Kennel
k = Kennel()
k.add(Dog("Aang",12,"American Akita","Male"))
d = Dog()
# d.Gender = " "


# d.Name = "Aang"
# d.Age = 12
# d.Breed = "American Akita"
# d.Gender = "Male"
print(k.display())
k.write_to_file()
