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
#print (data['ClumpThickness_c'].mean()) 
data['Mitoses_c'] = (data['Mitoses'] - data['Mitoses'].mean())
#rint (data['Mitoses_c'].mean()) 
#chuyển dữ liệu về 0 - 1
class1 =  data['Class'].replace((2,4), (0,1))
#print(class1.head(10))
reg2 = smf.ols('class1 ~ Mitoses_c + ClumpThickness_c', data).fit()
#print (reg2.summary())


#dặt dữ liệu
sub1 = data[['Class', 'UniformityofCellSize', 'UniformityofCellShape']].dropna()
#vễ biểu đồ biểu hiện tỉ lệ 
scat1 = seaborn.regplot(x="UniformityofCellSize", y="UniformityofCellShape", scatter=True, data=sub1)
scat1 = seaborn.regplot(x="UniformityofCellSize", y="UniformityofCellShape", scatter=True, order=2, data=sub1)
plt.xlabel('Tỷ lệ đồng nhất kích thước ô')
plt.ylabel('Tỷ lệ đồng nhất hình dạng tế bào')
#căn chỉnh dữ liệu 
sub1['UniformityofCellSize_c'] = (sub1['UniformityofCellSize'] - sub1['UniformityofCellSize'].mean())
sub1['UniformityofCellShape_c'] = (sub1['UniformityofCellShape'] - sub1['UniformityofCellShape'].mean())
sub1[["UniformityofCellSize_c", "UniformityofCellShape_c"]].describe()
#phan tích
reg3 = smf.ols('class1  ~ UniformityofCellSize_c + I(UniformityofCellSize_c**2) + UniformityofCellShape_c', data=sub1).fit()
print (reg3.summary())









#sub1['ClumpThickness_c'] = (sub1['ClumpThickness'] - sub1['ClumpThickness'].mean())