#  Breast-Cancer (Predictive Analytics)
Phân tích dữ liệu liên quan về Ung Thư Vú tại Hoa Kỳ 

*** Thành viên thực hiện:*** 
- ** Hướng dẫn: Thầy Đinh Nguyễn Trọng Nghĩa**
- Ngô Huy Thắng - 09DHTH1 - HUFI

## Nội dung: 
Trích: This breast cancer databases was obtained from the University of Wisconsin Hospitals, Madison from Dr. William H. Wolberg.
Mở Đầu:Ung thư vú là nguyên nhân thứ hai gây tử vong do ung thư ở phụ nữ tại Hoa Kỳ,chỉ đứng sau ung thư phổi.
Trong thập kỉ qua số lượng bị cũng đã giảm đáng kể.Tuy nhiên điều quan trọng là phải tiếp tục thực hiện các 
tiến bộ trong cách thức chẩn đoán để phát hiện bệnh sớm giúp nâng cơ hội sống sót cho các bệnh nhân.

## Với bộ dự liệu được trích ra từ file .csv 
## Cùng xem qua một bài Phân tích nhỏ:

## Add Thu vien
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
## Thiết lập để pandas hiển thị tất cả các cột
pd.set_option('display.max_columns', None)
# Thiết lập để pandas hiển thị tất cả các dòng
pd.set_option('display.max_rows', None)

pd.set_option('display.float_format', lambda x:'%f'%x)

## Đặt tên lại cho các Header
col = ['id', 'Clump Thickness', 'Uniformity of Cell Size', 
       'Uniformity of Cell Shape', 'Marginal Adhesion', 
       'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
       'Normal Nucleoli', 'Mitoses', 'Class']

## Đọc dữ liệu
data = pd.read_csv('D:\deaktop\hoc tap\year 3 - hk1\predictive analytics\BreastCancer/breast-cancer-wisconsin.csv',names=col,header=None)
 
## Xem xét kích thước dữ liệu
print('KICH THUOC DU KIEU')
print(len(data))
print(len(data.columns))
print('Xem du lieu khi da them header va ten ')
print(data.iloc[:3])

## Dem Bare Nuclei
print('Diem Bare Nuclei Phan Loai cac truong hop tu 1 - 10')
print(data['Bare Nuclei'].value_counts())

## Ta thấy trong Bare Nuclei có ? gán 0 cho nó dễ dũ liêu không bị sai số

print('Ta thấy trong Bare Nuclei có ? gán 0 cho nó dễ dũ liêu không bị sai số')
bare_index = data[data['Bare Nuclei'] == '?'].index
bare = np.array(bare_index)
bare1 = data.loc[bare,'Bare Nuclei'] == 0
print(bare1)

## Đếm Class số lành tính và ác tính 

print('đếm lành tính và ác tính')
print(data['Class'].value_counts())
## Tính % cho Class
print('Tính % cho Class')
print(data['Class'].value_counts(normalize=True).sort_index())

## Chuyển đổi Thành 1 - 0

print('Chuyển đổi Thành 1 - 0 cho Class')
data['Class'] = data['Class'] / 2 - 1
print(data['Class'].value_counts())
 
## Xem dữ liệu Info
print('Xem dữ liệu Info')
data.info()

## Vẽ Biễu Đồ cho Class

## Chuyển các thuộc tính sang dạng số
data['Class'] = pd.to_numeric(data['Class'], errors='coerce')
## Đồ thị ước lượng số lượng benign and malignant trong 699
sns.distplot(data['Class'].dropna(), kde=False)
plt.xlabel('Benign                                                                     Malignant')
plt.ylabel('Số lượng')
plt.title('Đồ thị uớc lượng benign and malignant trong 699')
plt.show()

## Vẽ Biễu Đồ cho Bare Nuclei

## Chuyển các thuộc tính sang dạng số
data['Bare Nuclei'] = pd.to_numeric(data['Bare Nuclei'], errors='coerce')
## Loại bỏ các giá trị ? có 16 trường hợp
data.replace('?',-9999, inplace = True)

## Đồ thị ước lượng Bare Nuclei
sns.distplot(data['Bare Nuclei'].dropna(), kde=False)
plt.ylabel('Số lượng')
plt.title('Đồ thị ước lượng Bare Nuclei')
plt.show()


**feedback** or **support** at [facebook/me](https://www.facebook.com/profile.php?id=100039855851785).
