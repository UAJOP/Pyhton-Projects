import pandas as pd
# Pandas kütüphanesi
import seaborn as sns
# Seaborn Kütüphanesi
import numpy as np
# Numpy Kütüphanesi
import matplotlib.pyplot as plt
# Mathplot kütüphanesi
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# Veri setimizde kullanacağımız modeli eğitmek için gerekli kütüphane.
from sklearn.linear_model import LinearRegression
# Veri setimizde kullanacağımız model.
from sklearn.metrics import mean_absolute_error, mean_squared_error
# Kurduğumuz model ne kadar iyi olduğunu test etmek için gerekli kütüphane.

from sklearn.preprocessing import OneHotEncoder
# Veri setinde değişken dönüşümü için kullalıcak kütüphane.
from sklearn.impute import SimpleImputer
# -TR- Veri analizi için gerekli kütüphanelirimizi yüklüyoruz
# -EN- We are installing the necessary libraries for data analysis.

df = pd.read_csv("cars.csv")

# -TR- İnceleyeceğimiz Veri Setini konsolumuzda analiz edebilmek için bir değişkene atıyoruz.
# -EN- We are assigning the dataset we will analyze to a variable in our console.

print(df.head())
# -TR- Veri seti düzgün yüklenmişmi diye bir kontrol yapıyoruz ve veri setinde ki ilk 5 veriyi ekrana yazdırıyoruz.
# -EN- We are checking if the dataset has been loaded correctly and printing the first 5 rows of the dataset to the screen.


print(df.info())
# -TR- Veri seti hakkında bilgi edinmek ve analiz edebilmek için info methodunu çağırıyoruz.
# -EN- We are calling the info method to get information about the dataset and analyze it.

print(df.describe().T)
# -TR- Veri setinde ki kolonları ve sütünları analiz edebilmek için describe methodunu çağıyoruz ve daha düzgün bir tablo çıktısı için .T methodunu kullanıyoruz.
# -EN- We are calling the describe method to analyze the columns and rows in the dataset, and we are using the .T method for a more organized table output.

cat_col = [col for col in df.columns if df[col].dtypes in ["category", "object"]]
print(f"Kategorik değerler : {cat_col}")
# -TR- Kategorik değişkenlerimizi sıralamak için  list comprehension özelliğini kullanıp veri setindeki bütün kolonları tarayıp veri türü Category veya object olanları cat_col adlı bir değişkene atıyoruz.
# -EN- We are using list comprehension to iterate through all columns in the dataset and assign those with data type 'Category' or 'object' to a variable called cat_col for sorting categorical variables.

for col in cat_col:
  print(f" {col}, sınıf değerleri :{df[col].value_counts()}")
# -TR- Kategorik değişkenlerimizin sınıf değerlerini bulmak için bir for döngüsü yardımı ile sınıf değerlerini value_counts methodu ile ekrana yazdırıyoruz.
# -EN- We are using a for loop to iterate through the categorical variables and printing the class values to the screen using the value_counts method.

num_col = [col for col in df.columns if df[col].dtypes in ["float64", "int64"]]
print(f" Sayısal değerler : {num_col}")
# -TR- Sayısal değişkenlerimizi bulmak için  list comprehension yöntemi ile veri türleri Float64 veya Int64 olan değişkenleri num_col adlı değişkene atıyoruz.
# -EN- We are using list comprehension to iterate through all columns in the dataset and assign those with data type 'Float64' or 'Int64' to a variable called num_col for finding numerical variables.

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["float64", "int64"]]
print(num_but_cat)

def remove_outliers(df,column):
    Q1 = df[column].quantile(0.25)
    # -TR- Q1 Veri setinin sıralandığında alt %25'lik dilimi temsil eder.
    # -EN- Q1 represents the bottom 25% of the data set when sorted.
    Q3 = df[column].quantile(0.75)
    # -TR- Q3 Veri setinin sıralandığında üst %25'lik dilimi temsil eder.
    # -EN- Q3 represents the top 25% of the data set when sorted.
    IQR = Q3-Q1
    # -TR- IQR Veri setinin merkezi eğilimini ve dağılımını ölçmek için kullanılır.
    # -EN- IQR is used to measure the central tendency and spread of the data set.
    low = Q1-1.5*IQR
    # -TR- Low alt sınırı temsil eder.
    # -EN- Low represents the lower boundary.
    high = Q3+1.5*IQR
    # -TR- High üst sınırı temsil eder.
    # -EN- High represents the upper boundary.
    kosul = ((df[column] >= low) & (df[column] <= high))
    # -TR- Alt sınır ve üst sınır arasında ki değerlerimizi ayıklamak için bir kosul yazıyoruz.
    # -EN- We write a condition to filter out the values between the lower and upper boundaries.
    clear_df = df[kosul]
    # -TR- Veri setimizi aykırı değerlerden kurtarmak için bu koşulu kullanıyoruz.
    # -EN- We use this condition to remove outliers from our data set.
    return clear_df
    # -TR- Geriye temiz bir veri setini döndürerek fonsiyonumuzu bitiriyoruz.
    # -EN- Finally, we return a clean data set.

# -TR- Bir fonksiyon oluşturup bu fonksiyon içinde aykırı değer analizi gerçekleştiriyoruz.
# -EN- We are creating a function to perform outlier analysis and removing the outliers within this function.

for col in num_col:
  df = remove_outliers(df, col)

# -TR- Oluşturduğumuz aykırı değerleri temizleme fonksiyonunu, veri setimizde ki bütün sayısal değişkenlerde aykırı değerleri temizlemek için bir for döngüsü açıyoruz.
# -EN- We open a for loop to clean outliers from all numerical variables in our dataset using the outlier removal function we created.

