import streamlit as st
import random
import math

# ========== SAYFA YAPILANDIRMASI ==========
st.set_page_config(page_title="NumNum Zeka - 7. Sınıf Tüm Dersler", page_icon="🎯")
st.title("🎯 NumNum Zeka - 7. Sınıf Dinamik Sorular")
st.markdown("**Her dersin her konusu için anında yeni nesil soru üretilir. Sonsuz havuz, tekrar yok!**")

# ========== OTURUM DURUMU ==========
if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = []
if "aktif_soru" not in st.session_state:
    st.session_state.aktif_soru = None
if "aktif_cevap" not in st.session_state:
    st.session_state.aktif_cevap = None
if "aktif_siklar" not in st.session_state:
    st.session_state.aktif_siklar = None
if "secili_ders" not in st.session_state:
    st.session_state.secili_ders = None
if "secili_konu" not in st.session_state:
    st.session_state.secili_konu = None
if "puan" not in st.session_state:
    st.session_state.puan = 0
if "dogru_sayisi" not in st.session_state:
    st.session_state.dogru_sayisi = 0
if "yanlis_sayisi" not in st.session_state:
    st.session_state.yanlis_sayisi = 0

# ========== 1. MATEMATİK (12 KONU) – DİNAMİK ÜRETECLER ==========

def mat_tam_sayilar():
    baslangic = random.randint(-50, -10)
    hareketler = []
    toplam = baslangic
    for _ in range(random.randint(3,6)):
        adim = random.randint(5,35)
        yon = random.choice(["yükseliyor", "dalıyor"])
        if yon == "yükseliyor":
            toplam += adim
            hareketler.append(f"{adim} m yükseliyor")
        else:
            toplam -= adim
            hareketler.append(f"{adim} m dalıyor")
    metin = f"Bir dalgıç deniz seviyesinden **{baslangic} m**'de iken " + ", ".join(hareketler) + f".\n\n**Dalgıcın son konumu kaç metredir?**"
    dogru = str(toplam)
    yanlisler = set()
    while len(yanlisler) < 3:
        sapma = random.choice([-5,-3,3,5,-8,8])
        y = toplam + sapma
        if y != toplam:
            yanlisler.add(str(y))
    siklar = [dogru] + list(yanlisler)
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_rasyonel():
    pay1 = random.randint(1,12)
    payda1 = random.randint(2,12)
    pay2 = random.randint(1,12)
    payda2 = random.randint(2,12)
    tip = random.choice(["karsilastir", "ondalik"])
    if tip == "karsilastir":
        if pay1/payda1 > pay2/payda2:
            dogru = ">"
        elif pay1/payda1 < pay2/payda2:
            dogru = "<"
        else:
            dogru = "="
        metin = f"{pay1}/{payda1} __ {pay2}/{payda2} ifadesinde boşluğa hangi işaret gelmelidir?"
        siklar = [">", "<", "=", "≠"]
        random.shuffle(siklar)
        return metin, dogru, siklar
    else:
        deger = pay1/payda1
        dogru = f"{deger:.2f}"
        metin = f"{pay1}/{payda1} rasyonel sayısının ondalık gösterimi (virgülden sonra 2 basamak) nedir?"
        yanlisler = [f"{deger+0.1:.2f}", f"{deger-0.1:.2f}", f"{deger+0.05:.2f}"]
        siklar = [dogru] + yanlisler
        random.shuffle(siklar)
        return metin, dogru, siklar

