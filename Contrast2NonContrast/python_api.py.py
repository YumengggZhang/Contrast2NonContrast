# This code is released under the CC BY-SA 4.0 license.
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

# Check if the environment variable is set
if os.getenv('KMP_DUPLICATE_LIB_OK') == 'TRUE':
    print("Environment variable set successfully.")
else:
    print("Failed to set environment variable.")


import os
import SimpleITK as sitk
import numpy as np
import torch
print('******************************')
print(torch.cuda.is_available())

# import pickle

from models import create_model
from options.train_options import TrainOptions
import matplotlib.pyplot as plt


# def load_array(file_path):
#     with open(file_path, 'rb') as f:
#         loaded_data = pickle.load(f)
#         return loaded_data

@torch.no_grad()
def save_fake_native(out_path,input_path,device='cpu'):
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


    img =  sitk.ReadImage(input_path)
    img_array = sitk.GetArrayFromImage(img)
    output_array = np.zeros_like(img_array)

    # patient_dir = os.path.join(data_path,patient)
    for i in range(img_array.shape[2]):
        orig_img = img_array[:,:,i]
        orig_img = orig_img / 1e3

        orig_img_in = np.expand_dims(orig_img, 0).astype(np.float64)
        orig_img_in = torch.from_numpy(orig_img_in).float().to(device)
        orig_img_in = orig_img_in.unsqueeze(0)

        output_array[:,:,i] = gen(orig_img_in)[0, 0].detach().cpu().numpy()
        
    img_output = sitk.GetImageFromArray(output_array)
    img_output.CopyInformation(img)
    sitk.WriteImage(img_output,out_path)

            
if __name__ == '__main__':
    save_fake_native(
        out_path = r'C:\Users\qzhuang4\Desktop\test.nii',
        input_path = r'C:\Users\qzhuang4\Desktop\uci_ucla\resize_crop_ucla\SUBJECT002_rest_v2_0000.nii',
        device='cuda',
    )

    # for img in os.listdir(r'predictions-orca-2'):
    #     print(img)
    #     plot_fake_image(img,'25.nii')