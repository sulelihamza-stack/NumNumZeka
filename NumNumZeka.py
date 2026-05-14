import streamlit as st
import random
import math

st.set_page_config(page_title="NumNum Zeka", page_icon="🎯")
st.markdown("""
<style>
    .stApp { background-color: #000000; }
    .stMarkdown, .stText, div, p, span { color: #ffffff !important; }
    .stButton button { background-color: #333333; color: white; border-radius: 10px; width: 100%; }
    .stSelectbox label, .stMetric label { color: white !important; }
    .stChatInput textarea { background-color: #1a1a1a; color: white; }
    .stSuccess, .stInfo, .stWarning { background-color: #222222 !important; }
</style>
""", unsafe_allow_html=True)

st.title("🎯 NumNum Zeka - 7. Sınıf")

if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = []
    st.session_state.aktif_soru = None
    st.session_state.aktif_cevap = None
    st.session_state.aktif_siklar = None
    st.session_state.secili_ders = None
    st.session_state.puan = 0
    st.session_state.dogru = 0
    st.session_state.yanlis = 0

# ==================== MATEMATİK ====================
def mat_tam():
    b = random.randint(-60, -10)
    t = b
    h = []
    for _ in range(random.randint(4, 7)):
        a = random.randint(5, 40)
        if random.choice([0,1]) == 0:
            t += a
            h.append(f"{a} m yükseliyor")
        else:
            t -= a
            h.append(f"{a} m dalıyor")
    m = f"Bir dalgıç **{b} m**'de iken " + ", ".join(h) + f"\n\n**Son konum kaç m?**"
    d = str(t)
    y = [str(t+random.choice([5,7,9])), str(t-random.choice([5,7,9])), str(t+random.choice([11,13]))]
    s = [d] + y
    random.shuffle(s)
    return m, d, s

def mat_ras():
    p1 = random.randint(1,12)
    pd1 = random.randint(2,12)
    p2 = random.randint(1,12)
    pd2 = random.randint(2,12)
    if p1/pd1 > p2/pd2:
        d = ">"
    elif p1/pd1 < p2/pd2:
        d = "<"
    else:
        d = "="
    m = f"{p1}/{pd1} __ {p2}/{pd2} yerine ne gelir?"
    s = [">", "<", "=", "≠"]
    random.shuffle(s)
    return m, d, s

def mat_ras_is():
    p1 = random.randint(1,8)
    pd1 = random.randint(2,8)
    p2 = random.randint(1,8)
    pd2 = random.randint(2,8)
    islem = random.choice(["+","-","x","/"])
    if islem == "+":
        sp = p1*pd2 + p2*pd1
        spd = pd1*pd2
    elif islem == "-":
        sp = p1*pd2 - p2*pd1
        spd = pd1*pd2
    elif islem == "x":
        sp = p1*p2
        spd = pd1*pd2
    else:
        sp = p1*pd2
        spd = pd1*p2
    eb = math.gcd(sp, spd)
    sp //= eb
    spd //= eb
    d = f"{sp}/{spd}" if spd != 1 else str(sp)
    m = f"{p1}/{pd1} {islem} {p2}/{pd2} = ?"
    s = [d, f"{sp+1}/{spd}", f"{sp-1}/{spd}", f"{sp}/{spd+1}"]
    random.shuffle(s)
    return m, d, s

def mat_ceb():
    a = random.randint(1,5)
    b = random.randint(-8,8)
    c = random.randint(1,5)
    d = random.randint(-8,8)
    islem = random.choice(["+","-"])
    if islem == "+":
        son = f"{a+c}x+{b+d}"
    else:
        son = f"{a-c}x+{b-d}"
    m = f"({a}x{b:+d}) {islem} ({c}x{d:+d}) = ?"
    s = [son, f"{a+c+1}x+{b+d}", f"{a+c}x+{b+d+1}", f"{a+c-1}x+{b+d}"]
    random.shuffle(s)
    return m, son, s

def mat_denk():
    a = random.randint(2,6)
    b = random.randint(2,15)
    c = random.randint(2,6)
    d = random.randint(2,15)
    if a == c:
        a = c+1
    coz = (d-b)/(a-c)
    if coz == int(coz):
        dogru = str(int(coz))
    else:
        dogru = f"{coz:.1f}"
    m = f"{a}x+{b}={c}x+{d} denkleminde x kaç?"
    y = [str(float(dogru)+i) for i in [-3,-2,2,3] if float(dogru)+i != float(dogru)][:3]
    s = [dogru] + y
    random.shuffle(s)
    return m, dogru, s

def mat_oran():
    a = random.randint(2,10)
    b = random.randint(2,10)
    k = random.randint(2,6)
    x = b*k
    d = str(x)
    m = f"{a}/{b} = {a*k}/x ise x kaç?"
    s = [d, str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(4,6))]
    random.shuffle(s)
    return m, d, s

