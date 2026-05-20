import streamlit as st
import random
import math

st.set_page_config(page_title="NumNum Zeka", page_icon="🎯")
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0a0f1f 0%, #0f172a 100%); }
    .stMarkdown, .stText, div, p, span, .stMetric label { color: #ffffff !important; }
    .stSelectbox > div > div { background-color: #1e293b !important; color: white !important; border-radius: 10px; border: 1px solid #3b82f6; }
    .stSelectbox label, .stSelectbox .st-ae { color: #000000 !important; }
    div[data-baseweb="select"] ul { background-color: #1e293b !important; }
    div[data-baseweb="select"] li { color: white !important; background-color: #1e293b !important; }
    div[data-baseweb="select"] li:hover { background-color: #3b82f6 !important; }
    .css-1d391kg h3, section[data-testid="stSidebar"] h3, div[data-testid="stSidebar"] .stMarkdown h3 { color: #000000 !important; }
    .stButton button { background-color: #3b82f6; color: white; border-radius: 12px; font-weight: bold; width: 100%; border: none; }
    .stButton button:hover { background-color: #2563eb; transform: scale(1.01); }
    .stChatInput textarea { background-color: #1e293b; color: white; border-radius: 20px; border: 1px solid #334155; }
    .stChatMessage { background-color: #1e293b; border-radius: 20px; padding: 12px; margin: 8px 0; border-left: 4px solid #3b82f6; }
    .stMetric { background-color: #1e293b; border-radius: 20px; padding: 12px; text-align: center; }
    hr { border-color: #334155; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 NumNum Zeka - 7. Sınıf (LGS Hazırlık)")
st.markdown("**Tamamen dinamik soru üreteci – her seferinde yeni şablon ve yeni sayılar**")

# ========== OTURUM ==========
if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = []
if "aktif_soru" not in st.session_state:
    st.session_state.aktif_soru = None
    st.session_state.aktif_cevap = None
    st.session_state.aktif_siklar = None
if "secili_ders" not in st.session_state:
    st.session_state.secili_ders = None
if "puan" not in st.session_state:
    st.session_state.puan = 0
if "dogru" not in st.session_state:
    st.session_state.dogru = 0
if "yanlis" not in st.session_state:
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

# ==================== DİNAMİK SORU TİPİ ÜRETİCİLERİ ====================
# Her konu için 5 rastgele şablon tipi

def mat_tam_sayilar():
    tip = random.randint(1,5)
    if tip == 1:  # sıralı işlemler (dalgıç/termometre/asansör benzeri)
        b = random.randint(-80,-10); t = b
        adimlar = random.randint(3,7)
        for _ in range(adimlar):
            t += random.choice([-1,1]) * random.randint(5,40)
        m = f"{b} sayısına {adimlar} adımda {t-b} eklendi. Sonuç?"
        d = str(t)
    elif tip == 2:  # çok adımlı işlem
        a = random.randint(-30,30); b = random.randint(-30,30); c = random.randint(-30,30)
        op1 = random.choice(["+","-"]); op2 = random.choice(["+","-"])
        if op1 == "+": ara = a + b
        else: ara = a - b
        if op2 == "+": son = ara + c
        else: son = ara - c
        m = f"{a} {op1} {b} {op2} {c} işleminin sonucu?"
        d = str(son)
    elif tip == 3:  # işlem önceliği
        a = random.randint(2,9); b = random.randint(2,9); c = random.randint(2,9)
        d = random.choice(["+","-"]); e = random.choice(["x","/"])
        if e == "x": ara = b * c
        else: ara = b // c if b%c==0 else round(b/c,1)
        if d == "+": son = a + ara
        else: son = a - ara
        m = f"{a} {d} ( {b} {e} {c} ) işleminin sonucu?"
        d = str(int(son)) if son == int(son) else f"{son:.1f}"
    elif tip == 4:  # sayı doğrusu
        x = random.randint(-40,40); y = random.randint(-40,40)
        while y == x: y = random.randint(-40,40)
        d = str(abs(x-y))
        m = f"{x} ile {y} arası uzaklık?"
    else:  # sıcaklık farkı
        t1 = random.randint(-20,0); t2 = random.randint(5,35)
        d = str(t2 - t1)
        m = f"Sabah {t1}°C, öğlen {t2}°C. Fark?"
    y = set()
    while len(y) < 3:
        sapma = random.choice([-10,-7,-5,5,7,10,12])
        y.add(str(int(d)+sapma))
    siklar = [d] + list(y)
    random.shuffle(siklar)
    return m, d, siklar

def mat_rasyonel():
    tip = random.randint(1,5)
    if tip == 1:  # karşılaştırma
        p1 = random.randint(1,12); pd1 = random.randint(2,12)
        p2 = random.randint(1,12); pd2 = random.randint(2,12)
        if p1/pd1 > p2/pd2: d = ">"
        elif p1/pd1 < p2/pd2: d = "<"
        else: d = "="
        m = f"{p1}/{pd1} __ {p2}/{pd2}"
        s = [">","<","=","≠"]; random.shuffle(s)
        return m, d, s
    elif tip == 2:  # ondalık
        p = random.randint(1,15); pd = random.randint(2,15)
        v = p/pd; d = f"{v:.2f}"
        m = f"{p}/{pd} ondalık hali (2 basamak)?"
        y = [f"{v+0.1:.2f}", f"{v-0.1:.2f}", f"{v+0.05:.2f}"]; s=[d]+y; random.shuffle(s); return m,d,s
    elif tip == 3:  # kesir problemleri (pastacı)
        p = random.randint(1,8); pd = random.randint(2,9)
        kalan = 1 - p/pd; kisi = random.randint(4,8)
        pay = int((kalan/kisi)*100); payda=100
        for i in range(2,20):
            if pay%i==0 and payda%i==0: pay//=i; payda//=i
        d = f"{pay}/{payda}" if payda!=1 else str(pay)
        m = f"Pastanın {p}/{pd}'i yenmiş, kalan {kisi} kişiye paylaştırılırsa kişi başı?"
        s = [d, f"{pay+1}/{payda}", f"{pay-1}/{payda}", f"{pay}/{payda+1}"]; random.shuffle(s); return m,d,s
    elif tip == 4:  # genişletme
        p = random.randint(1,10); pd = random.randint(2,10); carp = random.randint(2,5)
        d = str((p*carp)+(pd*carp))
        m = f"{p}/{pd} kesrini {carp} ile genişletince pay+payda?"
        y = [str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]; s=[d]+y; random.shuffle(s); return m,d,s
    else:  # işlem (toplama/çıkarma/çarpma/bölme)
        p1 = random.randint(1,8); pd1 = random.randint(2,8)
        p2 = random.randint(1,8); pd2 = random.randint(2,8)
        op = random.choice(["+","-","x","/"])
        if op == "+": sp = p1*pd2 + p2*pd1; spd = pd1*pd2
        elif op == "-": sp = p1*pd2 - p2*pd1; spd = pd1*pd2
        elif op == "x": sp = p1*p2; spd = pd1*pd2
        else: sp = p1*pd2; spd = pd1*p2
        eb = math.gcd(sp,spd); sp//=eb; spd//=eb
        d = f"{sp}/{spd}" if spd!=1 else str(sp)
        m = f"{p1}/{pd1} {op} {p2}/{pd2} = ?"
        s = [d, f"{sp+1}/{spd}", f"{sp-1}/{spd}", f"{sp}/{spd+1}"]; random.shuffle(s); return m,d,s

def mat_cebirsel():
    tip = random.randint(1,5)
    if tip == 1:  # toplama/çıkarma
        a = random.randint(1,5); b = random.randint(-8,8); c = random.randint(1,5); d = random.randint(-8,8)
        op = random.choice(["+","-"])
        if op == "+": son = f"{a+c}x + {b+d}"
        else: son = f"{a-c}x + {b-d}"
        m = f"({a}x{b:+d}) {op} ({c}x{d:+d}) = ?"
        s = [son, f"{a+c+1}x+{b+d}", f"{a+c}x+{b+d+1}", f"{a+c-1}x+{b+d}"]; random.shuffle(s); return m,son,s
    elif tip == 2:  # değer bulma
        a = random.randint(2,6); b = random.randint(1,10); x = random.randint(1,5)
        son = a*x + b; d = str(son)
        m = f"{a}x+{b}, x={x} için değeri?"
        s = [d, str(son+random.randint(2,5)), str(son-random.randint(2,5)), str(son+random.randint(1,2))]; random.shuffle(s); return m,d,s
    elif tip == 3:  # çevre
        a = random.randint(2,5); b = random.randint(1,8); d = f"{4*a}x+{4*b}"
        m = f"({a}x+{b}) kenarlı karenin çevresi?"
        s = [d, f"{4*a+1}x+{4*b}", f"{4*a}x+{4*b+1}", f"{4*a-1}x+{4*b}"]; random.shuffle(s); return m,d,s
    elif tip == 4:  # alan (dikdörtgen)
        a = random.randint(2,4); b = random.randint(1,5); c = random.randint(2,4); d = random.randint(1,5)
        son = f"({a*c})x² + ({a*d + b*c})x + {b*d}"
        m = f"({a}x+{b}) * ({c}x+{d}) çarpımı?"
        s = [son, f"{son[:-1]}+1", f"{son[:-1]}-1", f"{son[:-1]}+2"]; random.shuffle(s); return m,son,s
    else:  # sadeleştirme
        a = random.randint(2,8); b = random.randint(2,8)
        d = f"{a//math.gcd(a,b)}x / {b//math.gcd(a,b)}"
        m = f"{a}x / {b} sadeleştirilmiş hali?"
        s = [d, f"{a//math.gcd(a,b)+1}x/{b//math.gcd(a,b)}", f"{a//math.gcd(a,b)}x/{b//math.gcd(a,b)+1}", f"{a//math.gcd(a,b)-1}x/{b//math.gcd(a,b)}"]; random.shuffle(s); return m,d,s

def mat_denklem():
    tip = random.randint(1,5)
    if tip == 1:  # temel denklem
        a = random.randint(2,5); b = random.randint(2,15); c = random.randint(2,5); d = random.randint(2,15)
        if a == c: a += 1
        coz = (d-b)/(a-c); d_str = str(int(coz)) if coz==int(coz) else f"{coz:.1f}"
        m = f"{a}x + {b} = {c}x + {d}"
    elif tip == 2:  # parantezli
        a = random.randint(2,6); b = random.randint(1,10); c = random.randint(2,6); d = random.randint(1,12)
        coz = (a*b + d)/(a-c) if a!=c else random.randint(1,10)
        d_str = str(int(coz)) if coz==int(coz) else f"{coz:.1f}"
        m = f"{a}(x - {b}) = {c}x + {d}"
    elif tip == 3:  # sözel problem
        a = random.randint(1,5); b = random.randint(1,10); d_str = str(b)
        m = f"Bir sayının {a} katının {b} fazlası, {a+1} katına eşit. Sayı?"
    elif tip == 4:  # kesirli denklem
        a = random.randint(2,6); b = random.randint(1,12); c = random.randint(2,5)
        coz = c*b - a; d_str = str(coz)
        m = f"(x + {a}) / {b} = {c}"
    else:  # iki tarafta x
        a = random.randint(2,5); b = random.randint(1,10); c = random.randint(2,5)
        coz = (c-b)/a if a!=0 else 1; d_str = str(int(coz)) if coz==int(coz) else f"{coz:.1f}"
        m = f"{a}x + {b} = {c}"
    y = [str(float(d_str)+i) for i in [-3,-2,2,3] if float(d_str)+i != float(d_str)][:3]
    s = [d_str] + y; random.shuffle(s)
    return m, d_str, s

def mat_oran():
    tip = random.randint(1,5)
    if tip == 1:  # doğru orantı
        a = random.randint(2,10); b = random.randint(2,10); k = random.randint(2,6)
        x = b*k; d = str(x)
        m = f"{a}/{b} = {a*k}/x → x=?"
        s = [d, str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(4,6))]; random.shuffle(s); return m,d,s
    elif tip == 2:  # ters orantı
        a = random.randint(2,8); b = random.randint(2,8); x = a*b
        d = str(x)
        m = f"{a} işçi işi {b} günde bitiriyorsa, {a*b} işçi kaç günde bitirir?"
        s = [d, str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(2,4))]; random.shuffle(s); return m,d,s
    elif tip == 3:  # sınıf oranı
        k = random.randint(3,8); e = random.randint(3,8); toplam = random.randint(40,80)
        kiz = int(k/(k+e)*toplam); d = str(kiz)
        m = f"Kız/erkek oranı {k}/{e}, mevcut {toplam} → kız sayısı?"
        s = [d, str(kiz+random.randint(2,5)), str(kiz-random.randint(2,5)), str(kiz+random.randint(1,3))]; random.shuffle(s); return m,d,s
    elif tip == 4:  # harita ölçeği
        gercek = random.randint(100,500); olcek = random.choice([10000,25000,50000,100000])
        harita = gercek * 100000 / olcek
        d = f"{harita:.1f}"
        m = f"Ölçek 1/{olcek} olan haritada {gercek} km gerçek uzunluk kaç cm'dir?"
        s = [d, f"{float(d)+0.5:.1f}", f"{float(d)-0.5:.1f}", f"{float(d)+0.2:.1f}"]; random.shuffle(s); return m,d,s
    else:  # zincir orantı
        a = random.randint(2,6); b = random.randint(2,6); c = random.randint(2,6)
        d = f"{a}/{c}"
        m = f"a/b = {a}/{b}, b/c = {b}/{c} ise a/c?"
        s = [d, f"{a+1}/{c}", f"{a}/{c+1}", f"{a-1}/{c}"]; random.shuffle(s); return m,d,s

def mat_yuzde():
    tip = random.randint(1,5)
    sayi = random.randint(150,600); yuzde = random.choice([10,15,20,25,30,40,50,60])
    if tip == 1: son = int(sayi*yuzde/100); d = str(son); m = f"{sayi} TL'nin %{yuzde} indirimi?"
    elif tip == 2: son = int(sayi*(100-yuzde)/100); d = str(son); m = f"{sayi} TL'ye %{yuzde} indirimli fiyat?"
    elif tip == 3: son = int(sayi*(100+yuzde)/100); d = str(son); m = f"{sayi} TL'ye %{yuzde} zam yapılırsa fiyat?"
    elif tip == 4: # kâr-zarar
        maliyet = random.randint(100,300); kar = random.randint(10,50)
        d = str(int(maliyet*(100+kar)/100)); m = f"Maliyet {maliyet} TL, %{kar} kârla satış fiyatı?"
    else: # iskonto sonrası
        etiket = random.randint(200,500); indirim = random.randint(10,40)
        d = str(int(etiket*(100-indirim)/100)); m = f"{etiket} TL etiketli ürüne %{indirim} indirimli fiyat?"
    s = [d, str(int(d)+random.randint(4,10)), str(int(d)-random.randint(4,10)), str(int(d)+random.randint(1,3))]; random.shuffle(s)
    return m, d, s

def mat_aci():
    tip = random.randint(1,5)
    a = random.randint(30,150)
    if tip == 1: d = str(90-a); m = f"{a}°'nin tümleri?"
    elif tip == 2: d = str(180-a); m = f"{a}°'nin bütünleri?"
    elif tip == 3: # komşu bütünler
        d = str(180 - a); m = f"{a}°'nin bütünlerinin tümleri kaç derece?"
        d = str(90 - (180-a))
    elif tip == 4: # ters açı
        d = str(a); m = f"{a}°'nin ters açısı kaç derece?"
    else: # tümlerin bütünleri
        d = str(180 - (90-a)); m = f"{a}°'nin tümlerinin bütünleri kaç derece?"
    s = [d, str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]; random.shuffle(s)
    return m, d, s

def mat_cokgen():
    tip = random.randint(1,5)
    kenar = random.randint(3,8)
    if tip == 1: d = str((kenar-2)*180); m = f"{kenar} kenarlı iç açı toplamı?"
    elif tip == 2: d = str(int(360/kenar)); m = f"Düzgün {kenar} kenarlı dış açı?"
    elif tip == 3: d = str(kenar*(kenar-3)//2); m = f"{kenar} kenarlı köşegen sayısı?"
    elif tip == 4: # bir iç açı
        d = str(int((kenar-2)*180/kenar)); m = f"Düzgün {kenar} kenarlı bir iç açı?"
    else: # köşegen sayısı formülü
        d = str(kenar*(kenar-3)//2); m = f"{kenar} kenarlı çokgenin köşegen sayısı formülü?"
    s = [d, str(int(d)+random.randint(10,30)), str(int(d)-random.randint(10,30)), str(int(d)+random.randint(5,9))]; random.shuffle(s)
    return m, d, s

def mat_cember():
    tip = random.randint(1,5)
    r = random.randint(3,15); pi=3
    if tip == 1: d = str(2*pi*r); m = f"Yarıçap {r} cm çember çevresi (π=3)?"
    elif tip == 2: d = str(pi*r*r); m = f"Yarıçap {r} cm daire alanı (π=3)?"
    elif tip == 3: d = str(2*r); m = f"Yarıçap {r} cm çemberin çapı?"
    elif tip == 4: # daire dilimi
        aci = random.randint(30,180)
        alan = pi*r*r * aci/360
        d = f"{alan:.1f}"; m = f"Yarıçap {r} cm, merkez açı {aci}° daire diliminin alanı (π=3)?"
    else: # çember yayı
        aci = random.randint(30,180)
        yay = 2*pi*r * aci/360
        d = f"{yay:.1f}"; m = f"Yarıçap {r} cm, merkez açı {aci}° çember yayının uzunluğu (π=3)?"
    s = [d, str(float(d)+random.randint(5,15)), str(float(d)-random.randint(5,15)), str(float(d)+random.randint(1,4))]; random.shuffle(s)
    return m, d, s

def mat_veri():
    tip = random.randint(1,5)
    v = [random.randint(10,90) for _ in range(5)]
    if tip == 1: d = str(sum(v)//5); m = f"{v} aritmetik ortalama?"
    elif tip == 2: d = str(sorted(v)[2]); m = f"{v} medyan?"
    elif tip == 3: d = str(max(v)-min(v)); m = f"{v} açıklık?"
    elif tip == 4: # mod
        mod = random.choice(v); d = str(mod); m = f"{v} mod (tepe değer) ?"
    else: # standart sapma basit
        ort = sum(v)/5; varyans = sum((x-ort)**2 for x in v)/5
        ss = round(varyans**0.5,1); d = str(ss); m = f"{v} standart sapması (yaklaşık)?"
    s = [d, str(float(d)+random.randint(2,6)), str(float(d)-random.randint(2,6)), str(float(d)+random.randint(1,2))]; random.shuffle(s)
    return m, d, s

def mat_cisim():
    tip = random.randint(1,5)
    if tip == 1: return "Küpün kaç ayrıtı vardır?", "12", ["8","10","12","14"]
    elif tip == 2: return "Dikdörtgen prizmanın kaç yüzü vardır?", "6", ["4","5","6","8"]
    elif tip == 3: return "Kürenin kaç köşesi vardır?", "0", ["0","1","2","4"]
    elif tip == 4: return "Silindirin yan yüzeyi açılınca hangi şekil olur?", "Dikdörtgen", ["Kare","Üçgen","Dikdörtgen","Daire"]
    else: return "Kare prizmanın kaç ayrıtı vardır?", "12", ["8","10","12","14"]

# ==================== FEN (her konu için 5 rastgele tip) ====================
def fen_gunes():
    tip = random.randint(1,5)
    if tip == 1: return "Güneş sisteminin en büyük gezegeni?", "Jüpiter", ["Mars","Satürn","Jüpiter","Uranüs"]
    elif tip == 2: return "Dünya'nın doğal uydusu?", "Ay", ["Mars","Ay","Venüs","Jüpiter"]
    elif tip == 3: return "Güneş'e en yakın gezegen?", "Merkür", ["Venüs","Merkür","Dünya","Mars"]
    elif tip == 4: return "Halkalarıyla ünlü gezegen?", "Satürn", ["Jüpiter","Satürn","Uranüs","Neptün"]
    else: return "En sıcak gezegen?", "Venüs", ["Merkür","Venüs","Dünya","Mars"]

def fen_hucre():
    tip = random.randint(1,5)
    if tip == 1: return "Mitoz bölünme sonucu kaç hücre oluşur?", "2", ["1","2","4","8"]
    elif tip == 2: return "Hücrenin yönetim merkezi?", "Çekirdek", ["Mitokondri","Çekirdek","Ribozom","Koful"]
    elif tip == 3: return "Mayoz bölünme nerede olur?", "Üreme ana hücrelerinde", ["Vücut hücrelerinde","Üreme ana hücrelerinde","Sinir hücrelerinde","Kas hücrelerinde"]
    elif tip == 4: return "Hücrenin enerji üreten organeli?", "Mitokondri", ["Mitokondri","Ribozom","Lizozom","Golgi"]
    else: return "Protein sentezi nerede yapılır?", "Ribozom", ["Mitokondri","Ribozom","Çekirdek","Koful"]

def fen_kuvvet():
    tip = random.randint(1,5)
    if tip == 1:
        k = random.randint(5,20); v = random.randint(2,10); ke = int(0.5*k*v*v)
        return f"Kütlesi {k} kg, hızı {v} m/s cismin kinetik enerjisi (J)?", str(ke), [str(ke+10), str(ke-10), str(ke+20)]
    elif tip == 2:
        return "Potansiyel enerji nelere bağlıdır?", "Kütle ve yükseklik", ["Kütle ve hız","Kütle ve yükseklik","Hız ve yükseklik"]
    elif tip == 3:
        return "Sürtünme kuvveti hangi yönde etki eder?", "Harekete zıt yönde", ["Hareket yönünde","Dikey","Yatay"]
    elif tip == 4:
        return "Bir cismin sahip olduğu hareket enerjisine ne denir?", "Kinetik enerji", ["Potansiyel enerji","Mekanik enerji","Isı enerjisi"]
    else:
        m = random.randint(2,10); h = random.randint(5,20); ep = m*10*h
        return f"{m} kg kütleli cisim {h} m yükseklikte (g=10) potansiyel enerji (J)?", str(ep), [str(ep+20), str(ep-20), str(ep+50)]

def fen_madde():
    tip = random.randint(1,5)
    if tip == 1: return "Homojen karışımlara ne denir?", "Çözelti", ["Süspansiyon","Emülsiyon","Çözelti","Kolloid"]
    elif tip == 2: return "Bir elementin en küçük yapı taşı?", "Atom", ["Molekül","Atom","Hücre","Tanecik"]
    elif tip == 3: return "Heterojen karışıma örnek?", "Ayran", ["Tuzlu su","Şekerli su","Ayran","Hava"]
    elif tip == 4: return "Saf maddeler kaç grupta incelenir?", "2", ["1","2","3","4"]
    else: return "Yoğunluğu 0,9 ve 1,1 olan sıvılar eşit hacimde karışırsa karışım yoğunluğu?", "1,0", ["0,9","1,0","1,1","2,0"]

def fen_isik():
    tip = random.randint(1,5)
    if tip == 1: return "Işığın geri dönmesine ne denir?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]
    elif tip == 2: return "Işığın doğrultu değiştirmesine ne denir?", "Kırılma", ["Yansıma","Kırılma","Soğurma","Girişim"]
    elif tip == 3: return "Işığın en hızlı yayıldığı ortam?", "Boşluk", ["Boşluk","Hava","Su","Cam"]
    elif tip == 4: return "Aynalar hangi prensiple çalışır?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]
    else: return "Mercekler hangi prensiple çalışır?", "Kırılma", ["Yansıma","Kırılma","Soğurma","Dağılma"]

def fen_ureme():
    tip = random.randint(1,5)
    if tip == 1: return "Kurbağa gelişimine ne denir?", "Başkalaşım", ["Metamorfoz","Başkalaşım","Döllenme","Büyüme"]
    elif tip == 2: return "Bitkilerde tohum oluşumu için gerekli olay?", "Tozlaşma", ["Döllenme","Tozlaşma","Çimlenme","Fotosentez"]
    elif tip == 3: return "Memelilerde yavruları besleyen bez?", "Süt bezi", ["Ter bezi","Yağ bezi","Süt bezi","Salya bezi"]
    elif tip == 4: return "İnsanda döllenme nerede olur?", "Fallop tüpü", ["Rahim","Yumurtalık","Fallop tüpü","Vajina"]
    else: return "Kelebek gelişimi hangi gruptadır?", "Başkalaşım", ["Metamorfoz","Başkalaşım","Döllenme","Büyüme"]

def fen_elektrik():
    tip = random.randint(1,5)
    if tip == 1:
        r1 = random.randint(2,5); r2 = random.randint(2,5)
        return f"{r1}Ω ve {r2}Ω seri bağlanırsa eşdeğer direnç?", str(r1+r2), [str(r1+r2+1), str(r1+r2-1), str(r1+r2+2)]
    elif tip == 2:
        r1 = random.randint(2,5); r2 = random.randint(2,5)
        return f"{r1}Ω ve {r2}Ω paralel bağlanırsa eşdeğer direnç?", str(round((r1*r2)/(r1+r2),1)), [str(round((r1*r2)/(r1+r2)+0.5,1)), str(round((r1*r2)/(r1+r2)-0.5,1)), str(round((r1*r2)/(r1+r2)+0.2,1))]
    elif tip == 3: return "Bir ampulün parlaklığını artırmak için ne yapılır?", "Pil sayısı artırılır", ["Pil sayısı azaltılır","Direnç eklenir","Kablo uzatılır"]
    elif tip == 4: return "Devrede akımı kontrol eden eleman?", "Anahtar", ["Pil","Direnç","Anahtar","Ampul"]
    else: return "Ohm yasası nedir?", "V=I.R", ["V=I/R","I=V.R","R=V.I","V=I+R"]

# ==================== TÜRKÇE (rastgele 5 tip) ====================
def tur_paragraf():
    tip = random.randint(1,5)
    if tip == 1:
        return "Ne kadar bilirsen bil, anlatabildiğin kadarsın. Bu cümlede vurgulanan?", "Bilginin aktarımı önemlidir", ["Bilgi her şey değildir","Anlatmak zordur","Sessizlik erdemdir"]
    elif tip == 2:
        return "Teknoloji hayatımızı kolaylaştırsa da bizi tembelleştiriyor. Ana fikir?", "Teknoloji tembelleştiriyor", ["Teknoloji yararlıdır","Teknoloji gereksizdir","Teknoloji hayatı kolaylaştırır"]
    elif tip == 3:
        return "Kitap okumak zihnin jimnastiğidir. Ana fikir?", "Kitap okumak zihni geliştirir", ["Kitap okumak zaman kaybıdır","Sadece çocuklar okumalı","Kitap okumak sıkıcıdır"]
    elif tip == 4:
        return "Sanat, insanın duygularını ifade etme biçimidir. Sanatın işlevi?", "Duyguları ifade etmek", ["Para kazanmak","Eğlenmek","Zaman geçirmek"]
    else:
        return "Çevre kirliliği geleceğimizi tehdit ediyor. Kaygı nedir?", "Gelecek nesiller", ["Bugünün rahatı","Ekonomik kazanç","Teknoloji"]

def tur_fiil():
    f = random.choice(["gelmek","gitmek","bakmak","yazmak","okumak"])
    d = f.replace("mek","").replace("mak","") + "yor"
    return f"'{f}' fiilinin şimdiki zaman 2. tekil kişisi?", d, [d, d+"m", d+"k", d+"n"]

def tur_zarf():
    cumle = random.choice([("Hızlı koştu", "hızlı"), ("Çok güzel olmuş", "çok"), ("Yarın geleceğim", "yarın")])
    m, d = cumle
    s = [d, "koştu", "güzel", "geleceğim"]
    random.shuffle(s)
    return f"'{m}' cümlesindeki zarf?", d, s

def tur_anlam():
    soru = random.choice([("'Keşke daha çok çalışsaydım.' anlamı?", "pişmanlık", ["özlem","kararlılık","şart"]),
                          ("'Bu işi yapabilir misin?' anlamı?", "rica/istek", ["emir","koşul","olasılık"]),
                          ("'Yağmur yağsa da topraklar ıslansa.' anlamı?", "özlem", ["pişmanlık","koşul","kararlılık"])])
    return soru

def tur_yazim():
    return "Aşağıdakilerden hangisi doğru?", "herkes", ["herkez","herkes","herkeş","herkese"]

def tur_noktalama():
    return "Sıralı cümleleri ayırmak için hangi işaret?", "Noktalı virgül", ["Virgül","Nokta","Noktalı virgül","İki nokta"]

def tur_sozcuk():
    return "'Soğuk' zıt anlamlısı?", "sıcak", ["sıcak","buzlu","donuk","serin"]

def tur_cumle():
    return "'Kitap okumayı çok severim.' yüklemin türü?", "İsim cümlesi", ["Fiil cümlesi","İsim cümlesi","Devrik cümle","Birleşik cümle"]

# ==================== SOSYAL (rastgele 5 tip) ====================
def sos_iletisim():
    return "Duygu,düşünce ve bilgilerin aktarılması?", "İletişim", ["Empati","İletişim","Hoşgörü","Saygı"]
def sos_tarih():
    soru = random.choice([("İlk Türk devletlerinden biri?", "Asya Hun Devleti", ["Osmanlı","Asya Hun","Bizans","Roma"]),
                          ("Osmanlı'da Lale Devri yeniliği?", "Matbaa", ["Matbaa","Fetih","Anayasa","Cumhuriyet"]),
                          ("TBMM açılış tarihi?", "23 Nisan 1920", ["19 Mayıs 1919","23 Nisan 1920","29 Ekim 1923","30 Ağustos 1922"]),
                          ("Cumhuriyet ilan tarihi?", "29 Ekim 1923", ["23 Nisan 1920","29 Ekim 1923","30 Ağustos 1922","1 Kasım 1922"])])
    return soru
def sos_nufus():
    return "Bir ülkede yaşayan insan sayısı?", "Nüfus", ["Nüfus yoğunluğu","Nüfus","Göç","Demografi"]
def sos_bilim():
    return "Matematik, fizik, kimya gibi disiplinler?", "Bilim", ["Teknoloji","Sanat","Bilim","Edebiyat"]
def sos_ekonomi():
    return "İhtiyaçları karşılamak için yapılan faaliyet?", "Üretim", ["Tüketim","Üretim","Pazarlama","Reklam"]
def sos_kultur():
    return "Bir topluma ait maddi manevi değerler bütünü?", "Kültür", ["Medeniyet","Kültür","Gelenek","Görenek"]
def sos_demokrasi():
    return "Halkın kendini yönettiği yönetim?", "Demokrasi", ["Monarşi","Oligarşi","Demokrasi","Teokrasi"]

# ==================== DERS BİRLEŞTİRME ====================
tum_dersler = {
    "Matematik": {
        "Tam Sayılar": mat_tam_sayilar,
        "Rasyonel Sayılar": mat_rasyonel,
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
        "Paragraf": tur_paragraf,
        "Fiiller": tur_fiil,
        "Zarflar": tur_zarf,
        "Cümlede Anlam": tur_anlam,
        "Yazım": tur_yazim,
        "Noktalama": tur_noktalama,
        "Sözcük": tur_sozcuk,
        "Cümle Türleri": tur_cumle
    },
    "Sosyal Bilgiler": {
        "İletişim": sos_iletisim,
        "Tarih": sos_tarih,
        "Nüfus": sos_nufus,
        "Bilim": sos_bilim,
        "Ekonomi": sos_ekonomi,
        "Kültür": sos_kultur,
        "Demokrasi": sos_demokrasi
    }
}

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### 📊 SKOR")
    c1, c2 = st.columns(2)
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
            m, d, s = fonk()
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
            st.session_state.mesajlar = []
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
