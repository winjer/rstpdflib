from zope.interface import classProvides

from irstpdflib import IProcessPlugin

class ProcessPluginBase(object):

    classProvides(IProcessPlugin)


    section = None

    def __init__(self, verbose=False):
        pass

    def prepare(self, conf, settings, stylesheet):
        return settings, stylesheet

    def preprocess(self, conf, stream):
        return stream

    def postprocess(self, conf, stream):
        return stream

    def template(self, inconf, outconf):
        if self.section is not None:
            outconf[section] = {}
            outconf[section].update(inconf[section])
