# bandcamp-sniffer 


## Installation

    git clone https://github.com/Ricardo-Silva91/bandcamp-sniffer.git
    cd bandcamp-sniffer
    python setup.py install

## Usage
    usage: bandcamp-sniffer [-h] [-b BROWSER] [-d DISPLAY] [-v] [FILE]

    bandcamp sniffer

    positional arguments:
      FILE                  absolute path to json file to sniff to

    optional arguments:
      -h, --help            show this help message and exit
      -b BROWSER, --browser BROWSER
                            enter chrome or firefox, defaults to firefox
      -d DISPLAY, --display DISPLAY
                            show display, 0-no 1-yes , defaul=0
      -v, --version         display current version


## Author
* Ricardo Silva - https://github.com/Ricardo-Silva91

## Notes
* version - Python 3.x.
* Closing the bandcamp browser window before all albums have been downloaded is fine and will end processing early. The links which have been emailed already will still be downloaded as long as the Guerrilla Mail window is left open.
