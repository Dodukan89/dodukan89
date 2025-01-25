#Şifre oluşturucu (Googleden kat kat iyi :D!)
import random
import time
bUp = ["*","é","!","^","+","%","&","/","(",")","=","?","_","<",">","[","]","{","}","-",";",".",",","|","~","@","$","#","'","\\",":","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
bUl = int(input("Oluşacak random şifrenin uzunluğu kaç karakter olsun?"))
şifre = False
for i in range(bUl):
    if bUl <= 6:
        print("Eğer şifrenin güvenliği önemliyse, şifrenin uzunluğunu 6 karakterden fazla yapmalısın!")
        break
    else:
        print(bUp[random.randint(0,89)],end="")
        şifre = True
        time.sleep(0.1)
if şifre == True:
    print(" | İşte benzersiz şifren! Güvenliğin için bu şifreyi kimseyle paylaşma!")
