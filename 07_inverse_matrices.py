import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def visualize_matrix_properties(A, title=""):
    """Визуализация свойств матрицы: ранг, ядро, пространство столбцов"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    ax1, ax2, ax3, ax4 = axes.ravel()
    
    # 1. Исходное пространство и преобразование
    plot_transformation(ax1, A, "Исходное пространство → Преобразование")
    
    # 2. Пространство столбцов (Column Space)
    plot_column_space(ax2, A, "Пространство столбцов")
    
    # 3. Ядро (Null Space) 
    plot_null_space(ax3, A, "Ядро матрицы")
    
    # 4. Обратимость и определитель
    plot_invertibility(ax4, A, "Обратимость")
    
    plt.suptitle(f"{title}\nМатрица: {A[0]}, {A[1]} | Ранг: {np.linalg.matrix_rank(A)} | det: {np.linalg.det(A):.2f}")
    plt.tight_layout()
    plt.show()

def plot_transformation(ax, A, title):
    """Визуализация преобразования единичного квадрата"""
    # Единичные векторы i и j
    i = np.array([1, 0])
    j = np.array([0, 1])
    
    # Преобразованные векторы
    i_transformed = A @ i
    j_transformed = A @ j
    
    # Единичный квадрат
    square = np.array([[0, 1, 1, 0], [0, 0, 1, 1]])
    square_transformed = A @ square
    
    # Исходные векторы
    ax.quiver(0, 0, i[0], i[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.02, label='i')
    ax.quiver(0, 0, j[0], j[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.02, label='j')
    
    # Преобразованные векторы
    ax.quiver(0, 0, i_transformed[0], i_transformed[1], angles='xy', scale_units='xy', scale=1, color='red', alpha=0.5, width=0.015)
    ax.quiver(0, 0, j_transformed[0], j_transformed[1], angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.5, width=0.015)
    
    # Квадраты
    ax.plot(square[0], square[1], 'k--', alpha=0.5, label='Исходный')
    ax.plot(square_transformed[0], square_transformed[1], 'g-', linewidth=2, label='Преобразованный')
    
    ax.set_title(title)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_aspect('equal')

def plot_column_space(ax, A, title):
    """Визуализация пространства столбцов"""
    # Столбцы матрицы
    col1 = A[:, 0]
    col2 = A[:, 1]
    
    # Ранг матрицы
    rank = np.linalg.matrix_rank(A)
    
    ax.quiver(0, 0, col1[0], col1[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.02, label='Столбец 1')
    ax.quiver(0, 0, col2[0], col2[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.02, label='Столбец 2')
    
    # Пространство столбцов - все возможные комбинации
    if rank == 2:
        # Заполняем параллелограмм
        parallelogram = np.array([[0, 0], col1, col1 + col2, col2])
        ax.add_patch(Polygon(parallelogram, alpha=0.3, color='green', label='Пространство столбцов'))
    elif rank == 1:
        # Линия
        t = np.linspace(-2, 2, 100)
        line_x = t * col1[0] if np.linalg.norm(col1) > 1e-10 else t * col2[0]
        line_y = t * col1[1] if np.linalg.norm(col1) > 1e-10 else t * col2[1]
        ax.plot(line_x, line_y, 'g-', linewidth=3, alpha=0.5, label='Пространство столбцов')
    
    ax.set_title(f"{title} (ранг: {rank})")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_aspect('equal')

def plot_null_space(ax, A, title):
    """Визуализация ядра матрицы"""
    try:
        # Находим ядро (решаем A·v = 0)
        U, s, Vt = np.linalg.svd(A)
        null_space = Vt[-1:]  # Последняя строка Vt
        
        if np.allclose(null_space @ A.T, 0):
            v = null_space[0]
            # Масштабируем для наглядности
            v = v / np.linalg.norm(v) * 2
            
            ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, 
                     color='purple', width=0.03, label='Вектор ядра')
            ax.quiver(0, 0, -v[0], -v[1], angles='xy', scale_units='xy', scale=1, 
                     color='purple', width=0.03)
            
            # Линия ядра
            t = np.linspace(-2, 2, 100)
            ax.plot(t * v[0], t * v[1], 'purple', linestyle='--', alpha=0.7, label='Ядро матрицы')
            
            ax.set_title(f"{title} (размерность: 1)")
        else:
            ax.set_title(f"{title} (тривиальное)")
            
    except:
        ax.set_title(f"{title} (вычисление не удалось)")
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_aspect('equal')

def plot_invertibility(ax, A, title):
    """Визуализация обратимости"""
    det = np.linalg.det(A)
    
    # Тестовая точка
    point = np.array([1, 0.5])
    
    # Прямое преобразование
    transformed_point = A @ point
    
    # Попытка обратного преобразования
    try:
        A_inv = np.linalg.inv(A)
        recovered_point = A_inv @ transformed_point
        invertible = True
    except:
        invertible = False
    
    # Исходная и преобразованная точки
    ax.scatter(point[0], point[1], color='red', s=100, label='Исходная точка')
    ax.scatter(transformed_point[0], transformed_point[1], color='blue', s=100, label='После A')
    
    if invertible:
        ax.scatter(recovered_point[0], recovered_point[1], color='green', s=100, marker='s', label='После A⁻¹')
        ax.plot([point[0], transformed_point[0]], [point[1], transformed_point[1]], 'red', alpha=0.5)
        ax.plot([transformed_point[0], recovered_point[0]], [transformed_point[1], recovered_point[1]], 'green', alpha=0.5)
        status = "ОБРАТИМА"
    else:
        status = "НЕОБРАТИМА"
    
    ax.set_title(f"{title}: {status}\ndet = {det:.2f}")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_aspect('equal')

# Примеры матриц для исследования
matrices = {
    "Полный ранг (обратимая)": np.array([[1, 0.5], [0.5, 1]]),
    "Вырожденная (ранг 1)": np.array([[1, 2], [2, 4]]),
    "Поворот (det=1)": np.array([[0.8, -0.6], [0.6, 0.8]]),
    "Сжатие (det=0.5)": np.array([[0.7, 0], [0, 0.7]]),
}

# Запуск визуализации
for name, matrix in matrices.items():
    visualize_matrix_properties(matrix, name)