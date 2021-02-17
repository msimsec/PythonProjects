from selenium import webdriver
from instagramUserInfo import  username, password
import time
import instaloader

## Birinci Bölüm
driver = webdriver.Chrome() #Chrome Webdriver tanımı yapılıyor
url = "https://www.instagram.com/accounts/login/"
driver.get(url) #web adresi çağırılıyor.
time.sleep(2) #sayfanın tam açılması için 2sn bekleniyor.

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
#Açılan sayfadaki kullanıcı adı alanının xpath karşılığı alınıyor ve username buraya gönderiliyor
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)
#Açılan sayfadaki kullanıcı adı alanının xpath karşılığı alınıyor ve password buraya gönderiliyor
driver.find_element_by_css_selector('button[type=submit]').click()
#login butonunun css type değeri [] arasına girilerek click tıklama fonksiyonu tetiklenerek sayfaya giriş yapılıyor.

## İkinci Bölüm
time.sleep(3)
url = "https://www.instagram.com/"+username+"/followers/" #kullanıcının profil sayfası
driver.get(url) # profil sayfası çağırılıyor.
time.sleep(2)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click() # followersa tıklanıyor
time.sleep(2)

for i in range(1,4): # Folowers listesinde en başta bulunan ilk 3 satır çekilecek
   followers = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[%s]' % i)
   # açılan javascript bloğunun xpath bilgisi alınarak tüm satıra erişiliyor
   driver.execute_script("arguments[0].scrollIntoView();", followers)
   # followers elementi sayfa da görülmeyene kadar scroll sorgusu çalıştırılarak tüm satırların okunması sağlanıyor
   time.sleep(1)
   text = followers.text # gelen değerin text kısmı alınarak bir değişkene atanıyor
   list = text.split() #Her boşluk gördüğünde de karakter dizelerini ayırır. list değişkenine atar.
   print('{}:{}'.format(i, list[0])) #listenin ilk sutünü olan kullancı adı yazdırılır. ikinci sütün kullanıcı full isimdir.

## Üçüncü Bölüm
   ins = instaloader.Instaloader() # ins adında bir obje yaratılıyor.
   profile_Name = list[0] # değişkenin ilk indisinde bulunan kullanıcı adı değeri profile_Name değişkenine atanıyor.
   ins.download_profile(profile_Name, profile_pic_only = True)
   # download_profile fonk aracılığıyla aldığı kullanıcı adı paremetrese ait olan kullanıcının fotoğrafınıww indirme işlemini gerçekleştiriyor.


