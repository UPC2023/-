#1
# -*- coding:utf-8 -*-
# -*- coding:gb2312-*-
import requests
import urllib.request
from bs4 import BeautifulSoup
import bs4
import pandas as pd

text = "一，爬取大学排名校友会+分数线+软科"
print(f"{text:^{40}}")


url = 'http://www.gaokao.com/e/20210328/606032dc1b634.shtml'
data=[]
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
 
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip()])
 
 
def printUnivList(ulist, num):
    tplt = "{0:^10}\t.{1:{3}^10}\t.{2:^10}"
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
        data.append([u[0],u[1],u[2]])
       
 
def main():
    uinfo = []
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,140)
 
if __name__ == "__main__":
    main()
    filename = '大学排行榜校友会2021.xlsx'
    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_excel(filename, index=False)


with open('分数线2023.txt', 'r', encoding='utf-8') as file:
    cnt=1
    n=1
    a=[]
    a2=[]
    for line in file:
        if line.strip():
            if cnt==1:
                 a.append(n)
                 a.append(line.strip())
                 cnt+=1
            elif cnt==2:
                a.append(line.strip())
                cnt+=1
            elif cnt==3:
                b=line.split('：')
                #print(b)
                if len(b)==2:
                    a.extend([b[1][0:3]])
                    a2.append(a)
                    a=[]
                    cnt=1
                    n+=1
                
df = pd.DataFrame(a2,columns=['序号', '大学名称', '地区', '分数线'])
df.to_excel('分数线2023.xlsx', index=False)



with open('软科2024.txt', 'r', encoding='utf-8') as file:
    cnt=1
    a=[]
    a2=[]
    for line in file:
        if line.strip():
            if cnt<5:
                if cnt==1:
                    a.append(line.strip())
                elif cnt==2:
                    a.append(line.strip())
                cnt+=1
            elif cnt==5:
                b=line.split()
                if len(b)==4 or len(b)==3:
                    a.extend([b[0],b[2]])
                    a2.append(a)
                    a=[]
                    cnt=1
                else:
                    cnt+=1
            elif cnt==6:
                b=line.split()
                a.extend([b[0],b[2]])
                a2.append(a)
                a=[]
                cnt=1
df = pd.DataFrame(a2,columns=['排名', '大学名称', '省份', '评分'])
df.to_excel('软科2024.xlsx', index=False)

#2
text = "二，绘制饼图+直方图"
print(f"{text:^{40}}")

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['font.serif']=['KaiTi']

# 软科2024
df = pd.read_excel('软科2024.xlsx')

province_counts = df['省份'].value_counts()

explode = [0.1 if province == '山东' else 0 for province in province_counts.index]
plt.figure(figsize=(10,6))
plt.pie(province_counts, labels=province_counts.index, autopct='%1.1f%%', explode=explode)
plt.title('大学评分前120省份分布')

# 分数线2023
df = pd.read_excel('分数线2023.xlsx')

province_counts = df['地区'].value_counts()

explode = [0.1 if province[0:2] == '山东' else 0 for province in province_counts.index]
plt.figure(figsize=(10,6))
plt.pie(province_counts, labels=province_counts.index, autopct='%1.1f%%', explode=explode)
plt.title('大学分数线前120地区分布')

plt.show()

plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['font.serif']=['KaiTi']


