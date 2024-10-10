
# Contrast2NonContrast

This package is for generating 3d non-contrast cardiac CT images from contrast CTs. This package only accept dicom or nifty image format

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
pip install git+https://github.com/YumengggZhang/Contrast2NonContrast.git

```
