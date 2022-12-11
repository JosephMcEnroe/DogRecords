class Dog:
    name = "N/A"
    age = 0
    breed = "Unassigned breed"
    gender = "Unassigned gender"

    # Set and Get for Name
    def _get_name(self):
        return self.name

    def _set_name(self, name):
        if name != " ":
            self.name = name

    # Set and Get for Breed
    def _get_breed(self):
        return self.breed

    def _set_breed(self, breed):
        if not " ":
            self.breed = breed

    # Set and Get for Gender
    def _get_gender(self):
        return self.gender

    def _set_gender(self, gender):
        if not "":
            self.gender = gender

    # Set and get for Age
    def _get_age(self):
        return self.age

    def _set_age(self, age):
        if age > 0:
            self.age = age

    Name = property(_get_name, _set_name)
    Breed = property(_get_breed, _set_breed)
    Gender = property(_get_gender, _set_gender)
    Age = property(_get_age, _set_age)

    def __int__(self):
        self.Name = self.name
        self.Age = self.age
        self.Breed = self.breed
        self.gender = self.gender

    # parameterized constructor
    def __init__(self, name, age, breed, gender):
        self.Name = name
        self.Age = age
        self.Breed = breed
        self.Gender = gender

    def write(self):
        return "% s,% s,% s,% s" % (self.Name, self.Age, self.Breed, self.Gender)

    def print(self):
        return "Name: " + self.name + ", Age: " + str(self.age) + ", Breed: " + self.breed + ", Gender: " + self.gender;
