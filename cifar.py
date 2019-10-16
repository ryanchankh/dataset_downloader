import os
import tarfile


IMG_DIMS = (32, 32)
IMG_CHANNELS = 3
NUM_CLASS = 10


def main(FLAGS):

    return None



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--save_to", type=str, default="/tmp/cifar10_data", help="Save downloaded dataset to this directory."
            )
    FLAGS, _ = parser.parse_known_args()

