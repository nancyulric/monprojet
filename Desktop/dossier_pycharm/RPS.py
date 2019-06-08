# Variables

machine_player = ('stone', 'paper', 'scissors')
max_number_game = (1, 3, 5)
number_game_to_win = 5
human_player = ('stone', 'paper', 'scissors')



for i in machine_player:
    if 'stone' < 'paper':
        print('2')
        if 'stone' > 'scissors':
            print('1')
            if 'stone' == 'stone':
                print('0')
                if 'paper' > 'stone':
                    print('1')
                    if 'paper' < 'scissors':
                        print('2')
                        if 'paper' == 'paper':
                            print('0')
                            if 'scissors' < 'stone':
                                print('2')
                                if 'scissors' > 'paper':
                                    print('1')
                                    if 'scissors' == 'scissors':
                                        print('0')
