import streamlit as st
import random
import math

# ========== SAYFA YAPILANDIRMASI ==========
st.set_page_config(page_title="NumNum Zeka - 7. Sınıf Dinamik Matematik", page_icon="🧠")
st.title("🧮 NumNum Zeka - 7. Sınıf Matematik (Dinamik Sorular)")
st.markdown("**Her soru anında üretilir, sonsuz soru havuzu!**")

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
    st.session_state.secili_ders = None   # Burada sadece "Matematik" olacak
if "puan" not in st.session_state:
    st.session_state.puan = 0
if "dogru_sayisi" not in st.session_state:
    st.session_state.dogru_sayisi = 0
if "yanlis_sayisi" not in st.session_state:
    st.session_state.yanlis_sayisi = 0

# ========== DİNAMİK SORU ÜRETECİ FONKSİYONLARI (HER KONU İÇİN) ==========

# 1. Tam Sayılarla İşlemler
def soru_tam_sayilar():
    baslangic = random.randint(-50, -10)
    hareketler = []
    toplam = baslangic
    adim_sayisi = random.randint(3, 6)
    for _ in range(adim_sayisi):
        adim = random.randint(5, 35)
        yon = random.choice(["yükseliyor", "dalıyor"])
        if yon == "yükseliyor":
            toplam += adim
            hareketler.append(f"{adim} m yükseliyor")
        else:
            toplam -= adim
            hareketler.append(f"{adim} m dalıyor")
    metin = f"Bir dalgıç deniz seviyesinden **{baslangic} m**'de iken " + ", ".join(hareketler) + f".\n\n**Dalgıcın son konumu deniz seviyesine göre kaç metredir?**"
    dogru = str(toplam)
    yanlis = set()
    while len(yanlis) < 3:
        sapma = random.choice([-5, -3, 3, 5, -8, 8])
        y = toplam + sapma
        if y != toplam:
            yanlis.add(str(y))
    siklar = [dogru] + list(yanlis)
    random.shuffle(siklar)
    return metin, dogru, siklar

# 2. Rasyonel Sayılar
def soru_rasyonel():
    pay1 = random.randint(1, 12)
    payda1 = random.randint(2, 12)
    pay2 = random.randint(1, 12)
    payda2 = random.randint(2, 12)
    # İşlem türü: karşılaştırma, sıralama veya ondalık gösterim
    tip = random.choice(["karsilastir", "ondalik"])
    if tip == "karsilastir":
        buyuk = ">"
        if pay1/payda1 > pay2/payda2:
            dogru = ">"
        elif pay1/payda1 < pay2/payda2:
            dogru = "<"
        else:
            dogru = "="
        metin = f"{pay1}/{payda1} **{dogru}** {pay2}/{payda2} ifadesinde hangi işaret olmalıdır?"
        siklar = [">", "<", "=", "≠"]
        random.shuffle(siklar)
        return metin, dogru, siklar
    else:
        # rasyoneli ondalığa çevir
        deger = pay1 / payda1
        dogru = f"{deger:.2f}"
        metin = f"{pay1}/{payda1} rasyonel sayısının ondalık gösterimi (virgülden sonra iki basamak) nedir?"
        yanlis1 = f"{deger + 0.1:.2f}"
        yanlis2 = f"{deger - 0.1:.2f}"
        yanlis3 = f"{deger + 0.05:.2f}"
        siklar = [dogru, yanlis1, yanlis2, yanlis3]
        random.shuffle(siklar)
        return metin, dogru, siklar

