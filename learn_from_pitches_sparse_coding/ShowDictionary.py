import matplotlib.pyplot as plt
import numpy as np

patch_size = (8,8)
V = np.load('Dictionaries.npy')
plt.figure(figsize=(4.2, 4))
for i, patch in enumerate(V):
    plt.subplot(18, 18, i + 1)
    plt.imshow(patch.reshape(patch_size), cmap=plt.cm.gray, interpolation='nearest')
    plt.xticks(())
    plt.yticks(())
#plt.suptitle('Patches of poses')
plt.subplots_adjust(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)
plt.savefig('dictionary.png')
plt.show()
