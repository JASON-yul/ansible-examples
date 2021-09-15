#过滤路径下最新文件或jar包
# -*- coding:UTF-8 -*-
# -*- create on 2019/06/28 by HangLi -*-
import sys
import os
def find_new_file(dir):
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "//" + fn)
                    if not os.path.isdir(dir + "//" + fn) else 0)
    print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(dir, file_lists[-1])
    print('完整路径：', file)
    return file
dir = sys.argv[1]
find_new_file(dir)
