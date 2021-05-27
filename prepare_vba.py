import torch
torch.manual_seed(17)
import numpy as np
import os
# from data.scannetv2_inst import Dataset
# dataset = Dataset(test=True)
# dataset.testLoader()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


NUM_BLOCKS_ONE_DIM = 32
VOXEL_BLOCK_SIZE_ONE_DIM = 8
DIM = NUM_BLOCKS_ONE_DIM * VOXEL_BLOCK_SIZE_ONE_DIM



def flipped_sign(value):
    return np.sign(value) * (1 - value)


def plot_voxels(data, ind):
    """Plot voxels of `data`.
        Args:
            data - n-dimensional np.array
            ind - index of image for label
    """

    # Reshape and convert to bool
    data = data.reshape((DIM, DIM, DIM)).astype(bool)
    x, y, z = np.indices(data.shape).astype(float)

    # Add color
    c = np.ones(data.shape, object)
    c.fill('#7A88CC')
    c[np.where(data)] = '#FFD65D'

    fig = plt.figure()
    fig.patch.set_alpha(0.5)
    ax = fig.gca(projection='3d')
    ax.patch.set_alpha(0.5)  # Set semi-opacity
    # colors = np.zeros((3, 3, 3, 4))
    # colors[data] = [1, 0, 0, 0.5]
    # ax.voxels(data, facecolors=colors, edgecolor='gray')
    ax.voxels(data, edgecolor='gray')
    plt.savefig('label{}'.format(ind))  # Optional
    plt.show()



fig = plt.figure()


# vba = np.load('/mnt/c/Users/pejiang/Documents/GitHub/smg-pynfinitam/scenes/1.npy')
# vba = np.array([flipped_sign(xi["sdf"]) for xi in vba])
# np.save('flipped1.npy', vba)
vba = np.load('flipped1.npy')

plot_voxels(vba, 1)

# vba = np.reshape(vba, (DIM, DIM, DIM))

batch = 1
