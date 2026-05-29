import numpy as np
import matplotlib.pyplot as plt
from plot_helpers import save_lesson_figure

def change_basis(vectors, old_basis, new_basis):
    """
    Преобразует векторы из старого базиса в новый базис
    
    Parameters:
    vectors: матрица векторов (каждый столбец - вектор в старом базисе)  
    old_basis: матрица старого базиса (столбцы - базисные векторы)
    new_basis: матрица нового базиса (столбцы - базисные векторы)
    
    Returns:
    vectors_in_new_basis: векторы в новом базисе
    """
    transition = np.linalg.inv(new_basis) @ old_basis
    return transition @ vectors.T


def visualize_change_of_basis(vectors, old_basis, new_basis):
    """Показывает старый и новый базисы вместе с одними и теми же векторами."""
    vectors_in_new_basis = change_basis(vectors, old_basis, new_basis)

    fig, ax = plt.subplots(figsize=(8, 8))

    for basis, color, label in [
        (old_basis, "tab:gray", "старый базис"),
        (new_basis, "tab:orange", "новый базис"),
    ]:
        ax.quiver(0, 0, basis[0, 0], basis[1, 0], angles="xy", scale_units="xy", scale=1,
                  color=color, width=0.012, alpha=0.8, label=f"b1: {label}")
        ax.quiver(0, 0, basis[0, 1], basis[1, 1], angles="xy", scale_units="xy", scale=1,
                  color=color, width=0.008, alpha=0.55, label=f"b2: {label}")

    for index, vector in enumerate(vectors):
        ax.quiver(0, 0, vector[0], vector[1], angles="xy", scale_units="xy", scale=1,
                  width=0.015, label=f"v{index + 1} в старых координатах: {vector}")
        ax.text(vector[0] + 0.1, vector[1] + 0.1,
                f"new: {vectors_in_new_basis[:, index].round(2)}", fontsize=10)

    ax.set_xlim(-1, 6)
    ax.set_ylim(-1, 6)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_title("Смена базиса: объект тот же, координаты другие")
    ax.legend(loc="upper left")

    save_lesson_figure(fig, __file__, "13_change_of_basis.png")
    plt.show()

# Старый базис (стандартный)
old_basis = np.eye(2)  # [[1,0],[0,1]]

# Новый базис (базис Дженнифер)
new_basis = np.array([[2, 1],   # b1
                      [1, 2]])  # b2

# Векторы в старом базисе
vectors = np.array([[5, 3],    # v1
                    [1, 4]])   # v2 (каждый столбец - вектор)

# Преобразование
result = change_basis(vectors, old_basis, new_basis)
print("Векторы в новом базисе:")
print(result)

visualize_change_of_basis(vectors, old_basis, new_basis)
