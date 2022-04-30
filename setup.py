import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'snookerprofile',      
  packages = ['snookerprofile'], 
  version = '0.0.2',  
  license='MIT', 
  description = 'Snooker Profile Learning by Snooker Patcharee',
  long_description=DESCRIPTION,
  author = 'Snooker Patcharee',                 
  author_email = 'snooker.nnnn@gmail.com',     
  url = 'https://github.com/Snookerpatcharee/snookerprofile',  
  download_url = 'https://github.com/Snookerpatcharee/snookerprofile/archive/v0.0.1.zip',  
  keywords = ['snooker', 'profile', 'Snooker Patcharee'],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Software Development :: Utilities',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)