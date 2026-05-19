import streamlit as st
import random
import math

st.set_page_config(page_title="NumNum Zeka - 7. Sınıf LGS", page_icon="🎯")

# ========== MODERN RENK TEMASI (Koyu, uyumlu, profesyonel) ==========
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0a0f1f 0%, #0f172a 100%); }
    .stMarkdown, .stText, div, p, span, label, .stMetric label { color: #e2e8f0 !important; }
    .stButton button { background-color: #3b82f6; color: white; border-radius: 12px; font-weight: bold; transition: all 0.2s; width: 100%; }
    .stButton button:hover { background-color: #2563eb; transform: scale(1.01); box-shadow: 0 4px 12px rgba(59,130,246,0.4); }
    .stSelectbox, .stChatInput textarea { background-color: #1e293b; color: #e2e8f0; border-radius: 12px; border: 1px solid #334155; }
    .stChatMessage { background-color: #1e293b; border-radius: 20px; padding: 12px; margin: 8px 0; border-left: 4px solid #3b82f6; }
    .stMetric { background-color: #1e293b; border-radius: 20px; padding: 12px; text-align: center; }
    hr { border-color: #334155; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 NumNum Zeka - 7. Sınıf (LGS Hazırlık)")
st.markdown("**Her soru dinamik, her konuda 10+ tip, yeni nesil zor sorular**")

# ========== OTURUM DURUMU ==========
if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = []
    st.session_state.aktif_soru = None
    st.session_state.aktif_cevap = None
    st.session_state.aktif_siklar = None
    st.session_state.secili_ders = None
    st.session_state.puan = 0
    st.session_state.dogru = 0
    st.session_state.yanlis = 0

def sifirla():
    st.session_state.puan = 0
    st.session_state.dogru = 0
    st.session_state.yanlis = 0
    st.session_state.mesajlar = []
    st.session_state.aktif_soru = None
    st.session_state.aktif_cevap = None
    st.session_state.aktif_siklar = None
    st.session_state.secili_ders = None
    st.rerun()

# ==================== MATEMATİK - ZOR, UZUN, YENİ NESİL ====================
def mat_tam():
    tip = random.choice([1,2,3,4,5,6,7,8,9])
    if tip == 1:
        b = random.randint(-80,-15); t=b; h=[]
        for _ in range(random.randint(5,9)):
            a=random.randint(10,60)
            if random.choice([0,1])==0:
                t+=a; h.append(f"{a} m yükseliyor")
            else:
                t-=a; h.append(f"{a} m dalıyor")
        m = f"Bir dalgıç deniz seviyesinden {b} metre derinlikte iken sırasıyla: " + ", ".join(h) + f".\n\n**Dalgıcın son konumu kaç metredir?**"
        d=str(t)
    elif tip == 2:
        b=random.randint(-25,-5); t=b
        saatler=[f"{i+1}. saatte {random.randint(3,12)}°C artıyor" for i in range(random.randint(4,8))]
        for s in saatler: t+=int(s.split()[1].replace("°C",""))
        m = f"Sabah 06:00'da sıcaklık {b}°C. " + ", ".join(saatler) + f".\n\n**Saat 18:00'de sıcaklık kaç °C olur?**"
        d=str(t)
    elif tip == 3:
        s=random.randint(-80,80); t=s
        isl=[f"{random.choice(['+','-'])}{random.randint(8,60)}" for _ in range(random.randint(5,9))]
        for i in isl: t+=int(i)
        m = f"Ekranda {s} yazıyor. Sırayla " + ", ".join(isl) + f" tuşlanıyor.\n\n**Sonuç kaçtır?**"
        d=str(t)
    elif tip == 4:
        b=random.randint(-8,8); t=b
        katlar=[f"{random.randint(2,15)} kat {random.choice(['yukarı','aşağı'])}" for _ in range(random.randint(5,8))]
        for k in katlar:
            if "yukarı" in k: t+=int(k.split()[0])
            else: t-=int(k.split()[0])
        m = f"Asansör {b}. katta iken " + ", ".join(katlar) + f".\n\n**Son kat nedir?**"
        d=str(t)
    elif tip == 5:
        maas=random.randint(3000,6000); giderler=[random.randint(200,800) for _ in range(random.randint(4,7))]
        toplam_gider=sum(giderler)
        kalan=maas - toplam_gider
        m = f"Ali'nin maaşı {maas} TL'dir. Ay içinde " + ", ".join([f"{g} TL" for g in giderler]) + f" harcama yapıyor.\n\n**Ay sonunda kaç TL'si kalır?**"
        d=str(kalan)
    elif tip == 6:
        b=random.randint(500,3000); t=b
        hareket=[f"{random.randint(100,800)} m {random.choice(['çıkıyor','iniyor'])}" for _ in range(random.randint(4,8))]
        for h in hareket:
            if "çıkıyor" in h: t+=int(h.split()[0])
            else: t-=int(h.split()[0])
        m = f"Dağcı deniz seviyesinden +{b} m yükseklikte. " + ", ".join(hareket) + f".\n\n**Son yükseklik kaç metredir?**"
        d=str(t)
    elif tip == 7:
        d_s=random.randint(15,25); y_s=random.randint(3,10); b_s=random.randint(2,8)
        d_p=random.choice([4,5]); y_p=random.choice([-1,-2]); b_p=0
        toplam=d_s*d_p + y_s*y_p + b_s*b_p
        m = f"{d_s+y_s+b_s} soruluk sınavda {d_s} doğru (+{d_p}), {y_s} yanlış ({y_p}), {b_s} boş (0).\n\n**Toplam puan kaçtır?**"
        d=str(toplam)
    else:
        p=random.randint(200,800); adimlar=random.randint(5,10)
        for _ in range(adimlar):
            deg=random.choice([-50,-30,25,40,60,80])
            p+=deg
        m = f"Bir yarışmacı {p-adimlar*30} puanla başlıyor. {adimlar} hamlede " + ", ".join([f"{random.choice(['+','-'])}{random.randint(20,90)}" for _ in range(adimlar)]) + f" puan değişimi yaşıyor.\n\n**Son puan kaçtır?**"
        d=str(p)
    yanlis = set()
    while len(yanlis)<3:
        sapma = random.choice([-15,-10,-8,8,10,15,20])
        y = int(d)+sapma
        if y != int(d): yanlis.add(str(y))
    siklar = [d] + list(yanlis)
    random.shuffle(siklar)
    return m, d, siklar

def mat_rasyonel():
    tip = random.choice([1,2,3,4,5])
    if tip == 1:
        p1=random.randint(1,15); pd1=random.randint(2,15)
        p2=random.randint(1,15); pd2=random.randint(2,15)
        if p1/pd1 > p2/pd2: d=">"
        elif p1/pd1 < p2/pd2: d="<"
        else: d="="
        m = f"{p1}/{pd1} __ {p2}/{pd2} ifadesinde boşluğa hangi işaret gelir?"
        s=[">","<","=","≠"]; random.shuffle(s)
        return m,d,s
    elif tip == 2:
        p=random.randint(1,15); pd=random.randint(2,15)
        v=p/pd; d=f"{v:.2f}"
        m = f"{p}/{pd} rasyonel sayısının ondalık gösterimi (virgülden sonra 2 basamak) nedir?"
        y=[f"{v+0.1:.2f}", f"{v-0.1:.2f}", f"{v+0.05:.2f}"]; s=[d]+y; random.shuffle(s); return m,d,s
    elif tip == 3:
        p=random.randint(1,10); pd=random.randint(2,10)
        kalan=1-(p/pd); kisilik=random.randint(4,8)
        pay = int((kalan/kisilik)*100); payda=100
        for i in range(2,20):
            if pay%i==0 and payda%i==0: pay//=i; payda//=i
        d=f"{pay}/{payda}" if payda!=1 else str(pay)
        m = f"Bir pastanın {p}/{pd}'i yenmiştir. Kalan pasta {kisilik} kişiye eşit paylaştırılıyor.\n\n**Her bir kişi pastanın kaçta kaçını alır?**"
        s=[d, f"{pay+1}/{payda}", f"{pay-1}/{payda}", f"{pay}/{payda+1}"]; random.shuffle(s); return m,d,s
    else:
        p=random.randint(1,12); pd=random.randint(2,12)
        carp=random.randint(2,6); yp=p*carp; ypd=pd*carp
        d=str(yp+ypd)
        m = f"{p}/{pd} kesrini {carp} ile genişlettiğimizde pay ve paydanın toplamı kaç olur?"
        y=[str(int(d)+random.randint(5,20)), str(int(d)-random.randint(5,20)), str(int(d)+random.randint(1,4))]; s=[d]+y; random.shuffle(s); return m,d,s

def mat_rasyonel_islem():
    p1=random.randint(1,10); pd1=random.randint(2,10)
    p2=random.randint(1,10); pd2=random.randint(2,10)
    islem=random.choice(["+","-","x","/"])
    if islem=="+": sp=p1*pd2+p2*pd1; spd=pd1*pd2
    elif islem=="-": sp=p1*pd2-p2*pd1; spd=pd1*pd2
    elif islem=="x": sp=p1*p2; spd=pd1*pd2
    else: sp=p1*pd2; spd=pd1*p2
    eb=math.gcd(sp,spd); sp//=eb; spd//=eb
    d=f"{sp}/{spd}" if spd!=1 else str(sp)
    m = f"{p1}/{pd1} {islem} {p2}/{pd2} işleminin sonucu (sadeleştirilmiş) nedir?"
    s = [d, f"{sp+1}/{spd}", f"{sp-1}/{spd}", f"{sp}/{spd+1}"]; random.shuffle(s)
    return m, d, s

def mat_cebirsel():
    tip = random.choice([1,2,3])
    if tip == 1:
        a=random.randint(1,6); b=random.randint(-10,10); c=random.randint(1,6); d=random.randint(-10,10)
        islem=random.choice(["+","-"])
        if islem=="+": son=f"{a+c}x+{b+d}"
        else: son=f"{a-c}x+{b-d}"
        m = f"({a}x{b:+d}) {islem} ({c}x{d:+d}) işleminin en sade hali nedir?"
        s = [son, f"{a+c+1}x+{b+d}", f"{a+c}x+{b+d+1}", f"{a+c-1}x+{b+d}"]; random.shuffle(s)
        return m, son, s
    elif tip == 2:
        a=random.randint(2,7); b=random.randint(1,12); x=random.randint(1,6)
        son=a*x+b; d=str(son)
        m = f"{a}x+{b} ifadesinin x={x} için değeri kaçtır?"
        s=[d, str(son+random.randint(3,8)), str(son-random.randint(3,8)), str(son+random.randint(1,3))]; random.shuffle(s)
        return m, d, s
    else:
        a=random.randint(2,6); b=random.randint(1,10); d=f"{4*a}x+{4*b}"
        m = f"Bir kenarı ({a}x+{b}) cm olan karenin çevresi kaç cm'dir?"
        s=[d, f"{4*a+1}x+{4*b}", f"{4*a}x+{4*b+1}", f"{4*a-1}x+{4*b}"]; random.shuffle(s)
        return m, d, s

def mat_denklem():
    tip = random.choice([1,2,3])
    if tip == 1:
        a=random.randint(2,7); b=random.randint(2,20); c=random.randint(2,7); d=random.randint(2,20)
        if a==c: a=c+1
        coz=(d-b)/(a-c); dogru = str(int(coz)) if coz==int(coz) else f"{coz:.1f}"
        m = f"{a}x+{b} = {c}x+{d} denkleminin çözümü kaçtır?"
    elif tip == 2:
        a=random.randint(2,8); b=random.randint(1,12); c=random.randint(2,8); d=random.randint(2,15)
        coz = (a*b + d)/(a-c) if a!=c else random.randint(1,15)
        dogru = str(int(coz)) if coz==int(coz) else f"{coz:.1f}"
        m = f"{a}(x-{b}) = {c}x+{d} denkleminin çözümü kaçtır?"
    else:
        a=random.randint(1,6); b=random.randint(1,12); dogru=str(b)
        m = f"Bir sayının {a} katının {b} fazlası, aynı sayının {a+1} katına eşittir. Sayı kaçtır?"
    y = [str(float(dogru)+i) for i in [-3,-2,2,3] if float(dogru)+i != float(dogru)][:3]
    s = [dogru] + y; random.shuffle(s)
    return m, dogru, s

def mat_oran():
    tip = random.choice([1,2,3])
    if tip == 1:
        a=random.randint(2,12); b=random.randint(2,12); k=random.randint(2,7)
        x=b*k; d=str(x)
        m = f"{a}/{b} = {a*k}/x orantısında x kaçtır?"
        s = [d, str(x+random.randint(1,4)), str(x-random.randint(1,4)), str(x+random.randint(5,8))]; random.shuffle(s)
        return m, d, s
    else:
        k=random.randint(3,9); e=random.randint(3,9); toplam=random.randint(40,90)
        kiz=int(k/(k+e)*toplam); d=str(kiz)
        m = f"Bir sınıfta kızların erkeklere oranı {k}/{e}'tir. Sınıf mevcudu {toplam} ise kız sayısı kaçtır?"
        s = [d, str(kiz+random.randint(2,5)), str(kiz-random.randint(2,5)), str(kiz+random.randint(1,3))]; random.shuffle(s)
        return m, d, s

def mat_yuzde():
    tip = random.choice([1,2,3])
    s=random.randint(150,600); y=random.choice([10,15,20,25,30,40,50,60])
    if tip == 1:
        son=int(s*y/100); d=str(son)
        m = f"{s} TL'lik bir ürüne %{y} indirim yapılıyor. İndirim miktarı kaç TL'dir?"
    elif tip == 2:
        son=int(s*(100-y)/100); d=str(son)
        m = f"{s} TL'ye %{y} indirim uygulanırsa ödenecek tutar kaç TL olur?"
    else:
        son=int(s*(100+y)/100); d=str(son)
        m = f"{s} TL'ye %{y} zam yapılırsa yeni fiyat kaç TL olur?"
    s = [d, str(son+random.randint(4,10)), str(son-random.randint(4,10)), str(son+random.randint(1,3))]; random.shuffle(s)
    return m, d, s

def mat_aci():
    a=random.randint(30,160); tip=random.choice(["tümler","bütünler"])
    if tip=="tümler": d=str(90-a); m=f"{a}°'lik açının tümleri kaç derecedir?"
    else: d=str(180-a); m=f"{a}°'lik açının bütünleri kaç derecedir?"
    s = [d, str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]; random.shuffle(s)
    return m, d, s

def mat_cokgen():
    k=random.randint(3,9); tip=random.choice(["iç","dış","köşegen"])
    if tip=="iç": d=str((k-2)*180); m=f"{k} kenarlı bir çokgenin iç açıları toplamı kaç derecedir?"
    elif tip=="dış": d=str(int(360/k)); m=f"Düzgün {k} kenarlı bir çokgenin bir dış açısı kaç derecedir?"
    else: d=str(k*(k-3)//2); m=f"{k} kenarlı bir çokgenin köşegen sayısı kaçtır?"
    s = [d, str(int(d)+random.randint(10,35)), str(int(d)-random.randint(10,35)), str(int(d)+random.randint(5,10))]; random.shuffle(s)
    return m, d, s

def mat_cember():
    r=random.randint(3,18); tip=random.choice(["çevre","alan","çap"]); pi=3
    if tip=="çevre": d=str(2*pi*r); m=f"Yarıçapı {r} cm olan çemberin çevresi kaç cm'dir? (π=3)"
    elif tip=="alan": d=str(pi*r*r); m=f"Yarıçapı {r} cm olan dairenin alanı kaç cm²'dir? (π=3)"
    else: d=str(2*r); m=f"Yarıçapı {r} cm olan çemberin çapı kaç cm'dir?"
    s = [d, str(int(d)+random.randint(5,18)), str(int(d)-random.randint(5,18)), str(int(d)+random.randint(1,5))]; random.shuffle(s)
    return m, d, s

def mat_veri():
    v=[random.randint(10,100) for _ in range(6)]; ort=sum(v)//6; med=sorted(v)[2]; ac=max(v)-min(v)
    tip=random.choice(["ortalama","medyan","açıklık"])
    if tip=="ortalama": d=str(ort); m=f"{v} veri grubunun aritmetik ortalaması kaçtır?"
    elif tip=="medyan": d=str(med); m=f"{v} veri grubunun medyanı (ortanca) kaçtır?"
    else: d=str(ac); m=f"{v} veri grubunun açıklığı kaçtır?"
    s = [d, str(int(d)+random.randint(2,8)), str(int(d)-random.randint(2,8)), str(int(d)+random.randint(1,3))]; random.shuffle(s)
    return m, d, s

def mat_cisim():
    c=random.choice(["küp","dikdörtgen prizma","küre","silindir","kare prizma"])
    if c=="küp": return "Bir küpün kaç ayrıtı vardır?", "12", ["8","10","12","14"]
    elif c=="dikdörtgen prizma": return "Dikdörtgen prizmanın kaç yüzü vardır?", "6", ["4","5","6","8"]
    elif c=="küre": return "Kürenin kaç köşesi vardır?", "0", ["0","1","2","4"]
    elif c=="silindir": return "Silindirin yan yüzeyi açıldığında hangi şekil oluşur?", "Dikdörtgen", ["Kare","Üçgen","Dikdörtgen","Daire"]
    else: return "Kare prizmanın kaç ayrıtı vardır?", "12", ["8","10","12","14"]

# ==================== FEN BİLİMLERİ - ZOR UZUN SORULAR ====================
def fen_gunes():
    sorular = [
        ("Güneş sisteminin en büyük gezegeni olan Jüpiter'in kaç uydusu olduğu tahmin edilmektedir? (yaklaşık)", "80", ["60","70","80","90"]),
        ("Dünya'nın Güneş etrafında tam bir tur atması kaç gün sürer? (365 değil, tam değer)", "365.242", ["365.0","365.242","365.25","366"]),
        ("Bir uzay aracı Dünya'da 600 N ağırlığındaysa Ay'da kaç N olur? (g_Ay = 1.62 m/s²)", "99", ["90","99","108","120"]),
        ("Güneş'in yüzey sıcaklığı yaklaşık kaç °C'dir?", "5500", ["5000","5500","6000","6500"]),
        ("Samanyolu Galaksisi'nin şekli nedir?", "Sarmal", ["Eliptik","Sarmal","Düzensiz","Çubuklu sarmal"]),
        ("En sıcak gezegen Venüs'ün yüzey sıcaklığı yaklaşık kaç °C'dir?", "460", ["400","430","460","500"]),
    ]
    return random.choice(sorular)

def fen_hucre():
    sorular = [
        ("Mitoz bölünme sonucunda bir hücreden iki hücre oluşur. Bir insan hücresi (2n=46) art arda 3 mitoz geçirirse toplam kaç kromozom oluşur? (tüm hücrelerdeki kromozom toplamı)", "368", ["184","276","368","460"]),
        ("Hücre zarında bulunan ve madde geçişini kontrol eden proteinlere ne ad verilir?", "Taşıyıcı protein", ["Porin","Taşıyıcı protein","Kanal proteini","Reseptör"]),
        ("Mayoz bölünme sırasında homolog kromozomların birbirine sarılmasına ne denir?", "Sinapsis", ["Krossing over","Sinapsis","Tetrat","Mayoz I"]),
        ("Bitki hücresinde bulunup hayvan hücresinde bulunmayan organel hangisidir?", "Kloroplast", ["Mitokondri","Kloroplast","Ribozom","Golgi"]),
        ("Hücre iskeletini oluşturan protein lifleri hangisidir?", "Mikrotübül", ["Aktin","Mikrotübül","İntermediate filament","Keratin"]),
    ]
    return random.choice(sorular)

def fen_kuvvet():
    k=random.randint(5,30); v=random.randint(3,15); ke=int(0.5*k*v*v)
    sorular = [
        (f"Kütlesi {k} kg olan bir araç {v} m/s hızla giderken fren yaparak duruyor. Frenleme sırasında açığa çıkan ısı enerjisi kaç Joule'dür? (Kinetik enerji değişimi)", str(ke), [str(ke-20), str(ke+30), str(ke+15), str(ke-10)]),
        ("Bir cismin potansiyel enerjisi 500 J, yüksekliği 10 m ise kütlesi kaç kg'dır? (g=10 N/kg)", "5", ["3","4","5","6"]),
        ("Yay sabiti 250 N/m olan bir yay 0,4 m sıkıştırıldığında yayda depolanan enerji kaç J olur?", "20", ["15","20","25","30"]),
        ("Sürtünmeli yatay düzlemde 20 N kuvvetle çekilen 5 kg kütleli cisim sabit hızla hareket ediyorsa sürtünme katsayısı kaçtır? (g=10)", "0.4", ["0.2","0.3","0.4","0.5"]),
    ]
    return random.choice(sorular)

def fen_madde():
    sorular = [
        ("Tuz oranı %15 olan 200 g çözeltiye 40 g tuz eklenirse yeni tuz oranı yüzde kaç olur?", "29.2", ["25","27.5","29.2","31.8"]),
        ("Yoğunluğu 0,8 g/cm³ olan 200 cm³ sıvı ile yoğunluğu 1,2 g/cm³ olan 300 cm³ sıvı karıştırılıyor. Karışımın yoğunluğu kaç g/cm³ olur?", "1.04", ["0.96","1.00","1.04","1.08"]),
        ("Bir elementin periyodik tablodaki yeri 3. periyot 7A grubu ise bu element nedir?", "Klor", ["Flor","Klor","Brom","İyot"]),
        ("Homojen karışımlar için aşağıdakilerden hangisi yanlıştır?", "Işık saçarlar", ["Tek fazlıdır","Işık saçarlar","Bileşenleri ayrılamaz","Belirli bir formülü yoktur"]),
    ]
    return random.choice(sorular)

def fen_isik():
    sorular = [
        ("Işığın bir ortamdan başka bir ortama geçerken doğrultu değiştirmesi olayına kırılma denir. Bir ışık ışınının havadan suya gelme açısı 45°, kırılma açısı 32° ise suyun kırılma indisi nedir? (sin45=0.707, sin32=0.530)", "1.33", ["1.00","1.33","1.50","1.62"]),
        ("Bir aynada oluşan görüntü sanal, düz ve cisimle aynı boyda ise ayna türü nedir?", "Düzlem ayna", ["Çukur ayna","Tümsek ayna","Düzlem ayna","Parabolik ayna"]),
        ("Beyaz ışığın prizmadan geçerken renklerine ayrılması olayına ne denir?", "Dağılma", ["Yansıma","Kırılma","Dağılma","Girişim"]),
        ("Bir merceğin odak uzaklığı 20 cm ise optik gücü kaç diyoptridir?", "5", ["2","3","4","5"]),
    ]
    return random.choice(sorular)

def fen_ureme():
    sorular = [
        ("Kurbağa yumurtalarından çıkan larvalara ne ad verilir?", "İribaş", ["Yavru","İribaş","Sperm","Larva"]),
        ("Bitkilerde çiçek tozlarının dişicik tepesine taşınması olayına ne denir?", "Tozlaşma", ["Döllenme","Tozlaşma","Çimlenme","Polinasyon"]),
        ("İnsanda embriyonun rahime yerleşmesine ne denir?", "İmplantasyon", ["Ovulasyon","İmplantasyon","Gastrulasyon","Fertilizasyon"]),
        ("Kelebek gelişiminde pupa evresinden çıkan canlıya ne denir?", "İmago", ["Larva","Pupa","İmago","Yumurta"]),
    ]
    return random.choice(sorular)

def fen_elektrik():
    r1=random.randint(3,8); r2=random.randint(4,9); r3=random.randint(2,7)
    seri=r1+r2+r3; paralel=round(1/(1/r1+1/r2+1/r3),1)
    sorular = [
        (f"{r1}Ω, {r2}Ω ve {r3}Ω'luk üç direnç seri bağlanırsa eşdeğer direnç kaç Ω olur?", str(seri), [str(seri-2), str(seri+1), str(seri+3), str(seri-1)]),
        (f"{r1}Ω, {r2}Ω ve {r3}Ω'luk üç direnç paralel bağlanırsa eşdeğer direnç kaç Ω olur?", str(paralel), [str(paralel+0.5), str(paralel-0.5), str(paralel+1), str(paralel-1)]),
        ("Bir elektrik devresinde 12 V'luk bir pil üzerinden 2 A akım geçiyorsa devrenin toplam direnci kaç Ω'dur?", "6", ["4","5","6","7"]),
        ("Bir ampulün üzerinde 60 W, 220 V yazıyorsa ampulün direnci yaklaşık kaç Ω'dur?", "807", ["600","700","800","900"]),
    ]
    return random.choice(sorular)

# ==================== TÜRKÇE - UZUN PARAGRAFLI ZOR SORULAR ====================
def tur_paragraf():
    m = "Sanat, insanlığın en eski ifade biçimlerinden biridir. Mağara duvarlarına çizilen resimlerden günümüzün dijital sanatına kadar uzanan bu serüven, insanın kendini ifade etme arzusunun bir yansımasıdır. Sanat, sadece güzel olanı değil, aynı zamanda çirkin olanı, acıyı, sevinci, umudu ve umutsuzluğu da anlatır. Bu yönüyle sanat, toplumların aynasıdır. Bir toplumun değer yargılarını, inançlarını, korkularını ve hayallerini sanat eserlerinde okumak mümkündür.\n\n**Bu parçada vurgulanmak istenen ana düşünce nedir?**"
    d = "Sanat, toplumların aynasıdır"
    s = ["Sanat sadece güzel olanı anlatır", "Sanat, toplumların aynasıdır", "Sanat tarihi mağaralarla başlar", "Dijital sanat en gelişmiş sanattır"]
    random.shuffle(s)
    return m, d, s

def tur_sozcuk():
    sorular = [
        ("'Soğuk' kelimesinin zıt anlamlısı nedir?", "sıcak", ["sıcak","buzlu","donuk","serin"]),
        ("Eş sesli (sesteş) kelime örneği hangisidir?", "yüz", ["kalem","silgi","yüz","defter"]),
        ("'Yüzmek' kelimesi aşağıdaki cümlelerin hangisinde mecaz anlamda kullanılmıştır?", "Paralar içinde yüzüyor", ["Denizde yüzdü","Paralar içinde yüzüyor","Yüzmeyi çok sever","Nehirde yüzdü"]),
    ]
    return random.choice(sorular)

# ==================== SOSYAL BİLGİLER - ZOR SORULAR ====================
def sos_kultur():
    m = "UNESCO Dünya Mirası Listesi'nde yer alan Kapadokya, benzersiz peri bacaları ve yeraltı şehirleriyle ünlüdür. Bölgedeki volkanik tüflerin erozyonu sonucu oluşan bu oluşumlar, binlerce yıl boyunca farklı medeniyetlere ev sahipliği yapmıştır. Hristiyanlığın ilk dönemlerinde bu mağaralar ve yeraltı şehirleri, Hristiyanlar için bir sığınak ve ibadet yeri olmuştur. Ayrıca bölgede bulunan Göreme Açık Hava Müzesi, bu döneme ait freskleriyle dikkat çeker.\n\n**Kapadokya'nın UNESCO Dünya Mirası Listesi'ne alınmasının temel nedeni aşağıdakilerden hangisidir?**"
    d = "Doğal güzelliğinin yanı sıra tarihi ve kültürel önemi"
    s = ["Sadece doğal güzelliği", "Sadece yeraltı şehirleri", "Doğal güzelliği ve tarihi-kültürel değeri", "Freskleri ve ibadethaneleri"]
    random.shuffle(s)
    return m, d, s

# ==================== TÜM DERSLERİ BİRLEŞTİR ====================
tum_dersler = {
    "Matematik": {
        "Tam Sayılar": mat_tam,
        "Rasyonel Sayılar": mat_rasyonel,
        "Rasyonel İşlemler": mat_rasyonel_islem,
        "Cebirsel İfadeler": mat_cebirsel,
        "Denklemler": mat_denklem,
        "Oran-Orantı": mat_oran,
        "Yüzdeler": mat_yuzde,
        "Açılar": mat_aci,
        "Çokgenler": mat_cokgen,
        "Çember": mat_cember,
        "Veri Analizi": mat_veri,
        "Cisimler": mat_cisim
    },
    "Fen Bilimleri": {
        "Güneş Sistemi": fen_gunes,
        "Hücre": fen_hucre,
        "Kuvvet": fen_kuvvet,
        "Karışımlar": fen_madde,
        "Işık": fen_isik,
        "Üreme": fen_ureme,
        "Elektrik": fen_elektrik
    },
    "Türkçe": {
        "Paragrafta Anlam": tur_paragraf,
        "Sözcükte Anlam": tur_sozcuk
    },
    "Sosyal Bilgiler": {
        "Kültür ve Miras": sos_kultur
    }
}

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### 📊 SKOR")
    c1,c2 = st.columns(2)
    c1.metric("✅ Doğru", st.session_state.dogru)
    c2.metric("❌ Yanlış", st.session_state.yanlis)
    st.metric("🏆 Puan", st.session_state.puan)
    st.markdown("---")
    if st.button("🗑️ TÜM İSTATİSTİKLERİ SIFIRLA", use_container_width=True):
        sifirla()
    st.markdown("---")
    if st.session_state.secili_ders is None:
        sec_ders = st.selectbox("📚 Ders Seç", list(tum_dersler.keys()))
        if st.button("🚀 BAŞLA", use_container_width=True):
            st.session_state.secili_ders = sec_ders
            st.rerun()
    else:
        st.success(f"**{st.session_state.secili_ders}**")
        konular = list(tum_dersler[st.session_state.secili_ders].keys())
        sec_konu = st.selectbox("📌 Konu Seç", konular)
        if st.button("🎲 YENİ SORU", use_container_width=True):
            fonk = tum_dersler[st.session_state.secili_ders][sec_konu]
            m,d,s = fonk()
            st.session_state.aktif_soru = m
            st.session_state.aktif_cevap = d
            st.session_state.aktif_siklar = s
            st.session_state.mesajlar.append({
                "rol": "asistan",
                "icerik": f"**{st.session_state.secili_ders} - {sec_konu}**\n\n{m}\n\nA) {s[0]}\nB) {s[1]}\nC) {s[2]}\nD) {s[3]}"
            })
            st.rerun()
        if st.button("🔄 DERS DEĞİŞTİR", use_container_width=True):
            st.session_state.secili_ders = None
            st.session_state.aktif_soru = None
            st.rerun()

# ==================== ANA ALAN ====================
if st.session_state.secili_ders is None:
    st.info("🎓 **Başlamak için sol panelden ders ve konu seçin!**")
else:
    for msg in st.session_state.mesajlar:
        with st.chat_message(msg["rol"]):
            st.markdown(msg["icerik"])
    if st.session_state.aktif_soru:
        cevap = st.chat_input("Cevabını yaz (A, B, C, D):")
        if cevap:
            st.session_state.mesajlar.append({"rol": "kullanici", "icerik": cevap})
            harf_map = {"A":0,"B":1,"C":2,"D":3}
            if cevap.strip().upper() in harf_map:
                k_sec = st.session_state.aktif_siklar[harf_map[cevap.strip().upper()]]
            else:
                k_sec = cevap.strip()
            if k_sec == st.session_state.aktif_cevap:
                st.session_state.dogru += 1
                st.session_state.puan += 10
                yanit = f"✅ **DOĞRU!** +10 puan\n\n**Doğru:** {st.session_state.dogru} | **Yanlış:** {st.session_state.yanlis} | **Puan:** {st.session_state.puan}"
            else:
                st.session_state.yanlis += 1
                yanit = f"❌ **YANLIŞ!** Doğru cevap: **{st.session_state.aktif_cevap}**\n\n**Doğru:** {st.session_state.dogru} | **Yanlış:** {st.session_state.yanlis} | **Puan:** {st.session_state.puan}"
            st.session_state.mesajlar.append({"rol": "asistan", "icerik": yanit})
            st.session_state.aktif_soru = None
            st.rerun()
