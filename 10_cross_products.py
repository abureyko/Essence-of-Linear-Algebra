import numpy as np
import matplotlib.pyplot as plt

def visualize_cross_product():
    # Создаем два вектора в 3D
    a = np.array([3, 0, 0])  # Вдоль оси X
    b = np.array([0, 2, 0])  # Вдоль оси Y
    
    # Вычисляем векторное произведение
    cross = np.cross(a, b)
    
    # Создаем 3D график
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Отображаем векторы
    ax.quiver(0, 0, 0, a[0], a[1], a[2], color='blue', arrow_length_ratio=0.1, linewidth=3, label='a = [3, 0, 0]')
    ax.quiver(0, 0, 0, b[0], b[1], b[2], color='red', arrow_length_ratio=0.1, linewidth=3, label='b = [0, 2, 0]')
    ax.quiver(0, 0, 0, cross[0], cross[1], cross[2], color='green', arrow_length_ratio=0.1, linewidth=3, label='a × b = [0, 0, 6]')
    
    # Показываем параллелограмм
    vertices = np.array([[0, 0, 0], a, a+b, b])
    ax.plot(vertices[[0,1,2,3,0], 0], vertices[[0,1,2,3,0], 1], vertices[[0,1,2,3,0], 2], 
            'purple', alpha=0.3, label='Параллелограмм')
    
    # Настройки графика
    ax.set_xlim([-1, 4])
    ax.set_ylim([-1, 3])
    ax.set_zlim([-1, 7])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()

    # Добавляем информацию о площади
    area = np.linalg.norm(cross)
    ax.text(1, 1, 3, f'Площадь = {area}', fontsize=12, bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.9))
    
    plt.title('Векторное произведение: a × b = вектор, перпендикулярный a и b\nДлина = площади параллелограмма')
    plt.show()

# Запускаем визуализацию
visualize_cross_product()