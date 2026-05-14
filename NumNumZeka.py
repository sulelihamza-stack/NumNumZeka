import streamlit as st
import random
import math

# ========== SİYAH ARKA PLAN ==========
st.set_page_config(page_title="NumNum Zeka", page_icon="🎯")
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }
    .stMarkdown, .stText, .stChatMessage, div {
        color: #ffffff !important;
    }
    .stButton button {
        background-color: #333333;
        color: white;
        border-radius: 10px;
    }
    .stSelectbox label, .stMetric label {
        color: white !important;
    }
    .stChatInput textarea {
        background-color: #1a1a1a;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎯 NumNum Zeka - 7. Sınıf")

# ========== OTURUM ==========
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

# ========== MATEMATİK ==========
def mat_tam_sayilar():
    b = random.randint(-60,-10); t = b; h = []
    for _ in range(random.randint(4,7)):
        a = random.randint(5,40)
        if random.choice(["yükseliyor","dalıyor"]) == "yükseliyor":
            t += a; h.append(f"{a} m yükseliyor")
        else:
            t -= a; h.append(f"{a} m dalıyor")
    m = f"Bir dalgıç **{b} m**'de iken " + ", ".join(h) + f"\n\n**Son konum?**"
    d = str(t)
    y = set()
    while len(y) < 3:
        y.add(str(t + random.choice([-12,-9,-7,-5,5,7,9,12])))
    s = [d] + list(y)
    random.shuffle(s)
    return m, d, s

def mat_rasyonel():
    p1=random.randint(1,12); pd1=random.randint(2,12)
    p2=random.randint(1,12); pd2=random.randint(2,12)
    if p1/pd1 > p2/pd2: d=">"
    elif p1/pd1 < p2/pd2: d="<"
    else: d="="
    m = f"{p1}/{pd1} __ {p2}/{pd2} yerine hangi işaret gelir?"
    s = [">","<","=","≠"]
    random.shuffle(s)
    return m, d, s

def mat_rasyonel_islem():
    p1=random.randint(1,8); pd1=random.randint(2,8)
    p2=random.randint(1,8); pd2=random.randint(2,8)
    islem = random.choice(["+","-","x","/"])
    if islem=="+": sp=p1*pd2+p2*pd1; spd=pd1*pd2
    elif islem=="-": sp=p1*pd2-p2*pd1; spd=pd1*pd2
    elif islem=="x": sp=p1*p2; spd=pd1*pd2
    else: sp=p1*pd2; spd=pd1*p2
    eb=math.gcd(sp,spd); sp//=eb; spd//=eb
    d=f"{sp}/{spd}" if spd!=1 else str(sp)
    m = f"{p1}/{pd1} {islem} {p2}/{pd2} = ?"
    s = [d, f"{sp+1}/{spd}", f"{sp-1}/{spd}", f"{sp}/{spd+1}"]
    random.shuffle(s)
    return m, d, s

def mat_cebirsel():
    a=random.randint(1,5); b=random.randint(-8,8)
    c=random.randint(1,5); d=random.randint(-8,8)
    islem=random.choice(["+","-"])
    if islem=="+": son=f"{a+c}x+{b+d}"
    else: son=f"{a-c}x+{b-d}"
    m = f"({a}x{b:+#d}) {islem} ({c}x{d:+#d}) = ?"
    s = [son, f"{a+c+1}x+{b+d}", f"{a+c}x+{b+d+1}", f"{a+c-1}x+{b+d}"]
    random.shuffle(s)
    return m, son, s

def mat_denklem():
    a=random.randint(2,6); b=random.randint(2,15)
    c=random.randint(2,6); d=random.randint(2,15)
    if a==c: a=c+1
    coz=(d-b)/(a-c)
    d_str=str(int(coz)) if coz==int(coz) else f"{coz:.1f}"
    m = f"{a}x+{b}={c}x+{d} → x=?"
    y=[str(int(d_str)+i) for i in [-3,-2,2,3] if int(d_str)+i!=int(d_str)][:3]
    s=[d_str]+y; random.shuffle(s)
    return m, d_str, s

def mat_oran():
    a=random.randint(2,10); b=random.randint(2,10); k=random.randint(2,6)
    x=b*k; d=str(x)
    m = f"{a}/{b}={a*k}/x → x=?"
    s=[d, str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(4,6))]
    random.shuffle(s)
    return m, d, s