print(df.describe().T)
# -TR- Yaptığımız işlemler doğru sonuç alabildikmi diye veri setimizi incelemek için describe methodunu çağırıyoruz ve ekrana yazdırıyoruz.
# -EN- We call the `describe` method to examine our dataset and print it to the screen to see if our operations yielded correct results.

print(df.isnull().sum())
# -TR- Veri setimizde ki değişkenlerde boş değer alan bir değişken var mı diye kontrol etmek için .isnull() methodunu kullanıyoruz ve kaç tane boşluk olduğunu bulmak için .sum() meyhodunu kullanıyoruz.
# -EN- To check if there are any missing values in our dataset, we use the `.isnull()` method, and to find out how many missing values there are, we use the `.sum()` method.

for col in num_col:
  if df[col].isnull().any():
    df[col].fillna(df[col].mean(), inplace=True)
    print("Boşluk temizlendi")
# -TR- Boşluk analizimizi yaptıktan sonra bir for döngüsü ile boş değer alan değişkenlerimizi ortalama değerler ile dolduruyoruz ve veri setinde ki boşlukları temizliyoruz.
# -EN- After conducting our missing value analysis, we fill the missing values in our variables with the mean values using a for loop and clean the missing values in the dataset.

print(df.isnull().sum())
# -TR- Yaptığımız işlemden doğru sonuç alabildikmi diye tekrar boşluk analizi yapıyoruz.
# -EN- We conduct another missing value analysis to verify if our operations yielded correct results.


sns.scatterplot(x='Power', y='Price', hue='Transmission', data=df)
plt.title('Transmission ve Price Arasındaki İlişki')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Brand', data=df)
plt.title('Marka Dağılımı')
plt.xlabel('Marka')
plt.ylabel('Araç Sayısı')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(x='Year', data=df)
plt.title('Yıl Dağılımı')
plt.xlabel('Yıl')
plt.ylabel('Araç Sayısı')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 8))
df['Fuel_Type'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Yakıt Türü Dağılımı')
plt.ylabel('')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Transmission', data=df)
plt.title('Vites Türü Dağılımı')
plt.xlabel('Vites Türü')
plt.ylabel('Araç Sayısı')
plt.show()

plt.figure(figsize=(8, 8))
df['Owner_Type'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Sahip Türü Dağılımı')
plt.ylabel('')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Fuel_Type', hue='Transmission', data=df)
plt.title('Yakıt Türüne Göre Vites Türü Dağılımı')
plt.xlabel('Yakıt Türü')
plt.ylabel('Araç Sayısı')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Year', hue='Fuel_Type', data=df)
plt.title('Yıl ve Yakıt Türü Dağılımı')
plt.xlabel('Yıl')
plt.ylabel('Araç Sayısı')
plt.xticks(rotation=45)
plt.legend(title='Yakıt Türü', loc='upper right')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='Brand', hue='Transmission', data=df)
plt.title('Marka ve Vites Türü Dağılımı')
plt.xlabel('Marka')
plt.ylabel('Araç Sayısı')
plt.xticks(rotation=45)
plt.legend(title='Vites Türü', loc='upper right')
plt.show()


models = df['Model'].unique()
# Her bir model için benzersiz bir sayı atayacak bir sözlük oluşturun
model_map = {model: i for i, model in enumerate(models)}
# Model sütununu sayısal türe dönüştürün
df['Model'] = df['Model'].map(model_map)

brands = df['Brand'].unique()
brand_map = {brand: i for i, brand in enumerate(brands)}

# Brand sütununu sayısal türe dönüştür
df['Brand'] = df['Brand'].map(brand_map)

df['Fuel_Type'] = df['Fuel_Type'].map({'Petrol': 0, 'Diesel': 1})
df['Transmission'] = df['Transmission'].map({'Manual': 0, 'Automatic': 1})
df['Owner_Type'] = df['Owner_Type'].map({'First': 0, 'Second': 1, 'Third': 2})

X = df[['Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power', 'Seats', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Brand','Model']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


MAE = mean_absolute_error(y_test, y_pred)

print(f"Ortalama Mutlak Hata : {MAE}")

MSE = mean_squared_error(y_test, y_pred)

print(f"Ortalama Kare Hata : {MSE}")

RMSE = np.sqrt(MSE)

print(f"Kök Ortalama Kare Hata : {RMSE}")

print("Tahmin Sonuçları:")
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(predictions_df)

results = pd.DataFrame({
    'Actual': [2200000, 550000, 3200000, 1000000, 1500000, 600000, 1800000, 1800000, 3000000, 650000, 700000, 700000, 650000, 1600000, 2700000],
    'Predicted': [2.367836e+06, 3.868534e+05, 2.981689e+06, 1.503816e+06, 1.828165e+06, 5.867121e+05, 1.791424e+06, 1.571984e+06, 2.391514e+06, 8.891713e+05, 1.054986e+06, 9.903395e+05, 6.237287e+05, 2.138442e+06, 2.237813e+06]
})

# Sonuçları göster
print("Tahmin Sonuçları:")
print(results.to_string(index=False))


new_data = pd.DataFrame({
    'Year': [2019],
    'Kilometers_Driven': [50000],
    'Mileage': [15],
    'Engine': [1500],
    'Power': [120],
    'Seats': [5],
    'Fuel_Type': [0],
    'Transmission': [0],
    'Owner_Type': [0],
    'Brand': [1],
    'Model': [2]
})

prediction = model.predict(new_data)
print("Tahmin edilen fiyat:", prediction)




