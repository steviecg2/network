import glob
import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))

json_files = glob.glob(f'{DIRECTORY}/../features_snapshots/*ops.txt')
exception_files = glob.glob(f'{DIRECTORY}/../features_snapshots/*exception.txt')
for file in json_files:
    os.rename(file, file.replace('.txt', '.json'))
for file in exception_files:
    os.remove(file)
