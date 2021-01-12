import time as t

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
        currentInt = ""
        for i in range(len(inStr)):
            char = list(inStr)[i]
            if char != ' ':
                if char == ',' and currentInt != "":
                    try:
                        sortList += [int(currentInt)]
                        currentInt = ""
                    except:
                        printProg(0.05, "The input contains unexpected characters!")
                        t.sleep(0.5)
                        sortList = []
                        break
                else:
                    currentInt += char
                    if i == len(inStr)-1:
                        sortList += [int(currentInt)]
printProg(0.05, "Your input is ready to sort now. Below you can see it")
printProg(0.05, str(sortList))
t.sleep(0.5)
print("Work in Progress", end='')
t.sleep(0.5)
printProg(0.3, "..........")
t.sleep(0.5)
isSorted = False
while isSorted == False:
    isSorted = True
    for i in range(len(sortList)-1):
        if sortList[i] > sortList[i+1]:
            item1 = sortList[i]
            item2 = sortList[i+1]
            sortList[i] = item2
            sortList[i+1] = item1
            isSorted = False
printProg(0.05, "Your List has been sorted with Bubble sort. You're welcome")
printProg(0.05, str(sortList))
