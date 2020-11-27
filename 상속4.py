class car:
    def __init__(self):
        self.type = 'car'

    def horn(self):
        print('빵빵')

class ambulance(car):
    def __init__(self):
        super().__init__()
        self.type = 'ambulance'

    def horn(self):
        print(f'{self.type} : 삐뽀삐뽀')

class poclain(car):
    def __init__(self):
        super().__init__()
        self.type = 'poclain'

    def horn(self):
        print(f'{self.type} : 우우우웅')


def main():
    while True:
        select = input('1.앰뷸 2.포크레인 : ')
        if select == '1':
            c = ambulance()
        if select == '2':
            c = poclain()
        
        c.horn()


main()