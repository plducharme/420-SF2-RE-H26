import matplotlib.pyplot as plt
import math


def n_log_n(n):
    return n * math.log(n)


def carre_n(n):
    return n**2


coords_x = [x for x in range(1, 101)]
coords_y = [n_log_n(y) for y in coords_x]
coords_y_carre = [carre_n(y) for y in coords_x]

plt.title("Courbes de y en fonction de x")
plt.xlabel("x")
plt.ylabel("y")
# Courbe y = x log x
plt.plot(coords_x, coords_y, linestyle="--", color="b")
# Courbe y = x ** 2
plt.plot(coords_x, coords_y_carre, linestyle="-", color="g")

plt.legend(["y = x log(x)", "y = x ** 2"])
plt.show()

