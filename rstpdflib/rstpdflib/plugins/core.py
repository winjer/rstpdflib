
from StringIO import StringIO
from rstpdflib.plugin import ProcessPluginBase

class CorePlugin(ProcessPluginBase):

    def prepare(self, conf, settings, stylesheet):
        core = conf['core']
        docoptions = []
        docoptions.append("%spt" % core['fontsize'])
        docoptions.append(core['papersize'])
        docoptions.append(core['sided'])
        docoptions.extend(core['docoptions'])
        settings['documentclass'] = core['documentclass']
        settings["documentoptions"] = ",".join(docoptions)
        if core.as_bool('section-numbering'):
            settings['section_numbering'] = True
        settings['use_latex_toc'] = True
        settings['use_latex_docinfo'] = True
        stylesheet.append(r"\usepackage{chngcntr}")
        #stylesheet.append(r"\counterwithout{figure}")
        #stylesheet.append(r"\counterwithout{figure}{chapter}")
        if 'titlepage' in core and core.as_bool('titlepage'):
            stylesheet.append(r"\titlepage")
        if core['ae']:
            stylesheet.append(r"\usepackage{ae,aecompl}")
        if core['parskip']:
            stylesheet.append(r"\usepackage{parskip}")
        if 'lhead' in core or 'rhead' in core:
            stylesheet.append(r"\usepackage[today,short,fancyhdr]{svninfo}")
        if 'tocdepth' in core:
            stylesheet.append(r"\setcounter{tocdepth}{%s}" % core['tocdepth'])
        if 'secnumdepth' in core:
            stylesheet.append(r"\setcounter{secnumdepth}{%s}" % core['secnumdepth'])
        if 'titlehead' in core:
            stylesheet.append(r"\titlehead{%s}" % core['titlehead'])
        if 'issuer' in core:
            stylesheet.append(r"\publishers{%s}" % r"\\".join(core['issuer']))
        if 'lhead' in core:
            stylesheet.append(r"\lhead{%s}" % core['lhead'])
        if 'rhead' in core:
            stylesheet.append(r"\rhead{%s}" % core['rhead'])
        return settings, stylesheet

    def preprocess(self, conf, stream):
        out = StringIO()
        self.svninfo = None
        for l in stream:
            out.write(l)
            if l.startswith('.. rst2pdf'):
                if conf['core'].as_bool('section-numbering'):
                    print >>out, ".. sectnum::"
                    print >>out, ".. contents::"
            if 'lhead' in conf['core'] or 'rhead' in conf['core']:
                if l.startswith(".. $Id"):
                    self.svninfo = l[3:]
        return StringIO(out.getvalue())

    def postprocess(self, conf, stream):
        out = StringIO()
        for l in stream:
            if self.svninfo:
                if l.startswith(r"\title"):
                    print >>out, "\svnInfo %s" % self.svninfo
            out.write(l)
        return StringIO(out.getvalue())

    def template(self, inconf, outconf):
        outconf['core'] = {}
        ic = inconf['core']
        oc = outconf['core']
        for term in ('parskip', 'tocdepth', 'secnumdepth', 'ae', 'fontsize', 'papersize', 'sided', 'docoptions', 'documentclass',
                     'lhead', 'rhead', 'section-numbering', 'font-encoding', 'use-latex-toc', 'use-latex-docinfo', 'issuer', 'titlepage',
                     'titlehead'):
            if term in ic:
                oc[term] = ic[term]
        if 'lhead' in ic:
            lhead = raw_input("Company name [%s]?\n" % ic['lhead'])
            oc['lhead'] = lhead if lhead else ic['lhead']
        if 'rhead' in ic:
            rhead = raw_input("Document name [%s]?\n" % ic['rhead'])
            oc['rhead'] = rhead if rhead else ic['rhead']
        if 'issuer' in ic:
            issuer = [x.strip() for x in raw_input("Issuer [%s]?\n" % ", ".join(ic['issuer'])).split(",")]
            oc['issuer'] = issuer if issuer[0] else ic['issuer']
        return outconf

