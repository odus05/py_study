"""
Property : 관리 속성 만들기
클래스 속성에 대한 접근 제어를 제공하는 기능
Property를 사용하면 클래스 내부의 속성에 대해 읽기, 쓰기, 삭제 등의 동작을 캡슐화 할 수 있어, 객체 외부에서는 마치 일반적인 속성처럼 보이지만, 내부적으로는 특정 함수가 실행되도록 제어할 수 있음
    1) 데이터 은닉 : 클래스 내부에서 사용하는 데이터를 직접 노출시키지 않고, 속성에 대한 접근을 메서드를 통해 제어할 수 있음
    2) 유효성 검증 : 속성 값이 설정될 때 유효성 검사하거나, 값을 가져올 때 추가적인 변환 작업을 할 수 있음
    3) 속성 변경에 따른 추가 동작 등을 구현할 수 있음.
"""


class Person:
    def __init__(self, first_name):
        self._first_name = first_name
        
    @property
    def first_name(self):
        """이 메서드는 속성을 불러올 때 호출"""
        print("Getter Method Called!")
        return self._first_name
    
    @first_name.setter
    # @first_name.setter로 데코레이터를 지정하면 해당 속성을 변경하려 할 때마다 자동으로 호출된다.
    # 이때, 타입을 검사할 수 있음.
    def first_name(self, value):
        """이 메서드는 속성에 값을 설정할 때 호출"""
        print("Setter Method Called!!")
        if not isinstance(self._first_name, str):
            raise TypeError("Expected String")
        self._first_name = value
        
    @first_name.deleter
    def first_name(self):
        """이 메서드는 속성을 삭제할 때 호출"""
        print("Deleter Method Called!!")
        del self._first_name
        
if __name__ == "__main__":
    C_person = Person("Guido")
    print(C_person.first_name)
    C_person.first_name = 'Dave'
    
    try:
        C_person.first_name = 42
    except TypeError as e:
        print(e)
    
    del C_person.first_name 
    
# Property를 사용하면 계산된 속성도 쉽게 만들 수 있음
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @property
    # area는 읽기 전용 속성으로 정의되며, width와 height를 곱한 값을 반환
    def area(self):
        return self._width * self._height

rect = Rectangle(4, 5)
print(rect.area)