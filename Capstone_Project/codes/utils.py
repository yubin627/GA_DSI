# -*- coding: utf-8 -*-

from config import *
import os
import time
import torch
from torchvision import transforms
import numpy as np


def dump_model(model, epoch, batch_idx="final"):
    dump_folder = 'output/models'

    if not os.path.isdir(dump_folder):
        os.mkdir(dump_folder)
    save_path = os.path.join(dump_folder, "model_{}_{}.pth.tar".format(epoch, batch_idx))
    torch.save(model.state_dict(), save_path)
    return save_path


def load_model(path=None):
    if not path:
        return None
    full = os.path.join(DATASET_BASE, 'models', path)
    for i in [path, full]:
        if os.path.isfile(i):
            return torch.load(i)
    return None


def dump_feature(feat, img_path):

    feat_folder = '/output/features'
    if not os.path.isdir(feat_folder):
        os.mkdir(feat_folder)
    np_path = img_path.replace("/", "+")
    np_path = os.path.join(feat_folder, np_path)
    np.save(np_path, feat)


def load_feature(img_path):
    feat_folder = os.path.join(DATASET_BASE, 'features')
    np_path = img_path.replace("/", "+")
    np_path = os.path.join(feat_folder, np_path + '.npy')
    if os.path.isfile(np_path):
        feat = np.load(np_path)
        return feat
    else:
        return None

data_transform_test = transforms.Compose([
    transforms.Resize(CROP_SIZE),
    transforms.CenterCrop(CROP_SIZE),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


def timer_with_task(job=""):
    def timer(fn):
        def wrapped(*args, **kw):
            print("{}".format(job + "..."))
            tic = time.time()
            ret = fn(*args, **kw)
            toc = time.time()
            print("{} Done. Time: {:.3f} sec".format(job, (toc - tic)))
            return ret
        return wrapped
    return timer