def mat_yuzde():
    s=random.randint(100,500); y=random.choice([10,15,20,25,30,40,50])
    son=int(s*y/100); d=str(son)
    m = f"{s} TL'ye %{y} indirim → indirim kaç TL?"
    s=[d, str(son+random.randint(3,8)), str(son-random.randint(3,8)), str(son+random.randint(1,2))]
    random.shuffle(s)
    return m, d, s

def mat_aci():
    a=random.randint(30,150); tip=random.choice(["tümler","bütünler"])
    if tip=="tümler": d=str(90-a); m=f"{a}°'nin tümleri?"
    else: d=str(180-a); m=f"{a}°'nin bütünleri?"
    s=[d, str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
    random.shuffle(s)
    return m, d, s

def mat_cokgen():
    k=random.randint(3,8); tip=random.choice(["iç","dış"])
    if tip=="iç": d=str((k-2)*180); m=f"{k} kenarlı iç açı toplamı?"
    else: d=str(int(360/k)); m=f"Düzgün {k} kenarlı dış açı?"
    s=[d, str(int(d)+random.randint(10,30)), str(int(d)-random.randint(10,30)), str(int(d)+random.randint(5,9))]
    random.shuffle(s)
    return m, d, s

def mat_cember():
    r=random.randint(3,15); tip=random.choice(["çevre","alan"]); pi=3
    if tip=="çevre": d=str(2*pi*r); m=f"Yarıçap {r} cm çember çevresi? (π=3)"
    else: d=str(pi*r*r); m=f"Yarıçap {r} cm daire alanı? (π=3)"
    s=[d, str(int(d)+random.randint(5,15)), str(int(d)-random.randint(5,15)), str(int(d)+random.randint(1,4))]
    random.shuffle(s)
    return m, d, s

def mat_veri():
    v=[random.randint(10,90) for _ in range(5)]
    ort=sum(v)//5; med=sorted(v)[2]
    tip=random.choice(["ortalama","medyan"])
    if tip=="ortalama": d=str(ort); m=f"{v} ortalaması?"
    else: d=str(med); m=f"{v} medyanı?"
    s=[d, str(int(d)+random.randint(2,6)), str(int(d)-random.randint(2,6)), str(int(d)+random.randint(1,2))]
    random.shuffle(s)
    return m, d, s

def mat_cisim():
    c=random.choice(["küp","dikdörtgen prizma","küre","silindir"])
    b={
        "küp":("Bir küpün kaç ayrıtı vardır?","12"),
        "dikdörtgen prizma":("Dikdörtgen prizmanın kaç yüzü vardır?","6"),
        "küre":("Kürenin kaç köşesi vardır?","0"),
        "silindir":("Silindirin yan yüzeyi açılınca hangi şekil olur?","Dikdörtgen")
    }
    m,d=b[c]
    s=[d]+(["8","10","4"] if d=="12" else ["5","7","9"] if d=="6" else ["1","2","4"] if d=="0" else ["Kare","Üçgen","Daire"])
    random.shuffle(s)
    return m, d, s

# ========== FEN ==========
def fen_gunes():
    return "🌞 Güneş sisteminin en büyük gezegeni?", "Jüpiter", ["Mars","Satürn","Jüpiter","Uranüs"]
def fen_hucre():
    return "🔬 Mitoz bölünme sonucu kaç hücre oluşur?", "2", ["1","2","4","8"]
def fen_kuvvet():
    k=random.randint(5,20); v=random.randint(2,10); ke=int(0.5*k*v*v)
    return f"⚡ Kütlesi {k} kg, hızı {v} m/s olan cismin kinetik enerjisi?", str(ke), [str(ke+5), str(ke-5), str(ke+10)]
def fen_madde():
    return "🧪 Homojen karışımlara ne denir?", "Çözelti", ["Süspansiyon","Emülsiyon","Çözelti","Kolloid"]
def fen_isik():
    return "💡 Işığın geri dönmesine ne denir?", "Yansıma", ["Kırılma","Yansıma","Soğurma","Dağılma"]
def fen_ureme():
    return "🐸 Kurbağa gelişimine ne denir?", "Başkalaşım", ["Metamorfoz","Başkalaşım","Döllenme","Büyüme"]
def fen_elektrik():
    r1=random.randint(2,5); r2=random.randint(2,5)
    return f"⚡ {r1}Ω ve {r2}Ω direnç seri bağlanırsa eşdeğer direnç?", str(r1+r2), [str(r1+r2+1), str(r1+r2-1), str(r1+r2+2)]

# ========== TÜRKÇE ==========
def tur_fiil():
    f=random.choice(["gelmek","gitmek","bakmak","yazmak","okumak"])
    d=f.replace("mek","").replace("mak","")+"yor"
    return f"📖 '{f}' fiilinin şimdiki zaman 2. tekil kişi çekimi?", d, [d, d+"m", d+"k", d+"n"]
def tur_zarf():
    return "📝 'Hızlı koştu' cümlesindeki zarf?", "hızlı", ["hızlı","koştu","o","güzel"]
def tur_anlam():
    return "💬 'Keşke daha çok çalışsaydım.' cümlesindeki anlam?", "pişmanlık", ["pişmanlık","özlem","kararlılık","şart"]
def tur_paragraf():
    return "📄 'Ne kadar bilirsen bil, anlatabildiğin kadarsın.' cümlesinin ana fikri?", "Bilginin aktarımı önemlidir", ["Bilgi her şey değildir","Anlatmak zordur","Bilginin aktarımı önemlidir","Sessizlik erdemdir"]
def tur_yazim():
    return "✍️ Aşağıdakilerden hangisi doğru?", "herkes", ["herkez","herkes","herkeş","herkese"]
def tur_noktalama():
    return "🔖 Sıralı cümleleri ayırmak için hangi işaret kullanılır?", "Noktalı virgül", ["Virgül","Nokta","Noktalı virgül","İki nokta"]
def tur_sozcuk():
    return "🔤 'Soğuk' kelimesinin zıt anlamlısı?", "sıcak", ["sıcak","buzlu","donuk","serin"]
def tur_cumle():
    return "📌 'Kitap okumayı çok severim.' cümlesinin türü?", "İsim cümlesi", ["Fiil cümlesi","İsim cümlesi","Devrik cümle","Birleşik cümle"]

# ========== SOSYAL ==========
def sos_iletisim():
    return "🗣️ Duygu,düşünce ve bilgilerin aktarılması?", "İletişim", ["Empati","İletişim","Hoşgörü","Saygı"]
def sos_tarih():
    return "🏛️ İlk Türk devletlerinden biri?", "Asya Hun Devleti", ["Osmanlı","Asya Hun","Bizans","Roma"]
def sos_nufus():
    return "🌍 Bir ülkede yaşayan insan sayısı?", "Nüfus", ["Nüfus yoğunluğu","Nüfus","Göç","Demografi"]
def sos_bilim():
    return "🔬 Matematik, fizik, kimya gibi disiplinler?", "Bilim", ["Teknoloji","Sanat","Bilim","Edebiyat"]
def sos_ekonomi():
    return "💰 İhtiyaçları karşılamak için yapılan faaliyet?", "Üretim", ["Tüketim","Üretim","Pazarlama","Reklam"]
def sos_kultur():
    return "🏺 Bir topluma ait maddi manevi değerler bütünü?", "Kültür", ["Medeniyet","Kültür","Gelenek","Görenek"]
def sos_demokrasi():
    return "🗳️ Halkın kendi kendini yönettiği yönetim biçimi?", "Demokrasi", ["Monarşi","Oligarşi","Demokrasi","Teokrasi"]

# ========== DERS VE KONULAR ==========
tum_dersler = {
    "Matematik": {
        "Tam Sayılar": mat_tam_sayilar, "Rasyonel Sayılar": mat_rasyonel,
        "Rasyonel İşlemler": mat_rasyonel_islem, "Cebirsel İfadeler": mat_cebirsel,
        "Denklemler": mat_denklem, "Oran-Orantı": mat_oran,
        "Yüzdeler": mat_yuzde, "Açılar": mat_aci,
        "Çokgenler": mat_cokgen, "Çember": mat_cember,
        "Veri Analizi": mat_veri, "Cisimler": mat_cisim
    },
    "Fen": {"Güneş Sistemi": fen_gunes, "Hücre": fen_hucre, "Kuvvet": fen_kuvvet,
            "Karışımlar": fen_madde, "Işık": fen_isik, "Üreme": fen_ureme, "Elektrik": fen_elektrik},
    "Türkçe": {"Fiiller": tur_fiil, "Zarflar": tur_zarf, "Cümlede Anlam": tur_anlam,
               "Paragraf": tur_paragraf, "Yazım": tur_yazim, "Noktalama": tur_noktalama,
               "Sözcük": tur_sozcuk, "Cümle Türleri": tur_cumle},
    "Sosyal": {"İletişim": sos_iletisim, "Tarih": sos_tarih, "Nüfus": sos_nufus,
               "Bilim": sos_bilim, "Ekonomi": sos_ekonomi, "Kültür": sos_kultur, "Demokrasi": sos_demokrasi}
}

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown("### 📊 SKOR")
    c1,c2=st.columns(2)
    c1.metric("✅ Doğru", st.session_state.dogru)
    c2.metric("❌ Yanlış", st.session_state.yanlis)
    st.metric("🏆 Puan", st.session_state.puan)
    st.markdown("---")
    
    if st.session_state.secili_ders is None:
        ders = st.selectbox("Ders Seç", list(tum_dersler.keys()))
        if st.button("BAŞLA", use_container_width=True):
            st.session_state.secili_ders = ders
            st.rerun()
    else:
        st.success(f"**{st.session_state.secili_ders}**")
        konular = list(tum_dersler[st.session_state.secili_ders].keys())
        konu = st.selectbox("Konu Seç", konular)
        if st.button("🎲 YENİ SORU", use_container_width=True):
            fonk = tum_dersler[st.session_state.secili_ders][konu]
            m,d,s = fonk()
            if not isinstance(s, list) or len(s)!=4:
                s=[d, str(int(d)+random.randint(2,5)), str(int(d)-random.randint(2,5)), str(int(d)+random.randint(6,10))]
                random.shuffle(s)
            st.session_state.aktif_soru = m
            st.session_state.aktif_cevap = d
            st.session_state.aktif_siklar = s
            st.session_state.mesajlar.append({
                "rol": "asistan",
                "icerik": f"**{st.session_state.secili_ders} - {konu}**\n\n{m}\n\nA) {s[0]}\nB) {s[1]}\nC) {s[2]}\nD) {s[3]}"
            })
            st.rerun()
        if st.button("🔄 Ders Değiştir", use_container_width=True):
            st.session_state.secili_ders = None
            st.session_state.aktif_soru = None
            st.rerun()

# ========== ANA ALAN ==========
if st.session_state.secili_ders is None:
    st.info("🎓 Sol panelden ders ve konu seçip YENİ SORU'ya tıklayın.")
else:
    for msg in st.session_state.mesajlar:
        with st.chat_message(msg["rol"]):
            st.markdown(msg["icerik"])
    
    if st.session_state.aktif_soru:
        cevap = st.chat_input("Cevabını yaz (A, B, C, D):")
        if cevap:
            st.session_state.mesajlar.append({"rol": "kullanici", "icerik": cevap})
            harf = {"A":0,"B":1,"C":2,"D":3}
            if cevap.strip().upper() in harf:
                k_secim = st.session_state.aktif_siklar[harf[cevap.strip().upper()]]
            else:
                k_secim = cevap.strip()
            
            if k_secim == st.session_state.aktif_cevap:
                st.session_state.dogru += 1
                st.session_state.puan += 10
                yanit = f"✅ DOĞRU! +10 puan\nDoğru:{st.session_state.dogru} Yanlış:{st.session_state.yanlis} Puan:{st.session_state.puan}"
            else:
                st.session_state.yanlis += 1
                yanit = f"❌ YANLIŞ! Doğru cevap: {st.session_state.aktif_cevap}\nDoğru:{st.session_state.dogru} Yanlış:{st.session_state.yanlis}"
            
            st.session_state.mesajlar.append({"rol": "asistan", "icerik": yanit})
            st.session_state.aktif_soru = None
            st.rerun()
