from openpyxl import Workbook
import random as rd


class BirdSamples:

    def __init__(self, species):
        self.species = species
        self.sample = {}

    def generate_dataset(self):
        for bird in self.species:
            self.sample[bird] = rd.randint(1, 50)
        return

    def decrp_dict(self, key, value):
        key = []
        value = []

    def write_excel(self, rows, columns):
        wb = Workbook()
        wb.active()
        wb.create_sheet(title="birdsSample")

        for col in range(len(columns)):
            wb.row_dimension[1] = columns


if __name__ == '__main__':
    species = ["cuco", "picapau", "sabiá", "peru", "avestruz", "pombo"]
    bird = BirdSamples(species)
    bird.generate_dataset()
