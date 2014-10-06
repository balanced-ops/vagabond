#!/usr/bin/env python
"""
This installs the ``Vagrantfile``.
"""
import os
import glob
import sys

print sys.argv


ROOT = os.path.dirname(os.path.abspath(__file__))
print ROOT


def install_vagrantfile(dest):
    vagrantfile = glob.glob(os.path.join(ROOT, 'Vagrantfile'))
    if not vagrantfile:
        raise Exception('No Vagrantfile found in {}'.format(ROOT))
    try:
        os.symlink(vagrantfile, os.path.join(dest, 'Vagrantfile'))
    except OSError, ex:
        print ex
        raise


def install_sample_vagrantuser_file(dest):
    taret_vagrantuser = os.path.join(dest, '.vagrantuser')
    if os.path.exists(taret_vagrantuser):
        raise Exception('{} file already exists. Will not overwrite.'
                        .format(taret_vagrantuser))

    with open(os.path.join(dest, '.vagrantuser'), 'w+') as f:
        pass
