# -*- coding: UTF-8 -*-
'''
生成由数字、字母组成的4位验证码：
    实现一个用户登录页面，为了防止恶意破解，可以添加验证码。这里需要实现一个由数字、大写字母和小写字母组成的4位验证码。
'''

import random                                               # 导入标准模块中的random
if __name__ == '__main__':
    checkcode = ""                                          # 保存验证码的变量
    for i in range(4):                                      # 循环4次
        index = random.randrange(0,4)                       # 生成0~3中的一个数
        if index != i and index + 1 !=i:
            checkcode += chr(random.randint(97,122))        # 生成a~z中的一个小写字母
        elif index + 1 == i:
            checkcode += chr(random.randint(65,90))         # 生成A~Z中的一个大写字母
        else:
            checkcode += str(random.randint(1,9))           # 生成1-9中的一个数字
    print("验证码：", checkcode)                             # 输出生成的验证码
