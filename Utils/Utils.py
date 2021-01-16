import time as t
class Utils:
    def askForIntInput(self):
        sortList = []
        while sortList == []:
            self.printProg(0.05, "Please insert a the list/items: ")
            inStr = input()
            if ',' in inStr:
                currentInt = ""  # sets value for currentInt
                for i in range(len(inStr)):
                    char = list(inStr)[i]
                    if char != ' ':
                        if char == ',' and currentInt != "":
                            try:
                                sortList += [int(currentInt)]  # adds the new number to the list
                                currentInt = ""  # resets the value of currentInt
                            except:
                                self.printProg(0.05, "The input contains unexpected characters!")
                                t.sleep(0.5)
                                sortList = []  # resets tha value of the list
                                break
                        else:
                            currentInt += char  # adds the current character of the string input to the currentInt string
                            if i == len(inStr) - 1:
                                try:
                                    sortList += [int(currentInt)]  # adds the new number to the list
                                except:
                                    self.printProg(0.05, "The input contains unexpected characters!")
                                    t.sleep(0.5)
                                    sortList = []  # resets tha value of the list
        return sortList

    def printProg(self, time, text):
        for i in list(text):
            print(i, end='')
            t.sleep(time)
            print("")