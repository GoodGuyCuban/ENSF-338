import timeit

def pow2(n):
    num = pow(2,n)
    return num

def pow2_for(n):
    num = 1
    for i in range(n):
        num *= 2
    return num

def pow2_list_comprehension(n):
    num = [2**i for i in range(n)]
    return num

def main():
    print(timeit.timeit('pow2(10000)', setup='from __main__ import pow2'))
    print(timeit.timeit('pow2_for(1000)', setup='from __main__ import pow2_for'))
    print(timeit.timeit('pow2_list_comprehension(1000)', setup='from __main__ import pow2_list_comprehension'))
    
if __name__ == "__main__":
    main()