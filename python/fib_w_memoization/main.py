import time
import functools

MEMO_MAP = dict()

def fib_memoized(n):
    global MEMO_MAP
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif f'{n}' not in MEMO_MAP.keys():
        MEMO_MAP[f'{n}'] = fib_memoized(n-1) + fib_memoized(n-2)
    
    return MEMO_MAP[f'{n}']

@functools.lru_cache(maxsize=128)
def reg_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return reg_fib(n-1)+reg_fib(n-2)


if __name__ == "__main__":
    m_start_time = time.perf_counter()
    print(fib_memoized(113))
    m_end_time = time.perf_counter()
    print(f'memoized ran in: {m_end_time - m_start_time} ')
    start_time = time.perf_counter()
    print(reg_fib(113))
    end_time = time.perf_counter()
    print(f'non_memoized ran in : {end_time - start_time} ')