universities = ['清华大学', '北京大学', '中国科学院大学', '北京大学医学部', '上海交通大学医学院', '中国科学技术大学', '复旦大学', '浙江大学医学院', '复旦大学上海医学院', '中国人民大学', '南京大学', '哈尔滨工业大学（深圳）', '哈尔滨工业大学', '北京理工大学', '上海交通大学', '浙江大学', '同济大学', '北京航空航天大学', '武汉大学', '电子科技大学', '南开大学', '北京师范大学', '东南大学', '西安交通大学', '中国人民解放军国防科技大学', '上海中医药大学', '对外经济贸易大学', '中山大学', '华中科技大学', '厦门大学', '天津大学', '中国人民公安大学', '华东师范大学', '西安电子科技大学', '上海财经大学', '中国政法大学', '中央财经大学', '中国社会科学院大学', '华南理工大学', '重庆大学', '北京电影学院', '西北工业大学', '山东大学', '上海大学', '哈尔滨工业大学（威海）', '北京邮电大学', '上海外国语大学', '四川大学', '华东政法大学', '中南大学', '南京理工大学', '西南财经大学', '南京航空航天大学', '山东大学（威海）', '北京交通大学', '中国传媒大学', '上海对外经贸大学', '中央民族大学', '中国药科大学', '兰州大学', '海军军医大学', '华北电力大学', '华东理工大学', '深圳大学', '中国海洋大学', '中国医科大学', '湖南大学', '北京协和医学院', '北京工业大学', '贵州医科大学', '北京化工大学', '中央美术学院', '安徽大学', '西南政法大学', '华中师范大学', '东北大学秦皇岛分校', '北京科技大学', '南京师范大学', '河海大学', '首都师范大学', '吉林大学', '中国石油大学（北京）', '陕西师范大学', '西北大学', '苏州大学', '中国石油大学（华东）', '哈尔滨工程大学', '大连理工大学盘锦校区', '西北政法大学', '江南大学', '福州大学', '中国地质大学（北京）', '东北大学', '北京外国语大学', '北京林业大学', '中国矿业大学（北京）', '安徽医科大学', '南京审计大学', '中国人民解放军空军军医大学', '暨南大学', '杭州电子科技大学', '东华大学', '华南师范大学', '合肥工业大学', '南京邮电大学', '上海海关学院', '东北师范大学', '西北农林科技大学', '合肥工业大学宣城校区', '华北电力大学保定校区', '太原理工大学', '北京中医药大学', '西南交通大学', '上海电力大学', '中国农业大学', '武汉理工大学', '南京信息工程大学', '郑州大学', '中国美术学院']
scores = [691, 689, 683, 679, 679, 676, 674, 673, 671, 669, 668, 667, 663, 662, 660, 656, 651, 650, 650, 650, 647, 646, 644, 644, 641, 640, 638, 638, 638, 633, 632, 631, 627, 626, 623, 622, 622, 618, 617, 617, 616, 615, 614, 614, 613, 613, 612, 612, 612, 610, 609, 608, 607, 607, 605, 605, 605, 605, 604, 604, 603, 603, 602, 602, 601, 601, 600, 600, 600, 599, 598, 598, 598, 598, 595, 595, 595, 593, 593, 593, 593, 592, 592, 592, 592, 592, 591, 590, 590, 590, 590, 590, 589, 589, 589, 588, 588, 587, 587, 587, 585, 585, 585, 584, 584, 584, 584, 583, 583, 582, 582, 581, 581, 581, 580, 580, 580, 580, 579]

# 截取前5个元素
top_5_universities = universities[:5]
top_5_scores = scores[:5]

# 后5个元素
last_5_universities = universities[-5:]
last_5_scores = scores[-5:]

u=top_5_universities+last_5_universities
s=top_5_scores+last_5_scores

plt.figure(figsize=(10,6))
plt.rcParams['font.size'] = 10

plt.bar(u, s)


plt.title("各大学分数线直方图")
plt.xlabel("大学名称")
plt.ylabel("分数线")

plt.show()


plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['font.serif']=['KaiTi']
# 数据
universities = ['清华大学', '北京大学', '浙江大学', '上海交通大学', '复旦大学', '南京大学', '中国科学技术大学', '华中科技大学', '武汉大学', '西安交通大学', '中山大学', '北京航空航天大学', '东南大学', '北京理工大学', '四川大学', '哈尔滨工业大学', '同济大学', '中国人民大学', '北京师范大学', '天津大学', '南开大学', '山东大学', '西北工业大学', '厦门大学', '中南大学', '吉林大学', '中国农业大学', '大连理工大学', '华东师范大学', '华南理工大学', '电子科技大学', '湖南大学', '重庆大学', '南方科技大学', '北京科技大学', '南京航空航天大学', '南京理工大学', '兰州大学', '东北大学', '西安电子科技大学', '北京交通大学', '上海科技大学', '苏州大学', '华东理工大学', '哈尔滨工程大学', '东北师范大学', '华中农业大学', '中国石油大学（北京）', '南京农业大学', '郑州大学', '暨南大学', '南京师范大学', '武汉理工大学', '中国矿业大学', '江南大学', '上海大学', '中国海洋大学', '华中师范大学', '西南交通大学', '中国石油大学（华东）', '中国地质大学（武汉）', '陕西师范大学', '北京邮电大学', '浙江工业大学', '河海大学', '北京工业大学', '西北大学', '北京化工大学', '西南大学', '云南大学', '南昌大学', '深圳大学', '西北农林科技大学', '中国地质大学（北京）', '华北电力大学', '东华大学', '中国矿业大学（北京）', '宁波大学', '华南师范大学', '江苏大学', '福州大学', '扬州大学', '合肥工业大学', '北京林业大学', '南京邮电大学', '湖南师范大学', '福建师范大学', '浙江师范大学', '南京工业大学', '广西大学', '首都师范大学', '长安大学', '南京林业大学', '华南农业大学', '安徽大学', '贵州大学', '杭州电子科技大学', '广州大学', '河南大学', '广东工业大学', '山西大学', '湘潭大学', '南京信息工程大学', '海南大学', '山东师范大学', '浙江理工大学', '上海理工大学', '太原理工大学', '河北工业大学', '青岛大学', '大连海事大学', '燕山大学', '东北林业大学', '西安建筑科技大学', '昆明理工大学', '内蒙古大学', '江西师范大学', '西安理工大学', '上海师范大学']
scores = [992.6, 898.6, 793.8, 776.3, 697.0, 656.1, 578.4, 578.0, 577.3, 566.4, 539.6, 537.2, 530.7, 530.2, 527.9, 514.1, 509.6, 508.3, 501.4, 491.5, 481.8, 476.3, 459.9, 458.2, 456.1, 443.7, 440.6, 435.7, 431.2, 430.6, 426.1, 422.2, 407.5, 396.4, 384.8, 380.1, 373.4, 367.6, 366.8, 355.4, 352.1, 348.5, 347.0, 341.5, 340.9, 340.8, 338.1, 331.4, 330.8, 326.1, 323.4, 322.7, 322.7, 321.7, 320.6, 319.1, 318.5, 317.0, 313.9, 313.2, 312.6, 311.3, 309.7, 307.7, 306.1, 305.2, 300.9, 300.6, 297.8, 297.0, 296.4, 292.4, 291.4, 286.4, 282.8, 282.3, 281.3, 277.5, 271.8, 270.2, 269.6, 263.7, 263.1, 262.4, 258.9, 257.6, 257.3, 253.0, 251.9, 249.5, 249.5, 248.2, 247.7, 247.6, 247.2, 244.8, 243.5, 238.5, 237.5, 237.3, 236.9, 232.5, 231.7, 230.8, 230.7, 230.0]
universities_to_plot = universities[:5] + universities[-5:]
scores_to_plot = scores[:5] + scores[-5:]

plt.figure(figsize=(10,6))
plt.rcParams['font.size'] = 10

# 绘制
plt.bar(universities_to_plot, scores_to_plot)
plt.xlabel('大学')
plt.ylabel('软科分数线')
plt.title('各大学软科分数条形图')

plt.show()


#3

text = "三，将以上数据存入数据库"
print(f"{text:^{40}}")

import pandas as pd
import sqlite3

# 创建数据库连接
conn = sqlite3.connect('test.db')

# 读取Excel文件并存入数据库
df1 = pd.read_excel('软科2024.xlsx')
df1.to_sql('soft2024', conn, if_exists='replace', index=False)

df2 = pd.read_excel('分数线2023.xlsx')
df2.to_sql('score2023', conn, if_exists='replace', index=False)

df3 = pd.read_excel('大学排行榜校友会2021.xlsx')
df3.to_sql('rank2021', conn, if_exists='replace', index=False)

# 查
def query(file, column, value):
    df = pd.read_sql_query(f"SELECT * FROM {file} WHERE {column} = '{value}'", conn)
    return df

# 删
def delete(file, column):
    df = pd.read_sql_query(f"SELECT * FROM {file}", conn)
    df = df.drop(columns=[column])
    df.to_sql(file, conn, if_exists='replace', index=False)

# 改
def update(file, column, old_value, new_value):
    df = pd.read_sql_query(f"SELECT * FROM {file}", conn)
    df.loc[df[column] == old_value, column] = new_value
    df.to_sql(file, conn, if_exists='replace', index=False)
def updatehead(file, column, old_value, new_value):
    df = pd.read_sql_query(f"SELECT * FROM {file}", conn)
    df.loc[df[column] == old_value, column] = new_value
    df = df.rename(columns={column: new_value})
    df.to_sql(file, conn, if_exists='replace', index=False)
# 增
def add_data(file_name, data):
    table_name = file_name.split('.')[0]
    df = pd.read_sql_query("SELECT * from {}".format(table_name), conn)
    df.loc[len(df)] = data
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# 将数据库内容存回Excel
def save_to_excel(file):
    df = pd.read_sql_query(f"SELECT * FROM {file}", conn)
    df.to_excel(f"{file}.xlsx", index=False)
print("小提醒：必须更改rank2021的表头‘学校名称’为‘大学名称’，不然影响后续合并")

