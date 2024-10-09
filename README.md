
# Contrast2NonContrast

In this package, you can generate non-contrast 3d image from contrast 3d image.

In jupyter notebook:
```
from Contrast2NonContrast.python_api import save_noncontrast
save_noncontrast(
    input_path = 'path_to_your_contrast_file.nii',
    out_path = 'path_to_your_noncontrast_file.nii',
    device='cuda',#or 'cpu'
)
```
In python file:
```
from Contrast2NonContrast.python_api import save_noncontrast    
if __name__ == '__main__':
    save_noncontrast(
        input_path = 'path_to_your_contrast_file.nii',
        out_path = 'path_to_your_noncontrast_file.nii',
        device='cuda',#or 'cpu'
    )

```
You can install it through:
```
pip install git+https://github.com/YumengggZhang/Contrast2NonContrast.git git+https://github.com/Qiyu-Zh/TotalSegmentator_Crop.git git+https://github.com/Qiyu-Zh/Image-Toolbox.git

```
