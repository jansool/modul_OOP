import exceptions


lives = 3
level = 1
base_name = ''
base_score = 0


def comands(word):
    if word.lower() == 'help':
        print('\nWizard: 1\n Fighter: 2\n Robber: 3\n')
    elif word.lower() == 'exit':
        raise exceptions.GameOver
    elif word.lower() == 'scores':
        with open('scores.txt', 'r') as fp:
            for i in fp:
                print(i)
