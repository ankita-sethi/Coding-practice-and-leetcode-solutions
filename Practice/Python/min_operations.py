import math
from collections import Counter

def minOperation(locations):
    n = len(locations)
    freq = Counter(locations)
    max_freq= max(freq.values())
    return max(max_freq, math.ceil(n/2))

if __name__ == "__main__":
    n = int(input("Enter number of products: "))
    locations = list(map(int, input("Enter locations (space-separated): ").split()))
    
    result = minOperation(locations)
    print("Minimum operations needed:", result)
