import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np



def draw_path(points, ax=None):
    flag = 0
    if ax is None:
        flag = 1
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # 设置坐标轴范围
        ax.set_xlim([0, 150])
        ax.set_ylim([0, 150])
        ax.set_zlim([0, 150])

        # 设置坐标轴标签
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
    # 解包点坐标到x, y, z列表
    x, y, z = zip(*points)

    # 绘制路径
    ax.plot(x, y, z, marker='o')

    if flag == 1:
        plt.show()

def draw_scene(matrix, ax=None):
    flag = 0
    if ax is None:
        flag = 1
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # 设置坐标轴范围
        ax.set_xlim([0, 150])
        ax.set_ylim([0, 150])
        ax.set_zlim([0, 150])

        # 设置坐标轴标签
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
    # 获取矩阵大小
    matrix_size = matrix.shape
    
    # 计算放大后的每个体素的位置
    # 我们创建了一个辅助的空间坐标网格，使得每个体素都能被放大到适当的位置
    filled = np.argwhere(matrix)
    for x, y, z in filled:
        # 对于矩阵中的每个非空体素，我们绘制一个以该点为中心，尺寸为10的立方体
        # 注意这里简化处理，实际上可以根据需求调整立方体的颜色和透明度等属性
        ax.bar3d(x*10, y*10, z*10, 10, 10, 10, edgecolor='gray', color=(0, 0, 0, 0), alpha=0.1)

    if flag == 1:
        plt.show()

def draw_start_end(start, end, ax=None):
    flag = 0
    if ax is None:
        flag = 1
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # 设置坐标轴范围
        ax.set_xlim([0, 150])
        ax.set_ylim([0, 150])
        ax.set_zlim([0, 150])

        # 设置坐标轴标签
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
    # 绘制起点和终点
    ax.scatter(start[0], start[1], start[2], color='green', s=100)
    ax.scatter(end[0], end[1], end[2], color='red', s=100)

    if flag == 1:
        plt.show()

def draw_combined(points=None, matrix=None, start=None, end=None):
    if points is None and matrix is None and start is None and end is None:
        return  
    # 创建图形和3D坐标轴
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 设置坐标轴范围
    ax.set_xlim([0, 150])
    ax.set_ylim([0, 150])
    ax.set_zlim([0, 150])

    # 设置坐标轴标签
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # 绘制路径和场景
    if points is not None:
        draw_path(points, ax)
    if matrix is not None:
        draw_scene(matrix, ax)
    if start is not None and end is not None:
        draw_start_end(start, end, ax)

    # 显示图形
    plt.show()

if __name__ == "__main__":
    # 定义路径的点
    points = [(0, 0, 0), (50, 0, 0), (50, 100, 0), (50, 100, 100), (100, 100, 100)]

    draw_path(points)

    # 创建原始矩阵
    matrix_size = (15, 15, 15)
    matrix = np.zeros(matrix_size, dtype=int)

    # 添加障碍物
    matrix[5:10, 5:10, 0:10] = 1
    matrix[:3, :3, 10:] = 1

    draw_scene(matrix)

    # 定义起点和终点
    start = (0, 0, 0)
    end = (100, 100, 100)

    draw_start_end(start, end)

    draw_combined(points, matrix, start, end)