def mat_yuz():
    s = random.randint(100,500)
    y = random.choice([10,15,20,25,30,40,50])
    son = int(s*y/100)
    d = str(son)
    m = f"{s} TL'nin %{y} indirimi kaç TL?"
    s = [d, str(son+random.randint(3,8)), str(son-random.randint(3,8)), str(son+random.randint(1,2))]
    random.shuffle(s)
    return m, d, s

def mat_aci():
    a = random.randint(30,150)
    tip = random.choice(["tümler","bütünler"])
    if tip == "tümler":
        d = str(90-a)
        m = f"{a}°'nin tümleri kaç?"
    else:
        d = str(180-a)
        m = f"{a}°'nin bütünleri kaç?"
    s = [d, str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
    random.shuffle(s)
    return m, d, s

def mat_cok():
    k = random.randint(3,8)
    tip = random.choice(["iç","dış"])
    if tip == "iç":
        d = str((k-2)*180)
        m = f"{k} kenarlı çokgenin iç açı toplamı?"
    else:
        d = str(int(360/k))
        m = f"Düzgün {k} kenarlı çokgenin dış açısı?"
    s = [d, str(int(d)+random.randint(10,30)), str(int(d)-random.randint(10,30)), str(int(d)+random.randint(5,9))]
    random.shuffle(s)
    return m, d, s

def mat_cem():
    r = random.randint(3,15)
    tip = random.choice(["çevre","alan"])
    pi = 3
    if tip == "çevre":
        d = str(2*pi*r)
        m = f"Yarıçap {r} cm çemberin çevresi? (π=3)"
    else:
        d = str(pi*r*r)
        m = f"Yarıçap {r} cm dairenin alanı? (π=3)"
    s = [d, str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
    random.shuffle(s)
    return m, d, s

def mat_veri():
    v = [random.randint(10,90) for _ in range(5)]
    ort = sum(v)//5
    med = sorted(v)[2]
    tip = random.choice(["ortalama","medyan"])
    if tip == "ortalama":
        d = str(ort)
        m = f"{v} ortalaması kaç?"
    else:
        d = str(med)
        m = f"{v} medyanı kaç?"
    s = [d, str(int(d)+random.randint(2,6)), str(int(d)-random.randint(2,6)), str(int(d)+random.randint(1,2))]
    random.shuffle(s)
    return m, d, s

def mat_cis():
    c = random.choice(["küp","dikdörtgen prizma","küre","silindir"])
    if c == "küp":
        return "Bir küpün kaç ayrıtı vardır?", "12", ["8","10","12","14"]
    elif c == "dikdörtgen prizma":
        return "Dikdörtgen prizmanın kaç yüzü vardır?", "6", ["4","5","6","8"]
    elif c == "küre":
        return "Kürenin kaç köşesi vardır?", "0", ["0","1","2","4"]
    else:
        return "Silindirin yan yüzeyi açılınca hangi şekil olur?", "Dikdörtgen", ["Kare","Üçgen","Dikdörtgen","Daire"]

# ==================== FEN ====================
def fen1():
    return "Güneş sisteminin en büyük gezegeni?", "Jüpiter", ["Mars","Satürn","Jüpiter","Uranüs"]
def fen2():
    return "Mitoz bölünme sonucu kaç hücre oluşur?", "2", ["1","2","4","8"]
def fen3():
    k = random.randint(5,20)
    v = random.randint(2,10)
    ke = int(0.5*k*v*v)
    return f"Kütlesi {k} kg, hızı {v} m/s olan cismin kinetik enerjisi?", str(ke), [str(ke+5), str(ke-5), str(ke+10)]
def fen4():
    return "Homojen karışımlara ne denir?", "Çözelti", ["Süspansiyon","Emülsiyon","Çözelti","Kolloid"]
def fen5():
    return "Işığın geri dönmesine ne denir?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]
def fen6():
    return "Kurbağa gelişimine ne denir?", "Başkalaşım", ["Metamorfoz","Başkalaşım","Döllenme","Büyüme"]
def fen7():
    r1 = random.randint(2,5)
    r2 = random.randint(2,5)
    return f"{r1}Ω ve {r2}Ω direnç seri bağlanırsa eşdeğer direnç?", str(r1+r2), [str(r1+r2+1), str(r1+r2-1), str(r1+r2+2)]

# ==================== TÜRKÇE ====================
def tur1():
    f = random.choice(["gelmek","gitmek","bakmak","yazmak","okumak"])
    d = f.replace("mek","").replace("mak","") + "yor"
    return f"'{f}' fiilinin şimdiki zaman 2. tekil kişi çekimi?", d, [d, d+"m", d+"k", d+"n"]
def tur2():
    return "'Hızlı koştu' cümlesindeki zarf?", "hızlı", ["hızlı","koştu","o","güzel"]
def tur3():
    return "'Keşke daha çok çalışsaydım.' cümlesindeki anlam?", "pişmanlık", ["pişmanlık","özlem","kararlılık","şart"]
def tur4():
    return "'Ne kadar bilirsen bil, anlatabildiğin kadarsın.' ana fikri?", "Bilginin aktarımı önemlidir", ["Bilgi her şey değildir","Anlatmak zordur","Bilginin aktarımı önemlidir","Sessizlik erdemdir"]
def tur5():
    return "Aşağıdakilerden hangisi doğru yazılmıştır?", "herkes", ["herkez","herkes","herkeş","herkese"]
def tur6():
    return "Sıralı cümleleri ayırmak için hangi noktalama işareti kullanılır?", "Noktalı virgül", ["Virgül","Nokta","Noktalı virgül","İki nokta"]
def tur7():
    return "'Soğuk' kelimesinin zıt anlamlısı?", "sıcak", ["sıcak","buzlu","donuk","serin"]
def tur8():
    return "'Kitap okumayı çok severim.' cümlesi yüklemin türüne göre?", "İsim cümlesi", ["Fiil cümlesi","İsim cümlesi","Devrik cümle","Birleşik cümle"]

# ==================== SOSYAL ====================
def sos1():
    return "Duygu, düşünce ve bilgilerin aktarılmasına ne denir?", "İletişim", ["Empati","İletişim","Hoşgörü","Saygı"]
def sos2():
    return "İlk Türk devletlerinden biri?", "Asya Hun Devleti", ["Osmanlı","Asya Hun","Bizans","Roma"]
def sos3():
    return "Bir ülkede yaşayan insan sayısına ne denir?", "Nüfus", ["Nüfus yoğunluğu","Nüfus","Göç","Demografi"]
def sos4():
    return "Matematik, fizik, kimya gibi disiplinlere ne ad verilir?", "Bilim", ["Teknoloji","Sanat","Bilim","Edebiyat"]
def sos5():
    return "İhtiyaçları karşılamak için yapılan faaliyete ne denir?", "Üretim", ["Tüketim","Üretim","Pazarlama","Reklam"]
def sos6():
    return "Bir topluma ait maddi ve manevi değerler bütününe ne denir?", "Kültür", ["Medeniyet","Kültür","Gelenek","Görenek"]
def sos7():
    return "Halkın kendi kendini yönettiği yönetim biçimi?", "Demokrasi", ["Monarşi","Oligarşi","Demokrasi","Teokrasi"]

# ==================== DERS KONU BİRLEŞTİRME ====================
tum_dersler = {
    "Matematik": {
        "Tam Sayılar": mat_tam, "Rasyonel Sayılar": mat_ras, "Rasyonel İşlemler": mat_ras_is,
        "Cebirsel İfadeler": mat_ceb, "Denklemler": mat_denk, "Oran-Orantı": mat_oran,
        "Yüzdeler": mat_yuz, "Açılar": mat_aci, "Çokgenler": mat_cok,
        "Çember": mat_cem, "Veri Analizi": mat_veri, "Cisimler": mat_cis
    },
    "Fen Bilimleri": {
        "Güneş Sistemi": fen1, "Hücre": fen2, "Kuvvet": fen3,
        "Karışımlar": fen4, "Işık": fen5, "Üreme": fen6, "Elektrik": fen7
    },
    "Türkçe": {
        "Fiiller": tur1, "Zarflar": tur2, "Cümlede Anlam": tur3,
        "Paragraf": tur4, "Yazım": tur5, "Noktalama": tur6,
        "Sözcük": tur7, "Cümle Türleri": tur8
    },
    "Sosyal Bilgiler": {
        "İletişim": sos1, "Tarih": sos2, "Nüfus": sos3,
        "Bilim": sos4, "Ekonomi": sos5, "Kültür": sos6, "Demokrasi": sos7
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
            
            harf_map = {"A":0, "B":1, "C":2, "D":3}
            if cevap.strip().upper() in harf_map:
                kullanici_sec = st.session_state.aktif_siklar[harf_map[cevap.strip().upper()]]
            else:
                kullanici_sec = cevap.strip()
            
            if kullanici_sec == st.session_state.aktif_cevap:
                st.session_state.dogru += 1
                st.session_state.puan += 10
                yanit = f"✅ **DOĞRU!** +10 puan\n\n**Doğru:** {st.session_state.dogru} | **Yanlış:** {st.session_state.yanlis} | **Puan:** {st.session_state.puan}"
            else:
                st.session_state.yanlis += 1
                yanit = f"❌ **YANLIŞ!** Doğru cevap: **{st.session_state.aktif_cevap}**\n\n**Doğru:** {st.session_state.dogru} | **Yanlış:** {st.session_state.yanlis} | **Puan:** {st.session_state.puan}"
            
            st.session_state.mesajlar.append({"rol": "asistan", "icerik": yanit})
            st.session_state.aktif_soru = None
            st.session_state.aktif_cevap = None
            st.session_state.aktif_siklar = None
            st.rerun()
