# Special Method(Magic Method)

class Fruit:
    """Fruit Class Info"""
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def __repr__(self):
        return f"Fruit({self._name}, {self._price})"

    def __equal__(self, other):
        print("Called >> __equal__ Method.")
        if self._price == other._price:
            return True
        else:
            return False
        
    def __gt__(self, other):
        print('Called >> __gt__ Method.')
        if self._price > other._price:
            return True
        else:
            return False
        
    def __sub__(self, other):
        print('Called >> __sub__ Method.')
        return self._price - other._price

    def __add__(self, other):
        print('Called >> __add__ Method.')
        return self._price + other._price

        
        

# 객체의 Context 관리 및 프로토콜 지원
from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self._address = address
        self._family = family
        self._type = type
        self._sock = None
    
    # with 문을 만나면 __enter__ 호출
    def __enter__(self):
        if self._sock is not None:
            raise RuntimeError("Already Connected")
        self._sock = socket(self._family, self._type)
        self._sock.connect(self._address)
        return self._sock
    
    # with문 나가면, __exit__ 호출
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._sock.close()
        self._sock = None
        

if __name__ == "__main__":
    
    # instance 생성
    s1 = Fruit('Orange', 7500)
    s2 = Fruit('Banana', 3000)

    print(s1)
    print(s1.__doc__)

    # 매직메소드 출력
    print(s1 > s2)
    print(s1 == s2)
    print(s1 != s2)
    print(s1 - s2)
    print(s1 + s2)
        
    from functools import partial
    
    lazy_c = LazyConnection(("www.python.org", 80))
    with lazy_c as socket:
        socket.send(b'GET /index.html HTTP/1.0\r\n')
        
        
        
        
