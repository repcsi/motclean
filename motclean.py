import os
import shutil
import yaml

def check_free(path, free_limit):
    total, used, free= shutil.disk_usage(path)
    percentage_free = free / (total/100)

    if (percentage_free >= free_limit):
      print('free space is enough, exiting...')
      quit()
    else:
      print('insufficient free space, deleting...')

def remove_dir(directory):
    print("deleting directory {directory}...")
    shutil.rmtree(directory)

if __name__ == '__main__':

    stream = open(os.path.join("/motion/projects/motclean/","config.yaml"), 'r')
    config = yaml.load(stream, Loader=yaml.FullLoader)

    path = config['workdir']
    method = config['method']
    limit_free = config['free']

    dirs = os.listdir(path)
    dirs.sort()

    while True:
      check_free(path, limit_free)
      #print(f"deleting {dirs[0]}")
      remove_dir(os.path.join(path,dirs[0]))
      del dirs[0]

