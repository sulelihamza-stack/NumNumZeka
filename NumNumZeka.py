import streamlit as st
import random
import math

st.set_page_config(page_title="NumNum Zeka", page_icon="🎯")
st.title("🎯 NumNum Zeka - 7. Sınıf Tüm Dersler")

if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = []
if "aktif_soru" not in st.session_state:
    st.session_state.aktif_soru = None
    st.session_state.aktif_cevap = None
    st.session_state.aktif_siklar = None
    st.session_state.secili_ders = None
    st.session_state.puan = 0
    st.session_state.dogru = 0
    st.session_state.yanlis = 0

# ========== MATEMATİK (12 KONU) ==========

def mat_tam_sayilar():
    tip = random.choice([1,2,3,4,5,6])
    if tip == 1:
        b = random.randint(-60,-10); t = b; h = []
        for _ in range(random.randint(4,7)):
            a = random.randint(5,40)
            if random.choice(["yükseliyor","dalıyor"]) == "yükseliyor":
                t += a; h.append(f"{a} m yükseliyor")
            else:
                t -= a; h.append(f"{a} m dalıyor")
        m = f"Bir dalgıç deniz seviyesinden **{b} m**'de iken " + ", ".join(h) + f".\n\n**Son konum kaç metredir?**"; d = str(t)
    elif tip == 2:
        b = random.randint(-20,-5); t = b; h = []
        for _ in range(random.randint(4,7)):
            a = random.randint(5,30)
            if random.choice(["+","-"]) == "+":
                t += a; h.append(f"{a}°C artıyor")
            else:
                t -= a; h.append(f"{a}°C düşüyor")
        m = f"Termometre **{b}°C**'yi gösteriyor. " + ", ".join(h) + f".\n\n**Son sıcaklık kaç °C?**"; d = str(t)
    elif tip == 3:
        s = random.randint(-50,50); t = s; h = []
        for _ in range(random.randint(4,7)):
            a = random.randint(5,40)
            if random.choice(["+","-"]) == "+":
                t += a; h.append(f"+{a}")
            else:
                t -= a; h.append(f"-{a}")
        m = f"Ekranda **{s}** yazıyor. " + ", ".join(h) + f" tuşlanıyor.\n\n**Sonuç kaç?**"; d = str(t)
    elif tip == 4:
        b = random.randint(-5,5); t = b; h = []
        for _ in range(random.randint(4,7)):
            k = random.randint(3,12)
            if random.choice(["yukarı","aşağı"]) == "yukarı":
                t += k; h.append(f"{k} kat yukarı")
            else:
                t -= k; h.append(f"{k} kat aşağı")
        m = f"Asansör **{b}. katta** iken " + ", ".join(h) + f".\n\n**Son kat?**"; d = str(t)
    else:
        b = random.randint(200,1000); t = b; h = []
        for _ in range(random.randint(4,7)):
            miktar = random.randint(50,300)
            if random.choice(["yatırıyor","çekiyor"]) == "yatırıyor":
                t += miktar; h.append(f"{miktar} TL yatırıyor")
            else:
                t -= miktar; h.append(f"{miktar} TL çekiyor")
        m = f"Hesapta **{b} TL** var. " + ", ".join(h) + f".\n\n**Son bakiye kaç TL?**"; d = str(t)
    y = set()
    while len(y) < 3:
        sapma = random.choice([-12,-9,-7,-5,5,7,9,12])
        yd = int(d) + sapma
        if yd != int(d):
            y.add(str(yd))
    s = [d] + list(y)
    random.shuffle(s)
    return m, d, s

