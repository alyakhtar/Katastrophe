from distutils.core import setup
setup(
  name = 'katastrophe',
  packages = ['katastrophe'], # this must be the same as the name above
  version = '0.1',
  description = 'Download torrents from kat.ph directly through terminal',
  author = 'Aly Akhtar',
  author_email = 'samurai.aly@gmail.com',
  url = 'https://github.com/alyakhtar/katastrophe', # use the URL to the github repo
  download_url = 'https://github.com/alyakhtar/mypackage/tarball/0.1', # I'll explain this in a second
  entry_points='''
               [console_scripts]
               katastrophe=katastrophe:main
           ''',
  keywords = ['torrent', 'download', 'kat.ph'] # arbitrary keywords
)