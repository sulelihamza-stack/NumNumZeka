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
st.markdown("**Her seferinde yeni, rastgele üretilmiş sorular – sonsuz çeşitlilik**")

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
    tip = random.randint(1,8)
    if tip == 1:  # dalgıç
        b = random.randint(-80,-10); t = b; h = []
        for _ in range(random.randint(4,8)):
            a = random.randint(5,50)
            if random.choice([0,1]): t += a; h.append(f"{a} m yükseliyor")
            else: t -= a; h.append(f"{a} m dalıyor")
        m = f"Bir dalgıç {b} m'de iken " + ", ".join(h) + ". Son konum?"
        d = str(t)
    elif tip == 2:  # sıcaklık
        b = random.randint(-20,-5); t = b
        adim = random.randint(3,15); saat = random.randint(3,7)
        t += adim * saat
        m = f"Sabah {b}°C, her saat {adim}°C artarsa {saat} saat sonra kaç °C?"
        d = str(t)
    elif tip == 3:  # hesap makinesi
        s = random.randint(-50,50); t = s
        isl = []
        for _ in range(random.randint(3,6)):
            a = random.randint(5,40)
            if random.choice([0,1]): t += a; isl.append(f"+{a}")
            else: t -= a; isl.append(f"-{a}")
        m = f"Ekran {s} iken " + ", ".join(isl) + " tuşlanıyor. Sonuç?"
        d = str(t)
    elif tip == 4:  # asansör
        b = random.randint(-5,5); t = b
        for _ in range(random.randint(3,7)):
            a = random.randint(2,10)
            if random.choice([0,1]): t += a
            else: t -= a
        m = f"Asansör {b}. katta iken {random.randint(3,7)} hareket sonunda hangi kat?"
        d = str(t)
    elif tip == 5:  # maaş-gider
        maas = random.randint(3000,7000); gider = random.randint(1000, maas-500)
        d = str(maas - gider)
        m = f"Ali'nin maaşı {maas} TL, giderleri {gider} TL. Kalan?"
    elif tip == 6:  # dağcı
        b = random.randint(500,3000); t = b
        for _ in range(random.randint(3,6)):
            a = random.randint(100,800)
            if random.choice([0,1]): t += a
            else: t -= a
        m = f"Dağcı {b} m'de, {random.randint(3,6)} hareket sonunda yükseklik?"
        d = str(t)
    elif tip == 7:  # sınav puanı
        d_s = random.randint(15,25); y_s = random.randint(3,10)
        d_p = random.choice([4,5]); y_p = random.choice([-1,-2])
        toplam = d_s*d_p + y_s*y_p
        d = str(toplam)
        m = f"{d_s+y_s} soruluk sınav: {d_s} doğru (+{d_p}), {y_s} yanlış ({y_p}). Toplam puan?"
    else:  # borç/alacak
        borc = random.randint(100,1000); odeme = random.randint(50, borc)
        d = str(borc - odeme)
        m = f"{borc} TL borcun {odeme} TL'si ödenirse kalan borç?"
    yanlis = set()
    while len(yanlis) < 3:
        sapma = random.choice([-15,-10,-8,8,10,15,20])
        y = int(d) + sapma
        if y != int(d): yanlis.add(str(y))
    siklar = [d] + list(yanlis)
    random.shuffle(siklar)
    return m, d, siklar

