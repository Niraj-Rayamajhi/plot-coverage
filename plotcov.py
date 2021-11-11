#!/usr/bin/env python3

##*******Prepared by Niraj Rayamajhi - nirajr2@illinois.edu**********

import argparse, math
from numpy.core.numerictypes import english_lower
import pandas as pd
import matplotlib.pyplot as plt


def read_csv_file(file, skip):
    estimates = file.rstrip('/')
    estimates_handle = pd.read_csv(estimates, skiprows=int(skip))
    return estimates_handle

parser = argparse.ArgumentParser(
        description= 'plot coverage', usage='%(prog)s [options]')
parser.add_argument(
    '--covfileA', dest='covfileA', help = 'path to coverage csv file')
parser.add_argument(
    '--covfileB', dest='covfileB', help = 'path to coverage csv file')
parser.add_argument(
    '--strainA', dest='strainA', help = 'Species strainA')
parser.add_argument(
    '--strainB', dest='strainB', help = 'Species strainB')
parser.add_argument(
    '--scalar', dest='scalar', action='store_true', help = 'scale x-axis')
parser.add_argument(
    '--yscale', dest='yscale', type=float, help = 'scale value x-axis')
parser.add_argument(
    '--zoom', dest='zoom', action='store_true', help = 'Zoom In')
parser.add_argument(
    '--xmin', dest='xmin', help = 'minimum genomic position')
parser.add_argument(
    '--xmax', dest='xmax', help = 'maxmimum genomic position')
parser.add_argument(
    '--ymax', dest='ymax', help = 'maxmimum coverage')


def main():
    args = parser.parse_args()
    fig, ax = plt.subplots(2,1, sharex=True)
    fig.tight_layout()
    fig.set_figheight(5)
    fig.set_figwidth(10)
    if args.covfileA != None: 
        pd_handle_A = read_csv_file(args.covfileA, 0)
        mean_value_A = pd_handle_A["Coverage"].mean()
        if args.scalar == True:
            ax[0].plot(pd_handle_A["Position"], pd_handle_A["Coverage"]/args.yscale, color='#bfbbd9', label=args.strainA,linewidth=3)
            ax[0].set_ylabel('Coverage (X) ' + str(int(args.yscale)), fontsize=10)
            ax[0].axhline(mean_value_A/args.yscale, color ='r', lw = 1, alpha = 1, linestyle='--', label='mean coverage')
        else:
            ax[0].plot(pd_handle_A["Position"], pd_handle_A["Coverage"], color='#bfbbd9', label=args.strainA,linewidth=3)
            ax[0].set_ylabel('Coverage (X)', fontsize=10)
            ax[0].axhline(mean_value_A, color ='r', lw = 1, alpha = 1, linestyle='--', label='mean coverage')
        ax[0].legend(loc="upper right")
        ax[0].grid(axis='x')
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        if args.zoom == True and args.ymax != None:
            if args.scalar == True:
                ax[0].set_ylim(top = float(args.ymax)/args.yscale)
            else:
                ax[0].set_ylim(top = float(args.ymax))
        if args.zoom == True and args.ymax == None:
           pass
        ax[0].set_ylim(bottom = 0.0000)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
    if args.covfileB != None: 
        pd_handle_B = read_csv_file(args.covfileB, 0)
        mean_value_B = pd_handle_B["Coverage"].mean()
        if args.scalar == True:
            ax[1].plot(pd_handle_B["Position"], pd_handle_B["Coverage"]/args.yscale, color='#5a7d9a', label=args.strainB, linewidth=3) 
            ax[1].set_ylabel('Coverage (X) ' + str(int(args.yscale)), fontsize=10)
            ax[1].axhline(mean_value_B/args.yscale, color ='r', lw = 1, alpha = 1, linestyle='--', label='mean coverage')
        else:
            ax[1].plot(pd_handle_B["Position"], pd_handle_B["Coverage"], color='#5a7d9a', label=args.strainB, linewidth=3) 
            ax[1].set_ylabel('Coverage (X)', fontsize=10)
            ax[1].axhline(mean_value_B, color ='r', lw = 1, alpha = 1, linestyle='--', label='mean coverage')
        ax[1].legend(loc="upper right")
        ax[1].grid(axis='x')
        ax[1].set_ylim(bottom = 0.0000)
        ax[1].set_xlim(left = 1)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
    plt.xlabel("Genome Position (base pair)", fontsize=10)
    if args.zoom == True and args.ymax != None:
        if args.scalar != True:
            plt.axis([float(args.xmin), float(args.xmax), 0, float(args.ymax)])
        else:
            plt.axis([float(args.xmin), float(args.xmax), 0, float(args.ymax)/args.yscale])
    if args.zoom == True and args.ymax == None:
            start, end = plt.ylim()
            plt.axis([float(args.xmin), float(args.xmax), start, end])
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()
    fig.savefig('coverage.png', dpi=300)

if __name__ == '__main__':
    main()
