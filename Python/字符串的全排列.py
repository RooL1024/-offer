'''
Creat by HuangDandan
2018-08-23
dandanhuang@sjtu.edu.cn

'''

def Permutation(ss):
    if len(ss) <= 0:
        return []
    res = list()
    perm(ss, res, '')       #初始化path = '',path为首字符
    uniq = list(set(res))   #set()函数创建一个无需不重复的元素集，不需要判断元素是否重复
    return sorted(uniq)     #sorted()函数对任意对象进行排序


def perm(ss, res, path):
    if ss == '':
        res.append(path)
    else:
        for i in range(len(ss)):
            perm(ss[:i]+ss[i+1:], res, path+ss[i])

ss1 = 'abc'
print(Permutation(ss1))