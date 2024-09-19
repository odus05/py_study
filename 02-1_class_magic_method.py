"""
객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
데이터 관리 (ex: 리스트, 딕셔너리, 클래스)

1) 리스트 구조 : 많은 양의 데이터를 관리하기 불편, 인덱스 접근 시 실수 가능성 증가, 삭제 불편
2) 딕셔너리 구조 -> 코드 반복 지속되고, 중첩 해결 문제, 키 조회 예약 처리 등

ex) Ferrari, Bmw, Audi, Kia ....
"""

car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color' : 'White', 'horsepower': 400, 'price': 8000},
    {'color' : 'Black', 'horsepower': 270, 'price': 5000},
    {'color' : 'Silver', 'horsepower': 300, 'price': 6000}
]

cars_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color' : 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color' : 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color' : 'Silver', 'horsepower': 300, 'price': 6000}}
]


# 3) 클래스 구조: 설계 후, 재사용성 증가, 코드 반복 최소화, 메소드 활용 가능
class Car:
    """
    Car Class
    """
    # 클래스 변수
    car_count = 0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1
        
    def __str__(self):
        return f"Car({self._company}, {self._details})"
    
    def detail_info(self):
        print(f'Current ID : {id(self)}')
        print(f"Car detail info : {self._company}, {self._details.get('price')}")
        
    def get_price(self):
        return self._details.get("price") 
    
    def get_raise_price(self):
        return self._details.get("price") * Car.price_per_raise
    
    # Classs Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or more")
            return 
        cls.price_per_raise = per
        return 'Succed!'
    
    # Staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'Ok it is bmw'
        return 'Sorry it is not bmw'
    
    def __del__(self):
        Car.car_count -= 1
    
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 인스턴스 namespace 접근해서 없으면 상위(클래스)에서 검색
print(car1.__dict__)
print(car2.__dict__)

# 일반 함수 호출
car1.detail_info()
car2.detail_info()


print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car2.__class__))

# classmethod 사용하여 가격 인상정보 제공
Car.raise_price(2.0)
# 인상 전 가격
print(car1.get_price())
# 인상 후 가격
print(car1.get_raise_price())

# staticmethod 사용
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))


print(Car.car_count)

del car2
print(car1.car_count)
print(Car.car_count)
