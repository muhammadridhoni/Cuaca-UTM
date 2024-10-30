import numpy as np

# Konstanta
E0 = 500000       # False Easting (standar untuk UTM)
N0 = 0            # False Northing (0 untuk belahan utara, 10000000 untuk belahan selatan)
k0 = 0.9996       # Skala faktor untuk UTM
a = 6378137       # Jari-jari utama (WGS84)
n = 1 / 298.257223563  # Parameter flattening (WGS84 untuk bumi)

# Input variabel (masukkan berdasarkan lokasi dan titik target)
eta_prime = 0.5   # Nilai η' (contoh)
xi_prime = 1.0    # Nilai ξ' (contoh)
phi = np.radians(10)       # Latitude dalam radian (contoh)
lambda_ = np.radians(110)  # Longitude dalam radian (contoh)
lambda0 = np.radians(107)  # Meridian tengah zona UTM dalam radian (contoh)

# Koefisien untuk deret alpha (khusus untuk proyeksi ini)
alpha = [0.000837732164, 0.000036168889, 0.000002602048, 0.000000040215]

# Menghitung E (Easting)
E = E0 + k0 * a * (eta_prime + sum(alpha[j-1] * np.cos(2 * j * xi_prime) * np.sinh(2 * j * eta_prime) for j in range(1, 4+1)))

# Menghitung N (Northing)
N = N0 + k0 * a * (xi_prime + sum(alpha[j-1] * np.sin(2 * j * xi_prime) * np.cosh(2 * j * eta_prime) for j in range(1, 4+1)))

# Menghitung k (Faktor Skala)
sigma = 1.0  # Parameter σ (contoh)
tau = 1.0    # Parameter τ (contoh)
t = np.tan(phi)
k = (k0 * a / a) * np.sqrt(1 + ((1 - n) / (1 + n) * np.tan(phi))**2) * (sigma**2 + tau**2) / (t**2 + np.cos(lambda_ - lambda0)**2)

# Menghitung gamma (Konvergensi Grid)
gamma = np.arctan((tau * np.sqrt(1 + t**2) + sigma * t * np.tan(lambda_ - lambda0)) / (sigma * np.sqrt(1 + t**2) - tau * t * np.tan(lambda_ - lambda0)))

# Tampilkan hasil
print("Easting (E):", E)
print("Northing (N):", N)
print("Faktor Skala (k):", k)
print("Konvergensi Grid (γ):", gamma)



