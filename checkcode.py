# -*- coding: UTF-8 -*-
'''
生成由数字、字母组成的4位验证码：
    实现一个用户登录页面，为了防止恶意破解，可以添加验证码。这里需要实现一个由数字、大写字母和小写字母组成的4位验证码。
'''

import random
if __name__ == '__main__':
    checkcode = ""
    for i in range(4):
        index = random.randrange(0,4)
        if index != i and index + 1 !=i:
            checkcode += chr(random.randint(97,122))
        elif index + 1 == i:
            checkcode += chr(random.randint(65,90))
        else:
            checkcode += str(random.randint(1,9))
    print("验证码：", checkcode)
