import os, sys, glob

def prepare_test_data(path):
    files = sorted(glob.glob(path + '/*/*_vh_clean_2.ply'))
    for file in files:
        tail = os.path.split(file)[1]
        os.rename(file, os.path.join(TEST_DIR + tail))

def delete_sens(path):
    files = glob.glob(path + '/*/*.sens')
    for file in files:
        os.remove(file)

DATASETS_DIR = '/opt/datasets'
SCANNET_DIR = os.path.join(DATASETS_DIR, 'scannetv2')
TEST_DIR = os.path.join(SCANNET_DIR, 'test')
SCANS_DIR = os.path.join(DATASETS_DIR, 'scans_test')
SCANS_TEST_DIR = os.path.join(DATASETS_DIR, 'scans_test')
LABELS_FILE = 'scannetv2-labels.combined.tsv'

# if not os.path.exists(SCANNET_DIR):
#     os.makedirs(SCANNET_DIR)
#     if not os.path.exists(TEST_DIR):
#         os.makedirs(TEST_DIR)

#prepare_test_data(SCANS_TEST_DIR)
#os.rename(os.path.join(DATASETS_DIR, LABELS_FILE), os.path.join(SCANNET_DIR, LABELS_FILE))
delete_sens(SCANS_DIR)
delete_sens(SCANS_TEST_DIR)
