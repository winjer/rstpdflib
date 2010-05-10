
import config
import codecs
from docutils.core import publish_file
from StringIO import StringIO
import subprocess
import tempfile
from twisted.plugin import getPlugins
from irstpdflib import IProcessPlugin
import plugins

class Writer(object):

    def __init__(self, document):
        self.document = document

    @property
    def texname(self):
        if self.document.endswith(".rst") or self.document.endswith(".txt"):
            return self.document[:-4] + ".tex"
        return self.document + ".tex"

    def write(self):
        settings = {}
        stylesheet = []
        conf = config.DocumentConfig(self.document)
        for p in getPlugins(IProcessPlugin, plugins):
            p.prepare(conf.conf, settings, stylesheet)
        tmp = tempfile.mktemp()
        open(tmp, "w").write("\n".join(stylesheet))
        settings['stylesheet'] = tmp
        data = codecs.open(self.document, encoding="UTF-8").read()
        strm = StringIO(data.encode("iso-8859-15"))
        for p in getPlugins(IProcessPlugin, plugins):
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", p
            strm = p.preprocess(conf.conf, strm)
        latex = publish_file(strm, writer_name="latex", settings_overrides=settings)
        strm = StringIO(latex)
        for p in getPlugins(IProcessPlugin, plugins):
            strm = p.postprocess(conf.conf, strm)
        open(self.texname, "w").write(strm.read())
        status = subprocess.call("pdflatex %s" % self.texname, shell=True)
        if status == 0:
            status = subprocess.call("pdflatex %s" % self.texname, shell=True)
        if status == 0:
            status = subprocess.call("pdflatex %s" % self.texname, shell=True)


