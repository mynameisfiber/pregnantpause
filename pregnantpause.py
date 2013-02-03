#!/usr/bin/env python
"""
Elaine is a pain 
and she lives down the drain

she is also insane
and she will remaine
a bane

ps: plantaine
"""

from scikits import audiolab
import numpy as np
import bottleneck as bn

import sys
from progressbar import ProgressBar, ETA, Bar
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Make your sounds pregnant')
    parser.add_argument('--silce-seconds', dest='silence_seconds', default=2.0, type=float, help='How long of a silence to insert')
    parser.add_argument('--window-seconds', dest='window_seconds', default=0.5, type=float, help='Window size of analysis (smaller means more resolution)')
    parser.add_argument('input_file', metavar='input_file', type=str, help="Input file to analyse, must be a WAV file")
    parser.add_argument('output_file', metavar='output_file', type=str, nargs='?', default=None, help="Output file, must be a WAV file")

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    window_seconds = args.window_seconds
    silence_seconds = args.silence_seconds

    if not output_file:
        output_file = input_file + "-pregnant.wav"

    if not output_file.endswith(".wav"):
        print "Output file must end in .wav"
        sys.exit(-1)

    print "Reading file"
    try:
        data, fs, enc = audiolab.wavread(input_file)
    except IOError, e:
        print "Could not read file: %s" % e
        sys.exit(-1)


    # cast to mono
    if len(data.shape) == 2:
        data = data.sum(axis=0)  # should this be .mean()?

    window_frames= int(fs * window_seconds)
    silence_frames = int(fs * silence_seconds)

    print "Analyzing"
    move_std = bn.move_std(data, window=window_frames/2)
    mean_std = bn.nanmean(move_std)

    widgets = ["Creating file", Bar(), ETA()]
    pbar = ProgressBar(widgets=widgets, maxval=len(data)).start()

    new_data = []
    silence_count = 0
    for i, d in pbar(enumerate(data)):
        new_data.append(d)
        if move_std[i] is not np.nan and move_std[i] < mean_std:
            silence_count += 1
        else:
            if window_frames < silence_count < silence_frames:
                hs = silence_count / 2
                new_data = new_data[:-hs] + [0]*silence_frames + new_data[-1*hs:]
            silence_count = 0

    print "Writing file"
    audiolab.wavwrite(np.asarray(new_data), output_file, fs=fs)
    sys.exit(0)

