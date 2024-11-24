import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()
zeros = x_train[y_train == 9]

plt.figure(figsize=(10, 10))
for i in range(min(len(zeros), 1)):  
    plt.imshow(zeros[i], cmap='gray')
    plt.axis('off')

    plt.show()
