class bank:
    Bname='achureddy'
    nob= 100
    Roi=0.05
    def _init_ (self, name, accno, bal):
        self.name=name
        self.accno=accno
        self.bal=bal
    def checkbal(self):
        print(f'available balance :{self.bal}')
    def deposite (self, amt):
        self.bal+=amt
    def withdraw (self, money):
        if money> self.bal:
            print('insufficient balance')
        else:
            self.bal-=money
            print (f'{money}: withdraw succesfull')
            
    
obl=bank('achu',2545678,10000)
ob2=bank('reddy', 25675489,200000)

obl.withdraw(1000)
obl.checkbal()
    
