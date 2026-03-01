import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# ÇALIŞMA ALANI (WORKSPACE) PARAMETRELERİ
# ==========================================
N_NOKTA = 50000  # Üretilecek rastgele nokta sayısı
L1, L2, L3 = 0.5, 0.4, 0.3  # Kol uzunlukları (metre)

# 1. Mafsal Limitlerinin Belirlenmesi (Ödev Adım 5.2)
# q1: Taban motoru, tam tur dönebildiğini varsayıyoruz (-180° ile +180°)
q1 = np.random.uniform(-np.pi, np.pi, N_NOKTA)

# q2 ve q3: Dirsek ve Bilek motorları, çarpışma kısıtından dolayı +- 90° ile sınırlı
q2 = np.random.uniform(-np.pi/2, np.pi/2, N_NOKTA)
q3 = np.random.uniform(-np.pi/2, np.pi/2, N_NOKTA)

# 2. İleri Kinematik (FK) Denklemleri ile Pozisyon Hesaplama
X = L1 * np.cos(q1) + L2 * np.cos(q1+q2) + L3 * np.cos(q1+q2+q3)
Y = L1 * np.sin(q1) + L2 * np.sin(q1+q2) + L3 * np.sin(q1+q2+q3)

# 3. Görselleştirme (Matplotlib - Nokta Bulutu)
plt.figure(figsize=(8, 8))

# Noktaları çiz (s=nokta boyutu, alpha=saydamlık)
plt.scatter(X, Y, s=0.5, c='#1f77b4', alpha=0.3, label='Ulaşılabilir Alan')
plt.plot(0, 0, 'ko', markersize=8, label='Orijin (Robot Tabanı)')

# Maksimum teorik sınır çemberi (L1+L2+L3)
max_yari_cap = L1 + L2 + L3
cember = plt.Circle((0, 0), max_yari_cap, color='r', fill=False, linestyle='--', linewidth=2, label=f'Teorik Sınır (R={max_yari_cap}m)')
plt.gca().add_patch(cember)

# Grafik Ayarları
plt.title('3-DoF RRR Planar Kol - Çalışma Alanı (Workspace) Analizi', fontsize=14, fontweight='bold')
plt.xlabel('x Ekseni (m)', fontsize=12)
plt.ylabel('y Ekseni (m)', fontsize=12)
plt.axis('equal') # X ve Y eksen oranlarını eşitle
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper right')

# Ekranda göster
plt.show()