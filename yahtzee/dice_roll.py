#class: dice_roll
#contains the current roll of the dice in sorted order to keep consistent


class dice_roll:
    
    def __init__(self,d1,d2,d3,d4,d5):
        
        #sort dice to keep consistent
        dice=sorted([d1,d2,d3,d4,d5])
        
    def set_dice(d1,d2,d3,d4,d5):
        
        dice=sorted([d1,d2,d3,d4,d5])
        