import json
import matplotlib.pyplot as plt

def extract_data_high(filepath):
    #open file
    with open(filepath) as file:
        data = json.load(file)
    
    #extract energy scores from songs with a dancability score greater than or equal to 0.5
    energy = []
    for i in range(len(data)):
        if data[i]['danceability'] >= 0.5:
            energy.append(data[i]['energy'])
    
    return(energy)

def extract_data_low(filepath):
    #open file
    with open(filepath) as file:
        data = json.load(file)
    
    #extract energy scores from songs with a dancability score less than 0.5
    energy = []
    for i in range(len(data)):
        if data[i]['danceability'] < 0.5:
            energy.append(data[i]['energy'])
    
    return(energy)

def main():
    extract_data_high('/home/marcos/dev/ENSF-338/Assignment-1/songdata.json')
    extract_data_low('/home/marcos/dev/ENSF-338/Assignment-1/songdata.json')
    #plot seperate histograms
    plt.hist(extract_data_high('/home/marcos/dev/ENSF-338/Assignment-1/songdata.json'), bins=20, alpha=0.5, label='High')
    plt.hist(extract_data_low('/home/marcos/dev/ENSF-338/Assignment-1/songdata.json'), bins=20, alpha=0.5, label='Low')
    plt.legend(loc='upper right')
    plt.title('Energy Scores for High and Low Dancability Scores')
    plt.xlabel('Energy Score') 
    plt.ylabel('Frequency')
    plt.show()
    
if __name__ == "__main__":
    main()