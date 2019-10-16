import os
import urllib.request
import yaml

def get_download_url(name, paths_file="paths.yaml"):
    """Get download paths from url files."""

    with open(paths_file, 'r') as stream:
        try:
            paths_dict = yaml.safe_load(stream)
        except yaml.YAMLERROR as exc:
            print(exc)

    try:
        return paths_dict[name]
    except:
        print(f"{name} not found in paths.yaml.")


def save_raw(name, link, save_path, filetype="tar"):
    """Download the link, and save raw downloaded dataset 
    save path."""
    save_dir = os.path.join(save_path, name)

    print(f"Downloading file from {link}")
    filedata = urllib.request.urlopen(link)
    file_obj = filedata.read()

    if not os.path.exists(save_dir):
        print(f"Directory {save_dir} does not exist. Creating it now." )
        os.makedirs(save_dir)
    save_to = os.path.join(save_dir, f"raw.{filetype}")
    with open(save_to, 'wb+') as f:
        f.write(file_obj)
    print(f"Raw data saved to {save_to}")

        
