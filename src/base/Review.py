# coding:utf-8
class superList(list):

    # 这个方法类继承了 List 类，添加了对 “-” 的定义
    def __sub__(self, b):
        a = self[:]
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a


print superList([123, 1, 3]) - superList([2, 1, 4]) 
