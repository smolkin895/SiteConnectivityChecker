import sys
import pathlib


from rpchecker.checker import site_is_online
from rpchecker.cli import read_user_cli_args, display_check_result, display_total_check_result


def main():
    user_args = read_user_cli_args()
    urls = _get_websites_urls(user_args)
    if not urls:
        print('Error: no URLs to check', file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)


def _get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    return urls

def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with open(file_path) as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f'Error: empty input file, {file}',file=sys.stderr)
    else:
        print('Error:input file not found', file=sys.stderr)
    return[]

def _synchronous_check(urls):
    checked = 0
    for url in urls:
        error = ''
        try:
            result = site_is_online(url)
            checked += 1
        except Exception as e:
            error = str(e)
            result = False
        display_check_result(result, url, error)
    display_total_check_result(len(urls), checked)

if __name__ == "__main__":
    main()


