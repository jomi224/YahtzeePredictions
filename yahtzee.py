from yahtzee import *

#class to hold a user's current scoreboard
class scoreboard:
    
    def __init__(self):
        self.played=[False for i in range(15)]
        self.scores=[0 for i in range(15)]
        self.names=["ones","twos","threes","fours","fives","sixes","3ofakind","4ofakind","fullhouse","smallstraight","largestraight","yahtzee1","yahtzee2","yahtzee3","chance"]
        
    #Play a certain roll in a specific category based on string identifier
    def playName(name,score):
        ind=self.names.index[name]#find index of name
        self.played[ind]=0
        self.scores[ind]=score
    
    def playIndex(ind,score):
        self.played[ind]=0
        self.scores[ind]=score
        
#class to hold a specific dice roll combination
class roll:
    
    worth=0
    def __init__(self,my_dice):
        self.dice=my_dice
    
    #Method to calculate best value of roll
    
    def calculateValue(self,scoreboard):
        
        bestValues=[0 for i in range(15)]
        
        #Check for sets of numbers
        for i in range(1,7):
            bestValues[i-1]=self.dice.count(i)*i #Upper half calculation
            if self.dice.count(i)>=3:
                bestValues[6]=sum(self.dice)
            if self.dice.count(i)>=4:
                bestValues[7]=sum(self.dice)
            if self.dice.count(i)==5:
                bestValues[11]
        self.worth=max(bestValues)
        
    def getWorth(self):
        return self.worth
        
    def printRoll(self):
        print(self.dice[0],self.dice[1],self.dice[2],self.dice[3],self.dice[4])
    
    
#Recursive function to generate lists of all possible combinations of 5 dice
#total_dice is the number of dice we want to find, and start is the earliest dice we want to start at      
def generate_combinations(total_dice, start):
    if total_dice==0:
        yield []
    else:
        for i in range(start,7):
            for k in generate_combinations(total_dice-1,i):
                yield [i]+k



dice_combinations=[] #This will hold all 252 dice configurations

for i in generate_combinations(5,1):
    dice_combinations.append(roll(i))


for i in dice_combinations:
    i.printRoll()
    i.calculateValue(scoreboard())
    print(i.getWorth())
    i.printRoll()




