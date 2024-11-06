#!/usr/bin/env python3

import argparse
import sys

def cmdline_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    
    p.add_argument('required_positional_argument', help='desc')
    p.add_argument('--on', action='store_true', help='include to enable')
    p.add_argument('-v', '--verbosity', type=int, choices=[0,1,2], default=0, help='volba vymluvnosti')
    p.add_argument('-n', '--number')

    return p.parse_args()

if __name__ == '__main__':
    args = cmdline_args()
    print(args)

