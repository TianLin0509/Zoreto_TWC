import os
import parse
import re
path = input('输入.bib文件所在的文件夹路径，如(C:/mybib/)：\n')
G = [x for x in os.listdir(path) if x[-3:] == 'bib']
if len(G) > 0:
    g = G[0]
    print('成功读取到bib文件:' + g)
    with open(path +'/' + g, encoding = 'utf8') as b:
        c = b.read()
    pass
    # delete url and note
    p1 = re.compile(r'url = {.*},\n')
    c = re.sub(p1, "", c)
    p2 = re.compile(r'note = {.*?\n?.*?},\n')
    c = re.sub(p2, "", c)  # including '\n'
    # lower-case of Title
    p3 = re.compile('\ttitle = {.*?},')
    d = p3.findall(c)
    p4 = re.compile('{.*?}')
    try:
        for e in d:
            et = e
            idx = e.index('{')
            f = e[idx + 1:]
            for h in p4.findall(f):
                if not h.isupper():
                    et = et.replace(h, h[1:-1])
                pass
            c = c.replace(e, et)
    except:
        print('纠正大小写出错')
    # journal abbreviation
    with open(path + '/' + g, 'w', encoding='utf8') as b:
    # with open('f.bib', 'w', encoding='utf8') as b:
        b.write(c)
    print('bib文件成功处理并覆盖原文件！')
else:
    print('.bib file not found!')
