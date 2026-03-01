import numpy as np


def rrr_planar_ik(x, y, z, phi_deg, l1, l2, l3):

    print(f" Hedef Nokta: ({x}, {y}, {z}), Yönelim: {phi_deg}° ")

    if not np.isclose(z, 0.0):
        print("Seçilen RRR Planar kol yalnızca Z=0 düzleminde çalışır. Bu hedefe ulaşılamaz.\n")
        return None

    phi = np.radians(phi_deg)

    xw = x - l3 * np.cos(phi)
    yw = y - l3 * np.sin(phi)

    D = (xw ** 2 + yw ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)

    if abs(D) > 1.0:
        print("HATA: Hedef nokta robotun çalışma alanı (workspace) dışındadır.\n")
        return None

    # Singülerlik (Tekillik) Kontrolü (det(J) = 0)
    if np.isclose(D, 1.0) or np.isclose(D, -1.0):
        print("UYARI: Robot sınır singülerliği (kilitlenme) pozisyonundadır!")

    cozumler = []
    q2_secenekleri = [np.arccos(D), -np.arccos(D)]

    durum_isimleri = ["Dirsek Aşağı (Elbow Down)", "Dirsek Yukarı (Elbow Up)"]


    for i, q2 in enumerate(q2_secenekleri):
        q1 = np.arctan2(yw, xw) - np.arctan2(l2 * np.sin(q2), l1 + l2 * np.cos(q2))

        q3 = phi - q1 - q2

        q_deg = np.degrees([q1, q2, q3])
        cozumler.append(q_deg)

        print(f"{durum_isimleri[i]}: q1 = {q_deg[0]:.2f}°, q2 = {q_deg[1]:.2f}°, q3 = {q_deg[2]:.2f}°")

    print("\n")
    return cozumler
try:
    # l1,l2,l3
    print("Ters Kinematik için gerekli değerleri giriniz.")
    l1 = float(input("Robot 1. kol uzunluğunu giriniz:"))
    l2 = float(input("Robot 2. kol uzunluğunu giriniz:"))
    l3 = float(input("Robot 3. kol uzunluğunu giriniz:"))
    x = float(input("Lütfen  x değerini giriniz (metre): "))
    y = float(input("Lütfen  y değerini giriniz (metre): "))
    z = float(input("Lütfen  x değerini giriniz (metre): "))
    phi_deg = float(input("Lütfen Uç Efektör Yönelimini giriniz (derece): "))

    hedef = rrr_planar_ik(x, y, z, phi_deg,l1, l2, l3)
except ValueError:
    print("Hata: Lütfen sayısal bir değer giriniz!")

