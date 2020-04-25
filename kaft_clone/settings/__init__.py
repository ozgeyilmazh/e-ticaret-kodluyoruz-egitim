from .settings_base import *

if  DEBUG:
    from .settings_dev import *

else:
    from .setting_server import *