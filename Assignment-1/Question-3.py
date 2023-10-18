import collections
import string
import matplotlib.pyplot as plt

'''
requires: filepath to txt file

promises: itemized non-case sensitive count of each letter in txt file
'''
def countchars(filepath):
    
    with open(filepath, 'r') as file:
        text = (file.read()).lower()
    alphabet_set = set(string.ascii_lowercase)
    counter = collections.Counter(x for x in text if x in alphabet_set)
    
    frequency = {}
    for letter in string.ascii_lowercase:
        #create list of letter frequencies
        freq = int(counter[letter])/sum(counter.values())
        frequency[letter] = freq
        print(letter, counter[letter], 'Frequency: ', freq)
        
    
    print("total:", sum(counter.values()))
    
    #plot histogram of letter frequencies
    
    plt.bar(range(len(frequency)), list(frequency.values()), align='center')
    plt.xticks(range(len(frequency)), list(frequency.keys()))
    plt.title('Letter Frequency')
    plt.xlabel('Letter')
    plt.ylabel('Frequency')
    plt.show()


def main():
    countchars('/home/marcos/dev/ENSF-338/Assignment-1/gutenberg.txt')
    

if __name__ == "__main__":
    main()