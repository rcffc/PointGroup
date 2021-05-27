"""
Visualize 3d voxels and 2d images.
Author: @JustinShenk
Note: Requires matplotlib 2.0.2 or later to use the `ax.voxels` method (https://matplotlib.org/devdocs/gallery/mplot3d/voxels.html).

"""
import sys
# import tkinter
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()


def plot_voxels(data, ind):
    """Plot voxels of `data`.
        Args:
            data - n-dimensional np.array
            ind - index of image for label
    """

    # Reshape and convert to bool
    data = data.reshape((3, 3, 3)).astype(bool)
    x, y, z = np.indices(data.shape).astype(float)

    # Add color
    c = np.ones(data.shape, object)
    c.fill('#7A88CC')
    c[np.where(data)] = '#FFD65D'

    fig = plt.figure()
    fig.patch.set_alpha(0.5)
    ax = fig.gca(projection='3d')
    ax.patch.set_alpha(0.5)  # Set semi-opacity
    colors = np.zeros((3, 3, 3, 4))
    colors[data] = [1, 0, 0, 0.5]
    ax.voxels(data, facecolors=colors, edgecolor='gray')
    plt.savefig('label{}'.format(ind))  # Optional
    plt.show()


# Load two 3d data samples
labels_data = np.array([[0.,  1.,  1.,  0.,  1.,  1.,  0.,  1.,  0.,  0.,  1.,  0.,  0.,
                      1.,  1.,  0.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  1.,  1.,
                      0.],
                     [1.,  0.,  0.,  1.,  0.,  0.,  1.,  0.,  1.,  0.,  1.,  1.,  0.,
                      0.,  0.,  1.,  0.,  1.,  0.,  0.,  1.,  0.,  1.,  1.,  0.,  1.,
                      0.]])

# Plot y labels
for ind, data in enumerate(labels_data):
    plot_voxels(data, ind)

# Plot x inputs (2d views):
# data = np.load('first10.npy')

# for img_index, image in enumerate(data[:2]):
#     for view_index, view in enumerate(image):
#         if view_index < 2:  # For demo only
#             fig = plt.figure()
#             plt.title('Object {} - View {}'.format(img_index, view_index))
#             plt.imshow(view)
#             plt.savefig('Object{}-View{}'.format(img_index, view_index))
plt.savefig("mygraph.png")

plt.show()
