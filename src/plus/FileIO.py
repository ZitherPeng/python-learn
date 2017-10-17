# coding:utf-8
import codecs

f = open('../../docs/test.txt', 'r')
content = f.readlines()
print content

f = open('../../docs/test.txt', 'w')
f.write('I like apple')
f.close()

with codecs.open('../../docs/test.md', 'rb') as f:
    lines = f.readlines()
    print lines
    for line in lines:
        print line.strip()  # 把末尾的 /n 删除
