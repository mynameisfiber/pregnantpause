# PregnantPause 

## What is?!

Transcribing can be hard, especially if the speaker doesn't take proper pauses while speaking.  This little script intends to fix that!  This script will output a new audio file with the pauses extended!

## How does it work?

We analyse the windowed standard deviation of the waveforms and identify regions that are below the mean standard deviation.  These regions are considered to be "silence".  This assumption only really works for speech, but since we are focusing on transcribing I think it's quite a good assumption.

## Installing

Installation is quite simple!  Either clone the repo and install using python:

```
$ git clone https://github.com/mynameisfiber/pregnantpause.git
$ cd pregnantpause
$ sudo python setup.py install
$ pregnantpause.py --help
```

Or by using pip:

```
$ [sudo] pip install pregnantpause
$ pregnantpause.py --help
```

## Usage

Invoking with `--help` shows the list of usable parameters.  One thing to note is that we only operate on WAV files!
