def HemenAl(request, idsi):
    
    urun_detayi		=    	Urun.objects.get(id=idsi)
    
    
    import base64, hashlib

    oid			=	''.join([random.choice(string.digits + string.letters) for i in range(0, 10)])
    rnd			=	''.join([random.choice(string.digits + string.letters) for i in range(0, 30)])
    
    amount		= 	urun_detayi.Fiyat         # Islem tutari

    taksit 		= 	"12"         # taksit sayisi
    
    clientId		=	str(settings.__getattr__("CLIENTID"))
    okUrl		=	str(settings.__getattr__("OKURL"))
    failUrl		=	str(settings.__getattr__("FAILURL"))
    islemtipi		=	str(settings.__getattr__("ISLEMTIPI"))
    storekey		=	str(settings.__getattr__("STOREKEY"))
    

    hashstr = clientId + oid + str(amount).replace(',','.') + okUrl + failUrl + islemtipi + taksit  + rnd + storekey
    
    hashi = base64.b64encode(hashlib.sha1(hashstr).digest())
    
    
    return render_to_response(
    'est.html', 
    
    {'hashi':hashi,
    'oid':oid,
    'rnd':rnd,
    'amount':str(amount).replace(',','.'),
    'taksit':taksit,
    'hashi':hashi,
    'clientId':clientId,
    'okUrl':okUrl,
    'failUrl':failUrl,
    'storekey':storekey}, 
    
    context_instance=RequestContext(request))



def PayOdeme(request):       #~ Cum 24 Oca 2014 15:40:54 EET  - Muslu YÜKSEKTEPE

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



    if request.POST['mdStatus'] != "1":	
	Sonuc = Sonuc + " " + str(request.POST['mdErrorMsg'])
	

    return render_to_response('estsonuc.html', {'Sonuc':Sonuc,}, context_instance=RequestContext(request))
