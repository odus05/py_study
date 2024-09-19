"""
데코레이터(Decorator)는 함수를 다른 함수로 감싸서(클로저) 그 함수의 동작을 변경하거나 확장할 수 있는 기법.
1) 함수가 데이터로 취급될 때는 함수가 정의된 곳의 주변 환경 정보가 함께 저장된다.
2) 함수를 구성하는 문장과 실행 환경을 함께 묶은것을 "클로저"라고 부른다.
코드의 재사용성을 높이고, 중복 코드를 줄이는데 유용(로깅, 권한 확인, 실행시간 측정 등)
    - 로깅: 함수 호출 시마다 로그를 남겨야 할 때.
    - 권한 확인 : 사용자의 권한을 확인하고 적절한 권한이 없는 경우, 접근을 제한해야 할 때
    - 실행 시간 측정 : 함수의 실행 시간을 기록하고 싶을 때.
    - 캐싱 : 동일한 입력에 대해 이전 계산 결과를 캐싱하여 성능을 최적화하고 싶을 대

1. 클로저(Closure) - 상태 유지, 데이터 은닉, 간결한 코드
    - 중첩함수(Nested Fuction) : 함수 내부에 또 다른 함수가 정의되어 있는 경우
    - 외부 함수의 변수 참조 : 내부 함수는 외부 함수의 지역 변수를 접근할 수 있음.
    - 외부 함수의 실행 종료 후에도 내부 함수가 외부 변수를 기억: 내부 함수가 외부 함수의 변수를 계속해서 사용할 수 있음.
"""

def calc():
    a=3
    b=5
    def mul_add(x):
        return a * x + b 
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4), c(5))
# 8 11 14 17 20

# 클로저 내 지역 변수(free variable) 확인
print(c.__closure__)
print(c.__closure__[0].cell_contents) # 3
print(c.__closure__[1].cell_contents) # 5

print('='*50)


# 1-1) 클로저 내부에서 정의한 변수에 접근
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
    
    # 2. 데코레이터(Decorator)
    # 함수를 인자로 받아서, 함수 전후에 새로운 기능을 추가한 함수를 만들 수 있다.
    
    # 2-1) 실행시간 측정
    import time
    
    def time_checker(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            print(f"실행시간: {end_time - start_time}")
            return result
        return wrapper
    
    @time_checker
    def big_number(n):
        return n * n
    
    big_number(3)
    
    # 2-2) 로깅
    enable_tracing = True
    if enable_tracing:
        debug_log = open('./debug.log', 'w')
        
    def trace(func):
        if enable_tracing:
            print("__trace__")
            def call(*args, **kwargs):
                debug_log.write(f"Calling {func.__name__}, {args}, {kwargs}\n")
                result = func(*args, **kwargs)
                debug_log.write(f"{func.__name__} returned {result}\n")
                return result
            return call
        else:
            return func
    
    @time_checker
    @trace
    def big_number(n):
        return n * n
    
    print(big_number(10))
    
    # 2-3) 권한 확인
    def requires_permission(func):
        def wrapper(user):
            if not user.is_admin:
                raise PermissionError("User does not have the required permissions.")
            return func(user)
        return wrapper
    
    @requires_permission
    def access_dashboard(user):
        return "Welcom to the dashboard!"
    
    
