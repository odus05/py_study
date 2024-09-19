# 문제 : 순환 가능한 아이템에 접근할 때, for 순환문을 사용하고 싶지 않다.
with open("debug.log") as f:
    try:
        while True:
            # 해결 : iterator를 사용한다. 
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass
    
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x # generator 생성.
        x += increment

print(f"frange : {frange(0, 4, 0.5)}")

for n in frange(0, 4, 0.5):
    print(n , end=' ')

    
    
# Coroutine(코루틴)
"""
코루틴은 파이썬에서 비동기 프로그래밍을 구현하는 핵심 개녕 중 하나로,
함수 실행을 중단했다가 다시 재개할 수 있는 특수한 함수

코루틴은 동시성 프로그래밍을 지원하며, 비동기 작업을 효율적으로 처리하는데 사용

일반 함수와 달리, 코루틴은 중간에 실행을 멈추고 다른 작업을 수행한 후 다시 이어서 실행할 수 있습니다.
이를 통해 협력적인 멀티태스킹을 구현할 수 있습니다.

일반적으로 "async" 및 "await" 키워드를 사용하여 정의하고 실행.

    1) 비동기 I/O 처리: 네트워크 요청, 파일 읽기/쓰기, DB조회 같은 작업에서 I/O가 완료될 때까지 대기하는 대신 다른 작업을 처리할 수 있습니다.
    2) 동시성 지원: 스레드를 사용하지 않고도, 여러 작업을 동시에 처리하는 동시성을 구현할 수 있음
    3) 성능 최적화: 동기 코드와 비교했을 때, 비동기 코드에서는 여러 작업이 대기시간 없이 효율적 처리되어, CPU 사용률을 극대화할 수 있습니다.
"""


# Receiver 역활.
def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return start

@coroutine
def receiver():
    print("Ready to receive")
    while True:
        n = yield 
        print(f"Got {n}")
        
r = receiver()
r.send(1)
r.send("Test")
r.close()
