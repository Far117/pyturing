import sys,time

class CommandError():

    def __init__(self,inp,exp):
        print("Invalid input, "+inp)
        print("Expected "+exp)
        input("Press enter to exit...")
        sys.exit()


class TuringMachine():

    def __init__(self,tl):
        self.tapeLength=tl

        self.pos=int(self.tapeLength/2)
        self.blank="="
        self.zero="0"
        self.one="1"
        self.head="V"
        self.tape=[]
        self.rightLimit=self.tapeLength-2

        for x in range(self.tapeLength):
            self.tape.append(self.blank)

        self.printTape()

    def printTape(self):
        tmpTape=""
        machine=""

        if self.pos>=20 and self.pos <=self.rightLimit-20:
            for x in range(self.tapeLength):
                tmpTape=tmpTape+str(self.tape[x])
                if x==self.pos:
                    machine==machine+self.head
                else:
                    machine=machine+self.head
            tmpTape=tmpTape[self.pos-10:self.pos+10]
            machine="          "+self.head
            #machine=machine[self.pos-10:self.pos+10]
        elif self.pos<=20 and self.tapeLength>=20:
            for x in range(20):
                tmpTape=tmpTape+str(self.tape[x])
                if x==self.pos:
                    machine=machine+self.head
                else:
                    machine=machine+" "
        elif self.pos>=self.tapeLength-20 and self.tapeLength>20:
            for x in range(20):
                tmpTape=tmpTape+str(self.tape[self.tapeLength-20+x])
                if self.tapeLength-20+x==self.pos:
                    machine=machine+self.head
                else:
                    machine=machine+" "
        else:
            if self.tapeLength<=20:
                for x in range(len(self.tape)-1):
                    tmpTape=tmpTape+str(self.tape[x])
                    if x==self.pos:
                        machine=machine+self.head
                    else:
                        machine=machine+" "
            else:
                pass

        for x in range(100):
            print("")

        #tmpTape=tmpTape[::-1]

        print(machine)
        print(tmpTape)

        machine=""
        tmpTape=""

    def move(self,d):
        if d=="r":
            self.pos+=1
        elif d=="l":
            self.pos-=1
        else:
            x=CommandError(d,"either r for right or l for left (number++ or --).")
            x.__init__()

        self.printTape()
        time.sleep(1)

    def read(self):
        return self.tape[self.pos]
        time.sleep(.5)

    def write(self,bit):
        if bit==self.one:
            self.tape[self.pos]=self.one
        elif bit==self.zero:
            self.tape[self.pos]=self.zero
        elif bit==self.blank:
            self.erase()
        else:
            x=CommandError(bit,"either "+self.blank+" or "+self.zero+" or "+
            self.one)
            x.__init__()

        time.sleep(.6)

        self.printTape()

    def erase(self):
        self.tape[self.pos]=self.blank
        time.sleep(.7)
        self.printTape()

    def eraseAll(self):
        while self.pos!=0:
            self.move("l")
        for x in range(self.rightLimit):
            self.erase()
            self.move("r")
    def initialize(self,numbers):
        n=list(numbers)
        for x in n:
            if str(x)!=self.zero and str(x)!=self.one and str(x)!=self.blank:
                z=CommandError(x,"either "+self.blank+" or "+self.zero+" or "+
                self.one)
                z.__init__()
            else:
                self.write(str(x))
            self.move("r")
        self.printTape()
    def done(self):
        self.printTape()
        print("Program complete!")
        input("Press enter to see whole tape...")
        self.finalPrint()
        if input("Press enter to save, or type no to... not save.")!="no":
            self.save(input("Name your file: "))

        sys.exit()
    def finalPrint(self):
        for x in self.tape:
            print(str(x),end='')
    def save(self, name):
        print("Saving...")
        f=open(name+".txt","w")
        fil=""
        n=0
        for x in self.tape:
            n+=1
            f.write(str(x))
            if n==32:
                f.write("\n")
                n=0
        f.close()
        print("Save complete!")
        input("Press enter to continue...")








        '''
        if self.tapeLength<=20:
            for x in range(len(self.tape)-1):
                tmpTape=tmpTape+str(self.tape[x])
                if x==self.pos:
                    machine=machine+self.head
                else:
                    machine=machine+" "
        elif self.pos<=20:
            for x in range(20):
                tmpTape=tmpTape+str(self.tape[x])
            if x==self.pos:
                machine=machine+self.head
            else:
                machine=machine+" "
        elif self.pos>=self.tapeLength-20:
            for x in range(20):
                tmpTape=tmpTape+str(self.tape[self.tapeLength-x])
            if self.tapeLength-x==self.pos:
                machine=machine+self.head
            else:
                machine=machine+" "
        else:
            for x in range(20):
                tmpTape=tmpTape+str(self.tape[self.pos-x+10])
                if self.pos-x+10==self.pos:
                    machine=machine+self.head
                else:
                    machine=machine+" "
        '''