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
st.markdown("**Tüm konularda 10+ farklı soru tipi – sonsuz çeşitlilik**")

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

# ==================== MATEMATİK ====================
def mat_tam_sayilar():
    tip = random.randint(1,12)
    if tip == 1:
        b = random.randint(-80,-10); t = b; h = []
        for _ in range(random.randint(4,8)):
            a = random.randint(5,50)
            if random.choice([0,1]): t += a; h.append(f"{a} m yükseliyor")
            else: t -= a; h.append(f"{a} m dalıyor")
        m = f"Bir dalgıç {b} m'de iken " + ", ".join(h) + ". Son konum?"
        d = str(t)
    elif tip == 2:
        b = random.randint(-20,-5); artis = random.randint(3,15); saat = random.randint(3,7)
        t = b + artis * saat
        m = f"Sabah {b}°C, her saat {artis}°C artarsa {saat} saat sonra kaç °C?"
        d = str(t)
    elif tip == 3:
        s = random.randint(-50,50); t = s; isl = []
        for _ in range(random.randint(3,6)):
            a = random.randint(5,40)
            if random.choice([0,1]): t += a; isl.append(f"+{a}")
            else: t -= a; isl.append(f"-{a}")
        m = f"Ekran {s} iken " + ", ".join(isl) + " tuşlanıyor. Sonuç?"
        d = str(t)
    elif tip == 4:
        b = random.randint(-5,5); t = b
        for _ in range(random.randint(3,7)): t += random.randint(2,10) if random.choice([0,1]) else -random.randint(2,10)
        m = f"Asansör {b}. katta iken {random.randint(3,7)} hareket sonunda hangi kat?"
        d = str(t)
    elif tip == 5:
        maas = random.randint(3000,7000); gider = random.randint(1000, maas-500)
        m = f"Ali'nin maaşı {maas} TL, giderleri {gider} TL. Kalan?"
        d = str(maas - gider)
    elif tip == 6:
        b = random.randint(500,3000); t = b
        for _ in range(random.randint(3,6)): t += random.randint(100,800) if random.choice([0,1]) else -random.randint(100,800)
        m = f"Dağcı {b} m'de, {random.randint(3,6)} hareket sonunda yükseklik?"
        d = str(t)
    elif tip == 7:
        d_s = random.randint(15,25); y_s = random.randint(3,10); d_p = random.choice([4,5]); y_p = random.choice([-1,-2])
        toplam = d_s*d_p + y_s*y_p
        m = f"{d_s+y_s} soruluk sınav: {d_s} doğru (+{d_p}), {y_s} yanlış ({y_p}). Toplam puan?"
        d = str(toplam)
    elif tip == 8:
        a = random.randint(-30,30); b = random.randint(-30,30); c = random.randint(2,5); d = random.randint(-30,30)
        son = a + (b*c) - d
        m = f"{a} + {b} × {c} - {d} = ? (işlem önceliğine dikkat)"
        d = str(son)
    elif tip == 9:
        x = random.randint(-40,40); y = random.randint(-40,40)
        while y == x: y = random.randint(-40,40)
        m = f"{x} ile {y} arasındaki uzaklık kaç birim?"
        d = str(abs(x-y))
    elif tip == 10:
        t1 = random.randint(-25,0); t2 = random.randint(5,35)
        m = f"Sabah {t1}°C, öğlen {t2}°C. Sıcaklık farkı?"
        d = str(t2 - t1)
    elif tip == 11:
        borc = random.randint(100,1000); odeme = random.randint(50, borc)
        m = f"{borc} TL borcun {odeme} TL'si ödenirse kalan borç?"
        d = str(borc - odeme)
    else:
        fiyat = random.randint(100,1000); oran = random.randint(5,30)
        if random.choice([0,1]): d = str(int(fiyat * (100 - oran) / 100)); m = f"{fiyat} TL'ye %{oran} indirimli fiyat?"
        else: d = str(int(fiyat * (100 + oran) / 100)); m = f"{fiyat} TL'ye %{oran} zam yapılırsa fiyat?"
    yanlis = set()
    while len(yanlis) < 3:
        sapma = random.choice([-15,-10,-8,8,10,15,20])
        y = int(d) + sapma
        if y != int(d): yanlis.add(str(y))
    siklar = [d] + list(yanlis)
    random.shuffle(siklar)
    return m, d, siklar

def mat_rasyonel():
    tip = random.randint(1,6)
    if tip == 1:
        p1 = random.randint(1,12); pd1 = random.randint(2,12); p2 = random.randint(1,12); pd2 = random.randint(2,12)
        if p1/pd1 > p2/pd2: d = ">"; y = ["<","=","≠"]
        elif p1/pd1 < p2/pd2: d = "<"; y = [">","=","≠"]
        else: d = "="; y = [">","<","≠"]
        return f"{p1}/{pd1} __ {p2}/{pd2} yerine ne gelir?", d, y
    elif tip == 2:
        p = random.randint(1,15); pd = random.randint(2,15); v = p/pd
        d = f"{v:.2f}"
        return f"{p}/{pd} ondalık gösterimi (2 basamak)?", d, [f"{v+0.1:.2f}", f"{v-0.1:.2f}", f"{v+0.05:.2f}"]
    elif tip == 3:
        p = random.randint(1,10); pd = random.randint(2,10); kalan = 1 - (p/pd); kisi = random.randint(4,8)
        pay = int((kalan/kisi)*100); payda = 100
        for i in range(2,20):
            if pay%i==0 and payda%i==0: pay//=i; payda//=i
        d = f"{pay}/{payda}" if payda!=1 else str(pay)
        return f"Pastanın {p}/{pd}'i yenmiş. Kalan {kisi} kişiye paylaştırılırsa kişi başı?", d, [f"{pay+1}/{payda}", f"{pay-1}/{payda}", f"{pay}/{payda+1}"]
    elif tip == 4:
        p = random.randint(1,12); pd = random.randint(2,12); carp = random.randint(2,6)
        yp = p*carp; ypd = pd*carp
        d = str(yp + ypd)
        return f"{p}/{pd} kesrini {carp} ile genişletince pay+payda toplamı?", d, [str(int(d)+random.randint(5,20)), str(int(d)-random.randint(5,20)), str(int(d)+random.randint(1,4))]
    elif tip == 5:
        p = random.randint(2,9); pd = random.randint(2,9); carp = random.randint(2,4)
        if p % carp == 0 and pd % carp == 0:
            yp = p // carp; ypd = pd // carp
            d = str(yp + ypd)
        else:
            d = str(random.randint(2,10))
        return f"{p}/{pd} kesrini {carp} ile sadeleştirince pay ve payda toplamı?", d, [str(int(d)+random.randint(1,4)), str(int(d)-random.randint(1,4)), str(int(d)+random.randint(2,5))]
    else:
        p1 = random.randint(1,10); pd1 = random.randint(2,10); p2 = random.randint(1,10); pd2 = random.randint(2,10)
        fark = abs(p1/pd1 - p2/pd2)
        d = f"{fark:.2f}"
        return f"{p1}/{pd1} ile {p2}/{pd2} arasındaki fark (yaklaşık)?", d, [f"{fark+0.1:.2f}", f"{fark-0.1:.2f}", f"{fark+0.05:.2f}"]

