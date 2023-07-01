Copyright 2023, George Mpalanos, All rights reserved.

#Number of players
num_players = int(input("Number of players (between 2 and 6): "))
if num_players>6 or num_players<2:
    print("Something wrong happened: I'm setting the number of players to 3")
    num_players = 3
#number of coins
num_coins = int(input("Number of coins per player (between 5 and 100): "))
if num_coins<5 or num_coins>100:
    print("Something wrong happened: I'm setting the number of coins to 10")
    num_coins = 10

#PlayerList
lst = []
for i in range(1,num_players+1):
    lst.append(i)

#Player_Balance  
player_balance = {}
for i in range(1,num_players+1):
    player_balance.setdefault(i,num_coins)   
print("Game begins with %i players." % num_players,
      "\nEach player has %i coins." % num_coins)

#first random Banker
import random
r = random.randint(1,num_players)
print("Player %i is randomly chosen as banker." % r)
print()
change_bank = False
keep_bank = False
banker_defeats = 0
players_autobank = []
banker_defeats = 1
lst_bets = []
while 0 not in player_balance.values():
    #player who won with 4-5-6 or triple roll
    if change_bank == True and keep_bank == False and len(players_autobank)>=1:
        print("New Banker will be Player %i" % players_autobank[0])
        r = players_autobank[0]
        print("Current balance: ")
        for i in range(1,num_players+1):
            print("Player %i"% i ,"has %i coins." % player_balance[i] )
        print()
        while True:
            try:
                banker_bet=int(input("Player %i :You are the banker! Please enter a valid bank amount: " % r))
            except ValueError:
                print("You didn't type anything")
            else:
                while banker_bet<2 or banker_bet>player_balance[r]:
                    banker_bet=int(input("Player %i :You are the banker! Please enter a valid bank amount: " % r))
                break 
        banker_defeats = 0
        keep_bank = False
        change_bank = False
    #if banker lost all bets
    elif change_bank == True and keep_bank == False or banker_defeats == len(lst_bets):
        print("New Banker will be Player %i" % lst_bets[0])
        r = lst_bets[0]
        print("Current balance: ")
        for i in range(1,num_players+1):
            print("Player %i"% i ,"has %i coins." % player_balance[i] )
        print()
        while True:
            try:
                banker_bet=int(input("Player %i :You are the banker! Please enter a valid bank amount: " % r))
            except ValueError:
                print("You didn't type anything")
            else:
                while banker_bet<2 or banker_bet>player_balance[r]:
                    banker_bet=int(input("Player %i :You are the banker! Please enter a valid bank amount: " % r))
                break 
        banker_defeats = 0
        keep_bank = False
        change_bank = False
    #Banker keeps the bank
    else:
        print("Current balance: ")
        for i in range(1,num_players+1):
            print("Player %i"% i ,"has %i coins." % player_balance[i] )
        print()
        while True:
            try:
                banker_bet=int(input("Player %i :You are the banker! Please enter a valid bank amount: " % r))
            except ValueError:
                print("You didn't type anything")
            else:
                while banker_bet<2 or banker_bet>player_balance[r]:
                    banker_bet=int(input("Player %i :You are the banker! Please enter a valid bank amount: " % r))
                break 
        banker_defeats = 0
        keep_bank = False
        change_bank = False

    bets = {}
    banker_defeats = 0
    players_autobank = []
    max_bet = banker_bet
    bet_amount = 0 
    lst_bets = []

    #Bets with an order
    u = r
    while u != max(lst) and max_bet>0:
        u += 1
        bet_player = int(input("Player %i : Please enter a valid bet: " % u))
        bets.setdefault(u,bet_player)
        while  bet_player > max_bet or bet_player > player_balance[u]:
            bet_player = int(input("Player %i : Please enter a valid bet: " % u))
            bets[u] = bet_player
        max_bet = max_bet - bet_player
        bet_amount += bet_player
        lst_bets.append(u)
    u = 0
    while u != r-1 and max_bet>0:
        u += 1
        bet_player = int(input("Player %i : Please enter a valid bet: " % u))
        bets.setdefault(u,bet_player)
        while  bet_player > max_bet or bet_player > player_balance[u]:
            bet_player = int(input("Player %i : Please enter a valid bet: " % u))
            bets[u] = bet_player
        max_bet = max_bet - bet_player
        bet_amount += bet_player
        lst_bets.append(u)
    if bet_amount < banker_bet:
        banker_bet = banker_bet - (banker_bet - bet_amount) 

    print()

    print("Round starts: ")
    for i in lst:
        if i in bets:
            print("Player %i " % i,": has bet: %i " % bets[i])
        elif i not in bets and i!=r:
            print("Player %i " %i,": has bet: 0 coins")
    print("Player %i " % r,": Banker with bank amount = %i" % banker_bet)

    print()

    #Sum of bets
    w = sum(bets.values())
    scoreboard = {}
    player_turn_on = False
    replay_banker = True
    while replay_banker == True:
        press = input("Banker: press ENTER to roll dice :")
        rolls = []
        while press != "":
            press = input("Banker: press ENTER to roll dice :")

        import random
        for i in range(3):
            u = random.randint(1,6)
            rolls.append(u)
        print("Banker rolled:",rolls)

        rolls.sort()
        rolls_dict = {}
        for i in range(0,3):
            x = rolls.count(rolls[i])
            rolls_dict[rolls[i]] = x

    #Score_banker
        if 2 in rolls_dict.values() and 1 not in rolls and 6 not in rolls :
            player_turn_on = True
            for i in range(3):
                if rolls.count(rolls[i]) != 2:
                    x = rolls[i]
                    print("Banker scored %i points" % x)
                    scoreboard.setdefault('banker',x)
                    replay_banker = False
        elif 2 in rolls_dict.values() and rolls.count(6)==2 and rolls.count(1)==0:
            player_turn_on = True
            for i in range(3):
                if rolls.count(rolls[i]) != 2:
                    x = rolls[i]
                    print("Banker scored %i points" % x)
                    scoreboard.setdefault('banker',x)
                    replay_banker = False
        elif 2 in rolls_dict.values() and rolls.count(1)==2 and rolls.count(6)==0:
            player_turn_on = True
            for i in range(3):
                if rolls.count(rolls[i]) != 2:
                    x = rolls[i]
                    print("Banker scored %i points" % x)
                    scoreboard.setdefault('banker',x)
                    replay_banker = False

    #Lost_banker
        if 2 in rolls_dict.values() and rolls.count(1)==1 :
            print("Banker got an automatic lost")
            player_balance[r] -= banker_bet
            for i in bets:
                player_balance[i] += bets[i]
            replay_banker = False
            change_bank = True
        elif rolls == [1,2,3]:
            print("Banker got an automatic lost")
            player_balance[r] -= banker_bet
            for i in bets:
                player_balance[i] += bets[i]
            replay_banker = False
            change_bank = True

    #Win_banker
        if 2 in rolls_dict.values() and rolls.count(6)==1 :
            print("Banker got an automatic win")
            w = sum(bets.values())
            player_balance[r] = player_balance[r] + w
            for i in lst_bets:
                player_balance[i] -= bets[i]
            replay_banker = False
            keep_bank = True
        elif rolls[0]==rolls[1]==rolls[2]:
            print("Banker got an automatic win")
            w = sum(bets.values())
            player_balance[r] = player_balance[r] + w
            for i in lst_bets:
                player_balance[i] -= bets[i]
            replay_banker = False
            keep_bank = True
        elif rolls == [4,5,6]:
            print("Banker got an automatic win")
            w = sum(bets.values())
            player_balance[r] = player_balance[r] + w
            for i in lst_bets:
                player_balance[i] -= bets[i]
            replay_banker = False
            keep_bank = True

        #Banker rolls again
        if replay_banker == True:
            print("Banker rolls again")

    #if player_turn_on is true then players will play
    m = 1
    while player_turn_on == True :
        for z in bets:
            if  m > len(lst_bets):
                player_turn_on = False
                break
            m += 1
            replay_player = True
            while replay_player == True:
                press = input("Player %i : press ENTER to roll dice" % z)
                rolls = []
                while press != "":
                    press = input("Player %i : press ENTER to roll dice" % z)
                import random
                for i in range(3):
                    u = random.randint(1,6)
                    rolls.append(u)
                rolls.sort()
                rolls_dict = {}
                for i in range(0,3):
                    x = rolls.count(rolls[i])
                    rolls_dict[rolls[i]] = x
                print(rolls)

            #Lost_player
                if rolls == [1,2,3]:
                    print("Player %i lost" % z)
                    player_balance[z] -= bets[z]
                    replay_player = False

            #Win_player
                if rolls[0]==rolls[1]==rolls[2]:
                    print("Player %i got an automatic win" % z)
                    player_balance[z] = player_balance[z] + bets[z]
                    player_balance[r] -= bets[z]
                    replay_player = False
                    change_bank = True
                    players_autobank.append(z)
                elif rolls == [4,5,6]:
                    print("Player %i got an automatic win" % z)
                    player_balance[z] = player_balance[z] + bets[z]
                    player_balance[r] -= bets[z]
                    replay_player = False
                    change_bank = True
                    players_autobank.append(z)

            #Score_player
                if 2 in rolls_dict.values():
                    player_turn_on = True
                    for i in range(3):
                        if rolls.count(rolls[i]) != 2:
                            x = rolls[i]
                            print("Player %i" % z," scored %i points" % x)
                            scoreboard.setdefault(str(z),x)
                            if scoreboard[str(z)]> scoreboard['banker']:
                                print("Player %i wins" % z)
                                player_balance[z] += bets[z]
                                player_balance[r] -= bets[z]
                                banker_defeats += 1
                            elif scoreboard[str(z)]<scoreboard['banker']:
                                print("Banker wins!")
                                player_balance[z] -= bets[z]
                                player_balance[r] += bets[z]
                            else:
                                print("It's a tie between the banker and the player!")
                            replay_player = False
                #player rolls again
                if replay_player == True:
                    print("Player %i rolls again" % z)
else:
    #a player has 0 coins
    for i in player_balance:
        if player_balance[i]==0:
            print("Player %i is bankrupt.Game ends" % i)
    #winner_with_most_coins
    most_coins = max(player_balance.values())
    for j in player_balance:
        if player_balance[j]==most_coins:
            winner = j
            break
    print("Winner is player %i" % j ,"with %i coins" % most_coins)
    input()
