# Proxy 디자인 패턴

# 특별 메소드를 오버라이드 한 코드에서 super()를 사용하기도 한다.
# __setter__()구현에서 이름 확인이 들어 있다. 만약 이름이 밑줄로 시작하면 super()를 사용해서 __setter__()의 원래 구현을 호출한다.

class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    # 자신에게 없는 속성을 접근했을 때, 호출됨.    
    def __getattr__(self, name):
        print(f"Proxy.__getattr__(name={name})")
        return getattr(self._obj, name)
    
    # 자신에게 있던 없든 관계없이 무조건 호출됨.
    def __setattr__(self, name, value):
        print(f"Proxy.__setattr__(name={name}, value={value})")
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
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
    p.x = 42
    
    print(p.x)
    print('='*30)
    print(a.x)    