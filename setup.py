from setuptools import setup
setup(name='katastrophe',
      packages=['katastrophe'],
      version='1.1.4',
      description='Download torrents from kat.ph directly through terminal',
      author='Aly Akhtar',
      license='MIT',
      author_email='samurai.aly@gmail.com',
      url='https://github.com/alyakhtar/katastrophe',
      # download_url = 'https://github.com/alyakhtar/mypackage/tarball/0.1',
      entry_points='''
               [console_scripts]
               katastrophe=katastrophe:main
           ''',
      install_requires=[
          'beautifulsoup4', 'tabulate', 'requests', 'lxml', 'docopt'
      ],
      keywords=['torrent', 'download', 'kat.ph'], )
