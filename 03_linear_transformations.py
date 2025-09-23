import numpy as np
from matplotlib import pyplot as plt

A_ROTATE = np.array([[0,-1], [1, 0]]) # Матрица поворота на 90 градусов против часовой
A_SHEAR = np.array([[1, 0.5], [0,1]]) # Сдвиг 
A_SCALE =  np.array([[2, 0], [0,0.5]]) # Растяжение

# Преобразование базисных векторов i и j
def demonstrate_linear_transformations(matrix: np.ndarray, title: str = "") -> None:
    fig, ax = plt.subplots(figsize=(6,6))

    i_hat = np.array([1,0])
    j_hat = np.array([0,1])

    i_new = matrix @ i_hat
    j_new = matrix @ j_hat

    ax.quiver(0, 0, i_hat[0], i_hat[1], 
              angles='xy', scale_units='xy', scale=1,
              color='red', width=0.015, alpha=0.5,
              label='Исходный î')
    
    ax.quiver(0, 0, j_hat[0], j_hat[1],
              angles='xy', scale_units='xy', scale=1,
              color='blue', width=0.015, alpha=0.5,
              label='Исходный ĵ')
    
    ax.quiver(0, 0, i_new[0], i_new[1],
              angles='xy', scale_units='xy', scale=1,
              color='red', width=0.015, alpha=1,
              label='Новый î')
    
    ax.quiver(0, 0, j_new[0], j_new[1],
              angles='xy', scale_units='xy', scale=1,
              color='blue', width=0.015, alpha=1,
              label='Новый ĵ')
    # Рисуем преобразованную сетку (для лучшего понимания)
    # Создаем небольшую сетку точек вокруг начала координат
    x = np.linspace(-3, 3, 5)
    y = np.linspace(-3, 3, 5)
    X, Y = np.meshgrid(x, y)
    points = np.vstack([X.ravel(), Y.ravel()])
    
    # Применяем преобразование ко всем точкам
    transformed_points = matrix @ points
    
    # Рисуем исходную сетку (серые точки)
    ax.scatter(points[0, :], points[1, :], 
               color='gray', alpha=0.3, s=20, marker='o')
    
    # Рисуем преобразованную сетку (цветные точки)
    colors = ['purple'] * len(transformed_points[0])
    ax.scatter(transformed_points[0, :], transformed_points[1, :],
               c=colors, alpha=0.6, s=40, marker='s',
               label='Преобразованная сетка')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Линейное преобразование: {title}\n'
                 f'Матрица: {matrix[0]}\n{matrix[1]}')
    ax.set_aspect('equal')
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    matrices = {
        "Поворот на 90°": A_ROTATE,
        "Сдвиг": A_SHEAR, 
        "Растяжение/Сжатие": A_SCALE
    }
    
    for name, matrix in matrices.items():
        demonstrate_linear_transformations(matrix, name)

