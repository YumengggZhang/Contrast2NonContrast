
# Contrast2NonContrast

In this package, you can calculate hausdorff distance loss in GPU easily.
Exampe:
Multiple classes example:
```
example1
```

```
example2
```

Binary example:
```
import torch.nn as nn
sigmoid = nn.Sigmoid()
x = torch.rand(2, 1, 32, 32, 32).cuda()
y = torch.randint(0, 2, (2, 1, 32, 32, 32)).cuda()
loss = HD_loss(apply_nonlin=sigmoid, alpha = 2)
res = loss(x, y)
print(res)
```
bulabula

You can install it through:
```
!pip install git+https://github.com/YumengggZhang/Contrast2NonContrast.git
```
