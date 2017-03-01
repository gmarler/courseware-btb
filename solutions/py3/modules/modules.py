'''In this lab, you are creating a package named "greputils".  The
file layout will look like this:

  greputils/__init__.py
  greputils/contain.py
  greputils/files.py
  greputils/net/__init__.py
  greputils/net/html.py
  greputils/net/json.py
  greputils/net/text.py

Use "greputils_start.py" (in this directory) as a starting point.  You
must create the above directories and files, and copy each function
from greputils_start.py into the appropriate file, so the imports
below all work correctly. Unlike many other labs, you do NOT modify
the lab file (i.e., the file you are reading) - all you are doing is
creating and filling a directory named "greputils".

First, let's verify "greputils" is importable in your PYTHONPATH. (If
running in an IDE, you may need to add this manually.) An ImportError
means the test is not passing yet.

>>> import greputils


Now, let's try directly importing from sub-modules deep within the
package.

>>> from greputils.net.html import grep_html_as_text
>>> grep_html_as_text()
'Calling grep_html_as_text'

>>> from greputils.net.html import grep_html
>>> grep_html()
'Calling grep_html'

>>> from greputils.net.json import grep_json
>>> grep_json()
'Calling grep_json'

>>> from greputils.net.text import grep_text
>>> grep_text()
'Calling grep_text'

>>> from greputils.contain import contains
>>> contains()
'Calling contains'

>>> from greputils.contain import containsi
>>> containsi()
'Calling containsi'

>>> from greputils.files import grepfile
>>> grepfile()
'Calling grepfile'

>>> from greputils.files import grepfilei
>>> grepfilei()
'Calling grepfilei'


Let's make sure all items are available in the top-level.
>>> import greputils
>>> greputils.grepfile == grepfile
True
>>> greputils.grepfilei == grepfilei
True
>>> greputils.contains == contains
True
>>> greputils.containsi == containsi
True
>>> greputils.grep_html == grep_html
True
>>> greputils.grep_html_as_text == grep_html_as_text
True
>>> greputils.grep_text == grep_text
True
>>> greputils.grep_json == grep_json
True


It's sometimes useful to have multiple import points for the same
resources. Let's make all the greputils.net functions importable at
that level (and also make sure it's importing the exact same function
object):

>>> from greputils.net import grep_html_as_text as grep_html_as_text_net
>>> grep_html_as_text == grep_html_as_text_net
True

>>> from greputils.net import grep_html as grep_html_net
>>> grep_html == grep_html_net
True

>>> from greputils.net import grep_json as grep_json_net
>>> grep_json == grep_json_net
True

>>> from greputils.net import grep_text as grep_text_net
>>> grep_text == grep_text_net
True

'''

# Do not modify this file. Instead, create and appropriately fill a
# "greputils" directory which this file can import.

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
