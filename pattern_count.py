def PatternCount(Text,Pattern):
    '''Function to calculate the occurence of Pattern in Text'''
    count = 0
    for i in range(0,len(Text)-len(Pattern)+1): #+1 is added due to inclusiveness
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return(count)