def mat_rasyonel_islem():
    p1 = random.randint(1,8); pd1 = random.randint(2,8); p2 = random.randint(1,8); pd2 = random.randint(2,8)
    islem = random.choice(["+","-","x","/"])
    if islem == "+": sp = p1*pd2 + p2*pd1; spd = pd1*pd2
    elif islem == "-": sp = p1*pd2 - p2*pd1; spd = pd1*pd2
    elif islem == "x": sp = p1*p2; spd = pd1*pd2
    else: sp = p1*pd2; spd = pd1*p2
    eb = math.gcd(sp,spd); sp //= eb; spd //= eb
    d = f"{sp}/{spd}" if spd != 1 else str(sp)
    return f"{p1}/{pd1} {islem} {p2}/{pd2} = ?", d, [f"{sp+1}/{spd}", f"{sp-1}/{spd}", f"{sp}/{spd+1}"]

def mat_cebirsel():
    tip = random.randint(1,4)
    if tip == 1:
        a = random.randint(1,5); b = random.randint(-8,8); c = random.randint(1,5); d = random.randint(-8,8)
        islem = random.choice(["+","-"])
        if islem == "+": son = f"{a+c}x+{b+d}"
        else: son = f"{a-c}x+{b-d}"
        return f"({a}x{b:+d}) {islem} ({c}x{d:+d}) = ?", son, [f"{a+c+1}x+{b+d}", f"{a+c}x+{b+d+1}", f"{a+c-1}x+{b+d}"]
    elif tip == 2:
        a = random.randint(2,6); b = random.randint(1,10); x = random.randint(1,5)
        son = a*x + b; d = str(son)
        return f"{a}x+{b} ifadesinin x={x} için değeri?", d, [str(son+random.randint(2,6)), str(son-random.randint(2,6)), str(son+random.randint(1,2))]
    elif tip == 3:
        a = random.randint(2,5); b = random.randint(1,8); d = f"{4*a}x+{4*b}"
        return f"Bir kenarı ({a}x+{b}) cm olan karenin çevresi?", d, [f"{4*a+1}x+{4*b}", f"{4*a}x+{4*b+1}", f"{4*a-1}x+{4*b}"]
    else:
        a = random.randint(1,4); b = random.randint(1,6); c = random.randint(1,4); d = random.randint(1,6)
        toplam = f"{a+c}x+{b+d}"
        return f"{a}x+{b} ile {c}x+{d} toplamı?", toplam, [f"{a+c+1}x+{b+d}", f"{a+c}x+{b+d+1}", f"{a+c-1}x+{b+d}"]

def mat_denklem():
    tip = random.randint(1,4)
    if tip == 1:
        a = random.randint(2,6); b = random.randint(2,15); c = random.randint(2,6); d = random.randint(2,15)
        if a == c: a += 1
        coz = (d-b)/(a-c); dogru = str(int(coz)) if coz == int(coz) else f"{coz:.1f}"
        return f"{a}x+{b} = {c}x+{d} → x=?", dogru, [str(float(dogru)+i) for i in [-3,-2,2,3] if float(dogru)+i != float(dogru)][:3]
    elif tip == 2:
        a = random.randint(2,7); b = random.randint(1,10); c = random.randint(2,7); d = random.randint(1,12)
        coz = (a*b + d)/(a-c) if a!=c else random.randint(1,10)
        dogru = str(int(coz)) if coz == int(coz) else f"{coz:.1f}"
        return f"{a}(x-{b}) = {c}x+{d} → x=?", dogru, [str(float(dogru)+i) for i in [-2,2,3] if float(dogru)+i != float(dogru)][:3]
    elif tip == 3:
        a = random.randint(1,5); b = random.randint(1,10); dogru = str(b)
        return f"Bir sayının {a} katının {b} fazlası, {a+1} katına eşit. Sayı kaç?", dogru, [str(b+random.randint(1,4)), str(b-random.randint(1,4)), str(b+random.randint(2,5))]
    else:
        a = random.randint(2,6); b = random.randint(2,12); c = random.randint(2,6)
        coz = (c - b) / a if a != 0 else random.randint(1,10)
        dogru = str(int(coz)) if coz == int(coz) else f"{coz:.1f}"
        return f"{a}x + {b} = {c} ise x=?", dogru, [str(float(dogru)+i) for i in [-2,-1,1,2] if float(dogru)+i != float(dogru)][:3]

def mat_oran():
    tip = random.randint(1,3)
    if tip == 1:
        a = random.randint(2,10); b = random.randint(2,10); k = random.randint(2,6); x = b*k
        return f"{a}/{b} = {a*k}/x → x=?", str(x), [str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(4,6))]
    elif tip == 2:
        k = random.randint(3,8); e = random.randint(3,8); toplam = random.randint(40,80)
        kiz = int(k/(k+e) * toplam)
        return f"Kız/erkek oranı {k}/{e}, mevcut {toplam} → kız sayısı?", str(kiz), [str(kiz+random.randint(2,5)), str(kiz-random.randint(2,5)), str(kiz+random.randint(1,3))]
    else:
        a = random.randint(2,8); b = random.randint(2,8); c = random.randint(2,8)
        son = (a * c) / b
        d = str(int(son)) if son == int(son) else f"{son:.1f}"
        return f"a/b = {a}/{b} ve b/c = {b}/{c} ise a/c kaçtır?", d, [str(float(d)+0.5), str(float(d)-0.5), str(float(d)+0.2)]

def mat_yuzde():
    tip = random.randint(1,4)
    s = random.randint(150,600); y = random.choice([10,15,20,25,30,40,50,60])
    if tip == 1: son = int(s*y/100); return f"{s} TL'nin %{y} indirimi?", str(son), [str(son+random.randint(4,10)), str(son-random.randint(4,10)), str(son+random.randint(1,3))]
    elif tip == 2: son = int(s*(100-y)/100); return f"{s} TL'ye %{y} indirimli fiyat?", str(son), [str(son+random.randint(4,10)), str(son-random.randint(4,10)), str(son+random.randint(1,3))]
    elif tip == 3: son = int(s*(100+y)/100); return f"{s} TL'ye %{y} zam yapılırsa fiyat?", str(son), [str(son+random.randint(4,10)), str(son-random.randint(4,10)), str(son+random.randint(1,3))]
    else: son = int(s * (100 - y) / 100); return f"{s} TL'lik ürüne %{y} indirim yapılırsa ödenecek tutar?", str(son), [str(son+random.randint(4,10)), str(son-random.randint(4,10)), str(son+random.randint(1,3))]

