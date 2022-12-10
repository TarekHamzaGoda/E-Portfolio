class CarTypes:
    """A class to store car types"""
    def __init__(self):
        self.car_types = dict()

    def data_keys(self):
        return self.car_types.keys()

    def data_items(self):
        return self.car_types.items()

    def data_values(self):
        return self.car_types.values()


car_db = CarTypes()
car_db.car_types.update({"Sedan": {"Toyota": 2013}, "Hatchback": {"Volvo" : 2014}})

datakeys = car_db.data_keys()
dataitems = car_db.data_items()
datavalues = car_db.data_values()

print(datakeys)
print(datavalues)
print(dataitems)


