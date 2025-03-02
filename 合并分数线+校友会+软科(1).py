import pandas as pd
import os

df1 = pd.read_excel('分数线2023.xlsx')
df2 = pd.read_excel('软科2024.xlsx')

common_universities = set(df1['大学名称']).intersection(set(df2['大学名称']))

df1_common = df1[df1['大学名称'].isin(common_universities)]
df2_common = df2[df2['大学名称'].isin(common_universities)]

result = pd.merge(df1_common, df2_common, on='大学名称')

result.to_excel('2023分数线+软科2024.xlsx', index=False)

#三合一
df1 = pd.read_excel('2023分数线+软科2024.xlsx')
df2 = pd.read_excel('大学排行榜校友会2021.xlsx')

common_universities = set(df1['大学名称']).intersection(set(df2['大学名称']))

df1_common = df1[df1['大学名称'].isin(common_universities)]
df2_common = df2[df2['大学名称'].isin(common_universities)]

result = pd.merge(df1_common, df2_common, on='大学名称')

# 保存到新的Excel文件
result.to_excel('分数线+校友会+软科.xlsx', index=False)

#多余的删掉
file_path = "2023分数线+软科2024.xlsx"
if os.path.exists(file_path):
    os.remove(file_path)
