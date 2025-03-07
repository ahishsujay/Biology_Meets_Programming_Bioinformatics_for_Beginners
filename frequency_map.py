def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)

    #First for loop in order to construct the frequency map
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0

        #Second for loop to count occurences of Pattern
        for i in range(n-k+1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words
