import os
from totalsegmentator.python_api import totalsegmentator
from ImageTool.tool import resize
import os
import SimpleITK as sitk
import numpy as np
import torch

from models import create_model
from options.train_options import TrainOptions
import matplotlib.pyplot as plt

@torch.no_grad()
def save_fake_native(input_path,out_path,device='cpu'):
    # root_path - is the path to the raw Coltea-Lung-CT-100W data set.

    """Define Model Don't change"""

    opt = TrainOptions().parse()
    opt.load_iter = 90
    opt.isTrain = False
    opt.device = device
    opt.model = 'da_cytran'
    opt.name = 'da-56'

    model = create_model(opt)
    model.setup(opt)
    gen = model.netG_A
    # gen = model.netG_B
    gen.eval()
    ori =  sitk.ReadImage(input_path)
    ori_array = sitk.GetArrayFromImage(ori)
    _, bbox = totalsegmentator(input_path, task = "heartchambers_highres", crop_save=out_path, crop_add = 0)
    size =  sitk.ReadImage(out_path).GetSize()
    img = resize(out_path, (320, 256, -1))
    img_array = sitk.GetArrayFromImage(img)
    
    output_array = np.zeros_like(img_array)

    # patient_dir = os.path.join(data_path,patient)
    for i in range(img_array.shape[0]):
        orig_img = img_array[i]
        orig_img = orig_img / 1e3

        orig_img_in = np.expand_dims(orig_img, 0).astype(np.float64)
        orig_img_in = torch.from_numpy(orig_img_in).float().to(device)
        orig_img_in = orig_img_in.unsqueeze(0)

        output_array[i] = 1000 * gen(orig_img_in)[0, 0].detach().cpu().numpy()
    print("img_array:", np.max(output_array))
    img_output = sitk.GetImageFromArray(output_array)
    img_output.CopyInformation(img)
    sitk.WriteImage(img_output,out_path)
    resize_img = resize(out_path, size, out_path)
    ori_array[bbox[2][0]:bbox[2][1], bbox[1][0]:bbox[1][1], bbox[0][0]:bbox[0][1]] = sitk.GetArrayFromImage(resize_img)
    new_image = sitk.GetImageFromArray(ori_array)
    new_image.CopyInformation(ori)
    sitk.WriteImage(new_image,out_path)

            
if __name__ == '__main__':
    save_fake_native(
        input_path = r'/home/molloi-lab-linux2/Desktop/ZQY/Project perfusion/UCI/img/1_rest_v1_0000.nii',
        out_path = r'/home/molloi-lab-linux2/Desktop/ZQY/Project perfusion/1_rest_v1_0000.nii',
        device='cuda',
    )

