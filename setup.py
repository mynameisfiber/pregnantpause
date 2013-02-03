from distutils.core import setup

setup(
    name='pregnantpause',
    version='1.0.1',
    description='Extends the length of pauses in an audio track to help with transcribing',
    author='Micha Gorelick',
    author_email='mynameisfiber@gmail.com',
    url='http://github.com/mynameisfiber/pregnantpause/',
    scripts=['pregnantpause.py',],

    requires=['scikits.audiolab', 'numpy', 'bottleneck', 'progressbar', ],
)
