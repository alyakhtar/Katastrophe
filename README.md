# Katastrophe
<p align="left">
    <a href="https://pypi.python.org/pypi/katastrophe/1.1.5">
        <img src="https://img.shields.io/pypi/v/katastrophe.svg">
    </a>
    <a href="https://raw.githubusercontent.com/alyakhtar/Katastrophe/master/LICENSE.txt">
        <img src="https://img.shields.io/pypi/l/katastrophe.svg">
    </a>
</p>

**A Command-Line Interface for scraping Kickass torrents (kat.cr). Provides options to scrape top torrents in given categories, or searching for specific torrents. The user can select single, multiple or even specify a range for the torrent to download from any category.**

![ScreenShot](http://i.imgur.com/gVdTRPk.png)


## Installation

### Using [pip](https://pypi.python.org/pypi/pip/)

`$ pip install katastrophe`


### Get the latest build from the Source

* Clone the repo git clone https://github.com/alyakhtar/katastrophe
* Run python setup.py install


### Dependencies

* [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4/4.3.2)
* [tabulate](https://pypi.python.org/pypi/tabulate)
* [docopt](https://github.com/docopt/docopt)
* [requests](https://pypi.python.org/pypi/requests/)
* [lxml](https://pypi.python.org/pypi/lxml)


### Requires

* for Linux/Mac OS X
  - [Deluge](http://deluge-torrent.org)/[Transmission](http://transmissionbt.com)/[QBitTorrent](http://qbittorrent.sourceforge.net)/[Vuze](http://vuze.com)
* for Windows
  - [BitTorrent](https://www.bittorrent.com)/[μTorrent](https://utorrent.com)/[Deluge](http://deluge-torrent.org)



### Usage:
```sh
  katastrophe.py 
  katastrophe [-m | -t | -a | -s | -l | -g | -p | -b | -x | -M | -T | -A | -S | -B | -G | -P | -X]
  katastrophe -h | --help
  katastrophe --version

  Multi Download:
    i,j     From Serial No. i to Serial No. j
    ,i      From Serial No. 1 to Serial No. i 
    i,      From Serial No. i to serial no 25
    i,j,... Multiple Serial Numbers

```

### Options:

| Arguments               | Description                              |
| ----------------------- |:----------------------------------------:|
| -h, --help              | Show this screen                         |
| --version               | Show version                             |
| -m, --newmovies         | Show latest Movie Torrents               |
| -t, --newtv             | Show latest TV Torrents                  |
| -a, --newanime          | Show latest Anime Torrents               |
| -s, --newsongs          | Show latest Music Torrents               |
| -l, --newlosslessmusic  | Show latest Lossless Music Torrents      |
| -g, --newgames          | Show latest Game Torrents                |
| -p, --newapplications   | Shoe latest Application Torrents         |
| -b, --newbooks          | Show latest Book Torrents                |
| -x, --xxx               | Show latest XXX Torrents                 |
| -M, --movies            | Search by Movie Category                 |
| -T, --tv                | Search by TV Category                    |
| -A, --anime             | Search by Anime Category                 |
| -S, --songs             | Search by Music Category                 |
| -B, --books             | Search by Book Category                  |
| -G, --games             | Search by Games Category                 |
| -P, --applications      | Search by Applications Category          |
| -X, --XXX               | Search by XXX Category                   |

### Screenshots


#### Latest Movies


`$ katastrophe -m`


![ScreenShot](http://i.imgur.com/sMbc4Pb.png)


#### Latest TV Shows



`$ katastrophe -t`


![Screenshot](http://i.imgur.com/NJKtGWH.png)


#### Latest Games and Applications


`$ katastrophe -g`


![ScreenShot](http://i.imgur.com/YSQoOpS.png)


#### Latest Music 


`$ katastrophe -s`


![ScreenShot](http://i.imgur.com/PXcGIEO.png)


#### Latest Anime


`$ katastrophe -a`


![ScreenShot](http://i.imgur.com/IVnSAs1.png)


### Latest Books


`$ katastrophe -b`


![ScreenShot](http://i.imgur.com/DDwqrZF.png)


#### Latest Lossless Music


`$ katastrophe -l`


![ScreenShot](http://i.imgur.com/tknw3Zt.png)


#### Multiple Downloads


`$ Starting and Ending Torrent`


![ScreenShot](http://i.imgur.com/wy78wMu.png)


`$ Starting Torrent`


![ScreenShot](http://i.imgur.com/hBzll6P.png)


`$ Ending Torrent`


![ScreenShot](http://i.imgur.com/ziLjt25.png)

### Contribute

Found a bug or want to suggest a new feature? Report it by opening an issue. Feel free to send a pull request for any improvements or feature requests ;)


### License

MIT © [Aly Akhtar](https://github.com/alyakhtar)
