

class Dvd:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __str__(self):
        return f'{self.name}, {self.year}'


box_dvd = [None] * 15
box_dvd.append(Dvd('horror', 1996))
box_dvd.append(Dvd('komedy', 1980))
box_dvd[10] = Dvd('drama', 1988)

for e, i in enumerate(box_dvd):
    print(e, i)
