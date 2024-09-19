# Special Method(Magic Method)
from functools import total_ordering
""" 
functools.total_ordering 데코레이터를 사용하면 과정을 단순화 할 수 있음.
클래스에 데코레이터를 붙이고 __eq__() 와 비교 메소드
(__lt__,__le__,__gt__,__ge__) 중 하나만 더 정의하면 된다 .
"""
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width
        
        
@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()
        
    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)
    
    def add_room(self, room):
        self.rooms.append(room)
        
    def __str__(self):
        return f"{self.name}: {self.living_space_footage} square foot {self.style}"
    
    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage
    
    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage
            

    

if __name__ == "__main__":
    h1 = House("h1" , "Cape")
    h1.add_room(Room('Master Bedroom', 14, 21))
    h1.add_room(Room('Living Room', 18, 20))
    h1.add_room(Room('Kitchen', 12, 16))
        
    h2 = House("h1" , "Ranch")
    h1.add_room(Room('Master Bedroom', 14, 21))
    h1.add_room(Room('Living Room', 18, 15))
    h1.add_room(Room('Kitchen', 12, 13))
    
    print("Is h1 bigger than h2?" , h1 > h2)
    print("Is h1 smaller than h2?" , h1 < h2)
