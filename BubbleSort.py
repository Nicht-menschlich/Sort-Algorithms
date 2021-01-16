import time as t
from Utils.Utils import Utils as u
#This is just a method that animates the text and makes a new line after

sortList = u.askForIntInput()
#first the input of the list to be sorted happens
u.printProg(0.05, "You will be asked to insert numbers")
t.sleep(0.75)
u.printProg(0.05, "There it is possible to insert them seperately or in one piece seperating them with a ','!")
t.sleep(0.75)
u.printProg(0.05, "Have fun with my program!")
t.sleep(0.5)

u.printProg(0.05, "Your input is ready to sort now. Below you can see it")
u.printProg(0.05, str(sortList))
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
u.printProg(0.05, "Your List has been sorted with Bubble sort. You're welcome")
i.printProg(0.05, str(sortList))
