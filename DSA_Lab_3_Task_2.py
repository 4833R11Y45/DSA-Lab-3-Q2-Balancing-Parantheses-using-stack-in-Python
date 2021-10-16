#Name: Abeer Ilyas
#Registration Number: 200901055
from collections import deque    #Importing double ended queue
class isBalanced:                #Creating a class
    def __init__(self):          #Initiating
        self.container= deque()  #Linking
    def checker(self,inflow):    #Checking Boolean
        top_inflow=inflow[0]
        se=self.is_empty()       #Checking whether it is empty or not
        if se!="True":
            l=len(self.container)
            for i in range (0,l):
                self.container.pop()   #Popping function of a stack
        if top_inflow in "({[":        #Checker for open parantheses
            for i in inflow:
                if i in"{[(":
                 self.container.append(i)
                elif i in ")}]":       #Checker for closed parantheses
                 self.container.pop()
        elif top_inflow in "]})":
            self.container.append("notempty")
    def is_empty(self):
        return len(self.container)==0
iB=isBalanced()          
#Implementing the class on given expressions
iB.checker("({a+b})")
print(iB.is_empty())
iB.checker("))")
print(iB.is_empty())
iB.checker("}}a+b()")
print(iB.is_empty())
iB.checker("[a+b](x+2y){gg+kk}")
print(iB.is_empty())