import gzip
import numpy as np

def load_mnist(folder=''):

    f = gzip.open(folder + 'train-images-idx3-ubyte.gz','r')

    image_size = 28
    num_images = 60000

    f.read(15)
    buf = f.read(image_size * image_size * num_images)
    x_train = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    x_train = x_train.reshape(num_images, image_size, image_size)

    x_train[x_train>0]=1


    f = gzip.open(folder + 'train-labels-idx1-ubyte.gz','r')
    f.read(8)
    y_train = []
    for i in range(0,60000):   
        buf = f.read(1)
        labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
        y_train.append(labels[0])



    f = gzip.open(folder + 't10k-images-idx3-ubyte.gz','r')

    image_size = 28
    num_images = 10000




    f.read(15)
    buf = f.read(image_size * image_size * num_images)
    x_test = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    x_test = x_test.reshape(num_images, image_size, image_size)

    x_test[x_test>0]=1


    f = gzip.open(folder + 't10k-labels-idx1-ubyte.gz','r')
    f.read(8)
    y_test = []
    for i in range(0,10000):   
        buf = f.read(1)
        labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
        y_test.append(labels[0])

    return x_train, x_test, y_train, y_test