def mat_rasyonel():
    tip = random.choice([1,2,3,4])
    if tip == 1:
        p1 = random.randint(1,12); pd1 = random.randint(2,12)
        p2 = random.randint(1,12); pd2 = random.randint(2,12)
        if p1/pd1 > p2/pd2: d = ">"
        elif p1/pd1 < p2/pd2: d = "<"
        else: d = "="
        m = f"{p1}/{pd1} __ {p2}/{pd2} yerine hangi işaret gelir?"
        s = [">", "<", "=", "≠"]
        random.shuffle(s)
        return m, d, s
    elif tip == 2:
        p = random.randint(1,12); pd = random.randint(2,12)
        v = p/pd; d = f"{v:.2f}"
        m = f"{p}/{pd} rasyonel sayısının ondalık gösterimi (2 basamak) nedir?"
        y = [f"{v+0.1:.2f}", f"{v-0.1:.2f}", f"{v+0.05:.2f}"]
        s = [d] + y
        random.shuffle(s)
        return m, d, s
    elif tip == 3:
        p = random.randint(1,8); pd = random.randint(2,8)
        m = f"Bir pastanın {p}/{pd}'i yenmiş. Kalan 6 kişiye eşit paylaştırılıyor.\n\n**Herkes pastanın kaçta kaçını alır?**"
        k = 1 - (p/pd); son = k/6
        pay = int(son*100); payda = 100
        for i in range(2,20):
            if pay%i==0 and payda%i==0:
                pay//=i; payda//=i
        d = f"{pay}/{payda}" if payda!=1 else str(pay)
        y = [f"{pay+1}/{payda}", f"{pay-1}/{payda}", f"{pay}/{payda+1}"]
        s = [d] + y
        random.shuffle(s)
        return m, d, s
    else:
        p = random.randint(1,9); pd = random.randint(2,9)
        m = f"{p}/{pd} kesrini {random.randint(2,5)} ile genişletince oluşan kesrin pay ve paydası toplamı kaç?"
        carp = random.randint(2,5); yp = p*carp; ypd = pd*carp
        d = str(yp + ypd)
        y = [str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
        s = [d] + y
        random.shuffle(s)
        return m, d, s

def mat_rasyonel_islem():
    p1 = random.randint(1,8); pd1 = random.randint(2,8)
    p2 = random.randint(1,8); pd2 = random.randint(2,8)
    islem = random.choice(["+","-","x","/"])
    if islem == "+":
        sp = p1*pd2 + p2*pd1; spd = pd1*pd2
    elif islem == "-":
        sp = p1*pd2 - p2*pd1; spd = pd1*pd2
    elif islem == "x":
        sp = p1*p2; spd = pd1*pd2
    else:
        sp = p1*pd2; spd = pd1*p2
    eb = math.gcd(sp, spd); sp //= eb; spd //= eb
    d = f"{sp}/{spd}" if spd!=1 else str(sp)
    m = f"{p1}/{pd1} {islem} {p2}/{pd2} işleminin sonucu (sadeleştirilmiş) nedir?"
    y = [f"{sp+1}/{spd}", f"{sp-1}/{spd}", f"{sp}/{spd+1}"]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

def mat_cebirsel():
    tip = random.choice([1,2,3,4])
    if tip == 1:
        a = random.randint(1,5); b = random.randint(-8,8)
        c = random.randint(1,5); d = random.randint(-8,8)
        islem = random.choice(["+","-"])
        if islem == "+": son = f"{a+c}x + {b+d}"
        else: son = f"{a-c}x + {b-d}"
        m = f"**({a}x {b:+#d}) {islem} ({c}x {d:+#d})** işleminin en sade hali?"
        y = [f"{a+c+1}x + {b+d}", f"{a+c}x + {b+d+1}", f"{a+c-1}x + {b+d}"]
        s = [son] + y
        random.shuffle(s)
        return m, son, s
    elif tip == 2:
        a = random.randint(2,6); b = random.randint(1,10); x = random.randint(1,5)
        son = a*x + b; d = str(son)
        m = f"{a}x + {b} ifadesinin x={x} için değeri kaçtır?"
        y = [str(son+random.randint(2,6)), str(son-random.randint(2,6)), str(son+random.randint(1,2))]
        s = [d] + y
        random.shuffle(s)
        return m, d, s
    else:
        a = random.randint(2,5); b = random.randint(1,8)
        d = f"{4*a}x + {4*b}"
        m = f"Bir kenarı ({a}x+{b}) cm olan karenin çevresi kaç cm'dir?"
        y = [f"{4*a+1}x + {4*b}", f"{4*a}x + {4*b+1}", f"{4*a-1}x + {4*b}"]
        s = [d] + y
        random.shuffle(s)
        return m, d, s

def mat_denklem():
    a = random.randint(2,6); b = random.randint(2,15)
    c = random.randint(2,6); d = random.randint(2,15)
    if a == c: a = c+1
    coz = (d-b)/(a-c)
    d_str = str(int(coz)) if coz==int(coz) else f"{coz:.1f}"
    m = f"{a}x + {b} = {c}x + {d} denkleminin çözümü kaçtır?"
    y = set()
    while len(y) < 3:
        s = random.choice([-3,-2,2,3,-5,5])
        yd = int(d_str) + s if d_str.isdigit() else float(d_str) + s
        y.add(str(int(yd)) if yd==int(yd) else f"{yd:.1f}")
    s = [d_str] + list(y)
    random.shuffle(s)
    return m, d_str, s

def mat_oran():
    a = random.randint(2,10); b = random.randint(2,10); k = random.randint(2,6)
    x = b*k; d = str(x)
    m = f"{a}/{b} = {a*k}/x orantısında x kaçtır?"
    y = [str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(4,6))]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

