'''
模拟结账功能————计算实付金额
'''

def fun_checkout(money):
    '''
    功能：计算商品合计金额并进行折扣处理
        money：保存商品金额的列表
        返回商品的合计金额和折扣后的合计金额
    '''
    money_old = sum(money)  # 计算合计金额
    money_new = money_old
    if 500 <= money_new < 1000:                         # 合计金额满500享受9折优惠
        money_new = '{:.2f}'.format(money_old * 0.9)
    elif 1000 <= money_new <2000:                       # 合计金额满1000享受8折优惠
        money_new = '{:.2f}'.format(money_old * 0.8)
    else:                                               # 合计金额满2000享受6折优惠
        money_new = '{:.2f}'.format(money_old * 0.6)
    return money_old, money_new     # 返回商品原价的总金额和折扣后的总金额

print("开始结算")
list_money = []     # 定义保存商品金额的列表，在循环中会将输入的所有商品价格一一添加到此列表中

while True:
    # 请不要输入非法的金额，否则将会报异常（只需要输入正数）
    inmoney = float(input("请输入商品金额（输入0表示输入完毕）："))
    if int(inmoney) == 0:
        break       # 退出while循环
    else:
        list_money.append(inmoney)     # 将金额添加到商品金额的列表中

money = fun_checkout(list_money)        # 调用函数，将返回值写到money变量中
print("合计金额：", money[0], "应付金额：", money[1])     # 显示商品的合计金额和应付金额
