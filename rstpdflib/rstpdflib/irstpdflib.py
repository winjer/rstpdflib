from zope.interface import Interface

class IPlugin(Interface):
    """ A plugin to rstpdflib """

class IProcessPlugin(IPlugin):
    """ A plugin that processes a document """


