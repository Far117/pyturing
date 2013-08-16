import Turing #Only if Turing.py is in the same directory as your program

machine=Turing.TuringMachine(100) #creates a new Turing Machine
                                    #with 100 cells

machine.initialize("1101") #See README

#Movement demo

machine.move('r')
machine.move('l')

'''

To go all the way to one end, use:

while pos!=machine.rightLimit:
    machine.move('r')

to move right, and :

while pos!=0:
    machine.move('l')

to go left. Commented for time purposes.

'''


#Reading:

currentCell=machine.read()

#Writing:

machine.write("0")
machine.move("r")
machine.write("1")

#Erasing/reading/writing/moving mini-program:

while machine.read()!=machine.blank:
    if machine.read()==machine.one:
        machine.erase()
        machine.write("0")

    machine.move("l")

#Proper way to finish:

machine.done()