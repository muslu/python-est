python-est
==========

Python ile EST bankalarının sanal pos uygulamaları


Zamanla tüm örnekleri girmeyi planlıyorum.

Şu an için çalışıyor ve diğer bankalar ile entegrasyon yaptıkça güncelleyeceğim.

Çok detaya girip kafa karıştırmadan direk eklenecek kodları yazıyorum.

Kendi projenize ekleyerek test edebilirsiniz.


Herhangi bir sorunda musluyuksektepe@gmail.com adresinden ulaşabilirsiniz.


mdStatus değerlerine göre hata ve onay açıklamaları

    if request.POST['mdStatus'] == "0":		Sonuc	=	"Onaylanmamış"
    if request.POST['mdStatus'] == "1":		Sonuc	=	"Başarılı"
    if request.POST['mdStatus'] == "2":		Sonuc	=	"Kart sahibi banka veya Kart 3D-Secure Üyesi Değil"
    if request.POST['mdStatus'] == "3":		Sonuc	=	"Kart prefixi 3D-Secure sisteminde tanımlı değil"
    if request.POST['mdStatus'] == "4":		Sonuc	=	"Authentication Attempt"
    if request.POST['mdStatus'] == "5":		Sonuc	=	"Sistem ulaşılabilir değil"
    if request.POST['mdStatus'] == "6":		Sonuc	=	"3D-Secure Hatası"
    if request.POST['mdStatus'] == "7":		Sonuc	=	"Sistem Hatası"
    if request.POST['mdStatus'] == "8":		Sonuc	=	"Geçersiz Kart"
    if request.POST['mdStatus'] == "9":		Sonuc	=	"Üye İşyeri 3D-Secure sistemine kayıtlı değil"
    
    
www.muslu.org


Test Kart bilgileri:
https://testsanalpos.est.com.tr/servlet/est3Dgate
Kart No:  4848480011226398 (Visa)
CV2:      000
Yıl:      14
Ay:       06
