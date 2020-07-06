#menghitung faktorial di python

def faktorial(num):
    hasil=1
    for i in range(2, num+1):
        #print (i)
        #print(hasil, "*", i)
        hasil *= i
        #print("hasil:",hasil)
    return hasil

num= int(input("Bilangan :"))
print("Hasil faktorial : ",faktorial(num))
