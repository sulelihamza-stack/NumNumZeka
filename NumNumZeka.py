import streamlit as st
import random
import math
import time
import json
import os
from datetime import datetime

# ============================================================
# SAYFA YAPILANDIRMASI
# ============================================================
st.set_page_config(
    page_title="NumNum Zeka - 7. Sınıf Tüm Dersler", 
    page_icon="🎯", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Özel CSS ile görünüm iyileştirme
st.markdown("""
<style>
    .stApp {
        background-color: #f5f7fb;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    .chat-message {
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎯 NumNum Zeka - 7. Sınıf Tüm Dersler")
st.markdown("### *Müfredata %100 Uygun | Dinamik Soru Üreteci | Sonsuz Havuz*")
st.markdown("---")

# ============================================================
# OTURUM DURUMU (SESSION STATE) - TÜM DEĞİŞKENLER
# ============================================================
if "mesajlar" not in st.session_state:
    st.session_state.mesajlar = []
if "aktif_soru" not in st.session_state:
    st.session_state.aktif_soru = None
    st.session_state.aktif_cevap = None
    st.session_state.aktif_siklar = None
    st.session_state.secili_ders = None
    st.session_state.secili_konu = None
    st.session_state.puan = 0
    st.session_state.dogru = 0
    st.session_state.yanlis = 0
    st.session_state.oturum_baslangic = datetime.now()
    st.session_state.tarihce = []
    st.session_state.basari_yuzdesi = 0
    st.session_state.soru_sayisi = 0
    st.session_state.son_10_dogru = []
    st.session_state.aktif_tema = "açık"

# ============================================================
# YARDIMCI FONKSİYONLAR
# ============================================================

def update_stats(is_correct):
    """İstatistikleri güncelle"""
    if is_correct:
        st.session_state.dogru += 1
        st.session_state.puan += 10
        st.session_state.son_10_dogru.append(1)
    else:
        st.session_state.yanlis += 1
        st.session_state.son_10_dogru.append(0)
    
    st.session_state.soru_sayisi += 1
    
    if len(st.session_state.son_10_dogru) > 10:
        st.session_state.son_10_dogru.pop(0)
    
    if st.session_state.soru_sayisi > 0:
        st.session_state.basari_yuzdesi = (st.session_state.dogru / st.session_state.soru_sayisi) * 100
    
    st.session_state.tarihce.append({
        "zaman": datetime.now(),
        "sonuc": is_correct,
        "ders": st.session_state.secili_ders,
        "konu": st.session_state.secili_konu
    })

def get_basari_seviyesi():
    """Başarı seviyesine göre mesaj döndür"""
    yuzde = st.session_state.basari_yuzdesi
    if yuzde >= 90:
        return "🏆 Mükemmel! Üstün başarı gösteriyorsun!"
    elif yuzde >= 75:
        return "🌟 Çok iyi! Bu şekilde devam et!"
    elif yuzde >= 60:
        return "📈 İyi gidiyorsun! Daha da yükselebilirsin!"
    elif yuzde >= 40:
        return "📚 İyi bir başlangıç! Daha çok pratik yap!"
    else:
        return "💪 Yeni başlıyorsun! Bol bol soru çöz!"

# ============================================================
# MATEMATİK - 12 KONU (ÇOK TİPLİ DİNAMİK SORULAR)
# ============================================================

def mat_tam_sayilar():
    """Tam Sayılarla İşlemler - 8 farklı soru tipi"""
    tip = random.choice([1,2,3,4,5,6,7,8])
    
    if tip == 1:
        # Tip 1: Dalgıç sorusu
        baslangic = random.randint(-60, -10)
        toplam = baslangic
        hareketler = []
        for _ in range(random.randint(4, 8)):
            adim = random.randint(5, 45)
            yon = random.choice(["yükseliyor", "dalıyor"])
            if yon == "yükseliyor":
                toplam += adim
                hareketler.append(f"{adim} m yükseliyor")
            else:
                toplam -= adim
                hareketler.append(f"{adim} m dalıyor")
        metin = f"🐟 **Dalgıç Problemi**\n\nBir dalgıç deniz seviyesinden **{baslangic} metre** derinlikte iken sırasıyla: " + ", ".join(hareketler) + f".\n\n**Dalgıcın son konumu deniz seviyesine göre kaç metredir?**"
        dogru = str(toplam)
    
    elif tip == 2:
        # Tip 2: Termometre sorusu
        baslangic = random.randint(-20, -5)
        toplam = baslangic
        olaylar = []
        for _ in range(random.randint(4, 7)):
            degisim = random.randint(5, 30)
            yon = random.choice(["artıyor", "düşüyor"])
            if yon == "artıyor":
                toplam += degisim
                olaylar.append(f"{degisim}°C artıyor")
            else:
                toplam -= degisim
                olaylar.append(f"{degisim}°C düşüyor")
        metin = f"🌡️ **Sıcaklık Değişimi**\n\nBir termometre sabah **{baslangic}°C**'yi gösteriyor. Gün içinde sırasıyla: " + ", ".join(olaylar) + f".\n\n**Termometre gün sonunda kaç °C'yi gösterir?**"
        dogru = str(toplam)
    
    elif tip == 3:
        # Tip 3: Hesap makinesi
        sayi = random.randint(-50, 50)
        toplam = sayi
        islemler = []
        for _ in range(random.randint(4, 7)):
            adim = random.randint(5, 40)
            yon = random.choice(["+", "-"])
            if yon == "+":
                toplam += adim
                islemler.append(f"+{adim}")
            else:
                toplam -= adim
                islemler.append(f"-{adim}")
        metin = f"📱 **Hesap Makinesi**\n\nBir hesap makinesinde ekranda **{sayi}** yazmaktadır. Sırasıyla " + ", ".join(islemler) + f" tuşlarına basılıyor.\n\n**Ekrandaki son sayı kaçtır?**"
        dogru = str(toplam)
    
    elif tip == 4:
        # Tip 4: Asansör
        baslangic = random.randint(-5, 5)
        toplam = baslangic
        katlar = []
        for _ in range(random.randint(4, 7)):
            adim = random.randint(3, 12)
            yon = random.choice(["yukarı", "aşağı"])
            if yon == "yukarı":
                toplam += adim
                katlar.append(f"{adim} kat yukarı")
            else:
                toplam -= adim
                katlar.append(f"{adim} kat aşağı")
        metin = f"🏢 **Asansör Problemi**\n\nBir asansör zemin kata göre **{baslangic}. katta** iken sırasıyla: " + ", ".join(katlar) + f" hareket ediyor.\n\n**Asansör son durumda kaçıncı kattadır?**"
        dogru = str(toplam)
    
    elif tip == 5:
        # Tip 5: Banka hesabı
        baslangic = random.randint(200, 1000)
        toplam = baslangic
        islemler = []
        for _ in range(random.randint(4, 7)):
            miktar = random.randint(50, 300)
            yon = random.choice(["yatırıyor", "çekiyor"])
            if yon == "yatırıyor":
                toplam += miktar
                islemler.append(f"{miktar} TL yatırıyor")
            else:
                toplam -= miktar
                islemler.append(f"{miktar} TL çekiyor")
        metin = f"💰 **Banka Hesabı**\n\nBir hesapta başlangıçta **{baslangic} TL** bulunmaktadır. Hesap sahibi sırasıyla: " + ", ".join(islemler) + f".\n\n**Son durumda hesapta kaç TL vardır?**"
        dogru = str(toplam)
    
    elif tip == 6:
        # Tip 6: Dağcı
        baslangic = random.randint(500, 2500)
        toplam = baslangic
        hareketler = []
        for _ in range(random.randint(4, 7)):
            mesafe = random.randint(100, 600)
            yon = random.choice(["tırmanıyor", "iniyor"])
            if yon == "tırmanıyor":
                toplam += mesafe
                hareketler.append(f"{mesafe} m tırmanıyor")
            else:
                toplam -= mesafe
                hareketler.append(f"{mesafe} m iniyor")
        metin = f"⛰️ **Dağcı Problemi**\n\nBir dağcı deniz seviyesinden **+{baslangic} metre** yükseklikteki kamp alanından tırmanışa başlıyor. Sırasıyla: " + ", ".join(hareketler) + f".\n\n**Dağcının son yüksekliği kaç metredir?**"
        dogru = str(toplam)
    
    elif tip == 7:
        # Tip 7: Maaş zammı
        baslangic = random.randint(2500, 4000)
        toplam = baslangic
        zam_miktar = random.randint(150, 400)
        ay_sayisi = random.randint(3, 6)
        for _ in range(ay_sayisi):
            toplam += zam_miktar
        metin = f"💼 **Maaş Zammı**\n\nBir işçinin başlangıç maaşı **{baslangic} TL**'dir. Her ay **{zam_miktar} TL** zam almaktadır.\n\n**{ay_sayisi} ay sonunda işçinin maaşı kaç TL olur?**"
        dogru = str(toplam)
    
    else:
        # Tip 8: Oyun puanı
        baslangic = random.randint(100, 500)
        toplam = baslangic
        hamle_sayisi = random.randint(4, 8)
        for _ in range(hamle_sayisi):
            puan = random.randint(15, 50)
            if random.choice([True, False]):
                toplam += puan
        metin = f"🎮 **Oyun Skoru**\n\nBir oyuncu yarışmaya **{baslangic} puan** ile başlıyor. {hamle_sayisi} hamle sonucunda puan kazanıp kaybediyor.\n\n**Oyuncunun son puanı kaçtır?**"
        dogru = str(toplam)
    
    # Şıkları oluştur
    yanlisler = set()
    while len(yanlisler) < 3:
        sapma = random.choice([-12, -9, -7, -5, 5, 7, 9, 12])
        y = int(dogru) + sapma
        if y != int(dogru):
            yanlisler.add(str(y))
    siklar = [dogru] + list(yanlisler)
    random.shuffle(siklar)
    
    return metin, dogru, siklar

def mat_rasyonel():
    """Rasyonel Sayılar - 6 farklı soru tipi"""
    tip = random.choice([1, 2, 3, 4, 5, 6])
    
    if tip == 1:
        p1 = random.randint(1, 12); pd1 = random.randint(2, 12)
        p2 = random.randint(1, 12); pd2 = random.randint(2, 12)
        if p1/pd1 > p2/pd2:
            dogru = ">"
        elif p1/pd1 < p2/pd2:
            dogru = "<"
        else:
            dogru = "="
        metin = f"📊 **Kesir Karşılaştırma**\n\n{p1}/{pd1} __ {p2}/{pd2} ifadesinde boşluğa hangi işaret gelmelidir?"
        siklar = [">", "<", "=", "≠"]
        random.shuffle(siklar)
        return metin, dogru, siklar
    
    elif tip == 2:
        p = random.randint(1, 12); pd = random.randint(2, 12)
        v = p/pd; dogru = f"{v:.2f}"
        metin = f"🔢 **Kesir - Ondalık Dönüşüm**\n\n{p}/{pd} rasyonel sayısının ondalık gösterimi (virgülden sonra 2 basamak) nedir?"
        yanlis = [f"{v+0.1:.2f}", f"{v-0.1:.2f}", f"{v+0.05:.2f}"]
        siklar = [dogru] + yanlis
        random.shuffle(siklar)
        return metin, dogru, siklar
    
    elif tip == 3:
        p = random.randint(1, 8); pd = random.randint(2, 8)
        metin = f"🍰 **Kesir Problemleri**\n\nBir pastanın {p}/{pd}'i yenmiştir. Geriye kalan pasta 6 kişiye eşit olarak paylaştırılıyor.\n\n**Her bir kişi pastanın kaçta kaçını alır?**"
        kalan = 1 - (p/pd); son = kalan/6
        pay = int(son*100); payda = 100
        for i in range(2, 20):
            if pay % i == 0 and payda % i == 0:
                pay //= i; payda //= i
        dogru = f"{pay}/{payda}" if payda != 1 else str(pay)
        yanlis = [f"{pay+1}/{payda}", f"{pay-1}/{payda}", f"{pay}/{payda+1}"]
        siklar = [dogru] + yanlis
        random.shuffle(siklar)
        return metin, dogru, siklar
    
    elif tip == 4:
        p = random.randint(1, 9); pd = random.randint(2, 9)
        carp = random.randint(2, 5)
        metin = f"📐 **Kesir Genişletme**\n\n{p}/{pd} kesrini {carp} ile genişlettiğimizde oluşan yeni kesrin pay ve paydasının **toplamı** kaçtır?"
        yeni_pay = p * carp; yeni_payda = pd * carp
        dogru = str(yeni_pay + yeni_payda)
        yanlis = [str(int(dogru)+random.randint(5,15)), str(int(dogru)-random.randint(5,15)), str(int(dogru)+random.randint(1,4))]
        siklar = [dogru] + yanlis
        random.shuffle(siklar)
        return metin, dogru, siklar
    
    else:
        p1 = random.randint(1, 10); pd1 = random.randint(2, 10)
        p2 = random.randint(1, 10); pd2 = random.randint(2, 10)
        metin = f"📏 **Kesirler Arası Uzaklık**\n\n{p1}/{pd1} ile {p2}/{pd2} kesirleri arasındaki farkın mutlak değeri nedir? (Kesir olarak sadeleştiriniz)"
        fark = abs(p1/pd1 - p2/pd2)
        pay = int(fark * 100); payda = 100
        for i in range(2, 20):
            if pay % i == 0 and payda % i == 0:
                pay //= i; payda //= i
        dogru = f"{pay}/{payda}" if payda != 1 else str(pay)
        yanlis = [f"{pay+1}/{payda}", f"{pay-1}/{payda}", f"{pay}/{payda+1}"]
        siklar = [dogru] + yanlis
        random.shuffle(siklar)
        return metin, dogru, siklar

def mat_rasyonel_islem():
    """Rasyonel Sayılarla İşlemler - 5 tip"""
    p1 = random.randint(1, 8); pd1 = random.randint(2, 8)
    p2 = random.randint(1, 8); pd2 = random.randint(2, 8)
    islem = random.choice(["+", "-", "x", "/"])
    
    if islem == "+":
        sp = p1*pd2 + p2*pd1; spd = pd1*pd2
    elif islem == "-":
        sp = p1*pd2 - p2*pd1; spd = pd1*pd2
    elif islem == "x":
        sp = p1*p2; spd = pd1*pd2
    else:
        sp = p1*pd2; spd = pd1*p2
    
    eb = math.gcd(sp, spd); sp //= eb; spd //= eb
    dogru = f"{sp}/{spd}" if spd != 1 else str(sp)
    metin = f"🧮 **Kesir İşlemleri**\n\n{p1}/{pd1} {islem} {p2}/{pd2} işleminin sonucu nedir? (Sadeleştirilmiş kesir olarak yazınız)"
    yanlis = [f"{sp+1}/{spd}", f"{sp-1}/{spd}", f"{sp}/{spd+1}"]
    siklar = [dogru] + yanlis
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_cebirsel():
    """Cebirsel İfadeler - 4 tip"""
    tip = random.choice([1, 2, 3, 4])
    
    if tip == 1:
        a = random.randint(1, 5); b = random.randint(-8, 8)
        c = random.randint(1, 5); d = random.randint(-8, 8)
        islem = random.choice(["+", "-"])
        if islem == "+":
            sonuc = f"{a+c}x + {b+d}"
        else:
            sonuc = f"{a-c}x + {b-d}"
        metin = f"📐 **Cebirsel Toplama/Çıkarma**\n\n**({a}x {b:+#d}) {islem} ({c}x {d:+#d})** işleminin en sade hali aşağıdakilerden hangisidir?"
        yanlis = [f"{a+c+1}x + {b+d}", f"{a+c}x + {b+d+1}", f"{a+c-1}x + {b+d}"]
        siklar = [sonuc] + yanlis
        random.shuffle(siklar)
        return metin, sonuc, siklar
    
    elif tip == 2:
        a = random.randint(2, 6); b = random.randint(1, 10); x_val = random.randint(1, 5)
        sonuc = a*x_val + b
        dogru = str(sonuc)
        metin = f"🔢 **Cebirsel İfade Değeri**\n\n{a}x + {b} cebirsel ifadesinin **x = {x_val}** için değeri kaçtır?"
        yanlis = [str(sonuc+random.randint(2,6)), str(sonuc-random.randint(2,6)), str(sonuc+random.randint(1,2))]
        siklar = [dogru] + yanlis
        random.shuffle(siklar)
        return metin, dogru, siklar
    
    else:
        a = random.randint(2, 5); b = random.randint(1, 8)
        dogru = f"{4*a}x + {4*b}"
        metin = f"📏 **Geometrik Cebir**\n\nBir kenar uzunluğu **({a}x+{b}) cm** olan karenin **çevresi** kaç cm'dir?"
        yanlis = [f"{4*a+1}x + {4*b}", f"{4*a}x + {4*b+1}", f"{4*a-1}x + {4*b}"]
        siklar = [dogru] + yanlis
        random.shuffle(siklar)
        return metin, dogru, siklar

def mat_denklem():
    """Eşitlik ve Denklem - 4 tip"""
    tip = random.choice([1, 2, 3, 4])
    
    if tip == 1:
        a = random.randint(2, 6); b = random.randint(2, 15)
        c = random.randint(2, 6); d = random.randint(2, 15)
        if a == c: a = c+1
        cozum = (d-b)/(a-c)
        dogru = str(int(cozum)) if cozum == int(cozum) else f"{cozum:.1f}"
        metin = f"⚖️ **Denklem Çözme**\n\n{a}x + {b} = {c}x + {d} denklemini sağlayan **x** değeri kaçtır?"
    
    elif tip == 2:
        a = random.randint(2, 7); b = random.randint(1, 10)
        c = random.randint(2, 7); d = random.randint(1, 8)
        # a(x - b) = cx + d
        cozum = (a*b + d) / (a - c) if a != c else random.randint(1, 10)
        dogru = str(int(cozum)) if cozum == int(cozum) else f"{cozum:.1f}"
        metin = f"🔓 **Parantezli Denklem**\n\n{a}(x - {b}) = {c}x + {d} denkleminin çözümü kaçtır?"
    
    elif tip == 3:
        a = random.randint(1, 5); b = random.randint(1, 10)
        metin = f"💭 **Sözel Problem**\n\nBir sayının {a} katının {b} fazlası, aynı sayının {a+1} katına eşittir.\n\n**Bu sayı kaçtır?**"
        dogru = str(b)
    
    else:
        a = random.randint(2, 6); b = random.randint(1, 12); c = random.randint(2, 5)
        # (x + a)/b = c
        cozum = c*b - a
        dogru = str(cozum)
        metin = f"📖 **Kesirli Denklem**\n\n(x + {a}) / {b} = {c} denkleminin çözümü kaçtır?"
    
    yanlisler = set()
    while len(yanlisler) < 3:
        sapma = random.choice([-3, -2, 2, 3, -5, 5])
        y = int(dogru) + sapma if dogru.isdigit() else float(dogru) + sapma
        yanlisler.add(str(int(y)) if y == int(y) else f"{y:.1f}")
    siklar = [dogru] + list(yanlisler)
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_oran():
    """Oran ve Orantı - 4 tip"""
    tip = random.choice([1, 2, 3, 4])
    
    if tip == 1:
        a = random.randint(2, 10); b = random.randint(2, 10); k = random.randint(2, 6)
        x = b * k
        dogru = str(x)
        metin = f"🔄 **Doğru Orantı**\n\n{a}/{b} = {a*k}/x orantısında **x** kaçtır?"
    
    elif tip == 2:
        a = random.randint(2, 8); b = random.randint(2, 8)
        c = random.randint(2, 8); d = random.randint(2, 8)
        # a/b = a/b, b/c = b/c ise a/c = ?
        dogru = f"{a}/{c}"
        metin = f"📊 **Zincir Orantı**\n\na/b = {a}/{b} ve b/c = {b}/{c} ise **a/c** oranı kaçtır?"
        yanlis = [f"{a+1}/{c}", f"{a}/{c+1}", f"{a-1}/{c}"]
        siklar = [dogru] + yanlis
        random.shuffle(siklar)
        return metin, dogru, siklar
    
    else:
        k = random.randint(3, 8); e = random.randint(3, 8); toplam = random.randint(40, 80)
        kiz = int(k / (k+e) * toplam)
        dogru = str(kiz)
        metin = f"👥 **Sınıf Problemi**\n\nBir sınıfta kızların erkeklere oranı {k}/{e}'tir. Sınıf mevcudu **{toplam}** olduğuna göre **kız sayısı** kaçtır?"
    
    yanlisler = set()
    while len(yanlisler) < 3:
        sapma = random.choice([-5, -3, 3, 5, -8, 8])
        y = int(dogru) + sapma
        if y != int(dogru) and y > 0:
            yanlisler.add(str(y))
    siklar = [dogru] + list(yanlisler)
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_yuzde():
    """Yüzdeler - 3 tip"""
    tip = random.choice([1, 2, 3])
    
    if tip == 1:
        sayi = random.randint(100, 500); yuzde = random.choice([10, 15, 20, 25, 30, 40, 50])
        sonuc = int(sayi * yuzde / 100)
        dogru = str(sonuc)
        metin = f"🛍️ **İndirim Hesaplama**\n\n**{sayi} TL**'lik bir ürüne **%{yuzde}** indirim yapılıyor.\n\n**İndirim miktarı kaç TL'dir?**"
    
    elif tip == 2:
        sayi = random.randint(100, 500); yuzde = random.choice([10, 20, 25, 30, 50, 60, 75])
        sonuc = int(sayi * (100 - yuzde) / 100)
        dogru = str(sonuc)
        metin = f"🏷️ **İndirimli Fiyat**\n\n**{sayi} TL**'lik bir ürüne **%{yuzde}** indirim uygulanıyor.\n\n**İndirimli fiyat kaç TL'dir?**"
    
    else:
        sayi = random.randint(100, 500); yuzde = random.choice([10, 15, 20, 25, 30])
        artis = random.choice(["artırılıyor", "azaltılıyor"])
        if artis == "artırılıyor":
            sonuc = int(sayi * (100 + yuzde) / 100)
            metin = f"📈 **Yüzde Artış**\n\n**{sayi} TL**'lik bir ürünün fiyatı **%{yuzde} artırılıyor**.\n\n**Yeni fiyat kaç TL'dir?**"
        else:
            sonuc = int(sayi * (100 - yuzde) / 100)
            metin = f"📉 **Yüzde Azalış**\n\n**{sayi} TL**'lik bir ürünün fiyatı **%{yuzde} azaltılıyor**.\n\n**Yeni fiyat kaç TL'dir?**"
        dogru = str(sonuc)
    
    yanlis = [str(int(dogru)+random.randint(3,8)), str(int(dogru)-random.randint(3,8)), str(int(dogru)+random.randint(1,2))]
    siklar = [dogru] + yanlis
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_aci():
    """Doğrular ve Açılar"""
    aci = random.randint(30, 150)
    tip = random.choice(["tümler", "bütünler", "ters"])
    
    if tip == "tümler":
        dogru = str(90 - aci)
        metin = f"📐 **Tümler Açı**\n\n{aci}°'lik bir açının **tümleri** kaç derecedir?"
    elif tip == "bütünler":
        dogru = str(180 - aci)
        metin = f"📏 **Bütünler Açı**\n\n{aci}°'lik bir açının **bütünleri** kaç derecedir?"
    else:
        # Ters açılar eşittir
        dogru = str(aci)
        metin = f"🔄 **Ters Açı**\n\nBirbirine ters açı durumunda olan iki açıdan biri {aci}° ise **diğer açı** kaç derecedir?"
    
    yanlis = [str(int(dogru)+random.randint(5,15)), str(int(dogru)-random.randint(5,15)), str(int(dogru)+random.randint(1,4))]
    siklar = [dogru] + yanlis
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_cokgen():
    """Çokgenler"""
    kenar = random.randint(3, 8)
    tip = random.choice(["iç", "dış", "köşegen"])
    
    if tip == "iç":
        dogru = str((kenar-2)*180)
        metin = f"🟢 **Çokgen İç Açıları**\n\n**{kenar} kenarlı** bir çokgenin **iç açıları toplamı** kaç derecedir?"
    elif tip == "dış":
        dogru = str(int(360/kenar))
        metin = f"🔺 **Dış Açı**\n\nDüzgün **{kenar} kenarlı** bir çokgenin **bir dış açısı** kaç derecedir?"
    else:
        # Köşegen sayısı
        dogru = str(kenar * (kenar-3) // 2)
        metin = f"📐 **Köşegen Sayısı**\n\n**{kenar} kenarlı** bir çokgenin **toplam köşegen sayısı** kaçtır?"
    
    yanlis = [str(int(dogru)+random.randint(10,30)), str(int(dogru)-random.randint(10,30)), str(int(dogru)+random.randint(5,9))]
    siklar = [dogru] + yanlis
    random.shuffle(siklar)
    return metin, dogru, siklar

def mat_cember():
    """Çember ve Daire"""
    r = random.randint(3, 15)
    tip = random.choice(["çevre", "alan", "çap"])
    pi = 3
    
    if tip == "çevre":
        dogru = str(2*pi*r)
        metin = f"⭕ **Çemberin Çevresi**\n\nYarıçapı **{r} cm** olan bir çemberin **çevresi** kaç cm'dir? (π = 3)"
    elif tip == "alan":
        dogru = str(pi*r*r)
        metin = f"🔵 **Dairenin Alanı**\n\nYarıçapı **{r} cm** olan bir dairenin **alanı** kaç cm²'dir? (π = 3)"
    else:
        dogru = str(2*r)
        metin = f"📏 **Çap Hesaplama**\n\nYarıçapı **{r} cm** olan bir çemberin **çapı** kaç cm'dir?"
    
    yanlis = [str(int(dogru)+random.randint(5,15)), str(int(dogru)-random.randint(5,15)), str(int(dogru)+random.randint(1,4))]
    siklar = [dogru] + yanlis
    random.shuffle(siklar)
