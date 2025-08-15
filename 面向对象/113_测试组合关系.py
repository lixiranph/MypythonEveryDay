class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu=cpu
        self.screen=screen

class CPU:
    def calculate(self):
        print('算你姥姥')
        print('CPU对象',self)
class Screen:
    def show(self):
        print('显示一个好看的画面，亮瞎你的钛合金狗眼')
        print('Screen对象',self)

m=MobilePhone(CPU(),Screen())

m.cpu.calculate()
m.screen.show()