class Enemy:
    life = 3

    def attack(self):
        print('ouch')
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print('i am dead')
        else:
            print(str(self.life) + ' life left')


enemy1 = Enemy()
enemy2 = Enemy()

for i in range(3):
    enemy1.attack()
enemy2.attack()
enemy1.check_life()
enemy2.check_life()