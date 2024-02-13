import pandas as pd
import numpy as np

import os
import datetime

np.random.seed(datetime.time.second)

def get_foldlength(folder: str):
    num_files = 0
    for (dirpath, dirnames, filenames) in os.walk(folder):
        for filename in filenames:
            num_files += 1
    return num_files 
        
def get_random_image(folder: str):
    image_idx = np.randint(0, get_foldlength(folder))
    num_files = 0
    for (dirpath, dirnames, filenames) in os.walk(folder):
        for filename in filenames:
            if num_files == image_idx:
                return filename
            else: 
                num_files += 1

class CustomDataset(Dataset):
    def __init__(self, data_folders: list):
        self.data_folders = data_folders
        
    def __len__(self):
        total_samples = 0
        for folder in self.data_folders:
            total_samples += get_foldlength(folder)
            
    def __getitem__(self):
        folder_idx = np.randint(0, len(self.data_folders), (1, ))[0]
        folder = self.data_folders[folder_idx]
         
        random_image = get_random_image(folder)
        image = cv2.imread(f"{folder}/{random_image}")
        sample, label = image, folder.split('/')[-1]
        
        return sample, label
    