#!/Users/dminh/miniconda3/bin/python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('old')
parser.add_argument('new')
args = parser.parse_args()

import glob, os
FNs = glob.glob(f'*{args.old}*')
for FN in FNs:
    # shutil.move(FN, FN.replace(args.old, args.new))
    FN_n = FN.replace(args.old, args.new)
    os.system(f'git mv {FN} {FN_n}')

