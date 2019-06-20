from __future__ import print_function

import os.path as osp

import numpy as np
import PIL.Image


here = osp.dirname(osp.abspath(__file__))


def main():
    label_png = osp.join(here, '/home/ganesh/new_images/e-visas/paper_visas/1220.jpeg')
    print('loaded:', label_png)
    print()

    lbl = np.asarray(PIL.Image.open(label_png))
    labels = np.unique(lbl)
    print("///: ",labels)

    label_names_txt = osp.join(here, '/home/ganesh/label_names.txt')
    label_names = [name.strip() for name in open(label_names_txt)]
    print('# of labels:', len(labels))
    print('# of label_names:', len(label_names))
    if len(labels) != len(label_names):
        print('Number of unique labels and label_names must be same.')
        quit(1)
    print()

    print('label: label_name')
    for label, label_name in zip(labels, label_names):
        print('%d: %s' % (label, label_name))


if __name__ == '__main__':
    main()