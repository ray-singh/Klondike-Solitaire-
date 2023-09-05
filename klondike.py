    ###########################################################
    #
    #  Algorithm
    #    prompt for an option
    #    input an option
    #    loop while "Q" isn't entered
    #       call corresponding function
    #       output for result
    #       if function was unsuccesful, display error message.
    #       prompt for an ption
    #       input an option
    #   if "Q" is entered, terminate.
    ###########################################################
from cards import Card, Deck

#--------------------------------Starter Code---------------------------------#

MENU ='''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
    TT s d: Move card from end of Tableau pile s to end of pile d.
    TF s d: Move card from end of Tableau pile s to Foundation d.
    WT d: Move card from Waste to Tableau pile d.
    WF d: Move card from Waste to Foundation pile d.
    SW : Move card from Stock to Waste.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game        
    '''

#-----------------------------------------------------------------------------#

#----------------------------------Game Rules---------------------------------#
# Rank is an int (1-13), where aces are 1 and kings are 13.
# Suit is an int (1-4), where clubs are 1 and spades are 4. 
# Value is an int (1-10), where aces are 1 and face cards are 10.
    
    
#1. The deck of cards is shuffled and 28 cards are dealt into 7 columns to form 
#the tableau. #The cards are dealt in the following manner:
    #One card is placed in each of the 7 columns, from left to right
    #A second card is placed in the rightmost 6 columns, from left to right 
    #A third card is placed in the rightmost 5 columns, from left to right 
    #A fourth card is placed in the rightmost 4 columns, from left to right 
    #A fifth card is placed in the rightmost 3 columns, from left to right
    #A sixth card is placed in the rightmost 2 columns, from left to right 
    #A seventh card is placed in the rightmost column
#The last card placed in each column of the tableau is turned face up.
#The four foundations are initially empty. The remaining 24 cards become the 
#stock. The top card in the stock is turned over and placed face up in the
#waste pile (also known as the talon).


#2. Whenever an Ace is face up in the tableau or the waste (talon), it may be 
#moved above the tableau and become the first card in that suit’s foundation. 
#After that, additional cards of that same suit may be moved into the suit’s 
#foundation: the Two on the Ace, the Three on the Two, and so on. The objective 
#of the game is to move all 13 cards of each suit into the appropriate 
#foundation.

#3. The top card in the talon (waste) may be moved into a foundation or into 
#the tableau:
    #a) To be moved into one of the foundations, the card must be the correct 
    #suit and rank: it must be the same suit as the other cards in that 
    #foundation, and it must have a rank which is exactly one higher than the 
    #card that is currently at the top of the foundation (as above, the Two on 
    #the Ace, the Three on the Two, and so on).
    #b) To be moved into one of the columns in the tableau, the top card in the 
    #waste (talon) must be either a King (if the destination in the Tableau is 
    #empty), or the opposite color and exactly one rank lower than the card which 
    #is the last face-up card in that column. For example, a red Seven may be 
    #moved onto a black Eight. 
    
    
#4. The last card in any of the 7 columns in the tableau may be moved into a 
#foundation or into another column in the tableau:
    #a) To be moved into one of the foundations, the card must be the correct 
    #suit and rank (as above).
    #b) To be move elsewhere in the tableau, the card must be the opposite 
    #color and exactly one rank lower (as above).
    
#5. If all of the cards are moved out of a particular column of the tableau, a 
#King of any suit may be moved into that column. Note: a King is the only card 
#which may be moved into an empty column.

#6. At any point, the player may turn over the top card from the stock and 
#place it face up in the talon (waste pile). When the stock becomes empty, the 
#talon is turned over and becomes the stock.

#-----------------------------------------------------------------------------#

#----------------------------Function Definitions-----------------------------#

