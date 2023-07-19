import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider
from DataHandler import DataHandler

class Draw:
    def __init__(self, data_handler):
        self.fig = plt.figure()
        self.ax = plt.axes(projection='3d')
        self.x_axis = self.ax.set_xlabel('x-axis [m]')
        self.y_axis = self.ax.set_ylabel('y-axis [m]')
        self.z_axis = self.ax.set_zlabel('z-axis [m]')
        self.data_handler = data_handler

        # Initialize slider properties
        self.ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
        self.slider = Slider(self.ax_slider, 'Time', 1, len(data_handler.times), valinit=1, valstep=1)
        self.slider.on_changed(self.update_path)

    def draw_cylinder(self, radius=3, height=20, x_center=4, y_center=0, elevation=10, color='b'):
        resolution = 20
        x_center = x_center
        y_center = y_center
        radius = radius
        z_center = (0.5 * (height+elevation))
        z = np.linspace(elevation, elevation + height, resolution)

        theta = np.linspace(0, 2 * np.pi, resolution)
        theta_grid, z_grid = np.meshgrid(theta, z)
        x_grid = radius * np.cos(theta_grid) + x_center
        y_grid = radius * np.sin(theta_grid) + y_center
        self.ax.plot_surface(x_grid, y_grid, z_grid, linewidth=0, color=color)

    def draw_dronepath(self, x, y, z, offset, c='b', with_arrow=0, step=10):
        x_off = x[offset]
        y_off = y[offset]
        z_off = z[offset]

        self.ax.scatter(x_off, y_off, z_off, color='r', s=200)
        self.ax.plot(x_off, y_off, z_off, color='r')

        self.ax.scatter(x, y, z, color=c, s=1)
        self.ax.plot(x, y, z, color=c)

        if with_arrow == 1:
            for i in range(0, len(x) - step, step):
                self.ax.quiver(x[i], y[i], z[i], x[i + step], y[i + step], z[i + step], mutation_scale=10, fc="red")

    def draw_figure(self):
        plt.show()

    def update_path(self, val):
        offset = int(val) - 1
        self.ax.clear()
        print("off", offset)
        # self.draw_cylinder()
        
        # self.ax.scatter(self.x_off, self.y_off, self.z_off, color='y')
        # self.ax.plot(self.x_off, self.y_off, self.z_off, color='y')
        
        x, y, z, _, _, _, _ = self.data_handler.offset(
            self.data_handler.x, self.data_handler.y, self.data_handler.z,
            self.data_handler.xroll, self.data_handler.ypitch, self.data_handler.zyaw,
            self.data_handler.w, offset
        )
        self.draw_dronepath(x, y, z, offset)

        print("x", len(x))
        plt.draw()