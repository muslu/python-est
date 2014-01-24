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
