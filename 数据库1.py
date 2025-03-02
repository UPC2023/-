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

# 根据用户输入执行相应操作
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

file="rank2021"
df = pd.read_sql_query(f"SELECT * FROM {file}", conn)
df.to_excel("大学排行榜校友会2021.xlsx", index=False)

# 关闭数据库连接
conn.close()