def mat_rasyonel():
    tip = random.randint(1,4)
    if tip == 1:
        p1 = random.randint(1,12); pd1 = random.randint(2,12)
        p2 = random.randint(1,12); pd2 = random.randint(2,12)
        if p1/pd1 > p2/pd2: d = ">"
        elif p1/pd1 < p2/pd2: d = "<"
        else: d = "="
        m = f"{p1}/{pd1} __ {p2}/{pd2} yerine ne gelir?"
        s = [">","<","=","≠"]; random.shuffle(s)
        return m, d, s
    elif tip == 2:
        p = random.randint(1,15); pd = random.randint(2,15)
        v = p/pd; d = f"{v:.2f}"
        m = f"{p}/{pd} ondalık gösterimi (2 basamak)?"
        y = [f"{v+0.1:.2f}", f"{v-0.1:.2f}", f"{v+0.05:.2f}"]; s=[d]+y; random.shuffle(s); return m,d,s
    elif tip == 3:
        p = random.randint(1,10); pd = random.randint(2,10)
        kalan = 1 - (p/pd); kisi = random.randint(4,8)
        pay = int((kalan/kisi)*100); payda=100
        for i in range(2,20):
            if pay%i==0 and payda%i==0: pay//=i; payda//=i
        d = f"{pay}/{payda}" if payda!=1 else str(pay)
        m = f"Pastanın {p}/{pd}'i yenmiş. Kalan {kisi} kişiye paylaştırılırsa kişi başı?"
        s = [d, f"{pay+1}/{payda}", f"{pay-1}/{payda}", f"{pay}/{payda+1}"]; random.shuffle(s); return m,d,s
    else:
        p = random.randint(1,12); pd = random.randint(2,12); carp = random.randint(2,6)
        yp = p*carp; ypd = pd*carp
        d = str(yp + ypd)
        m = f"{p}/{pd} kesrini {carp} ile genişletince pay+payda toplamı?"
        y = [str(int(d)+random.randint(5,20)), str(int(d)-random.randint(5,20)), str(int(d)+random.randint(1,4))]; s=[d]+y; random.shuffle(s); return m,d,s

def mat_rasyonel_islem():
    p1 = random.randint(1,8); pd1 = random.randint(2,8)
    p2 = random.randint(1,8); pd2 = random.randint(2,8)
    islem = random.choice(["+","-","x","/"])
    if islem == "+": sp = p1*pd2 + p2*pd1; spd = pd1*pd2
    elif islem == "-": sp = p1*pd2 - p2*pd1; spd = pd1*pd2
    elif islem == "x": sp = p1*p2; spd = pd1*pd2
    else: sp = p1*pd2; spd = pd1*p2
    eb = math.gcd(sp,spd); sp //= eb; spd //= eb
    d = f"{sp}/{spd}" if spd != 1 else str(sp)
    m = f"{p1}/{pd1} {islem} {p2}/{pd2} = ?"
    s = [d, f"{sp+1}/{spd}", f"{sp-1}/{spd}", f"{sp}/{spd+1}"]; random.shuffle(s)
    return m, d, s

def mat_cebirsel():
    tip = random.randint(1,3)
    if tip == 1:
        a = random.randint(1,5); b = random.randint(-8,8); c = random.randint(1,5); d = random.randint(-8,8)
        islem = random.choice(["+","-"])
        if islem == "+": son = f"{a+c}x+{b+d}"
        else: son = f"{a-c}x+{b-d}"
        m = f"({a}x{b:+d}) {islem} ({c}x{d:+d}) = ?"
        s = [son, f"{a+c+1}x+{b+d}", f"{a+c}x+{b+d+1}", f"{a+c-1}x+{b+d}"]; random.shuffle(s)
        return m, son, s
    elif tip == 2:
        a = random.randint(2,6); b = random.randint(1,10); x = random.randint(1,5)
        son = a*x + b; d = str(son)
        m = f"{a}x+{b} ifadesinin x={x} için değeri?"
        s = [d, str(son+random.randint(2,6)), str(son-random.randint(2,6)), str(son+random.randint(1,2))]; random.shuffle(s)
        return m, d, s
    else:
        a = random.randint(2,5); b = random.randint(1,8); d = f"{4*a}x+{4*b}"
        m = f"Bir kenarı ({a}x+{b}) cm olan karenin çevresi?"
        s = [d, f"{4*a+1}x+{4*b}", f"{4*a}x+{4*b+1}", f"{4*a-1}x+{4*b}"]; random.shuffle(s)
        return m, d, s

