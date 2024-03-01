def func_B():
    print('func_B')
    func_c()

def func_A():
    print('func_A')
    func_B()
    func_D()

def func_D():
    print('func_D')
    func_c()
    func_B()

def func_c():
    print('func_C')

func_A()