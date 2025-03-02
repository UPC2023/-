import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import linregress

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 不用楷体了
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

# 大学名称
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


# 显示图形
plt.tight_layout()
plt.show()