def initialize():
    '''The function has no parameters and returns the starting state of the 
    game with the data structues that represent the tableau, stock, foundation, 
    and waste. It initialises these data structures with accordance to the game's
    rule.'''
    tableau = []
    cards = Deck()
    for y in range(28):
        card = cards.deal()
        card.flip_card()
        tableau.append(card)
    #According to the game rules, the number of cards in each column is supposed
    #to be equal to it's column number. 
    tableau = [[tableau[0]], 
               [tableau[1], tableau[7]], 
               [tableau[2], tableau[8], tableau[13]], 
               [tableau[3], tableau[9],tableau[14], tableau[18]], 
               [tableau[4], tableau[10],tableau[15], tableau[19], tableau[22]], 
               [tableau[5],tableau[11], tableau[16], tableau[20], tableau[23], tableau[25]], 
               [tableau[6], tableau[12], tableau[17], tableau[21], tableau[24], tableau[26], tableau[27]]]
    
    #Only the last cards in each column needs to be face up.
    for x in tableau:
        last_card = x[-1]
        last_card.flip_card()
    cards.shuffle()
#The stock is simply whatever remains in the deck. 
    stock = cards
    foundation = [[] for x in range(4)]
#The waste is the last card in the stock.
    waste = [stock.deal()]
    return tableau, stock, foundation, waste
    
def display(tableau, stock, foundation, waste):
    """ display the game setup """
    stock_top_card = "empty"
    found_top_cards = ["empty","empty","empty","empty"]
    waste_top_card = "empty"
    if len(waste):
        waste_top_card = waste[-1] 
    if len(stock):
        stock_top_card = "XX" #stock[-1]
    for i in range(4):
        if len(foundation[i]):
            found_top_cards[i] = foundation[i][-1]
    print()
    print("{:5s} {:5s} \t\t\t\t\t {}".format("stock","waste","foundation"))
    print("\t\t\t\t     ",end = '')
    for i in range(4):
        print(" {:5d} ".format(i+1),end = '')
    print()
    print("{:5s} {:5s} \t\t\t\t".format(str(stock_top_card), str(waste_top_card)), end = "")
    for i in found_top_cards:
        print(" {:5s} ".format(str(i)), end = "")
    print()
    print()
    print()
    print()
    print("\t\t\t\t\t{}".format("tableau"))
    print("\t\t ", end = '')
    for i in range(7):
        print(" {:5d} ".format(i+1),end = '')
    print()
    # calculate length of longest tableau column
    max_length = max([len(stack) for stack in tableau])
    for i in range(max_length):
        print("\t\t    ",end = '')
        for tab_list in tableau:
            # print card if it exists, else print blank
            try:
                print(" {:5s} ".format(str(tab_list[i])), end = '')
            except IndexError:
                print(" {:5s} ".format(''), end = '')
        print()
    print()
    print()
    

def stock_to_waste( stock, waste ):
    '''That function has two parameters: the data structure representing the 
    stock, and the data structure representing the waste. The function will 
    return True if the move was done successfully. Otherwise, 
    it returns False.'''
    
    if stock != []:
#This function will only work if the stock isn't empty.
        potential_waste = stock.deal()
        if potential_waste != None:
            waste.append(potential_waste)
            return True
        else:
            return False
    else:
        return False
    
       
def waste_to_tableau( waste, tableau, t_num ):
    '''The function has three parameters: the data structure representing 
    the waste, the data structure representing the tableau, and a column number 
    (the correct index in the tableau). The function will return True if the 
    move is valid (False otherwise). Move will be performed only if it's 
    valid.'''

    cards = tableau[t_num]
    original_length = len(cards)
    for x in waste:
        if original_length>0:
            last_card = cards[-1]
            rank_difference = int(last_card.rank() - x.rank())

#a red card will have suits as either 2 or 3. A black card will have suits 
#either 1 or 4. This is important to remember because a card can only be 
#moved to tableau if it is of the opposite color and a rank lower than the last 
#card in the column. 

            same_color = []
            same_color.append(int(x.suit()))
            if int(x.suit()) == 1:
                same_color.append(4)
            if int(x.suit()) == 4:
                same_color.append(1)
            if int(x.suit()) == 2:
                same_color.append(3)
            if int(x.suit()) == 3:
                same_color.append(2)
            

            x_suit = int(str(x.suit()))
            lc_suit = int(str(last_card.suit()))

            if x_suit == lc_suit or lc_suit in same_color:
                continue
            elif x_suit != lc_suit and (lc_suit not in same_color) and rank_difference == 1:
                tableau[t_num].append(x)
                waste.remove(x)
#Only a king can be placed into an empty tableau column. King cards have a rank
#of 13.
        elif original_length == 0:
            if x.rank() == 13:
                tableau[t_num].append(x)
                waste.remove(x)

    new_length = len(cards)
    if new_length != original_length:
        return True
    else:
        return False

