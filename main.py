from parser_code import parse_code
from visualization import draw_combined, draw_scene, draw_path, draw_start_end
import numpy as np

def main():
    # 定义场景的矩阵
    matrix_size = (15, 15, 15)
    matrix = np.zeros(matrix_size, dtype=int)
    matrix[5:10, 5:10, 0] = 1

    # 定义无人机的起点和终点
    start = (0, 0, 0)
    end = (150, 150, 150)

    # 定义无人机的初始坐标
    drone_coordinate = (0, 0, 0)

    # 定义无人机控制代码的文件路径
    file_path = 'sample.py'

    # 解析无人机控制代码
    coordinate_list = parse_code(file_path, drone_coordinate)

    # 绘制场景、路径和起点终点
    draw_combined(coordinate_list, matrix, start, end)

if __name__ == "__main__":

    main()


