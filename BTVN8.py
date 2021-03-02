# Add thu vien
import numpy
import pandas as pd
import statsmodels.api as sm
import seaborn
import statsmodels.formula.api as smf 
import matplotlib.pyplot as plt
%matplotlib inline
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 200
pd.set_option('display.float_format', lambda x:'%.2f'%x)
# Đặt tên lại cho các Header
col = ['id', 'ClumpThickness', 'UniformityofCellSize', 
        'UniformityofCellShape', 'MarginalAdhesion', 
        'SingleEpithelialCellSize', 'BareNuclei', 'BlandChromatin',
        'NormalNucleoli', 'Mitoses', 'Class']
# Đọc dữ liệu
data = pd.read_csv('D:\deaktop\hoc tap\year 3 - hk1\predictive analytics\BreastCancer/breast-cancer-wisconsin.csv',names=col,header=None)
#Làm sạch dữ liệu 
data['ClumpThickness'] =pd.to_numeric(data['ClumpThickness'], errors='coerce')
data['UniformityofCellSize'] = pd.to_numeric(data['UniformityofCellSize'], errors='coerce')
data['UniformityofCellShape'] = pd.to_numeric(data['UniformityofCellShape'], errors='coerce')
data['MarginalAdhesion'] = pd.to_numeric(data['MarginalAdhesion'], errors='coerce')
data['SingleEpithelialCellSize'] = pd.to_numeric(data['SingleEpithelialCellSize'], errors='coerce')
data['BareNuclei'] = pd.to_numeric(data['BareNuclei'], errors='coerce')
data['BlandChromatin'] =pd.to_numeric(data['BlandChromatin'], errors='coerce')
data['NormalNucleoli'] = pd.to_numeric(data['NormalNucleoli'], errors='coerce')
data['Mitoses'] = pd.to_numeric(data['Mitoses'], errors='coerce')
data['Class'] = pd.to_numeric(data['Class'], errors='coerce')
# căn chỉnh dữ liệu 
data['ClumpThickness_c'] = (data['ClumpThickness'] - data['ClumpThickness'].mean())
data['Mitoses_c'] = (data['Mitoses'] - data['Mitoses'].mean())
#chuyển dữ liệu về 0 - 1
class1 =  data['Class'].replace((2,4), (0,1))
# Mô hình hồi quy logistic

sub1 = data[['ClumpThickness_c', 'Class']].dropna()

log_reg = smf.logit(formula = 'class1 ~ ClumpThickness_c   ', data = sub1).fit()

print(log_reg.summary())


### Đánh giá mô hình logistic
X = sub1[['ClumpThickness_c']]
y = class1

# Chia dữ liệu thành 2 tập: train và test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)

#log_reg = sm.Logit(y_train, X_train).fit()

yhat = log_reg.predict(X_test) 
prediction = list(map(round, yhat))


from sklearn.metrics import (confusion_matrix, accuracy_score)


cm = confusion_matrix(y_test, prediction)
print ("Confusion Matrix : \n", cm)

print('Test accuracy = ', accuracy_score(y_test, prediction))