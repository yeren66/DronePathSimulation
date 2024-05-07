from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
from matplotlib.patches import FancyArrowPatch
import numpy as np

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d,  self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

    def set_3d_properties(self):
        xs, ys, zs = self._verts3d
        self._verts2d = proj3d.proj_transform(xs, ys, zs, self.axes.M)[:2]

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))

        return np.min(zs)

def draw_path_with_arrows(points, ax):
    global path_number
    x, y, z = zip(*points)
    color = ['g', 'b', 'c', 'm', 'y', 'k']

    # 绘制路径
    ax.plot(x, y, z, color=color[path_number % 6])

    # 在路径上添加箭头
    num_arrows = len(points) - 1
    for i in range(num_arrows):
        start_point = points[i]
        end_point = points[i + 1]
        arrow = Arrow3D([start_point[0], end_point[0]], [start_point[1], end_point[1]], [start_point[2], end_point[2]],
                        mutation_scale=20, lw=1, arrowstyle="-|>", color=color[path_number % 6])
        ax.add_artist(arrow)
    
    path_number += 1

# 示例用法
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
path_number = 0
# 示例 points
points = [(0, 0, 0), (1, 1, 1), (2, 0, 2)]
draw_path_with_arrows(points, ax)
plt.show()