while True:
    user_input = input("请输入操作（查询/更改/更改表头/删除/增加/退出）：")
    if user_input == "退出":
        print("已退出")
        break
    if user_input == "查询":
        file = input("请输入要查询的文件：(soft2024/score2023/rank2021).")
        column = input("请输入要查询的列名：")
        value = input("请输入要查询的值：")
        result = query(file,column, value)
        print(result)
    elif user_input == "更改":
        file = input("请输入文件：(soft2024/score2023/rank2021).")
        column = input("请输入要更改的列名：")
        row_id = input("请输入要更改的值：")
        new_value = input("请输入新的值：")
        update(file,column, row_id, new_value)
    elif user_input == "更改表头":
        file = input("请输入文件：(soft2024/score2023/rank2021).")
        column = input("请输入要更改的列名：")
        row_id = input("请输入要更改的值：")
        new_value = input("请输入新的值：")
        updatehead(file,column, row_id, new_value)
    elif user_input == "删除":
        file = input("请输入文件：(soft2024/score2023/rank2021).")
        column = input("请输入要删除的列名：")
        delete(file,column)
    elif user_input == "增加":
        file = input("请输入文件：(soft2024/score2023/rank2021).")
        data = input("请输入增加的这一行：(以英文逗号隔开).").split(',')
        add_data(file, data)
    else:
        print("无效的操作")

# 从数据库中读取数据并保存到原始Excel文件

file="rank2021"
df = pd.read_sql_query(f"SELECT * FROM {file}", conn)
df.to_excel("大学排行榜校友会2021.xlsx", index=False)

# 关闭数据库连接
conn.close()

#4

text = "四，合并校友会+分数线+软科"
print(f"{text:^{40}}")

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

#5
text = "五，建立合并文件的数据库"
print(f"{text:^{40}}")
print("提示：必须将在总分和评分前加上校友会和软科的前缀")
import pandas as pd
import sqlite3

# 连接
conn = sqlite3.connect('test2.db')

df1 = pd.read_excel('分数线+校友会+软科.xlsx')
df1.to_sql('three', conn, if_exists='replace', index=False)

# 查
def query(column, value):
    df = pd.read_sql_query(f"SELECT * FROM three WHERE {column} = '{value}'", conn)
    return df

# 删
def delete(column):
    df = pd.read_sql_query("SELECT * FROM three", conn)
    df = df.drop(columns=[column])
    df.to_sql('three', conn, if_exists='replace', index=False)

# 改
def update(column, old_value, new_value):
    df = pd.read_sql_query("SELECT * FROM three", conn)
    df.loc[df[column] == old_value, column] = new_value
    df = df.rename(columns={column: new_value})
    df.to_sql('three', conn, if_exists='replace', index=False)
def update2(column, old_value, new_value):
    df = pd.read_sql_query(f"SELECT * FROM three", conn)
    df.loc[df[column] == old_value, column] = new_value
    df.to_sql('three', conn, if_exists='replace', index=False)


# 增
def add_data(data):
    df = pd.read_sql_query("SELECT * from three", conn)
    df.loc[len(df)] = data
    df.to_sql('three', conn, if_exists='replace', index=False)

# 存回Excel
def save_to_excel():
    df = pd.read_sql_query("SELECT * FROM three", conn)
    df.to_excel("分数线+校友会+软科.xlsx", index=False)

while True:
    user_input = input("请输入操作（查询/更改（默认为更改表头）/更改内容/删除/增加/退出）：")
    if user_input == "退出":
        print("已退出")
        break
    if user_input == "查询":
        column = input("请输入要查询的列名：")
        value = input("请输入要查询的值：")
        result = query(column, value)
        print(result)
    elif user_input == "更改":
        column = input("请输入要更改的列名：")
        old = input("请输入要更改的值：")
        new = input("请输入新的值：")
        update(column, old, new)
    elif user_input == "更改内容":
        column = input("请输入要更改的列名：")
        old = input("请输入要更改的值：")
        new = input("请输入新的值：")
        update2(column, old, new)
    elif user_input == "删除":
        column = input("请输入要删除的列名：")
        delete(column)
    elif user_input == "增加":
        data = input("请输入增加的这一行：(以英文逗号隔开).").split(',')
        add_data(data)
    else:
        print("无效的操作")

save_to_excel()

# 关闭数据库连接
conn.close()

#6
text = "六，拟合曲线的绘制"
print(f"{text:^{40}}")

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import linregress

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 来点和楷体不一样的
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

