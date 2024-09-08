import time

class Timer():
    def __init__(self):
        self.start_time = time.perf_counter()
        
    def reset_time(self):
        self.start_time = time.perf_counter()
        
    def get_time(self):
        return time.perf_counter() - self.start_time


def check_timer(func):
    timer_dict = dict()
    
    def create_timer(name):
        if name not in timer_dict:
            timer_dict[name] = Timer()
    def get_timer(name):
        return timer_dict[name].get_time()
    
    def reset_timer(name):
        return timer_dict[name].reset_time()
        
    def wrapper(*args, name, delay=0, **kwargs):
        create_timer(name=name)
        if get_timer(name) > delay:
            return func(*args, **kwargs)
    

    wrapper.create_timer = create_timer
    wrapper.get_timer = get_timer
    wrapper.reset_timer = reset_timer
    
    return wrapper



@check_timer
def log(message):
    return message

#log = check_timer(log)

log(message="message1", name='first', delay=30)
log.get_timer(name='first')


log(message="message2", name='second')

if True:
    log.reset_timer(name="second")
log.get_timer(name='second')


log(message="message1", name='first', delay=30)

