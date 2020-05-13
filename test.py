class Bill:
    bill_list = []

    def init(self):
        pass

    def additem(self,what,kg,price):
        self.bill_list.append((what,kg,price))

    def printbill(self):
        print("The Bill is : \n")
        for item in self.bill_list:
            print(f"#{self.bill_list.index(item) + 1}")


man1=Bill()
man1.additem("banana",1.5,100)
man1.additem("orange",2,300)
man1.printbill()