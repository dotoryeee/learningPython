class test:
    var1 = 0
    def __init__(self):
        self.var2 = 0

    def add_var(self):
        test.var1+=1
        self.var2+=1
    
    def print_var(self):
        print(f'var1 : {test.var1}')
        print(f'var2 : {self.var2}')

t = test()
t2 = test()

t.add_var()
t2.add_var()

t.print_var()
t2.print_var()