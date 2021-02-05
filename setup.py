"""install for hitemp.

hitemp
======
"""

from setuptools import setup, find_packages

description = 'Automatically download & parse HITEMP line lists to a Pandas DataFrame'

setup(name='hitemp',
      version='1.0',
      description=description,
      long_description=description,
      long_description_content_type='text/markdown',
      url='https://github.com/radis/hitemp',
      author='Erwan Pannier',
      author_email='erwan.pannier@gmail.com',
      license='MIT License',
      packages=find_packages(),
      install_requires=[
          'radis>=0.9.28',
		  ],
      platforms="any",
      keywords=["hitemp", "spectroscopy"],
      classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing',
        "Operating System :: OS Independent"],
      zip_safe=True)
