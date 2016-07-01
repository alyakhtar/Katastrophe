from setuptools import setup
setup(name='katastrophe',
      packages=['katastrophe'],
      version='3',
      description='Command line interface to Kickass Torrents',
      author='Kevin Grant',
      license='MIT',
      author_email='kevinwgrant@gmail.com',
      url='https://github.com/wedwabbit/katastrophe',
      entry_points='''
               [console_scripts]
               katastrophe=katastrophe:main
           ''',
      install_requires=[
          'beautifulsoup4', 'tabulate', 'requests', 'lxml', 'docopt'
      ],
      keywords=['torrent', 'download', 'kat.cr', 'Kickass'], )
