#playMore = 'yes'
#while playMore != 'q':
#    print('This is a 2 player (r)ock, (p)aper, (c)issors game')
#    player1 = input('Player1, what is your name?')
#    player2 = input('PLayer2 what is your name?')


#    print(str(player1) + ''' - what is your play;
#     (r)ock
#     (p)aper
#     (c)issors''')
#    p1play = input()

#    print(str(player2) + ''' - what is your play;
#    (r)ock
#    (p)aper
#    (c)issors''')
#    p2play = input()
#    play = str(p1play) + str(p2play)


#    if p1play == p2play:
#        print('This is a tie; both players played - ' + str(p1play))
#    elif play == 'rp':
#        print('Player2 wins with paper beating rock')
#    elif play == 'rc':
#        print('Player1 win with rock beating cissors')
#    elif play == 'pr':
#        print('Player1 wins with paper beating rock')
#    elif play == 'pc':
#        print('Player 2 win with cissors beating paper')
#    elif play == 'cr':
#        print('Player2 win with rock beating cissors')
#    elif play == 'cp':
#        print('Player 1 win with cissors beating paper')
#    else:
#        print('Invalid input provided - only play the character r, p or c')
#    playMore = input('Press q to quit or any key to continue?')

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)