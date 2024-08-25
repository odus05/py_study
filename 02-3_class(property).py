# Property : 관리 속성 만들기
# 인스턴스 속성을 얻거나, 설정할 때 추가적인 처리(타입 체크, 검증 등) 가능

class Person:
    def __init__(self, first_name):
        self._first_name = first_name
        
    @property
    def first_name(self):
        print("Get Method!")
        return self._first_name
    
    @first_name.setter
    # @first_name.setter로 데코레이터를 지정하면 해당 속성을 변경하려 할 때마다 자동으로 호출된다.
    # 이때, 타입을 검사할 수 있음.
    def first_name(self, value):
        print("Set Method")
        if not isinstance(self._first_name, str):
            raise TypeError("Expected String")
        self._first_name = value
        
if __name__ == "__main__":
    C_person = Person("Guido")
    print(C_person.first_name)
    C_person.first_name = 'Dave'
    
    try:
        C_person.first_name = 42
    except TypeError as e:
        print(e)