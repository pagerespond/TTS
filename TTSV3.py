als="qwertyuopasdfghjışğüklizxcvbnmçö., 01234567890*-/@?QÜWERTÇÖYUIİOPASDFGHJKLZXCVBNM:){}<|(!#_?+="
art="qwertyuopasdfghjışğüklizxcvbnmçö., 01234567890*-/@?QÜWERTÇÖYUIİOPASDFGHJKLZXCVBNM:){}<|(!#_?+="
listeart2=[]
grpsfr={}
listegrpsfr=[]
import random

def anahtar_yap():
    alz=list(als)
    print("anahtar yap")
    fdosya=open("key.data","w")
    random.shuffle(alz)
    k=""
    k=k.join(alz)
    for d in list(k): 
        fdosya.write(d)
    fdosya.close()
    art=k
    return k
    print("islem tamamlandi")
        
def ozel_okuma(art2):
    global art
    art=art2
    return art2

def temel_okuma():
    global art
    try:
        fdosya=open("key.data","r")
        art=fdosya.readline()
        print("anahtar okundu")
        return art
    except:
        print("anahtar okunamadi")
    

def sfrokur():
    grpsfr.clear()
    listeart2.clear()
    listegrpsfr.clear()
    fdosya=open("sfr.data","r")
    v=0
    for i in fdosya:
        grpsfr[v]=i[:len(i)-1]
        listegrpsfr.append(i[:len(i)-1])
        v=v+1
    fdosya.close()
    for b in range (len(art)):
        listeart2.append(art[b])
    if v==0:
        print("Sifre anahtariniz yok olusturunuz")
        return False
    else:
        return True

def sfr_olustur():
    fdosya=open("sfr.data","a")
    def  sfrt():
        sfrtxt = "#+*-0123456789qazwsxedcrfvtgbyhn"
        sfrgrup={}
        for i in range (len(sfrtxt)):
            sfrgrup[i]=sfrtxt[i:i+1]
            size=24
        encSfrtxt=""
        for i in range(size):
            random.shuffle(sfrgrup)
            encSfrtxt+=random.choice(sfrgrup)
        return (encSfrtxt)
    print("Sifre olusturma basarili")
    for isifre in  range (len(art)):
        fdosya.write(sfrt()+"\n")
    fdosya.close()
    print("Sifre anahtari olusturuldu")

def veri_sfrleme():
        if sfrokur():
            while True:
                fdosya=open("datasfr.data","a")
                gelenveri=str(input("çıkmak için sadece 0 yaziniz> "))
                if gelenveri !="0":
                    for ir in range (len(gelenveri)):
                        fdosya.write(grpsfr[art.find(gelenveri[ir])])
                        fdosya.write(">")
                    fdosya.write("\n")
                    fdosya.close()
                else:
                    break;

def veri_sfrleme_t(t_veri):
        
        if sfrokur():
            while True:
                fdosya=open("datasfr.data","w")
                for gelenveri in t_veri:
                    for ir in range (len(gelenveri)):
                        fdosya.write(grpsfr[art.find(gelenveri[ir])])
                        fdosya.write(">")
                    fdosya.write("\n")
                fdosya.close()
                break;

def veri_coz():
    if sfrokur():
        fdosya=open("datasfr.data","r")
        for i in fdosya:
            sifre="Sifresiz bilgiler: "
            for vt in i.split(">"):
                wer=str(vt)
                if wer in listegrpsfr:
                    sifre=sifre+str(listeart2[listegrpsfr.index(wer)])
            print(sifre)

def veri_guncelle():
    al=["0","1","2","3","4","5","6","7","8","9","-"]
    if sfrokur():
        degisim=False
        nv=[]
        ku=[]
        ru=[]
        tk=True
        v=0
        fdosya=open("datasfr.data","r")
        for i in fdosya:
            sifre=""
            for vt in i.split(">"):
                wer=str(vt)
                if wer in listegrpsfr:
                    sifre=sifre+str(listeart2[listegrpsfr.index(wer)])
            print(str(v)+"-"+sifre)
            nv.append(sifre)
            v=v+1
        fdosya.close()
        if len(nv)>0:
            print("çıkmak için sadece -1 yaziniz")
            while True:
                gelenveri=str(input("numara yaziniz> "))
                if len(gelenveri)<=0:
                    tk=False
                for a in gelenveri:
                    if a in al:
                        tk=True
                    else:
                        tk=False
                        break
                if tk:
                    gelenveri=int(gelenveri)
                    if gelenveri !=-1:
                        if(len(nv)>gelenveri):
                            print(nv[gelenveri])
                            k=input("Degistir>")
                            if(len(k)>0):
                                nv[gelenveri]=k
                                ku.append(k)
                                degisim=True
                            else:
                                ru.append(nv[gelenveri])
                                nv.pop(gelenveri)
                                degisim=True
                        else:
                            print("böyle bir veriniz yok")
                    else:
                        if degisim:
                            print("Guncellemeleriniz")
                            print("degisenler")
                            for i in ku:
                                print(i)
                            print("silinenler")
                            for i in ru:
                                print(i)
                            print("islemler kaydedilsi mi ")
                            k=str(input("E / H >"))
                            if(k=='E' or k=='e' ):
                                veri_sfrleme_t(nv)
                                degisim=False
                                print("islemler kaydedildi")
                                break;
                            else:
                                degisim=False
                                print("islemler iptal edildi")
                                break;
                        else:
                            break

                else:
                    print("Sayi girmediniz")
                    
        else:
            print("Her hangi bir veri bulunmadi")

def veri_sil():
    print("Bütün sistem silinsin mi  ")
    k=str(input("E / H >"))
    if(k=='E' or k=='e' ):
        try:
            fdosya=open("datasfr.data","w")
            fdosya.close()
            fdosya=open("sfr.data","w")
            fdosya.close()
            fdosya=open("key.data","w")
            fdosya.close()
            print("Sistem silindi")
        except:
            print("Sistem silinemedi")
    else:
        print("Silme yapilmadi")

durum=False

temel_okuma()
while True:
    a=str(input("0 Gelismis mod \n1 Sistemi kur \n2 verileri şifrele \n3 verileri cöz \n4 verileri güncelle \n5 sistemi sil \n6 ozel anahtar olustur \n7 sifre olustur \n>>> "))
    if a=="0":
        print("ozel okuma mod")
        r=str(input("Anahtar giriniz /cikmak için 0>>>"))
        if(r!="0"):
            ozel_okuma(r)
            print("Gelimis Moddasiniz")
        else:
            art=temel_okuma()
            print("Temel Moddasiniz")
    elif a=="7":
        print("sifre olustur\n>>>")
        sfr_olustur()
    elif a=="2":
        print("veri sifrele\n>>>")
        veri_sfrleme()
    elif a=="3":
        print("veri cöz\n>>>")
        veri_coz()
    elif a=="4":
        print("veri guncelle\n>>>")
        veri_guncelle()
    elif a=="5":
        print("sistemi sil\n>>>")
        veri_sil()
    elif a=="6":
        anahtar_yap()
    elif a=="1":
        try:
            art=anahtar_yap()
            sfr_olustur()
            print("Sistem Kuruldu")
        except:
            print("Sistem kurulamadi")
    else:
        break;
        
        

