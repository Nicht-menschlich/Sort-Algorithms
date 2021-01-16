import time as t


class Utils:
    def askForIntInput(self):
        self.printProg(0.05, "You will be asked to insert numbers")
        t.sleep(0.75)
        self.printProg(0.05, "Please seperate each number with an ','")
        t.sleep(0.75)
        self.printProg(0.05, "Have fun with my program!")
        t.sleep(0.5)
        sortList = []
        while not sortList:
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

        self.printProg(0.05, "Your input is ready to sort now. Below you can see it")
        self.printProg(0.05, str(sortList))
        t.sleep(0.5)
        print("Work in Progress", end='')
        t.sleep(0.5)
        self.printProg(0.3, "..........")
        t.sleep(0.5)

        return sortList

    @staticmethod
    def printProg(time, text):
        for i in list(text):
            print(i, end='')
            t.sleep(time)
        print("")
