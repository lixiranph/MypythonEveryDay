# @property
# @属性.setter
class Account():
    def __init__(self):
        self.__money=0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        if isinstance(money,int):
            self.__money=money
        else:
            raise Exception('金钱类型有误')
A=Account()
A.money=100
print(A.money)