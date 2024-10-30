import numpy as np

# Constants
E0 = 500000  # False Easting (standard for UTM)
N0 = 0       # False Northing for Northern Hemisphere, 10000000 for Southern Hemisphere
k0 = 0.9996  # Scale factor for UTM
a = 6378137  # Major radius (WGS84)
n = 1 / 298.257223563  # Flattening parameter (WGS84 for Earth)

# Input variables (to be provided based on location and target point)
eta_prime = ...  # η'
xi_prime = ...   # ξ'
phi = ...        # Latitude in radians
lambda_ = ...    # Longitude in radians
lambda0 = ...    # Central meridian of the UTM zone in radians

# Constants for the series summation (specific to the projection)
alpha = [0.000837732164, 0.000036168889, 0.000002602048, 0.000000040215]

# Calculating E (Easting)
E = E0 + k0 * a * (eta_prime + sum(alpha[j-1] * np.cos(2 * j * xi_prime) * np.sinh(2 * j * eta_prime) for j in range(1, 4+1)))

# Calculating N (Northing)
N = N0 + k0 * a * (xi_prime + sum(alpha[j-1] * np.sin(2 * j * xi_prime) * np.cosh(2 * j * eta_prime) for j in range(1, 4+1)))

# Calculating k (Scale Factor)
sigma = ...  # parameter related to the ellipsoid, to be defined for UTM conversion
tau = ...    # another parameter related to the ellipsoid, to be defined for UTM conversion
t = np.tan(phi)
k = (k0 * a / a) * np.sqrt(1 + ((1 - n) / (1 + n) * np.tan(phi))**2) * (sigma**2 + tau**2) / (t**2 + np.cos(lambda_ - lambda0)**2)

# Calculating gamma (Grid Convergence)
gamma = np.arctan((tau * np.sqrt(1 + t**2) + sigma * t * np.tan(lambda_ - lambda0)) / (sigma * np.sqrt(1 + t**2) - tau * t * np.tan(lambda_ - lambda0)))

# Display results
print("Easting (E):", E)
print("Northing (N):", N)
print("Scale Factor (k):", k)
print("Grid Convergence (γ):", gamma)
