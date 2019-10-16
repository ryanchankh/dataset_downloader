import argparse
import os
import tarfile
import urllib

import utils


parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, help="name of the dataset")
parser.add_argument("--save_to", type=str, default="/tmp/tmp_dataset", help="Save downloaded dataset to this directory")
FLAGS = parser.parse_args()


download_url = utils.get_download_url(FLAGS.name)
utils.save_raw(FLAGS.name, download_url, FLAGS.save_to)


    
    

