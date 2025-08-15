'''
通过myMath一起配合使用
'''
import myMath
x=10
y=20
print(f'加{myMath.add(x,y)}')
print(f'减{myMath.sub(x,y)}')
print(f'乘{myMath.mul(x,y)}')
print(f'除{myMath.div(x,y)}')

from myMath import *
print(add(x,y))