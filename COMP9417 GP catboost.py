# import packages
import pandas as pd
import numpy as np
import csv
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, cross_val_score
import matplotlib.pyplot as plt


# !pip install --user catboost
from catboost import CatBoostClassifier

# read the csv file
train = pd.read_csv('train.csv')

# check if the dataframe has missing value
has_missing_values = train.isna().any().any()

print("Has missing value?", has_missing_values)

# A check of the number of cases where the action is equal to 1 and the number of cases where it is equal to 0
print("Number of cases where Action is equal to 1: ",(train['ACTION']== 1).sum())
print("Number of cases where Action is equal to 0: ",(train['ACTION']== 0).sum())

# Separate out the x and y data sets
x = train.loc[:, train.columns != 'ACTION']
y = train['ACTION']
print(x.shape)
print(y.shape)

'''
Since the test dataset in Competition did not give real 'action' results,
the team used the training dataset as the experimental dataset and divided 20% of the test dataset.
The data other than the test dataset is 80% of the training dataset and 20% of the validation dataset.
'''
X_model, X_test, y_model, y_test = train_test_split(x, y, train_size=0.8, random_state=1234)
X_train, X_validation, y_train, y_validation = train_test_split(X_model, y_model, train_size=0.8, random_state=1234)
'''
Next, the CatBoostClassifier model is defined and trained on the prepared training and validation datasets 
using the model. The model is defined with the following parameters.

- iterations: integer value, indicating the number of iterations to be performed during training, default is 1000.
- random_seed: integer value, for the random seed generator.
- eval_metric: parameter specifies the metric used to evaluate the performance of the model during training.
- loss_function: The loss function, used to optimise the model. In this case, the CrossEntropy function is used.

and the parameters defined when training the model

- cat_features: Indexed list of category-based feature columns, default is empty.
- eval_set: The features and target variable data for the validation set, used to verify the performance of the model.
- verbose: The level of detail for printing the training process, default is 0 for no printing. 
The higher the value, the more detailed the information will be printed.

'''

model = CatBoostClassifier(
    iterations=2000,
    random_seed=1,
    loss_function = 'CrossEntropy',
    eval_metric='AUC'
)
model.fit(
    X_train, y_train,
    cat_features=list(range(0, X_train.shape[1])),
    eval_set=(X_validation, y_validation),
    verbose=50
)

# make the plot
# plt.plot(model.evals_result_['validation']['AUC'])
# plt.title('AUC Curve')
# plt.xlabel('Iterations')
# plt.ylabel('AUC')
# plt.show()

# get the feature table
model.get_feature_importance(prettified=True)

# The trained model was used to train the test dataset.
# The AUC and accuracy of the model on the test dataset were evaluated.
preds = model.predict(X_test)

auc = roc_auc_score(y_test, preds)
print("catboost AUC is :", auc)

acc = accuracy_score(y_test, preds)
print("catboost accuracy is :", acc)

# cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
train_roc_auc = cross_val_score(model, X_train, y_train, scoring='roc_auc', cv=kf, n_jobs=-1)


final_mean = train_roc_auc.mean()
print("final mean of AUC after cv is :", final_mean)