
class Plugin(object):
    
    section = None
    
    def __init__(self, verbose=False):
        pass
    
    @classmethod
    def register(self, registry, **kw):
        registry.append(self(**kw))
        
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
