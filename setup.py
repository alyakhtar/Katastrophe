from distutils.core import setup
setup(
  name = 'katastrophe',
  packages = ['katastrophe'], 
  version = '0.1',
  description = 'Download torrents from kat.ph directly through terminal',
  author = 'Aly Akhtar',
  author_email = 'samurai.aly@gmail.com',
  url = 'https://github.com/alyakhtar/katastrophe', 
  download_url = 'https://github.com/alyakhtar/mypackage/tarball/0.1',
  entry_points='''
               [console_scripts]
               katastrophe=katastrophe:main
           ''',
  keywords = ['torrent', 'download', 'kat.ph'],
)