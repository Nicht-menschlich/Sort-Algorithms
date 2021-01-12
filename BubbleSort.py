import time as t
#This is just a method that animates the text and makes a new line after
def printProg(time, text):
    for i in list(text):
        print(i, end='')
        t.sleep(time)
    print()

#first the input of the list to be sorted happens
printProg(0.05, "You will be asked to insert numbers")
t.sleep(0.75)
printProg(0.05, "There it is possible to insert them seperately or in one piece seperating them with a ','!")
t.sleep(0.75)
printProg(0.05, "Have fun with my program!")
t.sleep(0.5)
sortList = []
while sortList == []:
    printProg(0.05, "Please insert a the list/items: ")
    inStr = input()
    if ',' in inStr:
        currentInt = "" #sets value for currentInt
        for i in range(len(inStr)):
            char = list(inStr)[i]
            if char != ' ':
                if char == ',' and currentInt != "":
                    try:
                        sortList += [int(currentInt)]   #adds the new number to the list
                        currentInt = "" #resets the value of currentInt
                    except:
                        printProg(0.05, "The input contains unexpected characters!")
                        t.sleep(0.5)
                        sortList = []   	#resets tha value of the list
                        break
                else:
                    currentInt += char  #adds the current character of the string input to the currentInt string
                    if i == len(inStr)-1:
                        try:
                            sortList += [int(currentInt)]   #adds the new number to the list
                        except:
                            printProg(0.05, "The input contains unexpected characters!")
                            t.sleep(0.5)
                            sortList = []   	#resets tha value of the list
printProg(0.05, "Your input is ready to sort now. Below you can see it")
printProg(0.05, str(sortList))
t.sleep(0.5)
print("Work in Progress", end='')
t.sleep(0.5)
printProg(0.3, "..........")
t.sleep(0.5)
#here the actual sorting starts
isSorted = False
while isSorted == False:
    isSorted = True #sets isSorted to true. It will be set to false as soon as one item is on the wrong position
    for i in range(len(sortList)-1):#goes through the list that is to sort 
        if sortList[i] > sortList[i+1]:
            #the two items at position i and i+1 are swapped because the smaller one should have a lower index
            item1 = sortList[i]
            item2 = sortList[i+1]
            sortList[i] = item2
            sortList[i+1] = item1
            isSorted = False    #tells the algorithm that it might still be unsorted
printProg(0.05, "Your List has been sorted with Bubble sort. You're welcome")
printProg(0.05, str(sortList))
