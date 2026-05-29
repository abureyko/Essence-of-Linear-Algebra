from pathlib import Path
import sys

import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).resolve().parents[1]))
from plot_helpers import save_lesson_figure


def vector_add(v, w):
    """Складывает два вектора покомпонентно"""
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def scalar_multiply(c, v):
    """Умножает вектор на скаляр"""
    return [c * v_i for v_i in v]


def linear_combination(vectors, coefficients):
    """
    Вычисляет линейную комбинацию векторов.
    
    Parameters:
    vectors: list of lists - список векторов (например, [[1, 2], [3, 4]])
    coefficients: list - список коэффициентов (например, [2, -1])
    
    Returns:
    list - результирующий вектор
    """
    # Умножаем каждый вектор на свой коэффициент
    scaled_vectors = [scalar_multiply(coef, vec) for coef, vec in zip(coefficients, vectors)]
    
    # Складываем все полученные векторы
    result = scaled_vectors[0]
    for vec in scaled_vectors[1:]:
        result = vector_add(result, vec)
    return result


def visualize_linear_combination(vectors, coefficients):
    """Показывает, как из масштабированных векторов собирается результат."""
    result = linear_combination(vectors, coefficients)
    scaled_vectors = [scalar_multiply(coef, vec) for coef, vec in zip(coefficients, vectors)]

    fig, ax = plt.subplots(figsize=(7, 7))
    colors = ["tab:blue", "tab:red", "tab:green", "tab:purple"]
    current = [0, 0]

    for index, vec in enumerate(scaled_vectors):
        ax.arrow(
            current[0],
            current[1],
            vec[0],
            vec[1],
            head_width=0.15,
            head_length=0.18,
            length_includes_head=True,
            color=colors[index % len(colors)],
            linewidth=2,
            label=f"{coefficients[index]} * v{index + 1} = {vec}",
        )
        current = vector_add(current, vec)

    ax.arrow(
        0,
        0,
        result[0],
        result[1],
        head_width=0.18,
        head_length=0.22,
        length_includes_head=True,
        color="black",
        linewidth=3,
        alpha=0.75,
        label=f"Результат = {result}",
    )

    ax.set_xlim(-1, max(5, result[0] + 1))
    ax.set_ylim(-1, max(5, result[1] + 1))
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_title("Линейная комбинация как маршрут по векторам")
    ax.legend(loc="upper left")

    save_lesson_figure(fig, __file__, "02_linear_combinations.png")
    plt.show()

# Пример использования
if __name__ == "__main__":
    # Базисные векторы
    i_hat = [1, 0]
    j_hat = [0, 1]
    
    # Коэффициенты
    coefs = [3, 2]
    
    # Линейная комбинация: 3*i_hat + 2*j_hat
    result = linear_combination([i_hat, j_hat], coefs)
    print(f"{coefs[0]}*i + {coefs[1]}*j = {result}")
    # Output: 3*i + 2*j = [3, 2]
    visualize_linear_combination([i_hat, j_hat], coefs)
