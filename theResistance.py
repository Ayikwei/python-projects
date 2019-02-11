
theResistanceFile = open('C:\\Users\\kwei4\\myPythonScripts\\theResistanceFile.txt')
theResistanceContent = theResistanceFile.read()
theResistanceContent =  theResistanceContent.lower()  
theResistanceContentByLine = theResistanceFile.readlines()



from collections import Counter

def countOfWords(theResistanceContent):
    skips = [".", ", ", ":", ";", "'", '"']
    
    #for ch in skips:
        #theResistanceContent = theResistanceContent.replace(ch, "")
    wordCount = {}
    theResistanceContent = theResistanceContent.split(" ")
    uniqueWords = set(theResistanceContent)
    #print('Number of unique words: ' + str(len(uniqueWords)))
    for word in theResistanceContent:
        if word in wordCount:
            wordCount[word]+=1
        else:
            wordCount[word] = 1
    print(len(wordCount))
    print(len(uniqueWords))

    

        
            

