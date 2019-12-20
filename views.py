def HemenAl(request, idsi):
    
    	urun_detayi		=    	Urun.objects.get(id=idsi)
    
    
    	import base64, hashlib

        #### ISBANK - ASSECCO

	asseco_oid = str(qs_orderid)
	asseco_rnd = str(int(time.time()))

	asseco_successurl = request.scheme_host + reverse('cc_asseco_paid_ok')
	asseco_errorurl = request.scheme_host + reverse('cc_asseco_paid_error')
	asseco_amount_due = amount_due

	taksit = ""  # taksit sayisi

	islemtipi = "Auth"
	clientId = "700655000100"
	storekey = "TRPS1234"

	#### 20-12-2019 Muslu @Makdos
	asseco_securethreedhash = clientId + asseco_oid + str(asseco_amount_due).replace(',','.') + asseco_successurl + asseco_errorurl + islemtipi + taksit + asseco_rnd + storekey

	asseco_hash =  (b64encode(hashlib.sha1(asseco_securethreedhash.encode('utf-8')).digest())).decode('utf-8')

	asseco_3d__dict = {
	    'clientid': clientId,
	    'asseco_hash': asseco_hash,
	    'asseco_amount_due': asseco_amount_due,
	    'asseco_successurl': asseco_successurl,
	    'asseco_errorurl': asseco_errorurl,
	    'asseco_oid': asseco_oid,
	    'asseco_rnd': asseco_rnd,
	    'islemtipi': islemtipi,
	    'taksit': taksit
	}

	###+ ISBANK - ASSECCO
    
    
    return render(
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
    'storekey':storekey})



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