def mat_aci():
    tip = random.choice(["tümler","bütünler","tümler_kat","bütünler_kat"])
    if tip == "tümler":
        a = random.randint(30,150)
        d = str(90 - a)
        m = f"{a}°'nin tümleri?"
    elif tip == "bütünler":
        a = random.randint(30,150)
        d = str(180 - a)
        m = f"{a}°'nin bütünleri?"
    elif tip == "tümler_kat":
        kat = random.randint(2,4)
        d = str(90 // (kat+1))
        m = f"Tümler açısı kendisinin {kat} katı olan açı kaç derecedir?"
    else:
        kat = random.randint(2,4)
        d = str(180 // (kat+1))
        m = f"Bütünler açısı kendisinin {kat} katı olan açı kaç derecedir?"
    y = [str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
    return m, d, y

def mat_cokgen():
    k = random.randint(3,8); tip = random.choice(["iç","dış","köşegen","iç_açı"])
    if tip == "iç": d = str((k-2)*180); m = f"{k} kenarlı iç açı toplamı?"
    elif tip == "dış": d = str(int(360/k)); m = f"Düzgün {k} kenarlı dış açısı?"
    elif tip == "köşegen": d = str(k*(k-3)//2); m = f"{k} kenarlı köşegen sayısı?"
    else:
        ic = (k-2)*180 // k
        d = str(ic)
        m = f"Düzgün {k} kenarlı bir iç açısı kaç derece?"
    y = [str(int(d)+random.randint(10,30)), str(int(d)-random.randint(10,30)), str(int(d)+random.randint(5,9))]
    return m, d, y

def mat_cember():
    r = random.randint(3,15); tip = random.choice(["çevre","alan","çap","yarıçap"])
    pi = 3
    if tip == "çevre": d = str(2*pi*r); m = f"Yarıçap {r} cm çember çevresi? (π=3)"
    elif tip == "alan": d = str(pi*r*r); m = f"Yarıçap {r} cm daire alanı? (π=3)"
    elif tip == "çap": d = str(2*r); m = f"Yarıçap {r} cm çemberin çapı?"
    else: d = str(r); m = f"Çapı {2*r} cm olan çemberin yarıçapı?"
    y = [str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
    return m, d, y

def mat_veri():
    v = [random.randint(10,90) for _ in range(5)]
    ort = sum(v)//5; med = sorted(v)[2]; ac = max(v)-min(v)
    tip = random.choice(["ortalama","medyan","açıklık","mod"])
    if tip == "ortalama": d = str(ort); m = f"{v} ortalaması?"
    elif tip == "medyan": d = str(med); m = f"{v} medyanı?"
    elif tip == "açıklık": d = str(ac); m = f"{v} açıklığı?"
    else:
        mod_list = [x for x in set(v) if v.count(x) > 1]
        if mod_list: d = str(mod_list[0]); m = f"{v} modu?"
        else: d = "Yok"; m = f"{v} modu?"
        y = [str(med), str(ort), str(ac)]
    if tip != "mod":
        y = [str(int(d)+random.randint(2,6)), str(int(d)-random.randint(2,6)), str(int(d)+random.randint(1,2))]
    return m, d, y

def mat_cisim():
    c = random.choice(["küp","dikdörtgen prizma","küre","silindir","kare prizma","koni"])
    if c == "küp": return "Küpün kaç ayrıtı vardır?", "12", ["8","10","12","14"]
    elif c == "dikdörtgen prizma": return "Dikdörtgen prizmanın kaç yüzü vardır?", "6", ["4","5","6","8"]
    elif c == "küre": return "Kürenin kaç köşesi vardır?", "0", ["0","1","2","4"]
    elif c == "silindir": return "Silindirin yan yüzeyi açılınca hangi şekil olur?", "Dikdörtgen", ["Kare","Üçgen","Dikdörtgen","Daire"]
    elif c == "kare prizma": return "Kare prizmanın kaç ayrıtı vardır?", "12", ["8","10","12","14"]
    else: return "Koninin kaç yüzü vardır?", "2", ["1","2","3","4"]

# ==================== FEN BİLİMLERİ ====================
def fen_gunes():
    tip = random.randint(1,10)
    if tip == 1: return "Güneş sisteminin en büyük gezegeni?", "Jüpiter", ["Mars","Satürn","Jüpiter","Uranüs"]
    elif tip == 2: return "Dünya'nın doğal uydusu?", "Ay", ["Mars","Ay","Venüs","Jüpiter"]
    elif tip == 3: return "Güneş'e en yakın gezegen?", "Merkür", ["Venüs","Merkür","Dünya","Mars"]
    elif tip == 4: return "Halkalarıyla ünlü gezegen?", "Satürn", ["Jüpiter","Satürn","Uranüs","Neptün"]
    elif tip == 5: return "En sıcak gezegen?", "Venüs", ["Merkür","Venüs","Dünya","Mars"]
    elif tip == 6: return "Kızıl gezegen olarak bilinen?", "Mars", ["Merkür","Venüs","Dünya","Mars"]
    elif tip == 7: return "Güneş sisteminde kaç gezegen var?", "8", ["6","7","8","9"]
    elif tip == 8: return "Dünya'nın Güneş etrafında turu kaç gün?", "365", ["360","365","366","370"]
    elif tip == 9: return "Güneş'in yüzey sıcaklığı yaklaşık?", "5500°C", ["4500°C","5500°C","6500°C","7500°C"]
    else: return "Hangi gezegen yan yatmış döner?", "Uranüs", ["Jüpiter","Satürn","Uranüs","Neptün"]

def fen_hucre():
    tip = random.randint(1,10)
    if tip == 1: return "Mitoz bölünme sonucu kaç hücre?", "2", ["1","2","4","8"]
    elif tip == 2: return "Hücrenin yönetim merkezi?", "Çekirdek", ["Mitokondri","Çekirdek","Ribozom","Koful"]
    elif tip == 3: return "Mayoz bölünme nerede?", "Üreme ana hücrelerinde", ["Vücut hücrelerinde","Üreme ana hücrelerinde","Sinir hücrelerinde","Kas hücrelerinde"]
    elif tip == 4: return "Hücrenin enerji üreten organeli?", "Mitokondri", ["Mitokondri","Ribozom","Lizozom","Golgi"]
    elif tip == 5: return "Protein sentezi nerede yapılır?", "Ribozom", ["Mitokondri","Ribozom","Çekirdek","Koful"]
    elif tip == 6: return "Bitki hücresinde bulunmayan organel?", "Sentriyol", ["Mitokondri","Ribozom","Sentriyol","Koful"]
    elif tip == 7: return "Hücrenin besin ve atık depoları?", "Koful", ["Mitokondri","Ribozom","Koful","Lizozom"]
    elif tip == 8: return "Kromozom sayısı mayoz sonucunda nasıl değişir?", "Yarıya iner", ["Aynı kalır","İki katına çıkar","Yarıya iner","Dört katına çıkar"]
    elif tip == 9: return "Canlıların temel yapı birimi?", "Hücre", ["Atom","Molekül","Hücre","Doku"]
    else: return "Hücre zarının görevi?", "Madde alışverişi", ["Enerji üretimi","Madde alışverişi","Protein sentezi","Yönetim"]

def fen_kuvvet():
    tip = random.randint(1,10)
    if tip == 1:
        k = random.randint(5,20); v = random.randint(2,10); ke = int(0.5*k*v*v)
        return f"Kütlesi {k} kg, hızı {v} m/s cismin kinetik enerjisi?", str(ke), [str(ke+10), str(ke-10), str(ke+20)]
    elif tip == 2: return "Potansiyel enerji nelere bağlıdır?", "Kütle ve yükseklik", ["Kütle ve hız","Kütle ve yükseklik","Hız ve yükseklik","Sadece kütle"]
    elif tip == 3: return "Bir cismin hareket durumunu değiştiren etki?", "Kuvvet", ["Enerji","Kuvvet","İş","Güç"]
    elif tip == 4: return "Sürtünme kuvveti hangi yönde?", "Harekete zıt yönde", ["Hareket yönünde","Harekete zıt yönde","Dikey","Yatay"]
    elif tip == 5:
        m = random.randint(2,10); h = random.randint(5,20); ep = m*10*h
        return f"{m} kg kütleli cisim {h} m yükseklikte potansiyel enerjisi (g=10)?", str(ep), [str(ep+20), str(ep-20), str(ep+50)]
    elif tip == 6: return "Bir cismin sürati arttıkça kinetik enerjisi nasıl değişir?", "Artar", ["Artar","Azalır","Değişmez","Önce artar sonra azalır"]
    elif tip == 7: return "Yayda depolanan enerji türü?", "Esneklik potansiyel enerjisi", ["Kinetik","Çekim potansiyeli","Esneklik potansiyeli","Isı"]
    elif tip == 8: return "İş birimi nedir?", "Joule", ["Newton","Joule","Watt","Pascal"]
    elif tip == 9: return "Kinetik enerji formülü?", "1/2 mv²", ["mgh","1/2 mv²","Fx","P/t"]
    else: return "Sürtünme kuvveti hangi faktörlere bağlıdır?", "Yüzey cinsi ve dik kuvvet", ["Yüzey cinsi ve hız","Yüzey cinsi ve dik kuvvet","Kütle ve hız","Yükseklik ve kütle"]

def fen_madde():
    tip = random.randint(1,10)
    if tip == 1: return "Homojen karışımlara ne denir?", "Çözelti", ["Süspansiyon","Emülsiyon","Çözelti","Kolloid"]
    elif tip == 2: return "Bir elementin en küçük yapı taşı?", "Atom", ["Molekül","Atom","Hücre","Tanecik"]
    elif tip == 3: return "Heterojen karışıma örnek?", "Ayran", ["Tuzlu su","Şekerli su","Ayran","Hava"]
    elif tip == 4: return "Yoğunluğu 0,9 ve 1,1 olan sıvılar eşit hacimde karışırsa karışım yoğunluğu?", "1,0", ["0,9","1,0","1,1","2,0"]
    elif tip == 5: return "Saf maddeler kaç grupta incelenir?", "2", ["1","2","3","4"]
    elif tip == 6: return "Aşağıdakilerden hangisi element değildir?", "Su", ["Oksijen","Hidrojen","Su","Altın"]
    elif tip == 7: return "Bir karışımı ayırmak için kullanılan yöntemlerden biri?", "Süzme", ["Süzme","Yanma","Paslanma","Mayalanma"]
    elif tip == 8: return "Bileşikler hangi yöntemle ayrılır?", "Kimyasal yöntemler", ["Fiziksel yöntemler","Kimyasal yöntemler","Mekanik yöntemler","Isıtma"]
    elif tip == 9: return "Tuzlu su hangi tür karışımdır?", "Homojen", ["Homojen","Heterojen","Süspansiyon","Emülsiyon"]
    else: return "Havanın bileşenleri nelerdir?", "Oksijen, azot, karbondioksit", ["Oksijen, hidrojen","Azot, helyum","Oksijen, azot, karbondioksit","Oksijen, klor"]

def fen_isik():
    tip = random.randint(1,10)
    if tip == 1: return "Işığın geri dönmesine ne denir?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]
    elif tip == 2: return "Işığın doğrultu değiştirmesine ne denir?", "Kırılma", ["Yansıma","Kırılma","Soğurma","Girişim"]
    elif tip == 3: return "Işığın en hızlı olduğu ortam?", "Boşluk", ["Boşluk","Hava","Su","Cam"]
    elif tip == 4: return "Aynalar hangi prensipte çalışır?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]
    elif tip == 5: return "Mercekler hangi prensipte çalışır?", "Kırılma", ["Yansıma","Kırılma","Soğurma","Dağılma"]
    elif tip == 6: return "Görme olayı nasıl gerçekleşir?", "Işık cisimden yansır ve göze gelir", ["Işık cisimden yansır","Işık gözden çıkar","Işık doğrudan göze gelir","Işık cisim tarafından soğrulur"]
    elif tip == 7: return "Düzlem aynada oluşan görüntünün özelliği?", "Sanal, düz ve aynı boyda", ["Gerçek, ters","Sanal, düz","Sanal, ters","Gerçek, düz"]
    elif tip == 8: return "Işık kırılması hangi durumda olur?", "Saydam ortam değiştiğinde", ["Saydam ortam değiştiğinde","Saydam olmayan ortamda","Aynada","Prizmada"]
    elif tip == 9: return "Beyaz ışığın prizmadan geçince renklerine ayrılması olayı?", "Dağılma", ["Yansıma","Kırılma","Dağılma","Soğurma"]
    else: return "Işığın en yavaş olduğu ortam?", "Cam", ["Boşluk","Hava","Su","Cam"]

def fen_ureme():
    tip = random.randint(1,10)
    if tip == 1: return "Kurbağa gelişimine ne denir?", "Başkalaşım", ["Metamorfoz","Başkalaşım","Döllenme","Büyüme"]
    elif tip == 2: return "Bitkilerde tohum oluşumu için gerekli olay?", "Tozlaşma", ["Döllenme","Tozlaşma","Çimlenme","Fotosentez"]
    elif tip == 3: return "Memelilerde yavruları besleyen bez?", "Süt bezi", ["Ter bezi","Yağ bezi","Süt bezi","Salya bezi"]
    elif tip == 4: return "İnsanda döllenme nerede olur?", "Fallop tüpü", ["Rahim","Yumurtalık","Fallop tüpü","Vajina"]
    elif tip == 5: return "Kelebek gelişimi hangi tür başkalaşıma girer?", "Tam başkalaşım", ["Tam başkalaşım","Yarım başkalaşım","Doğrudan gelişme","Pupa"]
    elif tip == 6: return "Çekirge hangi tür gelişim gösterir?", "Yarım başkalaşım", ["Tam başkalaşım","Yarım başkalaşım","Doğrudan gelişme","Larva"]
    elif tip == 7: return "Fotosentez hangi organelde gerçekleşir?", "Kloroplast", ["Mitokondri","Kloroplast","Ribozom","Koful"]
    elif tip == 8: return "Bitkilerde su ve mineral taşınması hangi yapı ile olur?", "Ksilem", ["Ksilem","Floem","Kambiyum","Öz"]
    elif tip == 9: return "İnsan embriyosu hangi yapıda gelişir?", "Rahim", ["Yumurtalık","Fallop tüpü","Rahim","Vajina"]
    else: return "Aşı hangi tür bağışıklığı sağlar?", "Yapay aktif", ["Doğal aktif","Yapay aktif","Doğal pasif","Yapay pasif"]

def fen_elektrik():
    tip = random.randint(1,10)
    if tip == 1:
        r1 = random.randint(2,5); r2 = random.randint(2,5)
        return f"{r1}Ω ve {r2}Ω seri bağlanırsa eşdeğer direnç?", str(r1+r2), [str(r1+r2+1), str(r1+r2-1), str(r1+r2+2)]
    elif tip == 2:
        r1 = random.randint(2,5); r2 = random.randint(2,5)
        es = round((r1*r2)/(r1+r2),1)
        return f"{r1}Ω ve {r2}Ω paralel bağlanırsa eşdeğer direnç?", str(es), [str(es+0.5), str(es-0.5), str(es+1)]
    elif tip == 3: return "Ampul parlaklığını artırmak için?", "Pil sayısı artırılır", ["Pil sayısı azaltılır","Direnç eklenir","Kablo uzatılır","Pil değiştirilir"]
    elif tip == 4: return "Devrede akımı kontrol eden eleman?", "Anahtar", ["Pil","Direnç","Anahtar","Ampul"]
    elif tip == 5: return "Gerilim birimi?", "Volt", ["Amper","Ohm","Volt","Watt"]
    elif tip == 6: return "Direnç birimi?", "Ohm", ["Amper","Ohm","Volt","Watt"]
    elif tip == 7: return "Akım birimi?", "Amper", ["Amper","Ohm","Volt","Watt"]
    elif tip == 8: return "Ohm kanunu nedir?", "V = I.R", ["V = I/R","I = V.R","V = I.R","R = V.I"]
    elif tip == 9: return "Bir devrede üç ampul seri bağlıysa biri patlarsa diğerleri?", "Söner", ["Söner","Işık vermez","Parlar","Sönmez"]
    else: return "Üç ampul paralel bağlıysa biri patlarsa diğerleri?", "Işık vermeye devam eder", ["Söner","Işık vermeye devam eder","Parlaklığı azalır","Parlaklığı artar"]

# ==================== TÜRKÇE ====================
def tur_anlam():
    sorular = [
        ("'Keşke daha çok çalışsaydım.' anlamı?", "pişmanlık", ["pişmanlık","özlem","kararlılık","şart"]),
        ("'Bu işi yapabilir misin?' anlamı?", "rica/istek", ["emir","rica/istek","koşul","olasılık"]),
        ("'Yağmur yağsa da topraklar ıslansa.' anlamı?", "özlem", ["özlem","pişmanlık","koşul","kararlılık"]),
        ("'Hava çok soğuk, bu yüzden okullar tatil edildi.' anlamı?", "neden-sonuç", ["amaç-sonuç","neden-sonuç","koşul","karşılaştırma"]),
        ("'Ders çalış ki başarılı olasın.' anlamı?", "amaç-sonuç", ["amaç-sonuç","neden-sonuç","koşul","açıklama"]),
        ("'Ne kadar bilirsen bil, anlatabildiğin kadarsın.' ana fikri?", "bilginin aktarımı önemlidir", ["bilgi her şeydir","anlatmak zordur","bilginin aktarımı önemlidir","sessizlik erdemdir"]),
        ("'Sınavdan yüksek almak için çok çalıştı.' anlamı?", "amaç", ["amaç","sonuç","koşul","karşılaştırma"]),
        ("'Sanki kimsenin haberi yokmuş gibi davranıyor.' anlamı?", "eleştiri", ["eleştiri","pişmanlık","özlem","kararlılık"]),
        ("'Lütfen kapıyı kapatır mısın?' anlamı?", "rica", ["emir","rica","istek","koşul"]),
        ("'Bu yemek çok tuzlu olmuş, keşke az tuz koysaydım.' anlamı?", "pişmanlık", ["pişmanlık","özlem","eleştiri","uyarı"]),
        ("'Elbette bu işi bitireceğiz, yeter ki birlikte çalışalım.' anlamı?", "koşul", ["koşul","amaç","neden","sonuç"]),
        ("'Bugün hava çok güzel, dışarı çıkmalıyız.' anlamı?", "öneri", ["öneri","karar","istek","zorunluluk"])
    ]
    return random.choice(sorular)

def tur_yazim():
    tip = random.randint(1,12)
    if tip == 1: return "Aşağıdakilerden hangisi doğru?", "herkes", ["herkez","herkes","herkeş","herkese"]
    elif tip == 2: return "Aşağıdakilerden hangisi doğru yazılmıştır?", "Her şey", ["Herşey","Her şey","Her-şey","Her şe'y"]
    elif tip == 3: return "'Türkiye'nin başkenti ...' cümlesinde boşluk?", "Ankara", ["İstanbul","Ankara","İzmir","Bursa"]
    elif tip == 4: return "Aşağıdakilerden hangisi yanlış yazılmıştır?", "çörekotu", ["çörekotu","çörek otu","çörek-otu","çörek otu bitkisi"]
    elif tip == 5: return "'Birşey' doğru yazımı?", "Bir şey", ["Birşey","Bir şey","Bir-şey","Bir şe'y"]
    elif tip == 6: return "Aşağıdakilerden hangisi doğrudur?", "çarşamba", ["çarşamba","ç arşamba","çarşamba","çarşamba günü"]
    elif tip == 7: return "'Yarın ki maç' mı, 'yarınki maç' mı doğrudur?", "yarınki", ["yarın ki","yarınki","yarın-ki","yarınk i"]
    elif tip == 8: return "Aşağıdakilerden hangisi ayrı yazılmalıdır?", "her şey", ["herşey","her şey","her-şey","herşeyi"]
    elif tip == 9: return "'Orijinal' doğru yazılışı?", "orijinal", ["orijinal","original","orijnal","orijinal"] 
    elif tip == 10: return "Aşağıdakilerden hangisi bitişik yazılmalıdır?", "sivrisinek", ["sivri sinek","sivrisinek","sivri-sinek","sivri sinekler"]
    elif tip == 11: return "'Milletvekili' doğru yazımı?", "milletvekili", ["millet vekili","milletvekili","millet-vekili","millet vekil"]
    else: return "'Hükümet' doğru yazımı?", "hükümet", ["hükümet","hükümet","hükümet","hükümet"]

def tur_noktalama():
    tip = random.randint(1,10)
    if tip == 1: return "Sıralı cümleleri ayırmak için hangi işaret?", "Noktalı virgül", ["Virgül","Nokta","Noktalı virgül","İki nokta"]
    elif tip == 2: return "Alıntı cümlelerden önce hangi işaret?", "İki nokta", ["Virgül","Nokta","Noktalı virgül","İki nokta"]
    elif tip == 3: return "Ünlem işareti hangi durumda?", "Sevinç, heyecan, korku", ["Soru sorarken","Sevinç, heyecan, korku","Alıntı yaparken","Sıralama yaparken"]
    elif tip == 4: return "Soru işareti hangi durumda?", "Soru cümlelerinde", ["Sevinçte","Şaşkınlıkta","Soru cümlelerinde","Alıntıda"]
    elif tip == 5: return "Cümle sonuna konan işaret?", "Nokta", ["Virgül","Nokta","Noktalı virgül","İki nokta"]
    elif tip == 6: return "Tırnak içindeki alıntıdan sonra noktalama işareti nereye konur?", "Tırnak dışına", ["Tırnağın içine","Tırnak dışına","Tırnaktan önce","Tırnaktan sonra"]
    elif tip == 7: return "Hitap sözlerinden sonra hangi işaret?", "Virgül", ["Virgül","Nokta","Ünlem","İki nokta"]
    elif tip == 8: return "Cümle içinde ögeleri ayırmak için hangi işaret?", "Virgül", ["Virgül","Nokta","Noktalı virgül","İki nokta"]
    elif tip == 9: return "Kesme işareti hangi durumda kullanılır?", "Özel isimlere eklenen eklerde", ["Sayılardan sonra","Özel isimlere eklenen eklerde","Kısaltmalarda","Belirtme durumunda"]
    else: return "Üç nokta (...) hangi durumda kullanılır?", "Tamamlanmamış cümlelerde", ["Soru cümlelerinde","Tamamlanmamış cümlelerde","Alıntılarda","Heyecan belirtmede"]

def tur_sozcuk():
    tip = random.randint(1,12)
    if tip == 1: return "'Soğuk' zıt anlamlısı?", "sıcak", ["sıcak","buzlu","donuk","serin"]
    elif tip == 2: return "Eş sesli kelime örneği?", "yüz", ["kalem","silgi","yüz","defter"]
    elif tip == 3: return "'Yüzmek' mecaz anlamda hangisinde?", "Paralar içinde yüzüyor", ["Denizde yüzdü","Paralar içinde yüzüyor","Yüzmeyi sever","Nehirde yüzdü"]
    elif tip == 4: return "'Ağız' mecaz anlamda hangisinde?", "Ağız alışkanlığı", ["Ağız ve diş sağlığı","Ağız alışkanlığı","Ağzını açtı","Ağzı sulandı"]
    elif tip == 5: return "'Kara' iki farklı anlamı?", "siyah/toprak", ["siyah/deniz","siyah/toprak","açık/koyu","soğuk/sıcak"]
    elif tip == 6: return "'Tatlı' gerçek anlamda hangisinde?", "Bal çok tatlıdır", ["Bal çok tatlıdır","Tatlı bir söz söyledi","Tatlı uyku","Tatlı çocuk"]
    elif tip == 7: return "'Ağır' mecaz anlamda hangisinde?", "Ağır bir hastalık geçirdi", ["Çanta ağır","Ağır taş","Ağır hastalık","Ağır kutu"]
    elif tip == 8: return "'Sıcak' zıt anlamlısı?", "soğuk", ["soğuk","buzlu","donuk","serin"]
    elif tip == 9: return "'Göz' 'gözetmek' anlamında hangisinde?", "Onu gözüm gibi sakınıyorum", ["Gözlerine baktım","Onu gözüm gibi sakınıyorum","Gözüm ağrıyor","Göz doktoruna gittim"]
    elif tip == 10: return "'Baş' 'başlangıç' anlamında hangisinde?", "Köprünün başında buluştuk", ["Başım ağrıyor","Köprünün başında buluştuk","Okulun başıdır","Başa baş mücadele"]
    elif tip == 11: return "'Sert' zıt anlamlısı?", "yumuşak", ["yumuşak","gevşek","esnek","kırılgan"]
    else: return "'Güzel' eş anlamlısı?", "hoş", ["kötü","çirkin","hoş","fena"]

def tur_paragraf():
    sorular = [
        ("Ne kadar bilirsen bil, anlatabildiğin kadarsın.\nAna fikir?", "Bilginin aktarımı önemlidir", ["Bilgi her şey değildir","Anlatmak zordur","Bilginin aktarımı önemlidir","Sessizlik erdemdir"]),
        ("Teknoloji hayatımızı kolaylaştırsa da bizi tembelleştiriyor. Ana fikir?", "Teknoloji insanı tembelleştirir", ["Teknoloji yararlıdır","Teknoloji gereksizdir","Teknoloji insanı tembelleştirir","Teknoloji hayatı kolaylaştırır"]),
        ("Kitap okumak zihnin jimnastiğidir. Vurgu?", "Kitap okumak zihinsel gelişim sağlar", ["Kitap okumak zaman kaybıdır","Sadece çocuklar okumalı","Kitap okumak sıkıcıdır","Kitap okumak zihinsel gelişim sağlar"]),
        ("Sanat, insanın duygularını ifade etme biçimidir. Sanatın işlevi?", "Duyguları ifade etmek", ["Para kazanmak","Eğlenmek","Zaman geçirmek","Duyguları ifade etmek"]),
        ("Başarıya giden yolda en büyük engel korkudur. Başarısızlık korkusu insanı ne yapar?", "Hedeflerinden vazgeçirir", ["Başarıya götürür","Güçlendirir","Cesaretlendirir","Hedeflerinden vazgeçirir"]),
        ("Çevre kirliliği geleceğimizi tehdit ediyor. Kaygı?", "Gelecek nesiller tehlikede", ["Bugünün rahatı","Ekonomik kazanç","Teknolojinin faydaları","Gelecek nesiller tehlikede"]),
        ("İnternet bilgiye ulaşmayı kolaylaştırdı ancak doğru bilgiye ulaşmayı zorlaştırdı. Eleştiri?", "Yanlış bilgiler hızla yayılıyor", ["İnternet yavaş","Bilgiye ulaşmak zor","Yanlış bilgiler hızla yayılıyor","Herkes yayın yapabiliyor"]),
        ("Spor, fiziksel ve ruh sağlığı için gereklidir. Sporun hangi yönü vurgulanıyor?", "Ruh sağlığına faydası", ["Fiziksel sağlık","Ruh sağlığına faydası","Sosyal fayda","Yarışma"]),
        ("Arkadaşlık, zor zamanlarda yanında olabilmektir. Gerçek arkadaşlığın özelliği?", "Zor zamanlarda destek olmak", ["Hediye almak","Birlikte eğlenmek","Zor zamanlarda destek olmak","Sır tutmak"]),
        ("Para mutluluğun tek kaynağı değildir. Ana fikir?", "Mutluluk parayla satın alınamaz", ["Para her şeydir","Mutluluk parayla satın alınamaz","Sağlık önemlidir","Sevgi önemlidir"])
    ]
    return random.choice(sorular)

def tur_fiil():
    f = random.choice(["gelmek","gitmek","bakmak","yazmak","okumak","koşmak","söylemek","anlamak"])
    kok = f.replace("mek","").replace("mak","")
    # Basit ünlü uyumu
    son_harf = kok[-1]
    if son_harf in "aı": ek = "ı"
    elif son_harf in "ei": ek = "i"
    elif son_harf in "ou": ek = "u"
    else: ek = "ü"
    dogru = kok + ek + "yorsun"
    s = [dogru, dogru.replace("yorsun","yor"), dogru.replace("yorsun","york"), dogru.replace("yorsun","yorn")]
    random.shuffle(s)
    return f"'{f}' fiilinin şimdiki zaman 2. tekil kişi çekimi?", dogru, s

def tur_zarf():
    cumleler = [
        ("Hızlı koştu", "hızlı", ["hızlı","koştu","o","güzel"]),
        ("Çok güzel olmuş", "çok", ["çok","güzel","olmuş","o"]),
        ("Yarın geleceğim", "yarın", ["yarın","geleceğim","ben","gün"]),
        ("Dikkatlice dinledi", "dikkatlice", ["dikkatlice","dinledi","o","sessizce"]),
        ("İçeri girdi", "içeri", ["içeri","girdi","o","hızla"]),
        ("Oldukça zordu", "oldukça", ["oldukça","zordu","o","çok"])
    ]
    return random.choice(cumleler)

def tur_cumle():
    sorular = [
        ("'Kitap okumayı çok severim.' yüklemin türüne göre?", "İsim cümlesi", ["Fiil cümlesi","İsim cümlesi","Devrik cümle","Birleşik cümle"]),
        ("'Hava çok soğudu.' olumlu mu olumsuz mu?", "Olumlu", ["Olumlu","Olumsuz","Soru","Ünlem"]),
        ("'Ah, bu kadar da olmaz!' cümle türü?", "Ünlem cümlesi", ["İsim cümlesi","Fiil cümlesi","Ünlem cümlesi","Soru cümlesi"]),
        ("'Sınav bitti, herkes sevindi.' cümle yapısı?", "Birleşik cümle", ["Basit cümle","Birleşik cümle","Sıralı cümle","Bağlı cümle"]),
        ("'Çalışıyorum çünkü sınav var.' cümlesi hangi anlamda?", "Neden-sonuç", ["Amaç-sonuç","Neden-sonuç","Koşul","Karşılaştırma"])
    ]
    return random.choice(sorular)

# ==================== SOSYAL BİLGİLER ====================
def sos_tarih():
    sorular = [
        ("İlk Türk devletlerinden biri?", "Asya Hun Devleti", ["Osmanlı","Asya Hun","Bizans","Roma"]),
        ("Osmanlı'da Lale Devri yeniliği?", "Matbaa", ["Matbaa","Fetih","Anayasa","Cumhuriyet"]),
        ("Milli Mücadele kongrelerinden?", "Sivas Kongresi", ["Lozan","Sivas","Erzurum","Amasya"]),
        ("İstanbul'un fethi hangi padişah?", "Fatih Sultan Mehmet", ["Yavuz Sultan Selim","Kanuni","Fatih Sultan Mehmet","II. Mahmut"]),
        ("TBMM açılış tarihi?", "23 Nisan 1920", ["19 Mayıs 1919","23 Nisan 1920","29 Ekim 1923","30 Ağustos 1922"]),
        ("Cumhuriyet ilan tarihi?", "29 Ekim 1923", ["23 Nisan 1920","29 Ekim 1923","30 Ağustos 1922","1 Kasım 1922"]),
        ("Osmanlı'nın kurucusu?", "Osman Bey", ["Orhan Bey","Murad Hüdavendigâr","Osman Bey","Yıldırım Bayezid"]),
        ("Malazgirt Savaşı hangi yıl?", "1071", ["1041","1071","1081","1091"]),
        ("Kurtuluş Savaşı başkomutanı?", "Mustafa Kemal Atatürk", ["İsmet İnönü","Mustafa Kemal Atatürk","Fevzi Çakmak","Kâzım Karabekir"]),
        ("Osmanlı'nın ilk başkenti?", "Bursa", ["Edirne","İstanbul","Bursa","Söğüt"])
    ]
    return random.choice(sorular)

def sos_iletisim():
    tip = random.randint(1,6)
    if tip == 1: return "Duygu, düşünce ve bilgilerin aktarılması?", "İletişim", ["Empati","İletişim","Hoşgörü","Saygı"]
    elif tip == 2: return "Karşısındakinin duygularını anlama?", "Empati", ["Sempati","Empati","Özgecilik","Fedakarlık"]
    elif tip == 3: return "Sözsüz iletişim örneği?", "Jest ve mimikler", ["Konuşmak","Jest ve mimikler","Mektup","Telefon"]
    elif tip == 4: return "İletişimde geri bildirim nedir?", "Mesaja cevap", ["Mesajı göndermek","Mesaja cevap","Mesajı kodlamak","Mesajı iletmek"]
    elif tip == 5: return "Aktif dinleme nedir?", "Karşıdakini anlamaya çalışmak", ["Sessiz kalmak","Karşıdakini anlamaya çalışmak","Sürekli konuşmak","Not almak"]
    else: return "Toplumsal iletişimi engelleyen faktör?", "Önyargı", ["Empati","Önyargı","Hoşgörü","Saygı"]

def sos_nufus():
    tip = random.randint(1,6)
    if tip == 1: return "Bir ülkede yaşayan insan sayısı?", "Nüfus", ["Nüfus yoğunluğu","Nüfus","Göç","Demografi"]
    elif tip == 2: return "Türkiye'nin en kalabalık şehri?", "İstanbul", ["Ankara","İzmir","İstanbul","Bursa"]
    elif tip == 3: return "Nüfus yoğunluğu en az bölge?", "Doğu Anadolu", ["Marmara","Doğu Anadolu","Akdeniz","Ege"]
    elif tip == 4: return "Göç veren bölge?", "Doğu Anadolu", ["Marmara","Ege","Doğu Anadolu","Akdeniz"]
    elif tip == 5: return "Türkiye'nin ikinci kalabalık şehri?", "Ankara", ["İstanbul","Ankara","İzmir","Bursa"]
    else: return "Nüfus sayımı kaç yılda bir yapılır?", "5 yıl", ["5 yıl","10 yıl","2 yıl","1 yıl"]

def sos_bilim():
    tip = random.randint(1,6)
    if tip == 1: return "Matematik, fizik, kimya gibi disiplinler?", "Bilim", ["Teknoloji","Sanat","Bilim","Edebiyat"]
    elif tip == 2: return "Teknolojinin olumlu etkisi?", "İletişim kolaylığı", ["Kirlilik","Trafik","İletişim kolaylığı","Sosyal izolasyon"]
    elif tip == 3: return "İcat ile keşif farkı?", "İcat yoktan var eder, keşif var olanı bulur", ["İcat var olanı bulur","Keşif yoktan var eder","İkisi aynı","İcat olmaz"]
    elif tip == 4: return "Bilimsel yöntemin ilk aşaması?", "Gözlem", ["Deney","Gözlem","Hipotez","Sonuç"]
    elif tip == 5: return "Buluş yapan kişiye ne denir?", "Mucit", ["Bilim insanı","Mucit","Araştırmacı","Mühendis"]
    else: return "Teknoloji nedir?", "Bilginin pratiğe dönüşmesi", ["Bilim","Bilginin pratiğe dönüşmesi","Araç gereç","Fabrika"]

def sos_ekonomi():
    tip = random.randint(1,6)
    if tip == 1: return "İhtiyaçları karşılamak için yapılan faaliyet?", "Üretim", ["Tüketim","Üretim","Pazarlama","Reklam"]
    elif tip == 2: return "Gelir ve gider arasındaki fark?", "Kâr", ["Zarar","Kâr","Bütçe","Tasarruf"]
    elif tip == 3: return "Vergi neden alınır?", "Kamu hizmetleri için", ["İhracat","Kamu hizmetleri","İthalat","Savunma"]
    elif tip == 4: return "Bütçe nedir?", "Gelir-gider planı", ["Gelir tablosu","Gider tablosu","Gelir-gider planı","Kâr tablosu"]
    elif tip == 5: return "Enflasyon nedir?", "Fiyatların sürekli artması", ["Fiyatların düşmesi","Fiyatların sürekli artması","Durgunluk","İşsizlik"]
    else: return "Tasarruf nedir?", "Gelirin harcanmayan kısmı", ["Harcama","Biriktirme","Gelirin harcanmayan kısmı","Yatırım"]

def sos_kultur():
    tip = random.randint(1,6)
    if tip == 1: return "Bir topluma ait maddi manevi değerler?", "Kültür", ["Medeniyet","Kültür","Gelenek","Görenek"]
    elif tip == 2: return "UNESCO Türkiye'den bir miras?", "Kapadokya", ["Ankara","İstanbul","Kapadokya","Antalya"]
    elif tip == 3: return "Somut olmayan kültürel miras?", "Hacivat Karagöz", ["Pamukkale","Efes","Hacivat Karagöz","Ayasofya"]
    elif tip == 4: return "Kültürel farklılıklara saygı neden önemli?", "Toplumsal barış için", ["Ekonomi için","Toplumsal barış için","Ticaret için","Savaş için"]
    elif tip == 5: return "Gelenek nedir?", "Kuşaktan kuşağa aktarılan kültürel öğeler", ["Değişen kurallar","Yeni icatlar","Kuşaktan kuşağa aktarılan kültürel öğeler","Bilimsel bulgular"]
    else: return "Müze nedir?", "Tarihi eserlerin sergilendiği yer", ["Okul","Kütüphane","Tarihi eserlerin sergilendiği yer","Cami"]

def sos_demokrasi():
    tip = random.randint(1,6)
    if tip == 1: return "Halkın kendini yönettiği yönetim?", "Demokrasi", ["Monarşi","Oligarşi","Demokrasi","Teokrasi"]
    elif tip == 2: return "Seçme ve seçilme yaşı?", "18", ["16","17","18","20"]
    elif tip == 3: return "Demokrasinin temel ilkesi?", "Milli egemenlik", ["Kuvvetler birliği","Milli egemenlik","Tek parti","Diktatörlük"]
    elif tip == 4: return "Hukukun üstünlüğü ne demek?", "Kanunlar herkese eşit", ["Zenginler farklı","Yöneticiler ayrıcalıklı","Kanunlar herkese eşit","Halk yargılanmaz"]
    elif tip == 5: return "Çoğulculuk nedir?", "Farklı düşüncelere saygı", ["Tek düşünce","Farklı düşüncelere saygı","Zorunlu birlik","Ortak karar"]
    else: return "Seçimlerin serbest ve adil olması neden önemlidir?", "Halkın iradesinin yansıması", ["Yöneticilerin işi","Halkın iradesinin yansıması","Uluslararası baskı","Gelenek"]

# ==================== DERS ve KONU SÖZLÜĞÜ ====================
tum_dersler = {
    "Matematik": {
        "Tam Sayılar": mat_tam_sayilar,
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
        "Cümlede Anlam": tur_anlam,
        "Yazım": tur_yazim,
        "Noktalama": tur_noktalama,
        "Sözcükte Anlam": tur_sozcuk,
        "Paragrafta Anlam": tur_paragraf,
        "Fiiller": tur_fiil,
        "Zarflar": tur_zarf,
        "Cümle Türleri": tur_cumle
    },
    "Sosyal Bilgiler": {
        "Tarih": sos_tarih,
        "İletişim": sos_iletisim,
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
