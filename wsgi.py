import sys

path = '/home/Verduu/dash'
if path not in sys.path:
    sys.path.append(path)

from dashapp import app
application = app.server
