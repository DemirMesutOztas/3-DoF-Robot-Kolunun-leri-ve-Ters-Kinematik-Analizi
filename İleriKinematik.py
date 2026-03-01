import numpy as np


def homojen_donusum(theta_derece, a, d=0, alpha=0):
    theta_rad = np.radians(theta_derece)

    c = np.cos(theta_rad)
    s = np.sin(theta_rad)

    return np.array([
        [c, -s * np.cos(alpha), s * np.sin(alpha), a * c],
        [s, c * np.cos(alpha), -c * np.sin(alpha), a * s],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

print("--- 3-DOF Robot Kinematik Hesaplayıcı ---")
try:
    # l1,l2,l3
    l1 = float(input("Robot 1. kol uzunluğunu giriniz:"))
    l2 = float(input("Robot 2. kol uzunluğunu giriniz:"))
    l3 = float(input("Robot 3. kol uzunluğunu giriniz:"))
    # theta1, theta2, theta3
    d1 = float(input("1. Mafsal açısını derece cinsinden giriniz:"))
    d2 = float(input("2. Mafsal açısını derece cinsinden giriniz:"))
    d3 = float(input("3. Mafsal açısını derece cinsinden giriniz:"))

    A1 = homojen_donusum(d1, l1)
    A2 = homojen_donusum(d2, l2)
    A3 = homojen_donusum(d3, l3)

    T03 = A1 @ A2 @ A3

    px, py, pz = T03[0,3], T03[1,3], T03[2,3]
    toplam_aci = d1 + d2 + d3

    print(f"Robotun boyutları: L1={l1}, L2={l2}, L3={l3}")
    print(f"Girilen açılar : {d1}°, {d2}°, {d3}°")
    print(f"Uç nokta konumu -> X: {px:.4f} m, Y: {py:.4f} m, Z: {pz:.4f} m")
    print(f"Uç nokta yönelimi: {toplam_aci}°")

except ValueError:
    print("Hata: Lütfen sayısal bir değer giriniz!")