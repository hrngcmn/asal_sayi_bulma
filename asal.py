a=int(input("bir sayi giriniz: "))
if a !=2 :# 2 sayısı asal olduğu bilinmelidir.
              #girilen sayı 2 den farklı bir değerdeyse if çalışır.
    for i in range(2, a):
            #rangenin sağındaki eleman sıralmaya dahil olmayacaktır.
            #  örneğin a nın değeri 5 olsun diyelim.
        if a % i == 0:             # 5 mod 2 !=0
                                #5 mod 3 !=0
                             #5 mod 4 !=0 sayma biter  (i=4 değerinde.) .
            break  # Eğer sıfıra eşitse for döngüsünden dan çık.
            # Girilen değer örneğin 9 olaydı  9%3 olduğunda 8. satırdaki kod çalıştığında i=3 değerinde kalırdı

    if a - 1 == i: #a=5 durumuna göre 5-1 = 4 fordaki sayılardan hiçbirine bölünmediğinden dolayı asal sayıdır.
            print(a, end=" asal sayısır.")
    else:    #Eğer 9-1=3 durumunda fordaki sayılardan birisine bölündüğü için asal DEGİLDİR.
            print(a, end=" asal değildir.")
if a == 2: # Girilen sayı 2 ise direk asal yazar.
     print(a,"asal sayıdır.")

