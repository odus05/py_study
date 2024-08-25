# 클로저
# 함수가 데이터로 취급될 때는 함수가 정의된 곳의 주변 환경 정보가 함께 저장

# 함수를 구성하는 문장과 실행 환경을 함께 묶은것을 "클로저"라고 부른다.

def calc():
    a=3
    b=5
    def mul_add(x):
        return a * x + b 
    return mul_add

c = calc()
print(c(1))

# 클로저 내 지역 변수(free variable) 확인
print(c.__closure__)
print(c.__closure__[0].cell_contents)
print(c.__closure__[1].cell_contents)

print('='*50)
# 클로저 내부에서 정의한 변수에 접근
def sample():
    n = 0
    
    def func():
        print(f'n = {n}')
        
    def get_n():
        print("Called Get Func")
        return n
    
    def set_n(val):
        print("Called Set Func")
        nonlocal n
        n = val
        
    func.get_n = get_n
    func.set_n = set_n
    return func

if __name__ == "__main__":
    f = sample()
    f()
    
    # 클로저 내 지역변수 접근 불가능
    n = 3
    f()
    
    # 내부 함수를 통해 접근 가능
    f.set_n(10)
    f()
    print(f.get_n())
    
    # 데코레이터
    # 함수를 인자로 받아서, 함수 전후에 새로운 기능을 추가한 함수를 만들 수 있다.
    import time
    
    def time_checker(func):
        def closure(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            print(f"실행시간: {end_time - start_time}")
            return result
        return closure
    
    @time_checker
    def big_number(n):
        return n * n
    
    big_number(3)
    
    
    enable_tracing = True
    if enable_tracing:
        debug_log = open('./debug.log', 'w')
        
    def trace(func):
        if enable_tracing:
            def call(*args, **kwargs):
                debug_log.write(f"Calling {func.__name__}, {args}, {kwargs}\n")
                result = func(*args, **kwargs)
                debug_log.write(f"{func.__name__} returned {result}\n")
                return result
            return call
        else:
            return func
        
    @trace
    def big_number(n):
        return n * n
    
    print(big_number(10))
    
    
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
