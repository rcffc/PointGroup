import os, sys, glob

def prepare_data(path):      
    files = glob.glob(path + '/*_vh_clean_2.ply') + glob.glob(path + '/*_vh_clean_2.labels.ply') + glob.glob(path + '/*_vh_clean_2.0.010000.segs.json') + glob.glob(path + '/*[0-9].aggregation.json') 
        
    for file in files:
        tail = os.path.split(file)[1]
        if tail[:12] in val:
            os.rename(file, os.path.join(VAL_DIR, tail))
        if tail[:12] in train:
            os.rename(file, os.path.join(TRAIN_DIR, tail))
        if tail[:12] in test:
            os.rename(file, os.path.join(TEST_DIR, tail))

def delete_sens(path):
    files = glob.glob(path + '/*/*.sens')
    for file in files:
        os.remove(file)

PROJECT_ROOT = '/home/pejiang_local/repos/PointGroup'
DATASETS_DIR = '/opt/datasets'
SCANNET_DIR = os.path.join(DATASETS_DIR, 'scannetv2')
TRAIN_DIR = os.path.join(SCANNET_DIR, 'train')
VAL_DIR = os.path.join(SCANNET_DIR, 'val')
TEST_DIR = os.path.join(SCANNET_DIR, 'test')

SCANS_DIR = os.path.join(DATASETS_DIR, 'scans')
SCANS_TEST_DIR = os.path.join(DATASETS_DIR, 'scans_test')
LABELS_FILE = 'scannetv2-labels.combined.tsv'

train = set(line.strip() for line in open(os.path.join(PROJECT_ROOT, 'dataset', 'scannetv2', 'scannetv2_train.txt')))
val = set(line.strip() for line in open(os.path.join(PROJECT_ROOT, 'dataset', 'scannetv2', 'scannetv2_val.txt')))
test = set(line.strip() for line in open(os.path.join(PROJECT_ROOT, 'dataset', 'scannetv2', 'scannetv2_test.txt')))

if not os.path.exists(SCANNET_DIR):
    os.makedirs(SCANNET_DIR)
if not os.path.exists(TRAIN_DIR):
    os.makedirs(TRAIN_DIR)
if not os.path.exists(VAL_DIR):
    os.makedirs(VAL_DIR)
if not os.path.exists(TEST_DIR):
    os.makedirs(TEST_DIR)


# delete_sens(SCANS_DIR)
# delete_sens(SCANS_TEST_DIR)
# os.rename(os.path.join(DATASETS_DIR, LABELS_FILE), os.path.join(SCANNET_DIR, LABELS_FILE))
prepare_data(SCANS_DIR + '/*')
# prepare_test_data(TEST_DIR)