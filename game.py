import models
import exceptions
import settings


def play():
    print('Hello!')
    while True:
        user_input = input("Please, enter your name \n-> ")
        if user_input.isalpha() and len(user_input) <= 20:
            if user_input.lower() == 'help' or user_input.lower() == 'exit' or user_input.lower() == 'scores':
                settings.comands(user_input)
            else:
                name = user_input
                break
        else:
            print('\nPlease, use only letters')
    player = models.Player(name)
    level = 3
    enemy = models.Enemy(level)
    if input(f"{player.name}, enter 'start' to start the game :)\n-> ").lower() == 'start':
        pass
    else:
        raise KeyboardInterrupt

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except exceptions.EnemyDown:
            player.score += 5
            player.level += 1
            print('ENEMY DOOOWN\nYOUR CURRENT LEVEL: {0}\nYOUR CURRENT SCORE: {1}'.format(player.level, player.score))
            level -= 1
            enemy = models.Enemy(level)
        if level == 0:
            print(f'{player.name.upper()}! \nYour total score: {player.score}\nYour level: {player.level}')
            raise (exceptions.GameOver(player.name, player.score))


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver as err:
        print('The game is over :(')
    except KeyboardInterrupt as error:
        print('keyboard interrupt ()_()')
    finally:
        input('Press Enter to exit')
        print('Goodbuy!')
