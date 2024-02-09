#  Source: assistant
# Destination: user

#  You can use NumPy to perform matrix multiplication on a GPU. This requires NumPy's linear algebra module and the Cupy library. Cupy is a drop-in replacement for NumPy that makes arrays on a wide range of devices, including GPUs. The following is an example of matrix multiplication on a GPU using NumPy, Cupy, and PyCUDA.

# ```
import timeit
import numpy as np
from cupy import mean, array_view

np.random.seed(123)
a = np.random.randn(512, 512)
b = np.random.randn(512, 512)

device = cupy.cuda.Device(0)
stream = cupy.cuda.Stream(device, True)
a_dev = array_view.array_view(a, device=device, stream=stream)
b_dev = array_view.array_view(b, device=device, stream=stream)
c_dev = a_dev @ b_dev

assert c_dev is not None

ms1 = mean(c_dev, axis=1, stream=stream)
ms2 = mean(c_dev, axis=0, stream=stream)

stream.synchronize()

print('mean of C along rows:', ms1)
print('mean of C along columns:', ms2)

ms1_host = ms1.get(stream)
ms2_host = ms2.get(stream)

print('mean of C along rows (host):', ms1_host)
print('mean of C along columns (host):', ms2_host)
# ```