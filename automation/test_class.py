class Player:
    
    country = 'korea'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def kick(self):
        print('kick!')

    def pass_ball(self):
        print('pass!')

    def throw_in(self):
        print('throw_in!')

player = Player('Hyukjun', '29')
player.kick()
player.pass_ball()
player.throw_in()
print(player.country)
print(player.name, player.age)
