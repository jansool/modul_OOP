import random
import exceptions
import settings


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise exceptions.EnemyDown


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = settings.lives
        self.level = settings.level
        self.score = 0

    @staticmethod
    def fight(attack, defence):
        if attack == defence:
            return 0
        elif ((attack == 1 and defence == 2) or
              (attack == 2 and defence == 3) or
              (attack == 3 and defence == 1)):
            return 1
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            print(f'{self.name.upper()}! \nYour total score: {self.score}\nYour level: {self.level}')
            raise (exceptions.GameOver(self.name, self.score))

    def attack(self, enemy_obj):
        player_num = 0
        while True:
            player_input = input("Your move:")
            if player_input.isdigit():
                if 1 <= int(player_input) <= 3:
                    player_num = int(player_input)
                    break
                else:
                    print("\nPlease use only '1', '2', or '3'")
            elif player_input.isalpha:
                settings.comands(player_input)
                print("\nPlease use only '1', '2', or '3'")
            else:
                print("\nPlease use only '1', '2', or '3'")

        result = Player.fight(player_num, enemy_obj.select_attack())
        if result == 0:
            print("it's a draw :|")
        elif result == 1:
            print("You attacked successfully :)")
            enemy_obj.decrease_lives()
            self.score += 1
        else:
            print("You missed :(")

    def defence(self, enemy_obj):
        player_num = 0
        while True:
            player_input = input("Your turn to defence:")
            if player_input.isdigit():
                if 1 <= int(player_input) <= 3:
                    player_num = int(player_input)
                    break
                else:
                    print("Please use only '1', '2', or '3'")
            elif player_input.isalpha:
                settings.comands(player_input)
            else:
                print("Please use only '1', '2', or '3'")

        result = Player.fight(enemy_obj.select_attack(), player_num)
        if result == 0:
            print("it's a draw!")
        elif result == -1:
            print("You defenced successfully!")
        else:
            print("Ups! You missed!")
            self.decrease_lives()

























