from random import randint

class train:
    def __init__(slf, trainNo) :#we can use as a slf instead of using self or else we can use different things like name Harry i
     slf.trainNo=trainNo
    def book(self,fro,to):
        print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to}")


    def getstatus(self,):
        print(f'trian no: {self.trainNo} is runing on time')
    def getfare(self,fro,to):
         print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to} is {randint(111,3200)}")

t=train(randint(0000,9999))
t.book("Rampur","Delhi")
t.getstatus()
t.getfare("Rampur","Delhi")         