def waste_to_foundation( waste, foundation, f_num ):
    '''That function has three parameters: the data structure representing 
    the waste, the data structure representing the foundations, and a 
    foundation number (the correct index in the foundation). 
    The function will return True if the move is valid (False otherwise). If 
    the move is valid, it'll perform it.'''    
#List of the cards in the specified fondation numbers has been made
#to ensure that they aren't empty (because indexing an empty list will raise
#errors).
    cards = foundation[f_num]
    original_length = len(cards)
    for x in waste:
        if len(cards) > 0:
            last_card = cards[-1]
            rank_difference = x.rank() - last_card.rank()
#a card can only be added to the foundation if it is of the same suit and a rank
#higher than the last card.
            if len(cards) != 0 and last_card.suit() == x.suit() and rank_difference == 1:
                foundation[f_num].append(x)
                waste.remove(x)
            elif len(cards) == 0:
                if x.rank() == 1:
                    foundation[f_num].append(x)
                    waste.remove(x)
        else:
            f_num_list = [y[0].suit() for y in foundation if len(y) >0]
            if x.suit() not in f_num_list and x.rank() == 1:
                foundation[f_num].append(x)
                waste.remove(x)

            
    new_length = len(cards)
    if new_length != original_length:
        return True
    else:
        return False
                    

def tableau_to_foundation( tableau, foundation, t_num, f_num ):
    '''The function has four parameters: the data structure representing the 
    tableau, the data structure representing the foundations, a column number, 
    and a foundation number. The function will return True if the move is 
    valid (False otherwise). Move will be performed only if it's valid.'''
#this function is extremely similar to waste_to_foundation(). But instead of 
#making one list, I made two because a foundaio column cann have more than 1
#card.

    t_cards = tableau[t_num]
    f_cards = foundation[f_num]
    if len(t_cards) != 0:
        last_card_t = t_cards[-1]
    else:
        last_card_t = 0
        
    if len(f_cards) != 0:
        last_card_f = f_cards[-1]
    else:
        last_card_f = 0
    
    original_length = len(f_cards)
    
    if last_card_t != 0 and last_card_f != 0:
        last_card_t_suit = int(str(last_card_t.suit()))
        last_card_f_suit = int(str(last_card_f.suit()))
        
        rank_diff = int(str(last_card_t.rank())) - int(str(last_card_f.rank()))
        if last_card_t_suit == last_card_f_suit and rank_diff==1:
            foundation[f_num].append(last_card_t)
            tableau[t_num].remove(last_card_t)
            if tableau[t_num] != []:
                if tableau[t_num][-1].is_face_up() == False:
                    tableau[t_num][-1].flip_card()
                
    elif last_card_f == 0 and last_card_t != 0:
        if last_card_t.rank() == 1:
            foundation[f_num].append(last_card_t)
            tableau[t_num].remove(last_card_t)
            if tableau[t_num] != []:
                if tableau[t_num][-1].is_face_up() == False:
                    tableau[t_num][-1].flip_card()

    new_len = len(foundation[f_num])
    if new_len == original_length:
        return False
    else:
        return True
        

def tableau_to_tableau( tableau, t_num1, t_num2 ):
    '''That function has three parameters: the data structure representing the 
    tableau, a source column number, and a destination column number. The 
    function will return True if the move is valid (False otherwise). If the 
    move was valid, it'll be performed.'''
