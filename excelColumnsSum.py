# coding=utf-8

import pandas as pd
import xlsxwriter
import sys

# 比如在命令行界面执行"python excelColumnSum.py 问卷调查.xls 1.xlsx"，
# 其中sys.argv[1]为"问卷调查.xls"，sys.argv[2]为"1.xlsx"，这两个是运行python脚本的两个参数。
# 注：使用sys.argv[1]、sys.argv[2]传参时必须要使用import sys来引用sys库。
filePath = sys.argv[1]
outputExcelName = sys.argv[2]

# 读取"问卷调查.xls"，将数据存储到data变量。
data = pd.read_excel(filePath)


# 初始化result变量的行索引和列索引，用来存储最终要导出的EXCEL表格。
resultColumn = data.columns

# 以下7行代码：遍历"问卷调查.xls"的所有数值（数值不能重复），存到resultIndex中，作为result变量的行索引。
# 注意：必须要先初始化resultIndex列表为空列表，
# 然后通过2层for循环遍历"问卷调查.xls"的所有数值，若当前数值data.loc[i][j]不在resultIndex列表中，则利用append将数值添加到resultIndex列表中。
resultIndex = []  # 初始化空列表
for i in data.index:
    for j in data.columns:
        if data.loc[i][j] not in resultIndex:
            resultIndex.append(data.loc[i][j])
        else:
            pass


# 初始化result变量，使用resultIndex为行索引，resultColumn为列索引
result = pd.DataFrame(index = resultIndex, columns = resultColumn)


# 用i来遍历data的所有列索引
for i in data:
    data1 = data[i].value_counts()  # 将data的列计数，并赋值给data1变量
    # 用j遍历data1的所有行索引
    for j in data1.index:
        result.loc[j][i] = data1.loc[j]  # 将data1第j行的值存到result变量的对应元素中


# 将result变量数据保存到新EXCEL表（使用xlsxwriter模块）
writer = pd.ExcelWriter(outputExcelName, engine="xlsxwriter")
## 也可以不指定Sheet_name，默认就是Sheet1，此程序Sheet_name指定为outputExcelName
result.to_excel(writer, sheet_name=outputExcelName)
writer.save()
