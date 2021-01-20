from Utils.Utils import Utils as u


sortList = u.askForIntInput(u)
isSorted = False
while not isSorted:
    isSorted = True #sets isSorted to true. It will be set to false as soon as one item is on the wrong position
    for i in range(len(sortList)-1):#goes through the list that is to sort 
        if sortList[i] > sortList[i+1]:
            #the two items at position i and i+1 are swapped because the smaller one should have a lower index
            item1 = sortList[i]
            item2 = sortList[i+1]
            sortList[i] = item2
            sortList[i+1] = item1
            isSorted = False    #tells the algorithm that it might still be unsorted
u.printProg(0.05, "Your List has been sorted with Bubble sort. You're welcome")
u.printProg(0.05, str(sortList))
