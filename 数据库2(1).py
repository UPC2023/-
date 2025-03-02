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