def mat_denklem():
    tip = random.randint(1,3)
    if tip == 1:
        a = random.randint(2,6); b = random.randint(2,15); c = random.randint(2,6); d = random.randint(2,15)
        if a == c: a += 1
        coz = (d-b)/(a-c); dogru = str(int(coz)) if coz == int(coz) else f"{coz:.1f}"
        m = f"{a}x+{b} = {c}x+{d} → x=?"
    elif tip == 2:
        a = random.randint(2,7); b = random.randint(1,10); c = random.randint(2,7); d = random.randint(1,12)
        coz = (a*b + d)/(a-c) if a!=c else random.randint(1,10)
        dogru = str(int(coz)) if coz == int(coz) else f"{coz:.1f}"
        m = f"{a}(x-{b}) = {c}x+{d} → x=?"
    else:
        a = random.randint(1,5); b = random.randint(1,10); dogru = str(b)
        m = f"Bir sayının {a} katının {b} fazlası, {a+1} katına eşit. Sayı kaç?"
    y = [str(float(dogru)+i) for i in [-3,-2,2,3] if float(dogru)+i != float(dogru)][:3]
    s = [dogru] + y; random.shuffle(s)
    return m, dogru, s

def mat_oran():
    tip = random.randint(1,2)
    if tip == 1:
        a = random.randint(2,10); b = random.randint(2,10); k = random.randint(2,6)
        x = b*k; d = str(x)
        m = f"{a}/{b} = {a*k}/x → x=?"
        s = [d, str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(4,6))]; random.shuffle(s)
        return m, d, s
    else:
        k = random.randint(3,8); e = random.randint(3,8); toplam = random.randint(40,80)
        kiz = int(k/(k+e) * toplam); d = str(kiz)
        m = f"Kız/erkek oranı {k}/{e}, mevcut {toplam} → kız sayısı?"
        s = [d, str(kiz+random.randint(2,5)), str(kiz-random.randint(2,5)), str(kiz+random.randint(1,3))]; random.shuffle(s)
        return m, d, s

def mat_yuzde():
    tip = random.randint(1,3)
    s = random.randint(150,600); y = random.choice([10,15,20,25,30,40,50,60])
    if tip == 1: son = int(s*y/100); d = str(son); m = f"{s} TL'nin %{y} indirimi?"
    elif tip == 2: son = int(s*(100-y)/100); d = str(son); m = f"{s} TL'ye %{y} indirimli fiyat?"
    else: son = int(s*(100+y)/100); d = str(son); m = f"{s} TL'ye %{y} zam yapılırsa fiyat?"
    s = [d, str(son+random.randint(4,10)), str(son-random.randint(4,10)), str(son+random.randint(1,3))]; random.shuffle(s)
    return m, d, s

def mat_aci():
    a = random.randint(30,150); tip = random.choice(["tümler","bütünler"])
    if tip == "tümler": d = str(90-a); m = f"{a}°'nin tümleri?"
    else: d = str(180-a); m = f"{a}°'nin bütünleri?"
    s = [d, str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]; random.shuffle(s)
    return m, d, s

