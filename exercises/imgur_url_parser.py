__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2025"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Jason M. Pittman"
__status__ = "Exercise"

""" Create a function that takes an imgur link (as a string) and extracts the unique id and type. Return an object containing the unique id, and a string indicating what type of link it is.

The link could be pointing to:

    An album (e.g. http://imgur.com/a/cjh4E)
    A gallery (e.g. http://imgur.com/gallery/59npG)
    An image (e.g. http://imgur.com/OzZUNMM)
    An image (direct link) (e.g. http://i.imgur.com/altd8Ld.png)

Examples

    imgurUrlParser("http://imgur.com/a/cjh4E") ➞ { id: "cjh4E", type: "album" }

    imgurUrlParser("http://imgur.com/gallery/59npG") ➞ { id: "59npG", type: "gallery" }

    imgurUrlParser("http://i.imgur.com/altd8Ld.png") ➞ { id: "altd8Ld", type: "image" } 

Started: Feb 05, 2025 @ 3:18am ET
Intervals: 1
Ended: Feb 05, 2025 @ 3:48am ET
"""

from urllib.parse import urlparse

def parse_url(url):
    link_id = ''
    link_type = ''

    parsed_url = urlparse(url)

    if '.png' in parsed_url.path:
        link_type = 'image'
        link_id = parsed_url.path.split('.')
    else:
        junk, link_type, link_id = parsed_url.path.split('/')

    return {'id': link_id, 'type': link_type}

if __name__ == '__main__':
    #url = "http://imgur.com/a/cjh4E"
    #url = "http://imgur.com/gallery/59npG"
    url ="http://i.imgur.com/altd8Ld.png"

    data = parse_url(url)
    
    if data['type'] == 'a':
        print(data['id'], 'album')

    elif data['type'] == 'gallery':
        print(data['id'], 'gallery')

    else:
        print(data['id'], 'image')
