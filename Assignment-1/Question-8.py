from time import perf_counter

def uppercaser(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
        data = data.upper()
        print(data)
           
def main():
    # use perf_counter() to measure time
    start = perf_counter()
    uppercaser('/home/marcos/dev/ENSF-338/Assignment-1/2701-0.txt')
    end = perf_counter()
    print("Time elapsed: ", end - start)
    
if __name__ == "__main__":
    main()