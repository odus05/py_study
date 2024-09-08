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
