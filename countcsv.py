# -*- coding: utf-8 -*-

import os
import pandas as pd

dir_path = './data20210906/'
output_file = 'counts.csv'

#### 循环读取csv文件
data_list = []
for file_name in os.listdir(dir_path):
    ## 若 包含历史输出 或 不是csv文件 则跳过该文件
    if file_name == output_file or not file_name.endswith('.csv'):
        continue
    data = pd.read_csv(dir_path + file_name)
    data_list.append(data)

#### 合并数据
data = pd.concat(data_list)

#### 分组计数
df = data['category'].str.split('/', expand= True)
df.columns = ['level_1', 'level_2', 'level_3']
df['count'] = 0
dd = df.groupby(['level_1', 'level_2', 'level_3']).count()

#### 输出结果
dd.to_csv(dir_path + output_file)
