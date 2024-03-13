import random





def main():
    num = [1, 2, 3, 4, 5, 6]
    roll = random.choices(num, k = 5)
    chance = 0
    change = []
    reroll = False
    yep = 1
    match = 0
    yahtzee = False
    change_l = []
    count = 0
    print(roll)
    while chance != 3:
        if reroll == True:
            change = []
            change_l = []
            print(roll)
            match = 0
            reroll = False
        if count == 3:
            break
        try:
            choice = int(input("Type which dice you want to change 1-5, type -1 when ready, or -2 to keep all: "))
        except ValueError:
            continue
        if choice-1 in change:
            print("Choice already made.")
            continue
        if(choice-1 >= 0) and (choice-1 <= 4):
            change_l.append(choice)
            print(change_l)
            change.append(choice-1)
        #print(change) testing
            continue
        elif choice == -1:
            count += 1
            reroll = True
        elif choice == -2:
            break
        for i in change:
            new = random.choice(num)
            roll[i] = new
            reroll = True
    return(roll)



def chance(roll):
    total = 0
    for dice in roll:
            total += dice
    return(total)

def ones(roll):
    total = 0
    for dice in roll:
        if dice == 1:
            total += dice
    return(total)

def twos(roll):
    total = 0
    for dice in roll:
        if dice == 2:
            total += dice
    return(total)

def threes(roll):
    total = 0
    for dice in roll:
        if dice == 3:
            total += dice
    return(total)

def fours(roll):
    total = 0
    for dice in roll:
        if dice == 4:
            total += dice
    return(total)

def fives(roll):
    total = 0
    for dice in roll:
        if dice == 5:
            total += dice
    return(total)

def sixes(roll):
    total = 0
    for dice in roll:
        if dice == 6:
            total += dice
    return(total)

def three_of_kind(roll):
    total = 0
    same = 0
    three = False
    for dice in roll:
        if same == 3:
            three = True
            break
        same = 0
        for num in roll:
            if dice == num:
                same += 1
    if three == True:
        for dice in roll:
            total += dice
    else:
        total = 0
    return(total)

def four_of_kind(roll):
    total = 0
    same = 0
    four = False
    for dice in roll:
        if same == 4:
            four = True
            break
        same = 0
        for num in roll:
            if dice == num:
                same += 1
    if four == True:
        for dice in roll:
            total += dice
    else:
        total = 0
    return(total)

def full_house(roll):
    total = 0
    pair = False
    three = False
    same = 0
    for dice in roll:
        if same == 3:
            three = True
        elif same == 2:
            pair = True
        print(pair)
        same = 0
        for num in roll:
            if dice == num:
                same += 1
    if (three == True) and (pair == True):
        total = 25
    else:
        total = 0
    return(total)

def YAHTZEE(roll):
    total = 0
    same = 0
    five = False
    for dice in roll:
        if same == 5:
            five = True
            break
        same = 0
        for num in roll:
            if dice == num:
                same += 1
    if five == True:
        total = 50
    else:
        total = 0
    return(total)

def small_straight(roll):
    print(roll)
    total = 0
    roll.sort()
    straight = 0
    num = 1
    for dice in roll:
        print(straight)
        if dice == num:
            continue
        if dice - num == 1:
            straight += 1
            num = dice
    if straight >= 3:
        total = 30
    else:
        total = 0
    return(total)

def large_straight(roll):
    print(roll)
    total = 0
    roll.sort()
    straight = 0
    num = 1
    for dice in roll:
        print(straight)
        if dice == num:
            continue
        if dice - num == 1:
            straight += 1
            num = dice
    if straight >= 4:
        total = 40
    else:
        total = 0
    return(total)

def total():
    total = 0 
    global score
    for i in score:
        if score[i] == "":
            continue
        elif i == "TOTAL SCORE":
            continue
        else:
            total += score[i]
            print(total)
    return(total)
       
        
            
        


def score_board():
    global score
    global total
    print("Ones:",score["Ones"], "\n"
      "Twos:",score["Twos"], "\n"
      "Threes:",score["Threes"], "\n"
      "Fours:",score["Fours"], "\n"
      "Fives:",score["Fives"], "\n"
      "Sixes:",score["Sixes"], "\n"
      "-------\n"
      "Three of a kind:",score["Three of a kind"], "\n"
      "Four of a kind:",score["Four of a kind"], "\n"
      "Full House:",score["Full House"], "\n"
      "Small straight:",score["Small straight"], "\n"
      "Large straight:",score["Large straight"], "\n"
      "Chance:",score["Chance"], "\n"
      "YAHTZEE:",score["YAHTZEE"], "\n"
      "-------:\n"
      "TOTAL SCORE:",score["TOTAL SCORE"], "\n")

        

score = {
    "Ones": '',
    "Twos": '',
    "Threes": '',
    "Fours": '',
    "Fives": '',
    "Sixes": '',
    "Sum": '',
    "Bonus": '',
    "Three of a kind": '',
    "Four of a kind": '',
    "Full House": '',
    "Small straight": '',
    "Large straight": '',
    "Chance": '',
    "YAHTZEE": '',
    "TOTAL SCORE": '',
    }

rounds = 0
while rounds != 13:
    roll = main()
    print(roll)
    score_board()
    place = input("Where would you like to place your roll?: ")
    if place.lower() == "ones":
        ones = ones(roll)
        score["Ones"] = ones
    if place.lower() == "twos":
        twos = twos(roll)
        score["Twos"] = twos
    if place.lower() == "threes":
        threes = threes(roll)
        score["Threes"] = threes
    if place.lower() == "fours":
        fours = fours(roll)
        score["Fours"] = fours
    if place.lower() == "fives":
        fives = fives(roll)
        score["Fives"] = fives
    if place.lower() == "sixes":
        sixes = sixes(roll)
        score["Sixes"] = sixes
    if place.lower() == "chance":
        chance = chance(roll)
        score["Chance"] = chance
    if place.lower() == "three of a kind":
        three_of_kind = three_of_kind(roll)
        score["Three of a kind"] =  three_of_kind
    if place.lower() == "four of a kind":
        four_of_kind = four_of_kind(roll)
        score["Four of a kind"] = four_of_kind
    if place.lower() == "full house":
        full_house = full_house(roll)
        score["Full House"] = full_house
    if place.lower() == "yahtzee":
        yahtzee = YAHTZEE(roll)
        score["YAHTZEE"] = yahtzee
    if place.lower() == "small straight":
        small_straight = small_straight(roll)
        score["Small straight"] = small_straight
    if place.lower() == "large straight":
        large_straight = large_straight(roll)
        score["Large straight"] = large_straight
    rounds += 1
    total_score = total()
    score["TOTAL SCORE"] = total_score
    score_board()


            
            
            
        
    
    
