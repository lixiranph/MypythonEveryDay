'''
模块引入的问题
1. 那些模块可以被引入
    builtins
    sys.path:
        列表：存储一系列目录
2. 被引入之后的模块更新问题

'''
import random
import sys
result=sys.path
result.append('F:\\TankBattle\\TankBattle')

import main25

game=main25.MainGame()
game.startGame()