#This function is extremely similar to waste_totableau(). The rules of adding a
#card to a tableau have been kept in mind. 

    t1 = tableau[t_num1]
    t2 = tableau[t_num2]
    original_len = len(t1)
    
    if len(t1) != 0:
        last_card_1 = t1[-1]
    else:
        last_card_1 = 0
    if len(t2) != 0:
        last_card_2 = t2[-1]
    else:
        last_card_2 = 0
    
    same_color = []
    card1_suit = int(str(last_card_1.suit()))
    same_color.append(card1_suit)
    if last_card_1 != 0 and last_card_2 != 0:
        if int(last_card_1.suit()) == 1:
            same_color.append(4)
        if int(last_card_1.suit()) == 4:
            same_color.append(1)
        if int(last_card_1.suit()) == 2:
            same_color.append(3)
        if int(last_card_1.suit()) == 3:
            same_color.append(2)
        
        card2_suit = int(str(last_card_2.suit()))
        
        rank_difference = int(str(last_card_2.rank())) - int(str(last_card_1.rank()))
        if rank_difference == 1 and (card2_suit not in same_color):
            tableau[t_num2].append(last_card_1)
            tableau[t_num1].remove(last_card_1)
            if len(tableau[t_num1]) != 0:
                if tableau[t_num1][-1].is_face_up() == False:
                    tableau[t_num1][-1].flip_card()
                
    elif last_card_1 != 0 and last_card_2 == 0:
        if last_card_1.rank() == 13:
            tableau[t_num2].append(last_card_1)
            tableau[t_num1].remove(last_card_1)
            if len(tableau[t_num1]) != 0:
                if tableau[t_num1][-1].is_face_up() == False:
                    tableau[t_num1][-1].flip_card()
    else:
        return False
    
    new_len = len(tableau[t_num1])
    if new_len != original_len:
        return True
    else:
        return False
    
def check_win (stock, waste, foundation, tableau):
    '''Returns True if the game is in a winning state: all cards are in the foundation, 
    stock is empty, waste is empty and tableau is empty. Otherwise, return 
    False.'''
#We need to ensure that the tableau is completely empty, so we use list
#comprehension to check the length of each list in the list of lists.

    tableau_len = [len(x) for x in tableau]
    if tableau_len.count(0) == 7 and int(len(stock))==0 and len(waste)==0:
        return True
    else:
        return False
        

def parse_option(in_str):
    '''Prompt the user for an option and check that the input has the 
           form requested in the menu, printing an error message, if not.
           Return:
        TT s d: Move card from end of Tableau pile s to end of pile d.
        TF s d: Move card from end of Tableau pile s to Foundation d.
        WT d: Move card from Waste to Tableau pile d.
        WF d: Move card from Waste to Foundation pile d.
        SW : Move card from Stock to Waste.
        R: Restart the game (after shuffling)
        H: Display this menu of choices
        Q: Quit the game        
        '''
    option_list = in_str.strip().split()
    
    opt_char = option_list[0][0].upper()
    
    if opt_char in 'RHQ' and len(option_list) == 1:  # correct format
        return [opt_char]
    
    if opt_char == 'S' and len(option_list) == 1:
        if option_list[0].upper() == 'SW':
            return ['SW']
    
    if opt_char == 'W' and len(option_list) == 2:
        if option_list[0].upper() == 'WT' or option_list[0].upper() == 'WF':
            dest = option_list[1] 
            if dest.isdigit():
                dest = int(dest)
                if option_list[0].upper() == 'WT' and (dest < 1 or dest > 7):
                    print("\nError in Destination")
                    return None
                if option_list[0].upper() == 'WF' and (dest < 1 or dest > 4):
                    print("\nError in Destination")
                    return None
                opt_str = option_list[0].strip().upper()
                return [opt_str,dest]
                               
    if opt_char == 'T' and len(option_list) == 3 and option_list[1].isdigit() \
        and option_list[2].isdigit():
        opt_str = option_list[0].strip().upper()
        if opt_str in ['TT','TF']:
            source = int(option_list[1])
            dest = int(option_list[2])
            # check for valid source values
            if opt_str in ['TT','TF'] and (source < 1 or source > 7):
                print("\nError in Source.")
                return None
            #elif opt_str == 'MFT' and (source < 0 or source > 3):
                #print("Error in Source.")
                #return None
            # source values are valid
            # check for valid destination values
            if (opt_str =='TT' and (dest < 1 or dest > 7)) \
                or (opt_str == 'TF' and (dest < 1 or dest > 4)):
                print("\nError in Destination")
                return None
            return [opt_str,source,dest]

    print("\nError in option:", in_str)
    return None   # none of the above


def main():   
    '''That function has no parameters; it controls overall execution of the 
    program.'''
    #NEED TO ADD LAST THREE OPTIONS
    tableau, stock, foundation, waste = initialize()
    print(MENU)
    display(tableau, stock, foundation, waste)
    in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
    in_str = parse_option(in_str)    
    while True:
        if in_str!= None:
            opt = in_str[0]
            if opt == "Q":
