from setuptools import setup

setup(
    name = 'pregnantpause',
    version = '1.2',
    description = 'Extends the length of pauses in an audio track to help with transcribing',
    author = 'Micha Gorelick',
    author_email = 'mynameisfiber@gmail.com',
    url = 'http://github.com/mynameisfiber/pregnantpause/',
    license = "GPLv2",

    classifiers = [
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Communications",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ],

    scripts = ['pregnantpause.py',],
    install_requires = ['numpy', 'progressbar', ],
    extras_require = {
        "fast" : ["bottleneck", ]
    }
)
