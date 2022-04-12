from http.client import HTTPConnection
from urllib.parse import urlparse as par

def site_is_online(url, timeout=2):
    """Returning True if the target URL is online
    Raise an Exception otherwise"""

    error = Exception('Unknown Error')
    parser = par(url)
    host  = parser.netloc or parser.path.split('/')[0]
    for port in(80,443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request('HEAD', '/')
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error
