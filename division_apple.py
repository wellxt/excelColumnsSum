# -*- coding: UTF-8 -*-

def division():
    '''
    功能：模拟幼儿园分苹果（但当输入的小朋友人数为0时，会报"ZeroDivisionError: integer division or modulo by zero"的错误。）
    场景模拟：模拟幼儿园老师分苹果。如果老师买来10个苹果，今天来了10个小朋友，那么输入10和10，程序给出的结果是每人分1个苹果。
    '''
    print("\n=====================分苹果了=====================")
    apple = int(input("请输入苹果的个数："))
    children = int(input("请输入来了几个小朋友："))
    result = apple // children                  # 计算每人分了多少个苹果
    remain = apple - result*children            # 计算剩下几个苹果
    if remain > 0:
        print(apple, "个苹果，平均分给", children,"个小朋友，每人分",result,"个，剩下", remain, "个。")
    else:
        print(apple, "个苹果，平均分给", children,"个小朋友，每人分",result,"个。")

if __name__ == "__main__":
    division()                                  # 调用分苹果的函数
