# Open csv file

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#OpenFile
#Remove the first row and column of these non-numeric elements
def readtrain():
    raw = pd.read_csv('train.csv')
    raw = np.array(raw)
    #raw = np.delete(raw, 0 , axis = 0)
    feature = raw [:,1 : ]  #不包含 action的所有值
    action_result = raw[:,0]
    return feature , action_result

#ReadFile
#Remove the first row and column of these non-numeric elements
def readtest():
    raw = pd.read_csv('test.csv')
    raw = np.array(raw)
    id = raw[:,0]
    feature = raw[:, 1:] #不包含id 的所有值
    return id ,feature

# Missing value query, if there is, delete
#find the missing value
def find_missing_value():
    feature, action_result = readtrain()
    missing_values = np.isnan(feature)
    if not np.all(missing_values != False):
        print("There is no missing value")
    else:
        print ("There are missing values")

#find_missing_value()

#there is no missingvalue

# find the outliervalue
#Find Missing Values

def find_outlier_values():
    feature, action_result = readtrain()
    fig,ax = plt.subplots()
    ax.boxplot(feature)
    plt.show()

#find_outlier_values()

#as the pic shows，only line 7 and line 8
# have no outlier values
# However consider other line are id
#some it is ok that some values are out.

#是否需要概率分布和直方图？
#if needed,code with yourself.

# def dis_and_histograms():
#     feature, action_result = readtrain()
#     # 绘制概率密度函数
#     sns.kdeplot(feature["column_name"], shade=True)
#     plt.show()
#     # 绘制直方图
#     sns.histplot(feature["column_name"], bins=20)
#     plt.show()
#
# dis_and_histograms()

# Correlation check
#Target variable check


#Normalize, all of them
from sklearn.preprocessing import MinMaxScaler

# raw = pd.read_csv('test.csv')
# data= np.array(raw)
#
#np.savetxt('normalized_test_data.csv', data,delimiter = ',')
#Scaler = MinMaxScaler()
#normalized_data = Scaler.fit_transform(data)
#np.savetxt('normalized_test_data.csv', data,delimiter = ',')
#np.savetxt('normalized_test_data.csv', normalized_data,delimiter = ',')

data = pd.read_csv('train.csv')

# corr_matrix = np.corrcoef(data.T)
# sns.heatmap(corr_matrix, annot=True,  fmt = '.2f',cmap='YlGnBu')
# plt.title('Correlation Matrix')
# plt.xlabel('Variables')
# plt.ylabel('Variables')
#
# plt.show()
fig, ax = plt.subplots(nrows=1, ncols=6, figsize=(40, 20))

data["RESOURCE"].hist(ax=ax[0], bins=10)
ax[0].set_title("RESOURCE")
ax[0].tick_params(axis='x', labelrotation=45)
ax[0].xaxis.set_tick_params(labelsize=8)

data["MGR_ID"].hist(ax=ax[1], bins=10)
ax[1].set_title("MGR_ID")
ax[1].tick_params(axis='x', labelrotation=45)
ax[1].xaxis.set_tick_params(labelsize=8)

data["ROLE_ROLLUP_1"].hist(ax=ax[2], bins=10)
ax[2].set_title("ROLE_ROLLUP_1")
ax[2].tick_params(axis='x', labelrotation=45)
ax[2].xaxis.set_tick_params(labelsize=8)

data["ROLE_ROLLUP_2"].hist(ax=ax[3], bins=10)
ax[3].set_title("ROLE_ROLLUP_2")
ax[3].tick_params(axis='x', labelrotation=45)
ax[3].xaxis.set_tick_params(labelsize=8)

data["ROLE_DEPTNAME"].hist(ax=ax[4], bins=10)
ax[4].set_title("ROLE_DEPTNAME")
ax[4].tick_params(axis='x', labelrotation=45)
ax[4].xaxis.set_tick_params(labelsize=8)

data["ROLE_TITLE"].hist(ax=ax[5], bins=10)
ax[5].set_title("ROLE_TITLE")
ax[5].tick_params(axis='x', labelrotation=45)
ax[5].xaxis.set_tick_params(labelsize=8)

plt.subplots_adjust(wspace=0.5, left=0.1, right=0.9)
plt.show()
