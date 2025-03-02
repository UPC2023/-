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
double_performance_df =  double_performance_df.sort_values(by='性价比指数1', ascending=False)
with pd.ExcelWriter('性价比分析表格.xlsx') as writer:
    low_cost_performance_df.to_excel(writer, sheet_name='性价比低', index=False)
    high_cost_performance_df.to_excel(writer, sheet_name='性价比高', index=False)
    double_performance_df.to_excel(writer, sheet_name='两者皆有', index=False)
