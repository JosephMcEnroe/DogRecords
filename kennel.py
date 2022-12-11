import csv
from dog import Dog


filename = "records.csv"


class Kennel:
    records = []

    def add(self, dog):
        self.records.append(dog)

    def display(self):
        data = ""
        for i in self.records:
            data += i.print() + "\n"
        return data

    def write_to_file(self):
        with open(filename, "w") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows("name,age,breed,gender")
            for i in self.records:
                csvwriter.writerows(i.write())
    def read_from_file(self):
        with open(filename, "r") as csvfile:
            csvreader = csv.reader(csvfile)
            # while(csvreader.End):


