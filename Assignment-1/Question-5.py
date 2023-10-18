def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n > 1:
        return lucas(n-2) + lucas(n-1)	

def main():
    print("Output of n = 0, n + 2: "+str(lucas(0+2)))
    print("Output of n = 1, n + 2: "+str(lucas(1+2)))
    
if __name__ == "__main__":
    main()