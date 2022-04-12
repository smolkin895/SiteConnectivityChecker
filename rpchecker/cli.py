import argparse
def read_user_cli_args():
    """Hand the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="rpchecker", description="check the availability of websites"
    )
    parser.add_argument(
        '-u',
        '--urls',
        metavar = 'URLs',
        nargs='+',
        type = str,
        default = [],
        help = 'enter one or more urls'
    )
    parser.add_argument(
        '-f',
        '--input_file',
        metavar = 'FILE',
        type = str,
        default = '',
        help = 'read URLs from a file'
    )
    return parser.parse_args()


def display_check_result(result, url, error=''):
    print(f'The status of {url} is:', end=' ')
    if result:
        print('"Online!" 👍', end='\n')
    else:
        print(f'"Offline!" 👎 \n  Error: "{error}"', end='\n')


def display_total_check_result(length, checked ):
    print('=======================================================================')
    print(f'Connected to {checked} sites, from total {length}')