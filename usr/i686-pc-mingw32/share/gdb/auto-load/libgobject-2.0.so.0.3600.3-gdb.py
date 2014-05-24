import sys
import gdb

# Update module path.
dir_ = '/Users/aaa/mxe/usr/i686-pc-mingw32/share/glib-2.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from gobject import register
register (gdb.current_objfile ())