# 3. Rasyonel Sayılarla İşlemler
def soru_rasyonel_islem():
    pay1 = random.randint(1, 8)
    payda1 = random.randint(2, 8)
    pay2 = random.randint(1, 8)
    payda2 = random.randint(2, 8)
    islem = random.choice(["+", "-", "x", "/"])
    if islem == "+":
        sonuc_pay = pay1*payda2 + pay2*payda1
        sonuc_payda = payda1*payda2
    elif islem == "-":
        sonuc_pay = pay1*payda2 - pay2*payda1
        sonuc_payda = payda1*payda2
    elif islem == "x":
        sonuc_pay = pay1*pay2
        sonuc_payda = payda1*payda2
    else:  # bölme
        sonuc_pay = pay1*payda2
        sonuc_payda = payda1*pay2
    ebob = math.gcd(sonuc_pay, sonuc_payda)
    if ebob:
        sonuc_pay //= ebob
        sonuc_payda //= ebob
    if sonuc_payda == 1:
        dogru = str(sonuc_pay)
    else:
        dogru = f"{sonuc_pay}/{sonuc_payda}"
    metin = f"{pay1}/{payda1} {islem} {pay2}/{payda2} işleminin sonucu kaçtır? (Kesir sadeleştirilmiş olmalı)"
    yanlis1 = f"{sonuc_pay+1}/{sonuc_payda}" if sonuc_payda != 1 else str(sonuc_pay+1)
    yanlis2 = f"{sonuc_pay-1}/{sonuc_payda}" if sonuc_payda != 1 else str(sonuc_pay-1)
    yanlis3 = f"{sonuc_pay}/{sonuc_payda+1}" if sonuc_payda != 1 else str(sonuc_pay)
    siklar = [dogru, yanlis1, yanlis2, yanlis3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# 4. Cebirsel İfadeler
def soru_cebirsel():
    a = random.randint(1, 5)
    b = random.randint(-8, 8)
    c = random.randint(1, 5)
    d = random.randint(-8, 8)
    islem = random.choice(["+", "-"])
    if islem == "+":
        sonuc = f"{a+c}x + {b+d}"
    else:
        sonuc = f"{a-c}x + {b-d}"
    metin = f"**({a}x {'+' if b>=0 else '-'} {abs(b)}) {islem} ({c}x {'+' if d>=0 else '-'} {abs(d)})** işleminin en sade hali aşağıdakilerden hangisidir?"
    # şık üret (gerçek sonuç + değiştirilmiş)
    y1 = f"{a+c+1}x + {b+d}"
    y2 = f"{a+c}x + {b+d+1}"
    y3 = f"{a+c-1}x + {b+d}"
    siklar = [sonuc, y1, y2, y3]
    random.shuffle(siklar)
    return metin, sonuc, siklar

# 5. Eşitlik ve Denklem
def soru_denklem():
    a = random.randint(2, 6)
    b = random.randint(2, 15)
    c = random.randint(2, 6)
    d = random.randint(2, 15)
    # Denklem: a*x + b = c*x + d
    cozum = (d - b) / (a - c) if a != c else random.randint(1, 10)
    if cozum != int(cozum):
        cozum = round(cozum, 1)
    dogru = str(cozum)
    metin = f"{a}x + {b} = {c}x + {d} denklemini sağlayan x değeri kaçtır?"
    yanlis = [str(cozum + random.choice([-2, -1, 1, 2])), str(cozum + random.choice([-3, 3])), str(cozum + random.choice([-4, 4]))]
    siklar = [dogru] + yanlis[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# 6. Oran ve Orantı
def soru_oran():
    a = random.randint(2, 10)
    b = random.randint(2, 10)
    k = random.randint(2, 6)
    # a/b = (a*k)/x -> x = b*k
    x = b * k
    dogru = str(x)
    metin = f"{a}/{b} = {a*k}/x orantısında x kaçtır?"
    yanlis = [str(x+random.randint(1,3)), str(x-random.randint(1,3)), str(x+random.randint(4,6))]
    siklar = [dogru] + yanlis[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# 7. Yüzdeler
def soru_yuzde():
    sayi = random.randint(100, 500)
    yuzde = random.choice([10, 15, 20, 25, 30, 40, 50])
    sonuc = int(sayi * yuzde / 100)
    dogru = str(sonuc)
    metin = f"Bir mağazada {sayi} TL'lik bir ürüne %{yuzde} indirim yapılıyor. **İndirim miktarı kaç TL'dir?**"
    yanlis = [str(sonuc+random.randint(3,8)), str(sonuc-random.randint(3,8)), str(sonuc+random.randint(1,2))]
    siklar = [dogru] + yanlis[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# 8. Doğrular ve Açılar
def soru_aci():
    aci = random.randint(30, 150)
    tip = random.choice(["tumler", "butunler"])
    if tip == "tumler":
        dogru = str(90 - aci)
        metin = f"{aci}°'lik açının tümleri kaç derecedir?"
    else:
        dogru = str(180 - aci)
        metin = f"{aci}°'lik açının bütünleri kaç derecedir?"
    yanlis = [str(int(dogru)+random.randint(5,15)), str(int(dogru)-random.randint(5,15)), str(int(dogru)+random.randint(1,4))]
    siklar = [dogru] + yanlis[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# 9. Çokgenler
def soru_cokgen():
    kenar = random.randint(3, 8)
    ic = (kenar - 2) * 180
    dis = 360 / kenar
    tip = random.choice(["ic", "dis"])
    if tip == "ic":
        dogru = str(ic)
        metin = f"{kenar} kenarlı bir çokgenin iç açılarının toplamı kaç derecedir?"
    else:
        dogru = str(int(dis))
        metin = f"Düzgün {kenar} kenarlı bir çokgenin bir dış açısı kaç derecedir?"
    yanlis = [str(int(dogru)+random.randint(10,30)), str(int(dogru)-random.randint(10,30)), str(int(dogru)+random.randint(5,9))]
    siklar = [dogru] + yanlis[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# 10. Çember ve Daire
def soru_cember():
    yaricap = random.randint(3, 15)
    tip = random.choice(["cevre", "alan"])
    pi = 3
    if tip == "cevre":
        cevre = 2 * pi * yaricap
        dogru = str(cevre)
        metin = f"Yarıçapı {yaricap} cm olan çemberin çevresi kaç cm'dir? (π=3 alınız)"
    else:
        alan = pi * yaricap * yaricap
        dogru = str(alan)
        metin = f"Yarıçapı {yaricap} cm olan dairenin alanı kaç cm²'dir? (π=3 alınız)"
    yanlis = [str(int(dogru)+random.randint(5,15)), str(int(dogru)-random.randint(5,15)), str(int(dogru)+random.randint(1,4))]
    siklar = [dogru] + yanlis[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# 11. Veri Analizi
def soru_veri():
    veri = [random.randint(10, 90) for _ in range(5)]
    ortalama = sum(veri) // 5
    medyan = sorted(veri)[2]
    tip = random.choice(["ortalama", "medyan"])
    if tip == "ortalama":
        dogru = str(ortalama)
        metin = f"{veri} veri grubunun aritmetik ortalaması kaçtır?"
    else:
        dogru = str(medyan)
        metin = f"{veri} veri grubunun medyanı (ortanca değeri) kaçtır?"
    yanlis = [str(int(dogru)+random.randint(2,6)), str(int(dogru)-random.randint(2,6)), str(int(dogru)+random.randint(1,2))]
    siklar = [dogru] + yanlis[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# 12. Cisimlerin Farklı Yönlerden Görünümleri
def soru_cisim():
    cisim = random.choice(["küp", "dikdörtgen prizma", "küre", "silindir"])
    sorular = {
        "küp": ("Bir küpün kaç ayrıtı vardır?", "12"),
        "dikdörtgen prizma": ("Dikdörtgen prizmanın kaç yüzü vardır?", "6"),
        "küre": ("Kürenin kaç köşesi vardır?", "0"),
        "silindir": ("Silindirin yan yüzeyi açıldığında hangi şekil oluşur?", "Dikdörtgen")
    }
    metin, dogru = sorular[cisim]
    yanlis = ["8", "10", "4"] if dogru == "12" else ["5", "7", "9"] if dogru == "6" else ["1", "2", "4"] if dogru == "0" else ["Kare", "Üçgen", "Daire"]
    siklar = [dogru] + yanlis[:3]
    random.shuffle(siklar)
    return metin, dogru, siklar

# ========== KONU - FONKSİYON EŞLEMESİ ==========
konu_uretici = {
    "Tam Sayılarla İşlemler": soru_tam_sayilar,
    "Rasyonel Sayılar": soru_rasyonel,
    "Rasyonel Sayılarla İşlemler": soru_rasyonel_islem,
    "Cebirsel İfadeler": soru_cebirsel,
    "Eşitlik ve Denklem": soru_denklem,
    "Oran ve Orantı": soru_oran,
    "Yüzdeler": soru_yuzde,
    "Doğrular ve Açılar": soru_aci,
    "Çokgenler": soru_cokgen,
    "Çember ve Daire": soru_cember,
    "Veri Analizi": soru_veri,
    "Cisimlerin Farklı Yönlerden Görünümleri": soru_cisim
}
konular_listesi = list(konu_uretici.keys())

# ========== YAN PANEL (SIDEBAR) ==========
with st.sidebar:
    st.header("📊 İstatistikler")
    col1, col2 = st.columns(2)
    col1.metric("✅ Doğru", st.session_state.dogru_sayisi)
    col2.metric("❌ Yanlış", st.session_state.yanlis_sayisi)
    st.metric("🏆 Toplam Puan", st.session_state.puan)
    
    st.markdown("---")
    if st.session_state.secili_ders:
        secilen_konu = st.selectbox("📌 Konu Seç", konular_listesi)
        if st.button("🎲 YENİ SORU", use_container_width=True):
            # dinamik soru üret
            uretici = konu_uretici[secilen_konu]
            soru_metni, dogru_cevap, siklar = uretici()
            st.session_state.aktif_soru = soru_metni
            st.session_state.aktif_cevap = dogru_cevap
            st.session_state.aktif_siklar = siklar
            st.session_state.mesajlar.append({
                "rol": "asistan",
                "icerik": f"**📐 Konu: {secilen_konu}**\n\n{soru_metni}\n\n🔽 Seçenekler:\n\nA) {siklar[0]}\nB) {siklar[1]}\nC) {siklar[2]}\nD) {siklar[3]}"
            })
            st.rerun()
    
    if st.button("🔄 SIFIRLA", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# ========== DERS SEÇİMİ (SADECE MATEMATİK VAR) ==========
if st.session_state.secili_ders is None:
    st.info("🎓 **NumNum Zeka - 7. Sınıf Matematik**\n\nBu uygulama, 7. sınıf müfredatının tüm konularını kapsayan **dinamik soru üreteci** ile çalışır. Sonsuz soru, hiçbiri tekrar etmez.\n\nBaşlamak için aşağıdaki butona tıklayın.")
    if st.button("🚀 MATEMATİK DERSİNE BAŞLA", use_container_width=True):
        st.session_state.secili_ders = "Matematik"
        st.rerun()
else:
    # ========== SOHBET ARAYÜZÜ ==========
    for mesaj in st.session_state.mesajlar:
        with st.chat_message(mesaj["rol"]):
            st.markdown(mesaj["icerik"])
    
    # Kullanıcı cevap girişi
    if st.session_state.aktif_soru:
        kullanici_cevap = st.chat_input("Cevabını yaz (A, B, C veya D) veya harf seç:")
        if kullanici_cevap:
            st.session_state.mesajlar.append({"rol": "kullanici", "icerik": kullanici_cevap})
            # Harf kontrolü (A-> index 0, B->1, ...)
            cevap_harf = kullanici_cevap.strip().upper()
            harf_map = {"A":0, "B":1, "C":2, "D":3}
            if cevap_harf in harf_map:
                kullanici_secimi = st.session_state.aktif_siklar[harf_map[cevap_harf]]
            else:
                kullanici_secimi = kullanici_cevap.strip()
            
            if kullanici_secimi == st.session_state.aktif_cevap:
                st.session_state.dogru_sayisi += 1
                st.session_state.puan += 10
                yanit = f"✅ **Doğru!** +10 puan\n\nDoğru sayısı: {st.session_state.dogru_sayisi}\nPuan: {st.session_state.puan}\n\nYeni soru için sağ panelden 'YENİ SORU' butonuna tıklayın."
            else:
                st.session_state.yanlis_sayisi += 1
                yanit = f"❌ **Yanlış!** Doğru cevap: **{st.session_state.aktif_cevap}**\n\nDoğru: {st.session_state.dogru_sayisi} | Yanlış: {st.session_state.yanlis_sayisi}\n\nYeni soru için butona tıklayın."
            
            st.session_state.mesajlar.append({"rol": "asistan", "icerik": yanit})
            st.session_state.aktif_soru = None
            st.session_state.aktif_cevap = None
            st.session_state.aktif_siklar = None
            st.rerun()
    else:
        # Aktif soru yoksa sadece bekleme mesajı
        st.chat_input("Yeni soru almak için sağ panelden bir konu seçip 'YENİ SORU' butonuna tıklayın.", disabled=True)