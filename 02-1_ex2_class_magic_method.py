# Special Method(Magic Method)

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
    from functools import partial
    
    lazy_c = LazyConnection(("www.python.org", 80))
    with lazy_c as socket:
        socket.send(b'GET /index.html HTTP/1.0\r\n')
        
        
        
        
