import os
import argparse

from rich.console import Console
from rich.traceback import install

from handler import arguments

install()
console = Console()

LOGO = r"""


        [bright_white bold]$$$$$$\$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\  
        $$  _$$  _$$\  \____$$\ $$  __$$\ \____$$  |\____$$\ $$  __$$\  \____$$\ 
        $$ / $$ / $$ | $$$$$$$ |$$ |  $$ |  $$$$ _/ $$$$$$$ |$$ |  $$ | $$$$$$$ |
        $$ | $$ | $$ |$$  __$$ |$$ |  $$ | $$  _/  $$  __$$ |$$ |  $$ |$$  __$$ |
        $$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |$$$$$$$$\\$$$$$$$ |$$ |  $$ |\$$$$$$$ |
        \__| \__| \__| \_______|\__|  \__|\________|\_______|\__|  \__| \_______|

                            ──── Apple Music Lyrics ────[/]


"""

def main():
    parser = argparse.ArgumentParser(
        description="Manzana: Apple Music Lyrics"
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s v1.0.0'
    )
    parser.add_argument(
        '-s',
        '--sync',
        help="Save timecode's in 00:00.000 format (three ms points)",
        action="store_true"
    )
    parser.add_argument(
        '--no-txt',
        help="Don't save lyrics as a .txt file",
        action="store_true"
    )
    parser.add_argument(
        '--no-lrc',
        help="Don't save time-synced lyrics as a .lrc file",
        action="store_true"
    )
    parser.add_argument(
        '--print',
        help="print time-synced lyrics",
        action="store_true"
    )
    parser.add_argument(
        'url',
        help="Apple Music URL for an album or a song",
        type=str
    )

    parser.add_argument(
        'cookie',
        help="Apple Music cookie The media-user-token",
        type=str,
        nargs='?',  # 参数可选
        default=None  # 如果没有提供 cookie 参数，默认为 None
    )
    args = parser.parse_args()
    
    arguments(args)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    #console.print(LOGO)
    main()