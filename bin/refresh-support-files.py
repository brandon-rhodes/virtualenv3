"""
Refresh any files in support-files/ that come from elsewhere
"""

import os
from urllib.request import urlopen
import sys

here = os.path.dirname(__file__)
support_files = os.path.join(here, '..', 'support-files')

files = [
    ('http://nightly.ziade.org/distribute_setup.py', 'ez_setup.py'),
    ('http://pypi.python.org/packages/source/d/distribute/distribute-0.6.3.tar.gz', 'distribute-0.6.3.tar.gz'),
    ]

def main():
    for url, filename in files:
        print('fetching', url, '...', end=' ')
        sys.stdout.flush()
        f = urlopen(url)
        content = f.read()
        f.close()
        print('done.')
        filename = os.path.join(support_files, filename)
        if os.path.exists(filename):
            f = open(filename, 'rb')
            cur_content = f.read()
            f.close()
        else:
            cur_content = ''
        if cur_content == content:
            print('  %s up-to-date' % filename)
        else:
            print('  overwriting %s' % filename)
            f = open(filename, 'wb')
            f.write(content)
            f.close()

if __name__ == '__main__':
    main()
