# decorators :

# var olan fonksiyonlara özellikler eklemeya yarar.

# örneğin yağtığımız uygulamada 100 ade fonksyion çalştığını varsayalım. bu fonksiyonların hangisi kaç sn çalştı onu bulmak için decorators kullanabiliriz.

def dec(f):                                                 # decoratorler içerisine fonksiyon alırlar
    def wrapper():                                          # wrapper fonksiyonunu oluşturduk
        print("fonksiyon çalışmadan önceki işlemler")       # wrapper fonksiyonu çalışmaya başladı ancak decorator içerisinde parametre olarak tanımlanan fonksiyon henüz çalışmadı
        f()                                                 # decorator de parametre olarak verilen fonksyion çakıştırıldı.
        print("fonksiyon çalştıktan sonraki işlemler")      # decoratorde parametre olarak verilen fonksyionun yapması gereken işlemler yapıldı
    return wrapper                                          # decorator fonksyionu çalışmasını tamamladı, sonuç olarak wrapper fonksiyonunun kendisini göndürmüş oldu.

@dec
def fonksiyon():                                            # standart bir fonksiyon tanımladık.
    print("fonksiyon çalışıyor...")                         # fonksiyon çağırıldığı zaman ne yapacaksa onu yapacak.

fonksiyon()

# fonksiyon çalışmadan önceki işlemler
# fonksiyon çalışıyor...
# fonksiyon çalştıktan sonraki işlemler


# girilen listedeki elemanların karelerini alıp ekrana bastıran bir fonksiyon yazalım


def karelerini_al(liste):
    for i in liste:
        print(i*i)

karelerini_al([3,4,5,6])                        # / 9 16 25 36 

karelerini_al([1,2,3,4,5])                      # / 1 4 9 16 15

# girilen listedeki elemanların kuplerini alıp ekrana bastıran bir fonksiyon yazalım

def kupleri_al(liste):
    for j in liste:
        print(j**3)
    
kupleri_al([1,2,3,4])                           # / 1 8 27 64


# karelerini_al ve kupleri_al fonksiyonlarının zamanlarını hesaplamak için decorator den faydalanalım
import time
def dec(fonk):                              # yazılan decratorsler sadece bu fonksiyon için değil genel kullanım içindir.
    def wrapper(*args,**kwargs):            # tam olarak içerine kaç tane parametre geleceğini kestiremediğimiz için işimizi garantiye alıp *args , **kwargs parametrelerini kullandık.
        baslangic = time.time()
        fonk(*args,**kwargs)
        bitis = time.time()
        print("işlem {} saniye sürdü".format(bitis-baslangic))
    return wrapper

@dec
def karelerini_al(liste):
    for i in liste:
        print(i*i)
@dec
def kupleri_al(liste):
    for j in liste:
        print(j**3)

karelerini_al([1,2,3,4,5,6,7])

kupleri_al([1,2,3,4,5,6,7])