def mat_yuzde():
    s = random.randint(100,500); y = random.choice([10,15,20,25,30,40,50])
    son = int(s*y/100); d = str(son)
    m = f"{s} TL'lik ürüne %{y} indirim. İndirim kaç TL?"
    y = [str(son+random.randint(3,8)), str(son-random.randint(3,8)), str(son+random.randint(1,2))]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

def mat_aci():
    a = random.randint(30,150); tip = random.choice(["tümler","bütünler"])
    if tip == "tümler":
        d = str(90-a); m = f"{a}°'lik açının tümleri kaç derece?"
    else:
        d = str(180-a); m = f"{a}°'lik açının bütünleri kaç derece?"
    y = [str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

def mat_cokgen():
    k = random.randint(3,8); tip = random.choice(["iç","dış"])
    if tip == "iç":
        d = str((k-2)*180); m = f"{k} kenarlı çokgenin iç açıları toplamı kaç derece?"
    else:
        d = str(int(360/k)); m = f"Düzgün {k} kenarlı çokgenin bir dış açısı kaç derece?"
    y = [str(int(d)+random.randint(10,30)), str(int(d)-random.randint(10,30)), str(int(d)+random.randint(5,9))]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

def mat_cember():
    r = random.randint(3,15); tip = random.choice(["çevre","alan"]); pi = 3
    if tip == "çevre":
        d = str(2*pi*r); m = f"Yarıçap {r} cm olan çemberin çevresi? (π=3)"
    else:
        d = str(pi*r*r); m = f"Yarıçap {r} cm olan dairenin alanı? (π=3)"
    y = [str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

def mat_veri():
    v = [random.randint(10,90) for _ in range(5)]
    ort = sum(v)//5; med = sorted(v)[2]
    tip = random.choice(["ortalama","medyan"])
    if tip == "ortalama":
        d = str(ort); m = f"{v} veri grubunun aritmetik ortalaması kaç?"
    else:
        d = str(med); m = f"{v} veri grubunun medyanı kaç?"
    y = [str(int(d)+random.randint(2,6)), str(int(d)-random.randint(2,6)), str(int(d)+random.randint(1,2))]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

def mat_cisim():
    c = random.choice(["küp","dikdörtgen prizma","küre","silindir"])
    bank = {
        "küp": ("Bir küpün kaç ayrıtı vardır?", "12"),
        "dikdörtgen prizma": ("Dikdörtgen prizmanın kaç yüzü vardır?", "6"),
        "küre": ("Kürenin kaç köşesi vardır?", "0"),
        "silindir": ("Silindirin yan yüzeyi açılınca hangi şekil oluşur?", "Dikdörtgen")
    }
    m, d = bank[c]
    y = ["8","10","4"] if d=="12" else ["5","7","9"] if d=="6" else ["1","2","4"] if d=="0" else ["Kare","Üçgen","Daire"]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

# ========== FEN BİLİMLERİ (7 KONU) ==========

def fen_gunes():
    soru = random.choice([
        ("Güneş sisteminin en büyük gezegeni hangisidir?", "Jüpiter", ["Mars","Satürn","Jüpiter","Uranüs"]),
        ("Dünya'nın doğal uydusunun adı nedir?", "Ay", ["Mars","Ay","Venüs","Jüpiter"]),
        ("Güneş'e en yakın gezegen hangisidir?", "Merkür", ["Venüs","Merkür","Dünya","Mars"]),
        ("Halkalarıyla ünlü gezegen hangisidir?", "Satürn", ["Jüpiter","Satürn","Uranüs","Neptün"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"🌞 **Güneş Sistemi ve Ötesi**\n\n{m}", d, s

def fen_hucre():
    soru = random.choice([
        ("Mitoz bölünme sonucunda bir hücreden kaç yeni hücre oluşur?", "2", ["1","2","4","8"]),
        ("Hücrenin yönetim merkezi hangi organeldir?", "Çekirdek", ["Mitokondri","Çekirdek","Ribozom","Koful"]),
        ("Mayoz bölünme nerede gerçekleşir?", "Üreme ana hücrelerinde", ["Vücut hücrelerinde","Üreme ana hücrelerinde","Sinir hücrelerinde","Kas hücrelerinde"]),
        ("Hücrenin enerji üreten organeli hangisidir?", "Mitokondri", ["Mitokondri","Ribozom","Lizozom","Golgi"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"🔬 **Hücre ve Bölünmeler**\n\n{m}", d, s

def fen_kuvvet():
    k = random.randint(5,20); v = random.randint(2,10); ke = int(0.5*k*v*v)
    d = str(ke); m = f"Kütlesi {k} kg olan cisim {v} m/s hızla gidiyor. Kinetik enerjisi kaç Joule? (KE=½mv²)"
    y = [str(ke+random.randint(5,15)), str(ke-random.randint(5,15)), str(ke+random.randint(1,4))]
    s = [d] + y; random.shuffle(s)
    return f"⚡ **Kuvvet ve Enerji**\n\n{m}", d, s

def fen_madde():
    soru = random.choice([
        ("Tuz oranı %20 olan 300 g çözeltiye 50 g tuz eklenirse yeni tuz oranı yüzde kaç?", "32.86", ["30","32.86","35","40"]),
        ("Yoğunluğu 0,9 g/cm³ ve 1,1 g/cm³ olan sıvılar eşit hacimde karıştırılırsa karışımın yoğunluğu kaç?", "1.0", ["0.9","1.0","1.1","2.0"]),
        ("Homojen karışımlara verilen diğer ad nedir?", "Çözelti", ["Süspansiyon","Emülsiyon","Çözelti","Kolloid"]),
        ("Bir elementin en küçük yapı taşı nedir?", "Atom", ["Molekül","Atom","Hücre","Tanecik"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"🧪 **Saf Madde ve Karışımlar**\n\n{m}", d, s

def fen_isik():
    soru = random.choice([
        ("Işığın bir engelle karşılaştığında geri dönmesine ne denir?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]),
        ("Işığın saydam ortamdan başka saydam ortama geçerken doğrultu değiştirmesine ne denir?", "Kırılma", ["Yansıma","Kırılma","Soğurma","Girişim"]),
        ("Işığın en hızlı yayıldığı ortam hangisidir?", "Boşluk", ["Boşluk","Hava","Su","Cam"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"💡 **Işığın Madde ile Etkileşimi**\n\n{m}", d, s

def fen_ureme():
    soru = random.choice([
        ("Bitkilerde tohum oluşumu için gerekli olay nedir?", "Tozlaşma", ["Döllenme","Tozlaşma","Çimlenme","Fotosentez"]),
        ("Kurbağalarda görülen gelişim evrelerine ne ad verilir?", "Başkalaşım", ["Metamorfoz","Başkalaşım","Döllenme","Büyüme"]),
        ("Memelilerde yavruların sütle beslenmesini sağlayan bez hangisidir?", "Süt bezi", ["Ter bezi","Yağ bezi","Süt bezi","Salya bezi"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"🐸 **Canlılarda Üreme, Büyüme ve Gelişme**\n\n{m}", d, s

def fen_elektrik():
    tip = random.choice([1,2])
    if tip == 1:
        r1 = random.randint(2,5); r2 = random.randint(2,5)
        d = str(r1+r2); m = f"{r1}Ω ve {r2}Ω'luk dirençler seri bağlanırsa eşdeğer direnç kaç Ω olur?"
        y = [str(int(d)+random.randint(1,3)), str(int(d)-random.randint(1,3)), str(int(d)+random.randint(4,6))]
    else:
        r1 = random.randint(2,5); r2 = random.randint(2,5)
        d = str(round((r1*r2)/(r1+r2),1)); m = f"{r1}Ω ve {r2}Ω'luk dirençler paralel bağlanırsa eşdeğer direnç kaç Ω olur?"
        y = [str(float(d)+random.choice([0.5,1,1.5])), str(float(d)-random.choice([0.5,1,1.5])), str(float(d)+random.choice([0.2,0.8]))]
    s = [d] + y; random.shuffle(s)
    return f"⚡ **Elektrik Devreleri**\n\n{m}", d, s

# ========== TÜRKÇE (8 KONU) ==========

def tur_fiil():
    f = random.choice(["gelmek","gitmek","bakmak","yazmak","okumak","koşmak","söylemek"])
    k = random.choice(["şimdiki zaman","geniş zaman","geçmiş zaman","gelecek zaman","emir kipi"])
    if k == "şimdiki zaman": d = f.replace("mek","").replace("mak","") + "yor"
    elif k == "geniş zaman": d = f.replace("mek","").replace("mak","") + "r"
    elif k == "geçmiş zaman": d = f.replace("mek","").replace("mak","") + "di"
    elif k == "gelecek zaman": d = f.replace("mek","").replace("mak","") + "ecek"
    else: d = f.replace("mek","").replace("mak","")
    m = f"'{f}' fiilinin **{k} 2. tekil kişi** çekimi nasıldır?"
    s = [d, d+"m", d+"k", d+"n"]; random.shuffle(s)
    return f"📖 **Fiiller (Kip ve Kişi Ekleri)**\n\n{m}", d, s

def tur_zarf():
    cumle = random.choice([
        ("Hızlı koştu", "hızlı", ["hızlı","koştu","o","güzel"]),
        ("Çok güzel olmuş", "çok", ["çok","güzel","olmuş","o"]),
        ("Yarın geleceğim", "yarın", ["yarın","geleceğim","ben","gün"]),
        ("Dikkatlice dinledi", "dikkatlice", ["dikkatlice","dinledi","o","sessizce"]),
        ("İçeri girdi", "içeri", ["içeri","girdi","o","hızla"])
    ])
    m, d, s = cumle; random.shuffle(s)
    return f"📝 **Zarflar**\n\n'{m}' cümlesindeki zarf hangisidir?", d, s

def tur_anlam():
    soru = random.choice([
        ("'Bugün hava çok güzel.' cümlesinde hangi duygu vardır?", "mutluluk", ["üzüntü","mutluluk","öfke","korku"]),
        ("'Keşke daha çok çalışsaydım.' cümlesinde hangi anlam vardır?", "pişmanlık", ["pişmanlık","özlem","kararlılık","şart"]),
        ("'Bu işi yapabilir misin?' cümlesi hangi anlamda kullanılmıştır?", "rica/istek", ["emir","rica/istek","koşul","olasılık"]),
        ("'Yağmur yağsa da topraklar ıslansa.' cümlesinde hangi anlam var?", "özlem", ["özlem","pişmanlık","koşul","kararlılık"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"💬 **Cümlede Anlam**\n\n{m}", d, s

def tur_paragraf():
    soru = random.choice([
        ("Teknoloji hayatımızı kolaylaştırsa da bizi tembelleştiriyor. Eskiden insanlar yürürdü şimdi araba kullanıyor. Merdivenlerden çıkardı şimdi asansör tercih ediyor.\n\nBu paragrafta asıl anlatılmak istenen nedir?",
         "Teknolojinin insanı tembelleştirmesi", ["Teknolojinin yararları","Teknolojinin insanı tembelleştirmesi","Spor yapmanın önemi","Asansörün icadı"]),
        ("Ne kadar bilirsen bil, anlatabildiğin kadarsın.\n\nBu cümlede vurgulanmak istenen nedir?",
         "Bilginin aktarımı önemlidir", ["Bilgi her şey değildir","Anlatmak zordur","Bilginin aktarımı önemlidir","Sessizlik erdemdir"]),
        ("Kitap okumak zihnin jimnastiğidir. Zihnimizi çalıştırır, hayal gücümüzü geliştirir.\n\nYazarın bu parçada vurguladığı fikir nedir?",
         "Kitap okumak zihni geliştirir", ["Kitap okumak zaman kaybıdır","Kitap okumak zihni geliştirir","Sadece çocuklar kitap okumalı","Kitap okumak sıkıcıdır"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"📄 **Paragrafta Anlam**\n\n{m}", d, s

def tur_yazim():
    soru = random.choice([
        ("Aşağıdakilerden hangisi doğru yazılmıştır?", "herkes", ["herkez","herkes","herkeş","herkese"]),
        ("'Türkiye'nin başkenti ...' cümlesinde boşluğa hangi şehir gelmelidir?", "Ankara", ["İstanbul","Ankara","İzmir","Bursa"]),
        ("'Herşey' kelimesinin doğru yazımı aşağıdakilerden hangisidir?", "Her şey", ["Herşey","Her şey","Her-şey","Her şe'y"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"✍️ **Yazım Kuralları**\n\n{m}", d, s

def tur_noktalama():
    soru = random.choice([
        ("Sıralı cümleleri ayırmak için hangi noktalama işareti kullanılır?", "Noktalı virgül", ["Virgül","Nokta","Noktalı virgül","İki nokta"]),
        ("Alıntı cümlelerden önce hangi işaret konulur?", "İki nokta", ["Virgül","Nokta","Noktalı virgül","İki nokta"]),
        ("Ünlem işareti hangi durumda kullanılır?", "Sevinç, heyecan, korku", ["Soru sorarken","Sevinç, heyecan, korku","Alıntı yaparken","Sıralama yaparken"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"🔖 **Noktalama İşaretleri**\n\n{m}", d, s

def tur_sozcuk():
    soru = random.choice([
        ("'Soğuk' kelimesinin zıt anlamlısı nedir?", "sıcak", ["sıcak","buzlu","donuk","serin"]),
        ("'Yüzmek' kelimesi hangi cümlede mecaz anlamda kullanılmıştır?", "Paralar içinde yüzüyor.", ["Denizde yüzdü.","Paralar içinde yüzüyor.","Yüzmeyi çok sever.","Nehirde yüzdü."]),
        ("Eş sesli (sesteş) kelime örneği hangisidir?", "yüz", ["kalem","silgi","yüz","defter"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"🔤 **Sözcükte Anlam**\n\n{m}", d, s

def tur_cumle():
    soru = random.choice([
        ("'Kitap okumayı çok severim.' cümlesi yüklemin türüne göre hangisidir?", "İsim cümlesi", ["Fiil cümlesi","İsim cümlesi","Devrik cümle","Birleşik cümle"]),
        ("'Hava çok soğudu.' cümlesi olumlu mu olumsuz mu?", "Olumlu", ["Olumlu","Olumsuz","Soru","Ünlem"]),
        ("'Ah, bu kadar da olmaz!' cümlesinin türü nedir?", "Ünlem cümlesi", ["İsim cümlesi","Fiil cümlesi","Ünlem cümlesi","Soru cümlesi"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"📌 **Cümle Türleri**\n\n{m}", d, s

# ========== SOSYAL BİLGİLER (7 KONU) ==========

def sos_iletisim():
    soru = random.choice([
        ("Duygu, düşünce ve bilgilerin aktarılması sürecine ne denir?", "İletişim", ["Empati","İletişim","Hoşgörü","Saygı"]),
        ("Bir kişinin karşısındakinin duygularını anlamaya çalışmasına ne ad verilir?", "Empati", ["Sempati","Empati","Özgecilik","Fedakarlık"]),
        ("Sözsüz iletişim örneği hangisidir?", "Jest ve mimikler", ["Konuşmak","Jest ve mimikler","Mektup","Telefon"])
    ])
    m, d, s = soru; random.shuffle(s)
    return f"🗣️ **İletişim ve İnsan İlişkileri**\n\n{m}", d, s

def sos_tarih():
    soru = random.choice([
        ("İlk Türk devletlerinden biri hangisidir?", "Asya Hun Devleti", ["Osmanlı","Asya Hun","Bizans","Roma"]),
        ("Osmanlı Devleti'nde Lale Devri'nde yapılan yeniliklerden biri nedir?", "Matbaa", ["Matbaa","Fetih","Anayasa","Cumhuriyet"]),
        ("Milli Mücadele döneminde açılan kongrelerden hangisi?", "Sivas Kongresi", ["
