#====================
#Input a sentence and reverse it as the output
#====================


sentenceList = []
reverseSentenceList = []
#function to split a string into a list of words
def splitSentence(oriSentence):
    global sentenceList
    sentenceList = oriSentence.split(" ")
#function to reverse the list
def reverse(sentenceList):
    global reverseSentenceList
    #for i in range(len(sentenceList)-1,-1,-1):
        #reverseSentenceList.append(sentenceList[i])
        #OR
    for i in reversed(sentenceList):
        reverseSentenceList.append(i)

#main function
#reveive a sentence as a string from user
oriSentence = raw_input("Please enter a sentence:")
###DEBUGGING### oriSentence = "This is freaking awesome"
splitSentence(oriSentence)
###DEBUGGING### print sentenceList
reverse(sentenceList)
###DEBUGGING### print reverseSentenceList
#convert the list back to a string

reverseSentence = " ".join(reverseSentenceList)
print reverseSentenceList
print reverseSentence