import numpy as np
import matplotlib.pyplot as plt

def cramer_visualization():
    # Система уравнений: 2x + 3y = 8; 4x + 1y = 6
    A = np.array([[2, 3], [4, 1]])  # Матрица коэффициентов
    b = np.array([8, 6])            # Вектор правой части
    
    # Исходные вектора
    v1 = A[:, 0]  # [2, 4] - первый столбец
    v2 = A[:, 1]  # [3, 1] - второй столбец
    
    # Вычисляем определители
    det_A = np.linalg.det(A)
    
    # Для x: заменяем первый столбец на b
    A_x = A.copy()
    A_x[:, 0] = b
    det_A_x = np.linalg.det(A_x)
    
    # Для y: заменяем второй столбец на b  
    A_y = A.copy()
    A_y[:, 1] = b
    det_A_y = np.linalg.det(A_y)
    
    # Решения
    x = det_A_x / det_A
    y = det_A_y / det_A
    
    # Визуализация
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Исходные вектора
    ax1.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.02, label='v1 = [2,4]')
    ax1.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.02, label='v2 = [3,1]')
    ax1.set_xlim(0, 5); ax1.set_ylim(0, 5)
    ax1.set_aspect('equal'); ax1.grid(True); ax1.legend()
    ax1.set_title(f'Исходные вектора\ndet(A) = {det_A:.1f}')
    
    # Для x: заменяем v1 на b
    ax2.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='green', width=0.02, label='b = [8,6]')
    ax2.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.02, label='v2 = [3,1]')
    ax2.set_xlim(0, 9); ax2.set_ylim(0, 7)
    ax2.set_aspect('equal'); ax2.grid(True); ax2.legend()
    ax2.set_title(f'Для x: заменяем v1 на b\ndet(A_x) = {det_A_x:.1f}')
    
    # Для y: заменяем v2 на b
    ax3.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.02, label='v1 = [2,4]')
    ax3.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='green', width=0.02, label='b = [8,6]')
    ax3.set_xlim(0, 9); ax3.set_ylim(0, 7)
    ax3.set_aspect('equal'); ax3.grid(True); ax3.legend()
    ax3.set_title(f'Для y: заменяем v2 на b\ndet(A_y) = {det_A_y:.1f}')
    
    plt.tight_layout()
    plt.show()
    
    print(f"Решение: x = {x:.1f}, y = {y:.1f}")
    print(f"Проверка: 2*{x:.1f} + 3*{y:.1f} = {2*x + 3*y:.1f}")

cramer_visualization()