#the program will terminate if the user enters "Q".
                break
            
            elif opt == "TT":
                
#This option is responsible for moving a tableau card to another column in the 
#tableau.
#It calls the tableau_to_tableau() functon. It also calls check_win() to check
#whether the user made a winning move. If both functions return true, a 
#congratulartory message is displayed. If only the former is true, it displays 
#the board after the move. If both return False, it'll display an error
#message.

                in_str[1] -= 1
                in_str[2] -= 1
                t_to_t = tableau_to_tableau(tableau, in_str[1], in_str[2])
                if t_to_t == True:
                    display(tableau, stock, foundation, waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau, stock, foundation, waste)
            
                in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
                in_str = parse_option(in_str)
        
            elif opt == "TF":

#This option is responsible for moving a tableau card to the foundation.
#It calls the tableau_to_foundation() functon. It also calls check_win() to check
#whether the user made a winning move. If both functions return true, a 
#congratulartory message is displayed. If only the former is true, it displays 
#the board after the move. If both return False, it'll display an error
#message.

#Column numbers are equal to one plus index number. To make the function work
#flawlessly, one is subtracted from the values returned by parse_option().

                in_str[1] -= 1
                in_str[2] -= 1
                t_to_f = tableau_to_foundation(tableau, foundation, in_str[1], in_str[2])
                win_status = check_win(stock, waste, foundation, tableau)
                if t_to_f == True and win_status == True:
                    print("You won!")
                    display(tableau, stock, foundation, waste)
                elif t_to_f == True and win_status == False:
                    display(tableau, stock, foundation, waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau, stock, foundation, waste)
    
                in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
                in_str = parse_option(in_str)
                
            
            elif opt == "WT":
                
#This option is responsible for moving a function from the wate to the tableau.
#It calls the waste_to_tableau(). If it returns True, it displays the board.
#Else, it prints an error message. 

#Column numbers are equal to one plus index number. To make the function work
#flawlessly, one is subtracted from the values returned by parse_option().
                
                in_str[1] -= 1
                w_to_t = waste_to_tableau(waste, tableau, in_str[1])
                if w_to_t == True:
                    display(tableau, stock, foundation, waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau, stock, foundation, waste)
    
                in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
                in_str = parse_option(in_str)
            
            elif opt == "WF":
                
#This option is responsible for moving a function from the wate to the tableau.
#It calls the waste_to_foundation() functon. It also calls check_win() to check
#whether the user made a winning move. If both functions return true, a 
#congratulartory message is displayed. If only the former is true, it displays 
#the board after the move. If both return False, it'll display an error
#message.

#Column numbers are equal to one plus index number. To make the function work
#flawlessly, one is subtracted from the values returned by parse_option().

                in_str[1] -= 1
                w_to_f = waste_to_foundation(waste, foundation, in_str[1])
                win_status = check_win(stock, waste, foundation, tableau)
                if w_to_f == True and win_status == True:
                    print("You won!")
                    display(tableau, stock, foundation, waste)
                elif w_to_f == True and win_status == False:
                    display(tableau, stock, foundation, waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau, stock, foundation, waste)
    
                in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
                in_str = parse_option(in_str)
    
            
            elif opt == "SW":
#This option is responsible for movng a card from stock to waste. It calls
#the stock_to_waste() function. If false is returned, it displays an error message.
                s_to_w = stock_to_waste(stock, waste)
                if s_to_w == True:
                    display(tableau, stock, foundation, waste)
                else:
                    print("\nInvalid move!\n")
                    display(tableau, stock, foundation, waste)
    
                in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
                in_str = parse_option(in_str)
            
            elif opt == "R":
#This option shuffles and re-initializes the game.
                stock.shuffle()
                tableau, stock, foundation, waste = initialize()
                print(MENU)
                display(tableau, stock, foundation, waste)
                in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
                in_str = parse_option(in_str)    
                
            
            elif opt == "H":
#This option prints the menu of options.
                print(MENU)
                in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
                in_str = parse_option(in_str)
                
        else:
            display(tableau, stock, foundation, waste)
            in_str = input("Input an option (TT,TF,WT,WF,SW,R,H,Q): ")
            in_str = parse_option(in_str)

#-----------------------------------------------------------------------------#


if __name__ == '__main__':
     main()