def mat_cokgen():
    k = random.randint(3,8); tip = random.choice(["iç","dış","köşegen"])
    if tip == "iç": d = str((k-2)*180); m = f"{k} kenarlı iç açı toplamı?"
    elif tip == "dış": d = str(int(360/k)); m = f"Düzgün {k} kenarlı dış açı?"
    else: d = str(k*(k-3)//2); m = f"{k} kenarlı köşegen sayısı?"
    s = [d, str(int(d)+random.randint(10,30)), str(int(d)-random.randint(10,30)), str(int(d)+random.randint(5,9))]; random.shuffle(s)
    return m, d, s

def mat_cember():
    r = random.randint(3,15); tip = random.choice(["çevre","alan","çap"]); pi=3
    if tip == "çevre": d = str(2*pi*r); m = f"Yarıçap {r} cm çember çevresi? (π=3)"
    elif tip == "alan": d = str(pi*r*r); m = f"Yarıçap {r} cm daire alanı? (π=3)"
    else: d = str(2*r); m = f"Yarıçap {r} cm çemberin çapı?"
    s = [d, str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]; random.shuffle(s)
    return m, d, s

def mat_veri():
    v = [random.randint(10,90) for _ in range(5)]
    ort = sum(v)//5; med = sorted(v)[2]; ac = max(v)-min(v)
    tip = random.choice(["ortalama","medyan","açıklık"])
    if tip == "ortalama": d = str(ort); m = f"{v} ortalaması?"
    elif tip == "medyan": d = str(med); m = f"{v} medyanı?"
    else: d = str(ac); m = f"{v} açıklığı?"
    s = [d, str(int(d)+random.randint(2,6)), str(int(d)-random.randint(2,6)), str(int(d)+random.randint(1,2))]; random.shuffle(s)
    return m, d, s

def mat_cisim():
    c = random.choice(["küp","dikdörtgen prizma","küre","silindir"])
    if c == "küp": return "Küpün kaç ayrıtı vardır?", "12", ["8","10","12","14"]
    elif c == "dikdörtgen prizma": return "Dikdörtgen prizmanın kaç yüzü vardır?", "6", ["4","5","6","8"]
    elif c == "küre": return "Kürenin kaç köşesi vardır?", "0", ["0","1","2","4"]
    else: return "Silindirin yan yüzeyi açılınca hangi şekil olur?", "Dikdörtgen", ["Kare","Üçgen","Dikdörtgen","Daire"]

# ==================== FEN BİLİMLERİ (tüm konular dinamik, 5-8 tip) ====================
def fen_gunes():
    tip = random.randint(1,6)
    if tip == 1: return "Güneş sisteminin en büyük gezegeni?", "Jüpiter", ["Mars","Satürn","Jüpiter","Uranüs"]
    elif tip == 2: return "Güneş'e en yakın gezegen?", "Merkür", ["Venüs","Merkür","Dünya","Mars"]
    elif tip == 3: return "Halkalarıyla ünlü gezegen?", "Saturn", ["Jüpiter","Satürn","Uranüs","Neptün"]
    elif tip == 4: return "Dünya'nın doğal uydusu?", "Ay", ["Mars","Ay","Venüs","Jüpiter"]
    elif tip == 5: return "En sıcak gezegen?", "Venüs", ["Merkür","Venüs","Dünya","Mars"]
    else: return "Kızıl gezegen olarak bilinen?", "Mars", ["Merkür","Venüs","Dünya","Mars"]

def fen_hucre():
    tip = random.randint(1,5)
    if tip == 1: return "Mitoz bölünme sonucu kaç hücre?", "2", ["1","2","4","8"]
    elif tip == 2: return "Hücrenin yönetim merkezi?", "Çekirdek", ["Mitokondri","Çekirdek","Ribozom","Koful"]
    elif tip == 3: return "Mayoz bölünme nerede?", "Üreme ana hücrelerinde", ["Vücut hücrelerinde","Üreme ana hücrelerinde","Sinir hücrelerinde","Kas hücrelerinde"]
    elif tip == 4: return "Hücrenin enerji üreten organeli?", "Mitokondri", ["Mitokondri","Ribozom","Lizozom","Golgi"]
    else: return "Protein sentezi nerede yapılır?", "Ribozom", ["Mitokondri","Ribozom","Çekirdek","Koful"]

def fen_kuvvet():
    tip = random.randint(1,4)
    if tip == 1:
        k = random.randint(5,20); v = random.randint(2,10); ke = int(0.5*k*v*v)
        return f"Kütlesi {k} kg, hızı {v} m/s cismin kinetik enerjisi?", str(ke), [str(ke+10), str(ke-10), str(ke+20)]
    elif tip == 2: return "Potansiyel enerji nelere bağlıdır?", "Kütle ve yükseklik", ["Kütle ve hız","Kütle ve yükseklik","Hız ve yükseklik"]
    elif tip == 3: return "Bir cismin hareket durumunu değiştiren etki?", "Kuvvet", ["Enerji","Kuvvet","İş","Güç"]
    else: return "Sürtünme kuvveti hangi yönde?", "Harekete zıt yönde", ["Hareket yönünde","Harekete zıt yönde","Dikey","Yatay"]

def fen_madde():
    tip = random.randint(1,4)
    if tip == 1: return "Homojen karışımlara ne denir?", "Çözelti", ["Süspansiyon","Emülsiyon","Çözelti","Kolloid"]
    elif tip == 2: return "Bir elementin en küçük yapı taşı?", "Atom", ["Molekül","Atom","Hücre","Tanecik"]
    elif tip == 3: return "Heterojen karışıma örnek?", "Ayran", ["Tuzlu su","Şekerli su","Ayran","Hava"]
    else: return "Tuz oranı %20 olan 200g çözeltiye 50g tuz eklenirse yeni oran?", "32", ["28","32","36","40"]

def fen_isik():
    tip = random.randint(1,4)
    if tip == 1: return "Işığın geri dönmesine ne denir?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]
    elif tip == 2: return "Işığın doğrultu değiştirmesine ne denir?", "Kırılma", ["Yansıma","Kırılma","Soğurma","Girişim"]
    elif tip == 3: return "Işığın en hızlı olduğu ortam?", "Boşluk", ["Boşluk","Hava","Su","Cam"]
    else: return "Aynalar hangi prensipte çalışır?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]

def fen_ureme():
    tip = random.randint(1,4)
    if tip == 1: return "Kurbağa gelişimine ne denir?", "Başkalaşım", ["Metamorfoz","Başkalaşım","Döllenme","Büyüme"]
    elif tip == 2: return "Bitkilerde tohum oluşumu için gerekli olay?", "Tozlaşma", ["Döllenme","Tozlaşma","Çimlenme","Fotosentez"]
    elif tip == 3: return "Memelilerde yavruları besleyen bez?", "Süt bezi", ["Ter bezi","Yağ bezi","Süt bezi","Salya bezi"]
    else: return "İnsanda döllenme nerede olur?", "Fallop tüpü", ["Rahim","Yumurtalık","Fallop tüpü","Vajina"]

def fen_elektrik():
    tip = random.randint(1,4)
    if tip == 1:
        r1 = random.randint(2,5); r2 = random.randint(2,5)
        return f"{r1}Ω ve {r2}Ω seri bağlanırsa eşdeğer direnç?", str(r1+r2), [str(r1+r2+1), str(r1+r2-1), str(r1+r2+2)]
    elif tip == 2:
        r1 = random.randint(2,5); r2 = random.randint(2,5)
        es = round((r1*r2)/(r1+r2),1)
        return f"{r1}Ω ve {r2}Ω paralel bağlanırsa eşdeğer direnç?", str(es), [str(es+0.5), str(es-0.5), str(es+1)]
    elif tip == 3: return "Ampul parlaklığını artırmak için?", "Pil sayısı artırılır", ["Pil sayısı azaltılır","Direnç eklenir","Kablo uzatılır"]
    else: return "Devrede akımı kontrol eden eleman?", "Anahtar", ["Pil","Direnç","Anahtar","Ampul"]

# ==================== TÜRKÇE (Yazım, Noktalama vb. 5+ tip) ====================
def tur_yazim():
    tip = random.randint(1,6)
    if tip == 1: return "Aşağıdakilerden hangisi doğru?", "herkes", ["herkez","herkes","herkeş","herkese"]
    elif tip == 2: return "Aşağıdakilerden hangisi doğru yazılmıştır?", "Her şey", ["Herşey","Her şey","Her-şey","Her şe'y"]
    elif tip == 3: return "'Türkiye'nin başkenti ...' cümlesinde boşluk?", "Ankara", ["İstanbul","Ankara","İzmir","Bursa"]
    elif tip == 4: return "Aşağıdakilerden hangisi yanlış yazılmıştır?", "çörekotu", ["çörekotu","çörek otu","çörek-otu","çörek otu bitkisi"]
    elif tip == 5: return "'Birşey' doğru yazımı?", "Bir şey", ["Birşey","Bir şey","Bir-şey","Bir şe'y"]
    else: return "Aşağıdakilerden hangisi doğru?", "herkes", ["herkez","herkes","herkeş","herkese"]

def tur_noktalama():
    tip = random.randint(1,5)
    if tip == 1: return "Sıralı cümleleri ayırmak için hangi işaret?", "Noktalı virgül", ["Virgül","Nokta","Noktalı virgül","İki nokta"]
    elif tip == 2: return "Alıntı cümlelerden önce hangi işaret?", "İki nokta", ["Virgül","Nokta","Noktalı virgül","İki nokta"]
    elif tip == 3: return "Ünlem işareti hangi durumda kullanılır?", "Sevinç, heyecan, korku", ["Soru sorarken","Sevinç, heyecan, korku","Alıntı yaparken","Sıralama yaparken"]
    elif tip == 4: return "Soru işareti hangi durumda?", "Soru cümlelerinde", ["Sevinçte","Şaşkınlıkta","Soru cümlelerinde","Alıntıda"]
    else: return "Cümle sonuna konan işaret?", "Nokta", ["Virgül","Nokta","Noktalı virgül","İki nokta"]

def tur_sozcuk():
    tip = random.randint(1,5)
    if tip == 1: return "'Soğuk' zıt anlamlısı?", "sıcak", ["sıcak","buzlu","donuk","serin"]
    elif tip == 2: return "Eş sesli kelime örneği?", "yüz", ["kalem","silgi","yüz","defter"]
    elif tip == 3: return "'Yüzmek' mecaz anlamda hangisinde?", "Paralar içinde yüzüyor", ["Denizde yüzdü","Paralar içinde yüzüyor","Yüzmeyi sever","Nehirde yüzdü"]
    elif tip == 4: return "'Ağız' hangi cümlede mecaz?", "Ağız alışkanlığı", ["Ağız ve diş sağlığı","Ağız alışkanlığı","Ağzını açtı","Ağzı sulandı"]
    else: return "'Kara' kelimesinin iki farklı anlamı?", "siyah/toprak", ["siyah/deniz","siyah/toprak","açık/koyu","soğuk/sıcak"]

def tur_fiil():
    f = random.choice(["gelmek","gitmek","bakmak","yazmak","okumak","koşmak"])
    d = f.replace("mek","").replace("mak","") + "yor"
    return f"'{f}' fiilinin şimdiki zaman 2. tekil kişi çekimi?", d, [d, d+"m", d+"k", d+"n"]

def tur_zarf():
    cumleler = [("Hızlı koştu", "hızlı", ["hızlı","koştu","o","güzel"]),
                ("Çok güzel olmuş", "çok", ["çok","güzel","olmuş","o"]),
                ("Yarın geleceğim", "yarın", ["yarın","geleceğim","ben","gün"]),
                ("Dikkatlice dinledi", "dikkatlice", ["dikkatlice","dinledi","o","sessizce"]),
                ("İçeri girdi", "içeri", ["içeri","girdi","o","hızla"])]
    return random.choice(cumleler)

def tur_anlam():
    sorular = [("'Keşke daha çok çalışsaydım.' anlamı?", "pişmanlık", ["pişmanlık","özlem","kararlılık","şart"]),
               ("'Bu işi yapabilir misin?' anlamı?", "rica/istek", ["emir","rica/istek","koşul","olasılık"]),
               ("'Yağmur yağsa da topraklar ıslansa.' anlamı?", "özlem", ["özlem","pişmanlık","koşul","kararlılık"]),
               ("'Hava çok soğuk, bu yüzden okullar tatil.' anlamı?", "sebep-sonuç", ["amaç-sonuç","sebep-sonuç","koşul","karşılaştırma"])]
    return random.choice(sorular)

def tur_paragraf():
    temalar = ["Teknoloji","Kitap","Sanat","Başarı","Çevre","Arkadaşlık","Mutluluk"]
    tema = random.choice(temalar)
    if tema == "Teknoloji":
        return "Teknoloji hayatımızı kolaylaştırsa da bizi tembelleştiriyor. Ana fikir?", "Teknoloji insanı tembelleştirir", ["Teknoloji yararlıdır","Teknoloji gereksizdir","Teknoloji zararlıdır","Teknoloji eğlencelidir"]
    elif tema == "Kitap":
        return "Kitap okumak zihnin jimnastiğidir. Vurgulanan?", "Kitap okumak zihinsel gelişim sağlar", ["Kitap okumak zaman kaybıdır","Sadece çocuklar okumalı","Kitap okumak sıkıcıdır","Kitap pahalıdır"]
    elif tema == "Sanat":
        return "Sanat, insanın duygularını ifade etme biçimidir. Sanatın işlevi?", "Duyguları ifade etmek", ["Para kazanmak","Eğlenmek","Zaman geçirmek","Reklam yapmak"]
    elif tema == "Başarı":
        return "Başarıya giden yolda en büyük engel korkudur. Başarısızlık korkusu insanı ne yapar?", "Hedeflerinden vazgeçirir", ["Başarıya götürür","Güçlendirir","Cesaretlendirir","Mutlu eder"]
    elif tema == "Çevre":
        return "Çevre kirliliği geleceğimizi tehdit ediyor. Asıl vurgu?", "Gelecek nesiller tehlikede", ["Bugünün rahatı","Ekonomik kazanç","Teknolojinin faydaları","Bireysel çaba"]
    elif tema == "Arkadaşlık":
        return "Gerçek arkadaş, zor zamanlarda yanında olandır. Bu cümlede vurgulanan?", "Zor zamanlarda destek olmak", ["Hediye almak","Birlikte eğlenmek","Sır tutmak","Sürekli iletişim"]
    else:
        return "Mutluluk parayla satın alınamaz. Ana fikir?", "Mutluluk maddi değildir", ["Para her şeydir","Mutluluk sağlıktır","Mutluluk sevgidir","Mutluluk başarıdır"]

def tur_cumle():
    sorular = [("'Kitap okumayı çok severim.' yüklemin türüne göre?", "İsim cümlesi", ["Fiil cümlesi","İsim cümlesi","Devrik cümle","Birleşik cümle"]),
               ("'Hava çok soğudu.' olumlu mu olumsuz mu?", "Olumlu", ["Olumlu","Olumsuz","Soru","Ünlem"]),
               ("'Ah, bu kadar da olmaz!' cümle türü?", "Ünlem cümlesi", ["İsim cümlesi","Fiil cümlesi","Ünlem cümlesi","Soru cümlesi"]),
               ("'Sınav bitti, herkes sevindi.' cümle yapısı?", "Birleşik cümle", ["Basit cümle","Birleşik cümle","Sıralı cümle","Bağlı cümle"])]
    return random.choice(sorular)

# ==================== SOSYAL BİLGİLER (her konu 5+ tip) ====================
def sos_tarih():
    tip = random.randint(1,6)
    if tip == 1: return "İlk Türk devletlerinden biri?", "Asya Hun Devleti", ["Osmanlı","Asya Hun","Bizans","Roma"]
    elif tip == 2: return "Osmanlı'da Lale Devri yeniliği?", "Matbaa", ["Matbaa","Fetih","Anayasa","Cumhuriyet"]
    elif tip == 3: return "Milli Mücadele kongrelerinden?", "Sivas Kongresi", ["Lozan","Sivas","Erzurum","Amasya"]
    elif tip == 4: return "İstanbul'un fethi hangi padişah?", "Fatih Sultan Mehmet", ["Yavuz Sultan Selim","Kanuni","Fatih Sultan Mehmet","II. Mahmut"]
    elif tip == 5: return "TBMM hangi tarihte açıldı?", "23 Nisan 1920", ["19 Mayıs 1919","23 Nisan 1920","29 Ekim 1923","30 Ağustos 1922"]
    else: return "Cumhuriyet hangi tarihte ilan edildi?", "29 Ekim 1923", ["23 Nisan 1920","29 Ekim 1923","30 Ağustos 1922","1 Kasım 1922"]

def sos_iletisim():
    tip = random.randint(1,4)
    if tip == 1: return "Duygu, düşünce ve bilgilerin aktarılması?", "İletişim", ["Empati","İletişim","Hoşgörü","Saygı"]
    elif tip == 2: return "Karşısındakinin duygularını anlama?", "Empati", ["Sempati","Empati","Özgecilik","Fedakarlık"]
    elif tip == 3: return "Sözsüz iletişim örneği?", "Jest ve mimikler", ["Konuşmak","Jest ve mimikler","Mektup","Telefon"]
    else: return "İletişimde geri bildirim nedir?", "Mesaja cevap", ["Mesajı göndermek","Mesaja cevap","Mesajı kodlamak","Mesajı iletmek"]

def sos_nufus():
    tip = random.randint(1,4)
    if tip == 1: return "Bir ülkede yaşayan insan sayısı?", "Nüfus", ["Nüfus yoğunluğu","Nüfus","Göç","Demografi"]
    elif tip == 2: return "Türkiye'nin en kalabalık şehri?", "İstanbul", ["Ankara","İzmir","İstanbul","Bursa"]
    elif tip == 3: return "Nüfus yoğunluğu en az bölge?", "Doğu Anadolu", ["Marmara","Doğu Anadolu","Akdeniz","Ege"]
    else: return "Göç veren bölgelerden biri?", "Doğu Anadolu", ["Marmara","Ege","Doğu Anadolu","Akdeniz"]

def sos_bilim():
    tip = random.randint(1,4)
    if tip == 1: return "Matematik, fizik, kimya gibi disiplinler?", "Bilim", ["Teknoloji","Sanat","Bilim","Edebiyat"]
    elif tip == 2: return "Teknolojinin olumlu etkisi?", "İletişim kolaylığı", ["Kirlilik","Trafik","İletişim kolaylığı","Sosyal izolasyon"]
    elif tip == 3: return "İcat ile keşif farkı?", "İcat yoktan var eder, keşif var olanı bulur", ["İcat var olanı bulur","Keşif yoktan var eder","İkisi aynı","İcat olmaz"]
    else: return "Bilimsel yöntemin ilk aşaması?", "Gözlem", ["Deney","Gözlem","Hipotez","Sonuç"]

def sos_ekonomi():
    tip = random.randint(1,4)
    if tip == 1: return "İhtiyaçları karşılamak için yapılan faaliyet?", "Üretim", ["Tüketim","Üretim","Pazarlama","Reklam"]
    elif tip == 2: return "Gelir ve gider arasındaki fark?", "Kâr", ["Zarar","Kâr","Bütçe","Tasarruf"]
    elif tip == 3: return "Vergi neden alınır?", "Kamu hizmetleri için", ["İhracat","Kamu hizmetleri","İthalat","Savunma"]
    else: return "Bütçe nedir?", "Gelir-gider planı", ["Gelir tablosu","Gider tablosu","Gelir-gider planı","Kâr tablosu"]

def sos_kultur():
    tip = random.randint(1,4)
    if tip == 1: return "Bir topluma ait maddi manevi değerler?", "Kültür", ["Medeniyet","Kültür","Gelenek","Görenek"]
    elif tip == 2: return "UNESCO Türkiye'den bir miras?", "Kapadokya", ["Ankara","İstanbul","Kapadokya","Antalya"]
    elif tip == 3: return "Somut olmayan kültürel miras?", "Hacivat Karagöz", ["Pamukkale","Efes","Hacivat Karagöz","Ayasofya"]
    else: return "Kültürel farklılıklara saygı neden önemli?", "Toplumsal barış için", ["Ekonomi için","Toplumsal barış için","Ticaret için","Savaş için"]

def sos_demokrasi():
    tip = random.randint(1,4)
    if tip == 1: return "Halkın kendini yönettiği yönetim?", "Demokrasi", ["Monarşi","Oligarşi","Demokrasi","Teokrasi"]
    elif tip == 2: return "Seçme ve seçilme yaşı?", "18", ["16","17","18","20"]
    elif tip == 3: return "Demokrasinin temel ilkesi?", "Milli egemenlik", ["Kuvvetler birliği","Milli egemenlik","Tek parti","Diktatörlük"]
    else: return "Hukukun üstünlüğü ne demek?", "Kanunlar herkese eşit", ["Zenginler farklı","Yöneticiler ayrıcalıklı","Kanunlar herkese eşit","Halk yargılanmaz"]

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
        "Yazım": tur_yazim,
        "Noktalama": tur_noktalama,
        "Sözcükte Anlam": tur_sozcuk,
        "Fiiller": tur_fiil,
        "Zarflar": tur_zarf,
        "Cümlede Anlam": tur_anlam,
        "Paragrafta Anlam": tur_paragraf,
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
