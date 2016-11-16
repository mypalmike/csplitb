#!/usr/bin/env python

import setuptools

setuptools.setup(name='csplitb',
  version='1.0.2',
  description='Split binary files on content boundaries',
  author='Michael White',
  author_email='csplitb@mypalmike.com',
  url='https://github.com/mypalmike/csplitb',
  packages=setuptools.find_packages(),
  include_package_data=True,
  scripts=['scripts/csplitb'],
  classifiers=[
      'Operating System :: POSIX',
      'Development Status :: 5 - Production/Stable',
      'Environment :: Console',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
      'Topic :: Utilities',
  ],
)