file_path = r"分数线+校友会+软科.xlsx"


data = pd.read_excel(file_path)

data.dropna(subset=['软科评分', '分数线', '校友会总分'], inplace=True)

soft_score = data['软科评分']
score_line= data['分数线']
total_score = data['校友会总分']
university_names = data['大学名称']

plt.figure(figsize=(15, 6))

# 第一个
plt.subplot(1, 2, 1)
sns.scatterplot(x=soft_score, y=score_line)
plt.title('软科评分与分数线的关系')
plt.xlabel('软科评分')
plt.ylabel('分数线')
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(soft_score, score_line)
line1 = slope1 * soft_score + intercept1
plt.plot(soft_score, line1, 'r', label=f'拟合线 y={slope1:.2f}x+{intercept1:.2f}\nR²={r_value1**2:.2f}')
plt.legend()

# 添加大学名称注释
for i, name in enumerate(university_names):
    plt.annotate(name, (soft_score[i], score_line[i]))
    
# 第二个
plt.subplot(1, 2, 2)
sns.scatterplot(x=score_line, y=total_score)
plt.title('分数线与校友会总分的关系')
plt.xlabel('分数线')
plt.ylabel('校友会总分')
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(score_line, total_score)
line2 = slope2 * score_line + intercept2
plt.plot(score_line, line2, 'g', label=f'拟合线 y={slope2:.2f}x+{intercept2:.2f}\nR²={r_value2**2:.2f}')
plt.legend()

for i, name in enumerate(university_names):
    plt.annotate(name, (score_line[i], total_score[i]))


plt.tight_layout()
plt.show()
#7
text = "七，性价比指数计算"
print(f"{text:^{40}}")
print("分数线越低，评分越高，则性价比越高")
import pandas as pd

data = pd.read_excel('分数线+校友会+软科.xlsx')

low_cost_performance = []
high_cost_performance = []
double_performance = []

for index, row in data.iterrows():
    university_name = row['大学名称']
    score_line = row['分数线']
    soft_score = row['软科评分']
    al_score = row['校友会总分']
    d1=score_line - 0.18 * soft_score - 540.25
    d2=al_score - 0.2 * score_line + 54.4
    if d1>0 and d2<0:
        low_cost_performance.append((university_name, score_line, soft_score, al_score))
    elif d1<0 and d2>0:
        high_cost_performance.append((university_name, score_line, soft_score, al_score))
    else:
        double_performance.append((university_name, score_line, soft_score, al_score))

def calculate_cost_performance1(row):
    score_line = row['分数线']
    soft_score = row['软科评分']
    return round(0.18 * soft_score + 540.25 - score_line,1)

def calculate_cost_performance2(row):
    score_line = row['分数线']
    al_score = row['校友会总分']
    return round(al_score - 0.2 * score_line + 54.4 ,1)

low_cost_performance_df = pd.DataFrame(low_cost_performance, columns=['大学名称', '分数线', '软科评分','校友会总分'])
high_cost_performance_df = pd.DataFrame(high_cost_performance, columns=['大学名称', '分数线', '软科评分','校友会总分'])
double_performance_df = pd.DataFrame(double_performance, columns=['大学名称', '分数线', '软科评分','校友会总分'])

# 计算性价比指数并添加到DataFrame中
low_cost_performance_df['性价比指数1'] = low_cost_performance_df.apply(calculate_cost_performance1, axis=1)
low_cost_performance_df['性价比指数2'] = low_cost_performance_df.apply(calculate_cost_performance2, axis=1)
high_cost_performance_df['性价比指数1'] = high_cost_performance_df.apply(calculate_cost_performance1, axis=1)
high_cost_performance_df['性价比指数2'] = high_cost_performance_df.apply(calculate_cost_performance2, axis=1)
double_performance_df['性价比指数1'] = double_performance_df.apply(calculate_cost_performance1, axis=1)
double_performance_df['性价比指数2'] = double_performance_df.apply(calculate_cost_performance2, axis=1)

#排序
low_cost_performance_df = low_cost_performance_df.sort_values(by='性价比指数1', ascending=True)
high_cost_performance_df = high_cost_performance_df.sort_values(by='性价比指数1', ascending=False)

with pd.ExcelWriter('性价比分析表格.xlsx') as writer:
    low_cost_performance_df.to_excel(writer, sheet_name='性价比低', index=False)
    high_cost_performance_df.to_excel(writer, sheet_name='性价比高', index=False)
    double_performance_df.to_excel(writer, sheet_name='两者皆有', index=False)
