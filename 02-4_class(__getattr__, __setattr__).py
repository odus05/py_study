"""
파이썬의 __getattr__, __setattr__은 객체의 속성에 접근할 때 커스터마이징 할 수 있는 특별한 매직 메소드들입니다.
이들은 객체의 속성에 대한 동적 접근 및 제어를 가능하게 하며, 속성접근 제어, 속성 값의 자동생성 또는 디버깅 등에 활용됩니다.

__getattr__: 존재하지 않는 속성에 접근하려 할 때 호출되는 메소드입니다.
즉, 객체에서 찾을 수 없는 속성에 접근할 때 이 매서드가 호출되어 해당 속성의 동적 처리나 기본 값을 반환할 수 있음(예: 로그 기록, 기본 값 설정)

__setattr__: 속성에 값을 할당할 때 호출됩니다. 객체의 모든 속성에 대한 값을 설정할 때 이 메소드를 호출하게 되며 이를 통해 속성값을 설정할 때 제어 및 추가 검증 등의 동작을 수행할 수 있음.


"""

# Proxy 디자인 패턴
"""
Proxy 디자인 패턴은 객체의 대리자 역활을 하는 객체를 만들어, 원래 객체에 대한 접근을 제어하는 디자인 패턴입니다.
이 패턴은 원래 객체에 대한 접근을 제한하거나, 객체에 대한 추가적인 작업을 처리해야할 때 사용됩니다.
프록시는 대리 객체로서 동작하며, 원래 객체와 동일한 인터페이스를 제공하지만, 원래 객체에 대한 실제 접근을 제어할 수 있는 기능을 제공합니다.

프록시 패턴은 구조적 디자인 패턴 중 하나로, 객체의 구조를 제어하거나 확장하는 데 도움을 줍니다.
이는 원래 객체에 직접 접근하는 대신 대리 객체를 통해 간접적으로 접근함으로써, 객체의 동작을 개선하거나 수정할 수 있는 유연성을 제공합니다.

"""
class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    # 자신에게 없는 속성을 접근했을 때, 호출됨.    
    def __getattr__(self, name):
        # 동적으로 속성을 생성하거나 기본 값을 제공할 수 있음.
        # 속성 접근 시 자동으로 처리할 수 있는 추가 로직을 삽입 기능 (예: 로그 기록, 기본값 설정)
        print(f"Proxy.__getattr__(name={name})")
        return getattr(self._obj, name)
    
    # 자신에게 있던 없든 관계없이 무조건 호출됨.
    # 만약, 이름이 밑줄"_"로 시작하면, super()를 사용해서 __setter__() 원래의 구현을 호출한다.
    def __setattr__(self, name, value):
        if name.startswith("_"):
            print(f"Proxy.__setattr__(name={name}, value={value})")
            # __setter__()구현에서 이름 확인이 들어 있다. 만약 이름이 밑줄로 시작하면 super()를 사용해서 __setter__()의 원래 구현을 호출한다.
            super().__setattr__(name, value) 
            # self._obj = obj 호출 시 부모의 __setattr__ 함수 호출 필요!
            # 특별 메소드를 오버라이드 한 코드에서 super()를 사용하기도 한다.
        else:
            print(f"Setting Object : {name} = {value}")
            setattr(self._obj, name, value)

if __name__ == "__main__":
    
    class A:
        def __init__(self, x):
            self.x = x
        def spam(self):
            print("A.spam")
            return 1
            
    a = A(42)
    p = Proxy(a)
    
    print(p.spam())    
    print("=" * 50)        
            
    p.x = 42
    print(p.x)
    print("=" * 50)   
    
    print(a.x)    
    
