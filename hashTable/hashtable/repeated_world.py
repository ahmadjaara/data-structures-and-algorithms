from .hash_table import HashaTable

def repeated_world(text):
    """
    function finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    """
    hash =HashaTable()
    res = text.lower().replace(",","").split()
    for i in res :
        idx = hash.get_hash(i)
        #index is empty, add the value there
        if not hash.map[idx]:
            hash.map[idx] = [[i]]
        else:
            for element in hash.map[idx]:
                if i == element[0]:
                    return i
            else:
                hash.map[idx].append([i])
                    

if "__main__"==__name__:
    str1="Once upon a time , there was a brave princess who..."
    str2="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief , it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    str3="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    print(repeated_world(str2))
