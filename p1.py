import numpy as np
import matplotlib.pyplot as plt

# Semilla para reproducibilidad
np.random.seed(4)

# Simulación de datos
x = np.random.normal(0, 1, 100)

# Histograma
fig, ax = plt.subplots()
ax.hist(x)
plt.title("*****")
plt.show()


print("Será")