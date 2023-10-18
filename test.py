import sys

def do_stuff():
  numbers = [float(x) for x in sys.argv[1:]]
  numbers = [x for x in numbers if x >= 0]
  
  #print(numbers)
  #print(sum(numbers))
  #print(len(numbers))
  
  m = sum(numbers) / len(numbers)
  print(f'{m}')

def main():
  do_stuff()
  
if __name__ == "__main__":
    main()