from collections import namedtuple


a=2
print(a)


class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("name")
print(dog)


class Singleton:
    _instance =None

    def __new__(cls):
        if cls.is_instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance



class House:

    def __init__(self):
        self.rooms= []
        self.walls= []
        self.windows= []
        self.flors= []
        self.swimming_pool = None
        self.garage =None
        self.taras=None
    
    def __str__(self):
        return (f"The House has the following\nrooms :{self.rooms}\nwalls: {self.walls}\nflors: {self.flors}\nwindows: {self.windows}\nswiming pool: {self.swimming_pool}\ngarage: {self.garage}")

class HouseBuilder:
    def __init__(self):
        self.house = House()
    
    def add_room(self, room):
        self.house.rooms.append(room)
        return self
    
    def add_walls(self, wall):
        self.house.walls.append(wall)
        return self
    
    def add_windows(self, *args):
        self.house.windows.append(args)
        return self
    
    def add_flors(self, flor):
        self.house.flors.append(flor)
        return self

    def add_garage(self):
        self.house.garage = True
        return self
	
    def add_swimming_pool(self):
        self.house.swimming_pool = True
        return self
	
    def build(self):
        return self.house

house = HouseBuilder().add_room("Salon").add_walls(1).build()
            
house2 = (HouseBuilder()
          .add_room("Salon").add_room("Kuchnia").add_room("Łazienka").add_room("Toaleta")
          .add_walls("Północcna")
          .add_walls("Południowa")
          .add_walls("Zachodnia")
          .add_walls("Wschodnia")
          .add_flors(1)
          .add_flors(2)
          .add_windows(1,3,4,5)
          .add_swimming_pool()
          .add_garage()
          .build())
	
print(house)
print(house2) 
