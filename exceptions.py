class EnemyDown(Exception):
    pass


class GameOver(Exception):
    def __init__(self, n, s):
        self.nam = n
        self.scor = s
        with open('scores.txt', 'a') as sfp:
            sfp.write('{0}: {1}\n'.format(self.nam, self.scor))
