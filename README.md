
# Contrast2NonContrast

In this package, you can generate non-contrast 3d image from contrast 3d image.


```
from Contrast2NonContrast.python_api import save_noncontrast    
if __name__ == '__main__':
    save_noncontrast(
        input_path = r'your_folder/contrast.nii',
        out_path = r'your_folder/noncontrast.nii',
        device='cuda',
    )
```


You can install it through:
```
pip install git+https://github.com/YumengggZhang/Contrast2NonContrast.git git+https://github.com/Qiyu-Zh/TotalSegmentator_Crop.git git+https://github.com/Qiyu-Zh/Image-Toolbox.git

```
