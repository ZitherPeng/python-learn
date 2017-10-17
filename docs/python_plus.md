# python 进阶
## 词典
词典 (dictionary)。与列表相似，词典也可以储存多个元素。这种储存多个元素的对象称为容器(container)。

```python
创建词典的方法:
>>>dic = {'tom':11, 'sam':57,'lily':100}
>>>print type(dic)
结果为：<type 'dict'>

通过词典的键来引用:
>>>print dic['tom']
>>>dic['tom'] = 30
```
```python
>>>print dic.keys()           # 返回dic所有的键
>>>print dic.values()         # 返回dic所有的值
>>>print dic.items()          # 返回dic所有的元素（键值对）
>>>dic.clear()                # 清空dic，dict变为{}
>>>del dic['tom']             # 删除 dic 的‘tom’元素
>>>print len(dic)             # 查询词典中的元素总数
```

## 文本文件输入输出

## 模块
```python
import a as b             # 引入模块a，并将模块a重命名为b
from a import function1   # 从模块a中引入function1对象。调用a中对象时，我们不用再说明模块，即直接使用function1，而不是a.function1。
from a import *           # 从模块a中引入所有对象。调用a中对象时，我们不用再说明模块，即直接使用对象，而不是a.对象。
```

