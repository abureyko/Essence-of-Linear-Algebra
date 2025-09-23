import matplotlib.pyplot as plt
import numpy as np

def demonstrate_composition(matrix1: np.ndarray, matrix2: np.ndarray, title: str="") -> None:
    fig1,  (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(15,5))
    point = np.array([1,2])

    # 1. ИСХОДНОЕ СОСТОЯНИЕ
    ax1.scatter(point[0], point[1], color = 'green', s=100,label = 'Исходная точка')
    ax1.set_title('Исходное состояние')
    ax1.set_xlim(-4,4)
    ax1.set_ylim(-4,4)
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2. ПОСЛЕДОВАТЕЛЬНОЕ ПРИМЕНЕНИЕ: сначала matrix2, потом matrix1
    point_after_first = matrix2 @ point
    point_after_second = matrix1 @ point_after_first

    ax2.scatter(point[0], point[1], color='green', s=100, alpha=0.3, label='Исходная')
    ax2.scatter(point_after_first[0], point_after_first[1], color='blue', s=100, label='После 1-го преобразования')
    ax2.scatter(point_after_second[0], point_after_second[1], color='red', s=100, label='После 2-го преобразования')

    ax2.arrow(point[0], point[1], 
              point_after_first[0]-point[0], point_after_first[1]-point[1],
              head_width=0.1, color='blue', alpha=0.5)
    ax2.arrow(point_after_first[0], point_after_first[1],
              point_after_second[0]-point_after_first[0], point_after_second[1]-point_after_first[1],
              head_width=0.1, color='red', alpha=0.5)
    
    ax2.set_title('Последовательно: B, затем A')
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-4, 4)
    ax2.grid(True, alpha=0.3)
    ax2.legend()


    # 3. КОМПОЗИЦИЯ: одно преобразование матрицей A@B
    composite_matrix = matrix1 @ matrix2
    point_after_composite = composite_matrix @ point
    
    ax3.scatter(point[0], point[1], color = 'green', s=100, alpha=0.3, label='Исходная')
    ax3.scatter(point_after_composite[0], point_after_composite[1], color='purple', s=100, label='После A@B')

    ax3.arrow(point[0], point[1], point_after_composite[0]-point[0], point_after_composite[1]-point[1], head_width=0.1, color='purple', alpha=0.7)

    ax3.set_title(f'Композиция: A@B\n{composite_matrix}')
    ax3.set_xlim(-4, 4)
    ax3.set_ylim(-4, 4)
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    
    plt.suptitle(f'Композиция преобразований: {title}', fontsize=14)
    plt.tight_layout()
    plt.show()

    # Проверка, что результаты совпадают
    print(f"Последовательно: {point_after_second}")
    print(f"Композиция:      {point_after_composite}")
    print(f"Результаты совпадают: {np.allclose(point_after_second, point_after_composite)}")
    print("-" * 50)

# Матрицы для экспериментов
A_ROTATE = np.array([[0, -1], [1, 0]])     # Поворот на 90°
A_SHEAR = np.array([[1, 0.5], [0, 1]])     # Сдвиг
A_SCALE = np.array([[2, 0], [0, 0.5]])     # Растяжение/сжатие

if __name__ == "__main__":
    # Экспериментируем с разными комбинациями!
    
    print("ЭКСПЕРИМЕНТ 1: Сдвиг → Поворот")
    demonstrate_composition(A_ROTATE, A_SHEAR, "Сдвиг → Поворот")
    
    print("ЭКСПЕРИМЕНТ 2: Поворот → Сдвиг (обратный порядок!)")
    demonstrate_composition(A_SHEAR, A_ROTATE, "Поворот → Сдвиг")
    
    print("ЭКСПЕРИМЕНТ 3: Растяжение → Сдвиг")
    demonstrate_composition(A_SHEAR, A_SCALE, "Растяжение → Сдвиг")