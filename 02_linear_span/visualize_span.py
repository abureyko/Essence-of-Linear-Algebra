from linear_combinations import linear_combination
import numpy as np
import matplotlib.pyplot as plt

def visualize_span(vec1, vec2, num_points=100):
    # 1. Генерируем случайные коэффициенты
    coefficents = np.random.uniform(-2,2,size=(num_points, 2))
    
    # 2. Для каждой пары коэффициентов вычисляем линейную комбинацию
    points = []
    for coef1, coef2 in coefficents:
        point = linear_combination([vec1, vec2], [coef1, coef2])
        points.append(point)

    # 3. Визуализация 
    fig, ax = plt.subplots(figsize=(8,8))

    # Рисуем сгенерированные точки
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    ax.scatter(x_vals, y_vals, alpha=0.6, color='purple', label='Линейная оболочка')

    # Рисуем исходные векторы
    ax.arrow(0, 0, vec1[0], vec1[1], head_width=0.15, head_length=0.15, 
             fc='red', ec='red', linewidth=2, label=f'Вектор 1: {vec1}')
    ax.arrow(0, 0, vec2[0], vec2[1], head_width=0.15, head_length=0.15,
             fc='blue', ec='blue', linewidth=2, label=f'Вектор 2: {vec2}')
    
    # Настройка графика 
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Линейная оболочка векторов {vec1} и {vec2}')
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.5)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.5)    
    ax.legend()
    plt.show()

if __name__ == '__main__':
    print("Пример 1: Два непараллельных вектора (покрывают всю плоскость)")
    visualize_span([2, 1], [1, 3])
    print("Пример 2: Два параллельных вектора (покрывают только линию)")
    visualize_span([1, 2], [2, 4])
    print("Пример 3: Базисные векторы")
    visualize_span([1, 0], [0, 1])