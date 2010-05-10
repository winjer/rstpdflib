
import os
import subprocess
from rstpdflib.plugin import Plugin
from StringIO import StringIO

class Images(Plugin):
    
    def make(self, filename):
        if filename.endswith(".pdf"):
            basename = filename[:-4]
            if os.path.exists(basename + ".svg"):
                command = "inkscape --export-pdf=%s %s" %(filename, basename + ".svg")
                print command
                subprocess.call(command, shell=True)
    
    def preprocess(self, conf, stream):
        out = StringIO()
        for l in stream:
            out.write(l)
            if l.startswith(".. figure::"):
                filename = l.strip()[12:]
                self.make(filename)
        return StringIO(out.getvalue())

register = Images.register
