#!/usr/bin/env python

import logging
import setuptools

import packaging_utils
from tfdetect import pkg

log = logging.getLogger(__name__)

_tf_pip_name = pkg.detect_tensorflow_package()
log.warn('Installing tensorflow as detected: %r', _tf_pip_name)

with open('README.rst', 'r') as fh:
    readme = fh.read()

conf = dict(
    name='tensorflow-auto-detect',
    summary=
    'Automatically install CPU or GPU tensorflow determined by looking for a CUDA installation.',
    author='Trevor Joynson',
    author_email='github@skywww.net',
    long_description=readme,
    license='GPL',
    packages=setuptools.find_packages(),
    version=pkg.get_version(),
    install_requires=[_tf_pip_name],
    keywords=['tensorflow', 'wtf'],
    classifier=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
    ],
)

conf = packaging_utils.setup_requirements()

if __name__ == '__main__':
    setuptools.setup(**conf)
