""" 
새로운 클로스나, 인스턴스 속성 만들기.
    - 새로운 종류의 인스턴스 속성을 만드려면, 그 기능을 디스크립터 클래스 형태로 정의
"""

class Integer:
    def __init__(self, name):
        self.name = name
        
    def __get__(self, instance, cls):
        print("__get__ Method Called")
        if instance is None:
            print("instance is None!")
            return self
        else:
            print(f"instance: {instance}, class: {cls}")
            print(f"get : {self.name}")
            return instance.__dict__[self.name]
        
    def __set__(self, instance, value):
        print("__set__ Method Called")
        if not isinstance(value, int):
            # 타입 확인 추가적 기능 추가
            raise TypeError("Expected an int")
        print(f"set : {self.name} = {value}")
        instance.__dict__[self.name] = value
        
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

if __name__ == "__main__":
    p = Point(2, 3)
    print(p.x)
    
    p.y = 5
    
    try:
        p.x = 2.3
    except TypeError as e:
        print(e) 
    
    