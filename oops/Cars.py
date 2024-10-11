class Cars():
    brake = None
    clutch = None
    accl = None
    validIp = [0, 1]

    def takeInput(self):

        print("Enter values  0/1, 0-off,1-on")
        self.brake = int(input("brake vlaue"))
        self.clutch = int(input("clutch vlaue"))
        self.accl = int(input("accl vlaue"))
        flag = True
        while (flag):
            if (self.brake in self.validIp) and (self.accl in self.validIp) and (self.clutch in self.validIp):
                print("input right")
                self.brake = bool(self.brake)
                self.accl = bool(self.accl)
                self.clutch = bool(self.clutch)
                flag = False
            else:
                print("Enter values again 0/1, 0-off,1-on")
                self.brake = int(input("brake vlaue"))
                self.clutch = int(input("clutch vlaue"))
                self.accl = int(input("accl vlaue"))

    def getValues(self):
        print(f"value of brake :{self.brake},"
              f"clutch: {self.clutch},"
              f"acclerator:{self.accl}")

    def startCar(self):

        if (self.brake == True) and (self.clutch == True) and (self.accl == True):
            print("car not starting")

        elif (self.brake == False) and (self.clutch == True) and (self.accl == True):
            print("car start")


def testMe():
    flag = 0
    mycars = Cars()
    try:
        mycars.takeInput()
        mycars.getValues()
        mycars.startCar()
    except:
        if flag < 3:
            flag = flag + 1
            print("wrong input")
            testMe()


testMe()