dataStr = 'Hello there. Is this working? Let me check! Testing! One. Two? Three!'

#Seperates strings by punctuation so dialog flow can be fed data in batches
def stringSeperator(string):
    seperators = []
    segments = []

    #stores index location of punctuation, so string can be seperated at those indices
    for i in range(0,len(string)):
        if (string[i] == '.' or string[i] == '!' or string[i] == '?'):
            seperators.append(i)

    #adds seperated strings to segments list object for the start, middle and end elements
    for n in range(0,len(seperators)+1):
        if ((n-1) < 0):
            segments.append(string[:seperators[n]] + string[seperators[n]])
        elif (n >= (len(seperators))):
            segments.append(string[(seperators[n-1]+1):] + string[len(seperators)+1])
        else:
            segments.append(string[(seperators[n-1]+1):seperators[n]] + string[seperators[n]])

    #removes last element which is a subset of the first string segment
    segments.pop(len(segments)-1)

    return segments

print(stringSeperator(dataStr))
