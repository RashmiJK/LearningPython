# Using the concept of object oriented programming and inheritance, create a super class named
# Computer, which has two sub classes named Desktop and Laptop.

# Define two methods in the Computer class named getspecs and displayspecs, to get the
# specifications and display the specifications of the computer.

# You can use any specifications which you want.
# The Desktop class and the Laptop class should have one specification which is exclusive to
# them for example laptop can have weight as a special specification.

class Computer:
    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor


    def getspecs(self):
        print('Please enter the details')
        self.ram = input('Enter Ram size: ')
        self.memory = input('Memory size: ')
        self.processor = input('Enter processor')


    def displayspecs(self):
        print('Here are the specs of the computer')
        print(' Ram size is: '+ self.ram + ' Memory size is: '+ self.memory + ' processor is: '+ self.processor)



class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor


    def get_case_details(self):
        self.casecolor = input(' Enter case color: ')


    def put_case_color(self):
        print('case color is: '+ self.casecolor)



class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight


    def getweight(self):
        self.weight = input('Enter weight: ')


    def displayweight(self):
        print('Weight is: '+ self.weight)




comp = Laptop('')
comp.getspecs()
comp.getweight()
comp.displayspecs()
comp.displayweight()