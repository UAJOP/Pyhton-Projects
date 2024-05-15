import pandas as pd
# Pandas kütüphanesi
import seaborn as sns
# Seaborn Kütüphanesi
import numpy as np
# Numpy Kütüphanesi
import matplotlib.pyplot as plt
# Mathplot kütüphanesi
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split
# Veri setimizde kullanacağımız modeli eğitmek için gerekli kütüphane.
from sklearn.linear_model import LinearRegression
# Veri setimizde kullanacağımız model.
from sklearn.metrics import mean_absolute_error, mean_squared_error
# Kurduğumuz model ne kadar iyi olduğunu test etmek için gerekli kütüphane.

from sklearn.preprocessing import OneHotEncoder

# Veri setini yükleme ve ön işleme adımları
df = pd.read_csv("2018-2019_Daily_Attendance_20240429.csv")

# Aykırı değerleri temizleme fonksiyonu
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    low = Q1 - 1.5 * IQR
    high = Q3 + 1.5 * IQR
    kosul = ((df[column] >= low) & (df[column] <= high))
    clear_df = df[kosul]
    return clear_df

num_col = [col for col in df.columns if df[col].dtypes in ["float64", "int64"]]
for col in num_col:
    df = remove_outliers(df, col)

for col in num_col:
    if df[col].isnull().any():
        df[col].fillna(df[col].mean(), inplace=True)



# Özellikleri ve hedef değişkeni seçme
X = df[['Enrolled', 'Absent', 'Present', 'Released']]
y = df['Date']



# Eğitim ve test kümelerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Model oluşturma ve eğitme
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Hata metriklerini hesaplama
MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)

# Sonuçları yazdırma
print(f"Ortalama Mutlak Hata : {MAE}")
print(f"Ortalama Kare Hata : {MSE}")
print(f"Kök Ortalama Kare Hata : {RMSE}")
