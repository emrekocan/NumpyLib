import numpy as np

#1 - (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturma.
result = np.array([10,15,30,45,60])

#2 - (5-15) arasaındaki sayılarla numpy dizisi oluşturma.
result = np.arange(5,15)

#3 - (50-100) arasında 5'er artan numpy dizisi oluşturma.
result = np.arange(50,100,5)

#4 - 10 elemanlı sıfırlardan oluşan bir dizi oluşturma.
result = np.zeros(10)

#5 - 10 elemanlı birlerden oluşan bir dizi oluşturma.
result = np.ones(10)

#6 - (0-100) arasında eşit aralıklı 5 sayı üretin.
result = np.linspace(0,100,5)

#7 - (10-30) arasında rastgele 5 tane tamsayı üretin.
result = np.random.randint(10,30,5)

#8 - [-1 ile 1] arasında 10 sayı üretin.
result = np.random.randn(10)

#9 - (3*5) boyutlarında (10-50) arasında rastgele bir matris üretin.
#result = np.random.randint(10,50,15).reshape(3,5)

#10 - Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.
matris = np.random.randint(10,50,15).reshape(3,5)
#rowTotal = matris.sum(axis = 1)
#colTotal = matris.sum(axis = 0)
print(matris)
#print(rowTotal)
#print(colTotal)

#11 - Üretilen matrisin en büyük, en küçük ve ortalaması nedir?
result = matris.max()
result = matris.min()
result = matris.mean()

#12 - Üretilen matrisin en büyük değerinin indeksi kaçtır?
result = matris.argmax()
result = matris.argmin()

#13 - (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
arr = np.arange(10,20)
print(arr)

result = arr[0:3]



print(result)