def mat_rasyonel_islem():
    pay1 = random.randint(1,8)
    payda1 = random.randint(2,8)
    pay2 = random.randint(1,8)
    payda2 = random.randint(2,8)
    islem = random.choice(["+","-","x","/"])
    if islem == "+":
        sonuc_pay = pay1*payda2 + pay2*payda1
        sonuc_payda = payda1*payda2
    elif islem == "-":
        sonuc_pay = pay1*payda2 - pay2*payda1
        sonuc_payda = payda1*payda2
    elif islem == "x":
        sonuc_pay = pay1*pay2
        sonuc_payda = payda1*payda2
    else:
        sonuc_pay = pay1*payda2
        sonuc_payda = payda1*pay2
    ebob = math.gcd(sonuc_pay, sonuc_payda)
    if ebob:
        sonuc_pay //= ebob
        sonuc_payda //= ebob
    dogru = f"{sonuc_pay}/{sonuc_payda}" if sonuc_payda != 1 else str(sonuc_pay)
    metin = f"{pay1}/{payda1} {islem} {pay2}/{payda2} işleminin sonucu (sadeleştirilmiş kesir) nedir?"
    yanlisler = [
        f"{sonuc_pay+1}/{sonuc_payda}" if sonuc_payda != 1 else str(sonuc_pay+1),
        f"{sonuc_pay-1}/{sonuc_payda}" if sonuc_payda != 1 else str(sonuc_pay-1),
        f"{sonuc_pay}/{sonuc_payda+1}" if sonuc_payda != 1 else str(sonuc_pay)
    ]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_cebirsel():
    a = random.randint(1,5)
    b = random.randint(-8,8)
    c = random.randint(1,5)
    d = random.randint(-8,8)
    islem = random.choice(["+","-"])
    if islem == "+":
        sonuc = f"{a+c}x + {b+d}"
    else:
        sonuc = f"{a-c}x + {b-d}"
    metin = f"**({a}x {b:+#d}) {islem} ({c}x {d:+#d})** işleminin en sade hali hangisidir?"
    yanlisler = [
        f"{a+c+1}x + {b+d}",
        f"{a+c}x + {b+d+1}",
        f"{a+c-1}x + {b+d}"
    ]
    siklar = [sonuc] + yanlisler
    random.shuffle(siklar)
    return metin, sonuc, siklar

def mat_denklem():
    a = random.randint(2,6)
    b = random.randint(2,15)
    c = random.randint(2,6)
    d = random.randint(2,15)
    if a == c:
        a = c+1
    cozum = (d - b) / (a - c)
    if cozum == int(cozum):
        dogru = str(int(cozum))
    else:
        dogru = f"{cozum:.1f}"
    metin = f"{a}x + {b} = {c}x + {d} denklemini sağlayan x değeri kaçtır?"
    yanlisler = [str(float(dogru)+random.choice([-2,-1,1,2])), str(float(dogru)+random.choice([-3,3])), str(float(dogru)+random.choice([-4,4]))]
    siklar = [dogru] + yanlisler[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_oran():
    a = random.randint(2,10)
    b = random.randint(2,10)
    k = random.randint(2,6)
    x = b * k
    dogru = str(x)
    metin = f"{a}/{b} = {a*k}/x orantısında x kaçtır?"
    yanlisler = [str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(4,6))]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_yuzde():
    sayi = random.randint(100,500)
    yuzde = random.choice([10,15,20,25,30,40,50])
    sonuc = int(sayi * yuzde / 100)
    dogru = str(sonuc)
    metin = f"{sayi} TL'lik bir ürüne %{yuzde} indirim yapılıyor. İndirim miktarı kaç TL'dir?"
    yanlisler = [str(sonuc+random.randint(3,8)), str(sonuc-random.randint(3,8)), str(sonuc+random.randint(1,2))]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_aci():
    aci = random.randint(30,150)
    tip = random.choice(["tumler","butunler"])
    if tip == "tumler":
        dogru = str(90 - aci)
        metin = f"{aci}°'lik açının tümleri kaç derecedir?"
    else:
        dogru = str(180 - aci)
        metin = f"{aci}°'lik açının bütünleri kaç derecedir?"
    yanlisler = [str(int(dogru)+random.randint(5,15)), str(int(dogru)-random.randint(5,15)), str(int(dogru)+random.randint(1,4))]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_cokgen():
    kenar = random.randint(3,8)
    tip = random.choice(["ic","dis"])
    if tip == "ic":
        dogru = str((kenar-2)*180)
        metin = f"{kenar} kenarlı bir çokgenin iç açıları toplamı kaç derecedir?"
    else:
        dogru = str(int(360/kenar))
        metin = f"Düzgün {kenar} kenarlı bir çokgenin bir dış açısı kaç derecedir?"
    yanlisler = [str(int(dogru)+random.randint(10,30)), str(int(dogru)-random.randint(10,30)), str(int(dogru)+random.randint(5,9))]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_cember():
    r = random.randint(3,15)
    tip = random.choice(["cevre","alan"])
    pi = 3
    if tip == "cevre":
        dogru = str(2*pi*r)
        metin = f"Yarıçapı {r} cm olan çemberin çevresi kaç cm'dir? (π=3)"
    else:
        dogru = str(pi*r*r)
        metin = f"Yarıçapı {r} cm olan dairenin alanı kaç cm²'dir? (π=3)"
    yanlisler = [str(int(dogru)+random.randint(5,15)), str(int(dogru)-random.randint(5,15)), str(int(dogru)+random.randint(1,4))]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_veri():
    veri = [random.randint(10,90) for _ in range(5)]
    ortalama = sum(veri)//5
    medyan = sorted(veri)[2]
    tip = random.choice(["ortalama","medyan"])
    if tip == "ortalama":
        dogru = str(ortalama)
        metin = f"{veri} veri grubunun aritmetik ortalaması kaçtır?"
    else:
        dogru = str(medyan)
        metin = f"{veri} veri grubunun medyanı (ortanca değeri) kaçtır?"
    yanlisler = [str(int(dogru)+random.randint(2,6)), str(int(dogru)-random.randint(2,6)), str(int(dogru)+random.randint(1,2))]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_cisim():
    cisim = random.choice(["küp","dikdörtgen prizma","küre","silindir"])
    soru_bank = {
        "küp": ("Bir küpün kaç ayrıtı vardır?", "12"),
        "dikdörtgen prizma": ("Dikdörtgen prizmanın kaç yüzü vardır?", "6"),
        "küre": ("Kürenin kaç köşesi vardır?", "0"),
        "silindir": ("Silindirin yan yüzeyi açıldığında hangi şekil oluşur?", "Dikdörtgen")
    }
    metin, dogru = soru_bank[cisim]
    yanlisler = ["8","10","4"] if dogru=="12" else ["5","7","9"] if dogru=="6" else ["1","2","4"] if dogru=="0" else ["Kare","Üçgen","Daire"]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    return metin, dogru, siklar

