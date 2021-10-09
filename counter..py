def countWordsFromFile():
    fileName=input("Enter the file name:")
    file=open(fileName,"r")
    noOfWords=0
    for l in file:
        w=l.split()
        print(w)
        noOfWords=noOfWords+len(w)
    print("number of words are:",noOfWords)
countWordsFromFile()