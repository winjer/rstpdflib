
import os
from rstpdflib import plugins

class PluginRegistry(list):
    
    def __init__(self, **kw):
        plugdir = os.path.dirname(plugins.__file__)
        for i in os.listdir(plugdir):
            if i == '__init__.py':
                continue
            if i.endswith(".py"):
                modpath = "rstpdflib.plugins.%s" % i[:-3]
                mod = __import__(modpath, {}, {}, ['not empty'])
                mod.register(self, **kw)



registry = PluginRegistry()
