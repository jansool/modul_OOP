class EnemyDown(Exception):
    pass


class GameOver(Exception):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        with open('scores.txt', 'a') as sfp:
            sfp.write('{0}: {1}\n'.format(self.name, self.score))
