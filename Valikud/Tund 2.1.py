﻿#Näidised:

#Ainult positiivsed arvud korrutame
# a=float(input("A: "))
# b=float(input("B: "))
# if a>0 and b>0: 
#     print(f"Korrutis võrdub: {a*b}")

# #Kas a on paaris või paaritu arv?
# if a%2==0 and a!=0:
#     print(f"Arv {a} on paaris.")
# elif a==0:
#     print(f"Arv {a} on määramatu.")
# else:
#     print(f"Arv {a} on paaritu.")

# #Ema-robot 5-, 4-, 3-, 2-, 1-
# try:
#     hinne=int(input("Mis hinne sai täna koolis? "))
#     if hinne in range(1,6):
#         print("Hinne: ")
#         if hinne==5:
#             print("Väga hea!")
#         elif hinne==4:
#             print("Hea!")
#         elif hinne==3:
#             print("Rahuldav!")
#         elif hinne==2 or hinne==1:
#             print("Mitte rahuldav")
#     else:
#         print("Ei ole hinne")
# except Exception as e:
#     print("Viga: ", e)

# nimi="PYTHON"
# print(nimi.isupper())
# if nimi.isupper():
#     print("Suured tähed.")
# else:
#     print("Ei ole kõik suured tähed.")


# #Ülesanne1
# nimi=input("Mis on sinu nimi? ")
# if nimi=="JUKU":
#     print("Lähme kinno!")
#     vanus=int(input("Kui vana sa oled? "))
#     if vanus<6:
#         print("Sulle pilet tasuta!")
#     elif vanus<14:
#         print("Sulle on vaja osta lastepilet!")
#     elif vanus<65:
#         print("Sulle on vaja osta täispilet!")
#     elif vanus>65:
#         print("Sulle on vaja osta sooduspilet!")
#     elif vanus<0 and vanus>100:
#         print("Viga andmed!")
# else:
#     print("Ma olen hõivatud!Mine kinno ise")

# #Ülesanne 2.2
# nimed = {"Kirill", "Nastja", "Arseni"}
# nimi1 = input("Sisesta esimese inimese nimi: ")
# nimi2 = input("Sisesta teise inimese nimi: ")
# nimi3 = input("Sisesta kolmanda isiku nimi: ")
# if (nimi1 in nimed) and (nimi2 in nimed) and (nimi3 in nimed) and nimi1!=nimi2 and nimi2!=nimi3 and nimi1!=nimi3:
#     print("Nad on pinginaabrid!")
# else:
#     print("Täna ei ole pinginaabrid!")

# #Ülesanne 3
# try:
#     a=float(input("Sisesta toa pikkus: "))
#     b=float(input("Sisesta toa laius: "))
#     if a>0 and b>0:
#         pindala=a*b
#         print(f"Põranda pindala on {pindala} ruutmeetri.")
#         remont=input("Kas soovid põrandat vahetada?")
#         if remont.lower() == "jah" :
#             hind=float(input("Sisesta põranda vahetuse hind: "))
#             if hind>0:

#                 koguhind=pindala*hind
#                 print(f"Põranda vahetamise hind on {koguhind} eurot. ")
#             else:
#                 print("Vale hind!")
#         else:
#             print("Remondi ei tehta.")
#     else:
#         print("Viga!")
# except:
#     print("Viga!")

# #Ülesanne 4
# alghind=float(input("Sisesta toode alghind: "))
# if alghind>700:
#     soodus=alghind*0.70
#     print(f"Soodus hind on {soodus} eurot.")
# else:
#     print("Soodustus ei kehti.")

# #Ülesanne 5
# try:
#     temp=float(input("Sisesta temperatuur: "))
#     if temp>18:
#         print("Temperatuur on üle 18, tuba on soe")
#     elif temp==18:
#         print("Temperatuur on täpselt 18, see on minimaalne toasoojus.")
#     else:
#         print("Temperatuur on alla 18, võib olla liiga külm.")
# except:
#     print("Viga!")


# #Ülesanne 6
# try:
#     pikkus=float(input("Siseta oma pikkus: "))
#     if pikkus>165:
#         print("Sa oled pikk")
#     elif pikkus==165
#         print("Sul on keskmine pikkus")
#     else:
#         print("Sa oled lühike")
# except:
#     print("Viga!Kirjuta oma pikkus")

# #Ülesanne 7
try:
    pikkus=float(input("Siseta oma pikkus: "))
    sugu=input("Sisita oma sugu: ").strip().lower()

    if pikkus>165:
        print("Sa oled pikk,", end=" ")
    elif pikkus==165:
        print("Sul on keskmine pikkus,", end=" ")
    else:
        print("Sa oled lühike,", end=" ")

        if sugu=="naine":
            print("Sa oled naine.")
        elif sugu=="mees":
            print("Sa oled mees.")
        else:
            print("Kirjuta sa oled mees või naine!!!!")

except ValueError:
    print("Viga!Kirjuta oma pikkus.")

#Ülesanne 8
