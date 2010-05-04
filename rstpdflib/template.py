
from configobj import ConfigObj

import os

templatedir = os.path.join(os.path.dirname(__file__), "templates")

class Template(object):
    
    def __init__(self, filename):
        if not os.path.exists(filename):
            raise KeyError("%s does not exist" % filename)
        self.name = os.path.basename(filename)[:-4]
        self.filename = filename
        self.conf = ConfigObj(filename)
        
    def __str__(self):
        return "%s (%s)" % (self.name, self.conf['template']['description'])

class Templates(object):
    
    def __init__(self):
        pass
        
    @property
    def templates(self):
        for f in os.listdir(templatedir):
            if not f.endswith(".ini"):
                continue
            pathname = os.path.join(templatedir, f)
            yield Template(pathname)

    def template(self, name):
        pathname = os.path.join(templatedir, name + ".ini")
        return Template(pathname)