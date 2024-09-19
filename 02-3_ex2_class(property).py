""" 
게으른 계산을 하는 Property 사용
    - 읽기 전용 속성을 Property로 정의하고, 이 속성에 접근할 때만 계산하도록 하고 싶다. 단, 한 번 접근하고 나면 이 값을 캐시해 놓고 다음 번에 접근할 때에는 다시 계산하지 않도록 하고 싶다.
"""
class lazyproperty:
    def __init__(self, func):
        self.func = func
        
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value  = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
        
        
if __name__ == "__main__":
    import math
    class Circle:
        def __init__(self, radius):
            self.radius = radius
        
        
        @lazyproperty
        # area = lazyproperty(area)
        def area(self):
            print("Computing area")
            return math.pi * self.radius ** 2
        
        @lazyproperty
        def perimeter(self):
            print("Computing perimeter")
            return 2 * math.pi * self.radius 
        
c = Circle(4.0)
print(c.radius)
print(c.__dict__)
print("="*30)

print(c.area)
print(c.__dict__)
print("="*30)

print(c.area)
print("="*30)

print(c.perimeter)
print(c.__dict__)
print("="*30)

print(c.perimeter)
print("="*30)

