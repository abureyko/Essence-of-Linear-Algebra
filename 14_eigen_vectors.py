import numpy as np
import matplotlib.pyplot as plt
from plot_helpers import save_lesson_figure

# Найди собственные векторы этой матрицы вручную
A = np.array([[4, 1],
              [2, 3]])

#(4-x)*(3-x)-2=0
#x1 = 2; x2 = 5

# Проверь: являются ли эти векторы собственными?
v1 = np.array([1, 1])
v2 = np.array([1, -2])
#v1*x1 = (2;2) v1*x2 = (5;5)
#v2*x1 = (2;-4) v2*x2 = (5;-10)

print("A·v1 =", A @ v1)  # = λ·v1?
print("A·v2 =", A @ v2)  # = λ·v2?

#A*v1 = v1*x2 = (5;5) -> v1 собственный вектор 
#A*v2 = v2*x1 = (2;-4) -> v2 собственный вектор 


def visualize_eigen_vectors(matrix, eigenvectors):
    fig, ax = plt.subplots(figsize=(8, 8))
    colors = ["tab:blue", "tab:red"]

    for index, vector in enumerate(eigenvectors):
        transformed = matrix @ vector
        color = colors[index]

        ax.quiver(0, 0, vector[0], vector[1], angles="xy", scale_units="xy", scale=1,
                  color=color, width=0.012, alpha=0.45, label=f"v{index + 1} = {vector}")
        ax.quiver(0, 0, transformed[0], transformed[1], angles="xy", scale_units="xy", scale=1,
                  color=color, width=0.018, label=f"A·v{index + 1} = {transformed}")
        ax.plot([vector[0], transformed[0]], [vector[1], transformed[1]],
                color=color, linestyle="--", alpha=0.5)

    ax.set_xlim(-3, 6)
    ax.set_ylim(-5, 6)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_title("Собственные векторы: направление сохраняется")
    ax.legend(loc="upper left")

    save_lesson_figure(fig, __file__, "14_eigen_vectors.png")
    plt.show()


visualize_eigen_vectors(A, [v1, v2])
