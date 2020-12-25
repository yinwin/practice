'''
题目：模仿静态变量的用法
'''
def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()
# 类的属性
# 作为类的一个属性
class Static:
    StacticVar = 5
    def varfunc(self):
        self.StacticVar += 1
        print(self.StacticVar)
print(Static.StacticVar)
a = Static
for i in range(3):
    a.varfunc
