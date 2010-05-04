
import os
from configobj import ConfigObj
from rstpdflib import registry
import template

class DocumentConfig(object):
    
    def __init__(self, filename, tpt=None):
        self.document = filename
        if tpt is not None:
            self.conf = self.template(tpt)
        else:
            self.conf = self.read()
        self.setdefaults()
        
    def setdefaults(self):
        self.conf['DEFAULT'] = {}
        self.conf['DEFAULT']['templatedir'] = template.templatedir

    @property
    def filename(self):
        if self.document.endswith(".rst") or self.document.endswith(".txt"):
            filename = self.document[:-4] + ".ini"
        else:
            filename = self.document + ".ini"
        return filename

    def write(self):
        del self.conf['DEFAULT']
        self.conf.write(open(self.filename, "w"))
        self.setdefaults()
        
    def _read(self, filename):
        return ConfigObj(open(filename, "r"), interpolation="template")

    def read(self):
        if os.path.exists(self.filename):
            return self._read(self.filename)
        else:
            raise IOError("No configuration file found, you should initialise this document first")
        
    def template(self, template):
        conf = ConfigObj(interpolation="template")
        for plugin in registry.registry:
            plugin.template(template.conf, conf)
        return conf
