import os
import argparse
import time
import random
import numpy as np

import torch
import torch.nn as nn
import torch.functional as F
import torchvision.transforms as T 

from torch.backends import cudnn
from torch.utils.data.dataloader import DataLoader

# import utils
from utils.avgmeters import AverageMeter
# import model and ...

# setting random seed
seed = 1
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)            
torch.cuda.manual_seed(seed)       
torch.cuda.manual_seed_all(seed) 
cudnn.deterministic = True



def main(cfg):
    pass



if __name__ == "__main__": 
    # add parser
    parser = argparse.ArgumentParser(description='Trains my model',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # optimzer option
    parser.add_argument('--epochs', type=int, default=20, help="number of epochs to train")
    parser.add_argument('--lr', type=float, default=0.001, help="learning rate")
    parser.add_argument('--weight_decay', type=float, default=0.0005, help="l2 pernalized term")
    parser.add_argument('--batch_size', type=int, default=64, help="batch_size")
    # parser.add_argument('--')