matematik_konulari = {
    "Tam Sayılarla İşlemler": mat_tam_sayilar,
    "Rasyonel Sayılar": mat_rasyonel,
    "Rasyonel Sayılarla İşlemler": mat_rasyonel_islem,
    "Cebirsel İfadeler": mat_cebirsel,
    "Eşitlik ve Denklem": mat_denklem,
    "Oran ve Orantı": mat_oran,
    "Yüzdeler": mat_yuzde,
    "Doğrular ve Açılar": mat_aci,
    "Çokgenler": mat_cokgen,
    "Çember ve Daire": mat_cember,
    "Veri Analizi": mat_veri,
    "Cisimlerin Farklı Yönlerden Görünümleri": mat_cisim
}

# ========== 2. FEN BİLİMLERİ (7 KONU) – DİNAMİK ÜRETECLER ==========

def fen_gunes():
    sorular = [
        ("Güneş sisteminin en büyük gezegeni hangisidir?", "Jüpiter", ["Mars","Satürn","Jüpiter","Uranüs"]),
        ("Dünya'nın doğal uydusunun adı nedir?", "Ay", ["Mars","Ay","Venüs","Jüpiter"]),
        ("Güneş'e en yakın gezegen hangisidir?", "Merkür", ["Venüs","Merkür","Dünya","Mars"]),
        ("Bir yıldızın parlaklığı ve rengi hakkında ne söylenebilir? En sıcak yıldız rengi hangisidir?", "Mavi", ["Kırmızı","Mavi","Sarı","Beyaz"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🌞 **Güneş Sistemi ve Ötesi**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def fen_hucre():
    sorular = [
        ("Mitoz bölünme sonucunda bir hücreden kaç yeni hücre oluşur?", "2", ["1","2","4","8"]),
        ("Hücrenin yönetim merkezi hangi organeldir?", "Çekirdek", ["Mitokondri","Çekirdek","Ribozom","Koful"]),
        ("Mayoz bölünme nerede gerçekleşir?", "Üreme ana hücrelerinde", ["Vücut hücrelerinde","Üreme ana hücrelerinde","Sinir hücrelerinde","Kas hücrelerinde"]),
        ("Kromozom sayısı mayoz bölünme sonucunda nasıl değişir?", "Yarıya iner", ["Aynı kalır","İki katına çıkar","Yarıya iner","Dört katına çıkar"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🔬 **Hücre ve Bölünmeler**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def fen_kuvvet():
    k = random.randint(5,20)
    v = random.randint(2,10)
    ke = int(0.5 * k * v * v)
    soru = f"Kütlesi {k} kg olan bir cisim {v} m/s hızla hareket ediyor. Cismin kinetik enerjisi kaç Joule'dür? (Formül: KE = 1/2 * m * v²)"
    dogru = str(ke)
    yanlisler = [str(ke+random.randint(5,15)), str(ke-random.randint(5,15)), str(ke+random.randint(1,4))]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    metin = f"⚡ **Kuvvet ve Enerji**\n\n{soru}"
    return metin, dogru, siklar

def fen_madde():
    sorular = [
        ("Tuz oranı %20 olan 300 g çözeltiye 50 g tuz eklenirse yeni tuz oranı yüzde kaç olur?", "32.86", ["30","32.86","35","40"]),
        ("Yoğunluğu 0,9 g/cm³ ve 1,1 g/cm³ olan iki sıvı eşit hacimde karıştırılırsa karışımın yoğunluğu kaç g/cm³ olur?", "1.0", ["0.9","1.0","1.1","2.0"]),
        ("Homojen karışımlara verilen diğer ad nedir?", "Çözelti", ["Süspansiyon","Emülsiyon","Çözelti","Kolloid"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🧪 **Saf Madde ve Karışımlar**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def fen_isik():
    sorular = [
        ("Işığın bir engelle karşılaştığında geri dönmesine ne denir?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]),
        ("Işığın saydam ortamdan başka saydam ortama geçerken doğrultu değiştirmesine ne ad verilir?", "Kırılma", ["Yansıma","Kırılma","Soğurma","Girişim"]),
        ("Kırılma indisi büyük olan ortamda ışık hızı nasıldır?", "Daha küçük", ["Daha büyük","Aynı","Daha küçük","Sıfır"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"💡 **Işığın Madde ile Etkileşimi**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def fen_ureme():
    sorular = [
        ("Bitkilerde tohum oluşumu için gerekli olay nedir?", "Tozlaşma", ["Döllenme","Tozlaşma","Çimlenme","Fotosentez"]),
        ("Kurbağalarda görülen gelişim evrelerine ne ad verilir?", "Başkalaşım", ["Metamorfoz","Başkalaşım","Döllenme","Büyüme"]),
        ("Memelilerde yavruların sütle beslenmesini sağlayan bez hangisidir?", "Süt bezi", ["Ter bezi","Yağ bezi","Süt bezi","Salya bezi"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🐸 **Canlılarda Üreme, Büyüme ve Gelişme**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def fen_elektrik():
    r1 = random.randint(2,5)
    r2 = random.randint(2,5)
    sec = random.choice(["seri","paralel"])
    if sec == "seri":
        dogru = str(r1+r2)
        metin = f"{r1}Ω ve {r2}Ω'luk iki direnç seri bağlanırsa eşdeğer direnç kaç Ω olur?"
    else:
        dogru = str(round((r1*r2)/(r1+r2),1))
        metin = f"{r1}Ω ve {r2}Ω'luk iki direnç paralel bağlanırsa eşdeğer direnç kaç Ω olur?"
    yanlisler = [str(float(dogru)+random.choice([1,2,3])), str(float(dogru)-random.choice([1,2,3])), str(float(dogru)+random.choice([0.5,1.5]))]
    siklar = [dogru] + yanlisler
    random.shuffle(siklar)
    metin = f"⚡ **Elektrik Devreleri**\n\n{metin}"
    return metin, dogru, siklar

fen_konulari = {
    "Güneş Sistemi ve Ötesi": fen_gunes,
    "Hücre ve Bölünmeler": fen_hucre,
    "Kuvvet ve Enerji": fen_kuvvet,
    "Saf Madde ve Karışımlar": fen_madde,
    "Işığın Madde ile Etkileşimi": fen_isik,
    "Canlılarda Üreme, Büyüme ve Gelişme": fen_ureme,
    "Elektrik Devreleri": fen_elektrik
}

# ========== 3. TÜRKÇE (8 KONU) – DİNAMİK ÜRETECLER ==========

def tur_fiil():
    fiiller = ["gelmek","gitmek","bakmak","yazmak","okumak","koşmak","söylemek"]
    fiil = random.choice(fiiller)
    kip = random.choice(["şimdiki zaman","geniş zaman","geçmiş zaman","gelecek zaman","emir kipi"])
    kisi = random.choice(["1. tekil","2. tekil","3. tekil","1. çoğul","2. çoğul","3. çoğul"])
    if kip == "şimdiki zaman":
        ek = "yor"
    elif kip == "geniş zaman":
        ek = "r"
    elif kip == "geçmiş zaman":
        ek = "di"
    elif kip == "gelecek zaman":
        ek = "ecek"
    else:
        ek = ""
    if kisi == "1. tekil":
        kisi_ek = "um"
    elif kisi == "2. tekil":
        kisi_ek = "sun"
    else:
        kisi_ek = ""
    metin = f"📖 **Fiiller (Kip ve Kişi Ekleri)**\n\n'{fiil}' fiilinin **{kip} {kisi}** çekimi nasıldır?"
    dogru = fiil.replace("mek","").replace("mak","") + ek + kisi_ek
    siklar = [dogru, dogru+"m", dogru+"k", dogru+"n"]
    random.shuffle(siklar)
    return metin, dogru, siklar

def tur_zarf():
    cumleler = [
        ("Hızlı koştu", "hızlı", ["hızlı","koştu","o","güzel"]),
        ("Çok güzel olmuş", "çok", ["çok","güzel","olmuş","o"]),
        ("Yarın geleceğim", "yarın", ["yarın","geleceğim","ben","gün"]),
        ("Dikkatlice dinledi", "dikkatlice", ["dikkatlice","dinledi","o","sessizce"])
    ]
    cumle, dogru, siklar = random.choice(cumleler)
    metin = f"📝 **Zarflar**\n\n'{cumle}' cümlesinde altı çizili olması gereken zarf hangisidir?"
    return metin, dogru, siklar

def tur_anlam():
    sorular = [
        ("'Bugün hava çok güzel.' cümlesinde hangi duygu vardır?", "mutluluk", ["üzüntü","mutluluk","öfke","korku"]),
        ("'Keşke daha çok çalışsaydım.' cümlesinde hangi anlam vardır?", "pişmanlık", ["pişmanlık","özlem","kararlılık","şart"]),
        ("'Bu işi yapabilir misin?' cümlesi hangi anlamda kullanılmıştır?", "rica/istek", ["emir","rica/istek","koşul","olasılık"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"💬 **Cümlede Anlam**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def tur_paragraf():
    paragraflar = [
        ("Teknoloji hayatımızı kolaylaştırsa da bizi tembelleştiriyor. Eskiden insanlar yürürdü şimdi araba kullanıyor. Merdivenlerden çıkardı şimdi asansör tercih ediyor.", "Teknolojinin insanı tembelleştirmesi", ["Teknolojinin yararları","Teknolojinin insanı tembelleştirmesi","Spor yapmanın önemi","Asansörün icadı"]),
        ("Ne kadar bilirsen bil, anlatabildiğin kadarsın.", "Bilginin aktarımı önemlidir", ["Bilgi her şey değildir","Anlatmak zordur","Bilginin aktarımı önemlidir","Sessizlik erdemdir"])
    ]
    paragraf, dogru, siklar = random.choice(paragraflar)
    metin = f"📄 **Paragrafta Anlam**\n\n{paragraf}\n\nBu paragrafta asıl anlatılmak istenen nedir?"
    random.shuffle(siklar)
    return metin, dogru, siklar

def tur_yazim():
    sorular = [
        ("Aşağıdakilerden hangisi doğru yazılmıştır?", "herkes", ["herkez","herkes","herkeş","herkese"]),
        ("'Türkiye'nin başkenti ...' cümlesinde boşluğa hangi şehir gelmelidir?", "Ankara", ["İstanbul","Ankara","İzmir","Bursa"]),
        ("Birleşik kelimelerden hangisi doğru yazılmıştır?", "çörekotu", ["çörekotu","çörek otu","çörek-otu","çörek otu bitkisi"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"✍️ **Yazım Kuralları**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def tur_noktalama():
    sorular = [
        ("Sıralı cümleleri ayırmak için hangi noktalama işareti kullanılır?", "Noktalı virgül", ["Virgül","Nokta","Noktalı virgül","İki nokta"]),
        ("Alıntı cümlelerden önce hangi işaret konulur?", "İki nokta", ["Virgül","Nokta","Noktalı virgül","İki nokta"]),
        ("Ünlem işareti hangi durumda kullanılır?", "Sevinç, heyecan, korku", ["Soru sorarken","Sevinç, heyecan, korku","Alıntı yaparken","Sıralama yaparken"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🔖 **Noktalama İşaretleri**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def tur_sozcuk():
    sorular = [
        ("'Soğuk' kelimesinin zıt anlamlısı nedir?", "sıcak", ["sıcak","buzlu","donuk","serin"]),
        ("'Yüzmek' kelimesi hangi cümlede mecaz anlamda kullanılmıştır?", "Paralar içinde yüzüyor.", ["Denizde yüzdü.","Paralar içinde yüzüyor.","Yüzmeyi çok sever.","Nehirde yüzdü."]),
        ("Eş sesli (sesteş) kelime örneği hangisidir?", "yüz", ["kalem","silgi","yüz","defter"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🔤 **Sözcükte Anlam**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def tur_cumle():
    sorular = [
        ("'Kitap okumayı çok severim.' cümlesi yüklemin türüne göre hangisidir?", "İsim cümlesi", ["Fiil cümlesi","İsim cümlesi","Devrik cümle","Birleşik cümle"]),
        ("'Hava çok soğudu.' cümlesi olumlu mu olumsuz mu?", "Olumlu", ["Olumlu","Olumsuz","Soru","Ünlem"]),
        ("'Ah, bu kadar da olmaz!' cümlesinin türü nedir?", "Ünlem cümlesi", ["İsim cümlesi","Fiil cümlesi","Ünlem cümlesi","Soru cümlesi"])
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"📌 **Cümle Türleri**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

turkce_konulari = {
    "Fiiller (Kip ve Kişi Ekleri)": tur_fiil,
    "Zarflar": tur_zarf,
    "Cümlede Anlam": tur_anlam,
    "Paragrafta Anlam": tur_paragraf,
    "Yazım Kuralları": tur_yazim,
    "Noktalama İşaretleri": tur_noktalama,
    "Sözcükte Anlam": tur_sozcuk,
    "Cümle Türleri": tur_cumle
}

# ========== 4. SOSYAL BİLGİLER (7 KONU) – DİNAMİK ÜRETECLER ==========

def sos_iletisim():
    sorular = [
        ("Duygu, düşünce ve bilgilerin aktarılması sürecine ne denir?", "İletişim", ["Empati","İletişim","Hoşgörü","Saygı"]),
        ("Bir kişinin karşısındakinin duygularını anlamaya çalışmasına ne ad verilir?", "Empati", ["Sempati","Empati","Özgecilik","Fedakarlık"]),
        ("Sözsüz iletişim örneği hangisidir?", "Jest ve mimikler", ["Konuşmak","Jest ve mimikler","Mektup","Telefon"]),
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🗣️ **İletişim ve İnsan İlişkileri**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def sos_tarih():
    sorular = [
        ("İlk Türk devletlerinden biri hangisidir?", "Asya Hun Devleti", ["Osmanlı","Asya Hun","Bizans","Roma"]),
        ("Osmanlı Devleti'nde Lale Devri'nde yapılan yeniliklerden biri nedir?", "Matbaa", ["Matbaa","Fetih","Anayasa","Cumhuriyet"]),
        ("Milli Mücadele döneminde açılan kongrelerden hangisi?", "Sivas Kongresi", ["Lozan","Sivas","Erzurum","Amasya"]),
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🏛️ **Türk Tarihi'nde Yolculuk**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def sos_nufus():
    sorular = [
        ("Bir ülkede yaşayan insan sayısına ne denir?", "Nüfus", ["Nüfus yoğunluğu","Nüfus","Göç","Demografi"]),
        ("Türkiye'nin en kalabalık şehri hangisidir?", "İstanbul", ["Ankara","İzmir","İstanbul","Bursa"]),
        ("Nüfus yoğunluğu en az olan bölgemiz hangisidir?", "Doğu Anadolu", ["Marmara","Doğu Anadolu","Akdeniz","Ege"]),
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🌍 **Nüfus ve Yerleşme**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def sos_bilim():
    sorular = [
        ("Matematik, fizik, kimya gibi disiplinlere ne ad verilir?", "Bilim", ["Teknoloji","Sanat","Bilim","Edebiyat"]),
        ("İcat ile keşif arasındaki fark nedir?", "İcat yoktan var olanı yapmak, keşif var olanı bulmak", ["İcat var olanı bulmak","Keşif yoktan var etmek","İcat yoktan var olanı yapmak, keşif var olanı bulmak","İkisi de aynı"]),
        ("Teknolojinin olumlu etkilerine örnek?", "İletişim kolaylığı", ["Kirlilik","Trafik","İletişim kolaylığı","Sosyal izolasyon"]),
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🔬 **Bilim ve Teknoloji**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def sos_ekonomi():
    sorular = [
        ("İhtiyaçları karşılamak için yapılan her türlü faaliyete ne denir?", "Üretim", ["Tüketim","Üretim","Pazarlama","Reklam"]),
        ("Gelir ve gider arasındaki farka ne denir?", "Kâr", ["Zarar","Kâr","Bütçe","Tasarruf"]),
        ("Vergi neden alınır?", "Kamu hizmetleri için", ["İhracat için","Kamu hizmetleri için","İthalat için","Savunma için"]),
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"💰 **Ekonomi ve Sosyal Hayat**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def sos_kultur():
    sorular = [
        ("Bir topluma ait maddi ve manevi değerler bütününe ne denir?", "Kültür", ["Medeniyet","Kültür","Gelenek","Görenek"]),
        ("UNESCO Dünya Mirası listesinde Türkiye'den bir yer?", "Kapadokya", ["Ankara","İstanbul","Kapadokya","Antalya"]),
        ("Somut olmayan kültürel mirasa örnek?", "Hacivat Karagöz", ["Pamukkale","Efes","Hacivat Karagöz","Ayasofya"]),
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🏺 **Kültür ve Miras**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

def sos_demokrasi():
    sorular = [
        ("Halkın kendi kendini yönettiği yönetim biçimi?", "Demokrasi", ["Monarşi","Oligarşi","Demokrasi","Teokrasi"]),
        ("TBMM hangi tarihte açıldı?", "23 Nisan 1920", ["19 Mayıs 1919","23 Nisan 1920","29 Ekim 1923","30 Ağustos 1922"]),
        ("Seçme ve seçilme yaşı kaçtır?", "18", ["16","17","18","20"]),
    ]
    soru, dogru, siklar = random.choice(sorular)
    metin = f"🗳️ **Demokrasi Serüveni**\n\n{soru}"
    random.shuffle(siklar)
    return metin, dogru, siklar

sosyal_konulari = {
    "İletişim ve İnsan İlişkileri": sos_iletisim,
    "Türk Tarihi'nde Yolculuk": sos_tarih,
    "Nüfus ve Yerleşme": sos_nufus,
    "Bilim ve Teknoloji": sos_bilim,
    "Ekonomi ve Sosyal Hayat": sos_ekonomi,
    "Kültür ve Miras": sos_kultur,
    "Demokrasi Serüveni": sos_demokrasi
}

# ========== DERS VE KONU BİRLEŞTİRME ==========
tum_dersler = {
    "Matematik": matematik_konulari,
    "Fen Bilimleri": fen_konulari,
    "Türkçe": turkce_konulari,
    "Sosyal Bilgiler": sosyal_konulari
}

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📊 Performans")
    col1, col2 = st.columns(2)
    col1.metric("✅ Doğru", st.session_state.dogru_sayisi)
    col2.metric("❌ Yanlış", st.session_state.yanlis_sayisi)
    st.metric("🏆 Puan", st.session_state.puan)
    
    st.markdown("---")
    if st.session_state.secili_ders is None:
        secilecek_ders = st.selectbox("📚 Ders Seç", list(tum_dersler.keys()))
        if st.button("🚀 Dersi Başlat", use_container_width=True):
            st.session_state.secili_ders = secilecek_ders
            st.session_state.secili_konu = None
            st.rerun()
    else:
        st.success(f"Seçili Ders: **{st.session_state.secili_ders}**")
        konular = list(tum_dersler[st.session_state.secili_ders].keys())
        secilen_konu = st.selectbox("📌 Konu Seç", konular)
        if st.button("🎲 YENİ SORU", use_container_width=True):
            uretici = tum_dersler[st.session_state.secili_ders][secilen_konu]
            soru_metni, dogru, siklar = uretici()
            st.session_state.aktif_soru = soru_metni
            st.session_state.aktif_cevap = dogru
            st.session_state.aktif_siklar = siklar
            st.session_state.secili_konu = secilen_konu
            st.session_state.mesajlar.append({
                "rol": "asistan",
                "icerik": f"**{st.session_state.secili_ders} - {secilen_konu}**\n\n{soru_metni}\n\n**Seçenekler:**\nA) {siklar[0]}\nB) {siklar[1]}\nC) {siklar[2]}\nD) {siklar[3]}"
            })
            st.rerun()
        if st.button("🔄 Ders Değiştir", use_container_width=True):
            st.session_state.secili_ders = None
            st.session_state.secili_konu = None
            st.session_state.aktif_soru = None
            st.rerun()
    st.markdown("---")
    if st.button("🔄 Tüm İstatistikleri Sıfırla", use_container_width=True):
        st.session_state.puan = 0
        st.session_state.dogru_sayisi = 0
        st.session_state.yanlis_sayisi = 0
        st.rerun()

# ========== ANA ALAN: SOHBET ARAYÜZÜ ==========
if st.session_state.secili_ders is None:
    st.info("🎓 **NumNum Zeka - 7. Sınıf Tüm Dersler**\n\nBaşlamak için sol panelden bir ders ve konu seçip 'YENİ SORU' butonuna tıklayın.\n\nHer soru dinamik olarak üretilir, sonsuz havuz vardır.")
else:
    for mesaj in st.session_state.mesajlar:
        with st.chat_message(mesaj["rol"]):
            st.markdown(mesaj["icerik"])
    
    if st.session_state.aktif_soru:
        kullanici_cevap = st.chat_input("Cevabını yazınız (A, B, C, D) veya şıkkın metnini girin...")
        if kullanici_cevap:
            st.session_state.mesajlar.append({"rol": "kullanici", "icerik": kullanici_cevap})
            cevap_harf = kullanici_cevap.strip().upper()
            harf_map = {"A":0, "B":1, "C":2, "D":3}
            if cevap_harf in harf_map:
                kullanici_secimi = st.session_state.aktif_siklar[harf_map[cevap_harf]]
            else:
                kullanici_secimi = kullanici_cevap.strip()
            
            if kullanici_secimi == st.session_state.aktif_cevap:
                st.session_state.dogru_sayisi += 1
                st.session_state.puan += 10
                yanit = f"✅ **Doğru!** +10 puan\n\nToplam: {st.session_state.dogru_sayisi} doğru, {st.session_state.yanlis_sayisi} yanlış\nPuan: {st.session_state.puan}\n\nYeni soru için sol panelden 'YENİ SORU' butonuna tıklayın."
            else:
                st.session_state.yanlis_sayisi += 1
                yanit = f"❌ **Yanlış!** Doğru cevap: **{st.session_state.aktif_cevap}**\n\nDoğru: {st.session_state.dogru_sayisi} | Yanlış: {st.session_state.yanlis_sayisi}\n\nYeni soru için butona basın."
            
            st.session_state.mesajlar.append({"rol": "asistan", "icerik": yanit})
            st.session_state.aktif_soru = None
            st.session_state.aktif_cevap = None
            st.session_state.aktif_siklar = None
            st.rerun()
    else:
        st.chat_input("Yeni soru almak için sol panelden konu seçip 'YENİ SORU' butonuna tıklayın.", disabled=True)
