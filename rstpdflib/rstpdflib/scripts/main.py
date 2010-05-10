import sys
import optparse

from rstpdflib import config
from rstpdflib import writer
from rstpdflib import template

def run():
    parser = optparse.OptionParser(usage="%prog [options] filename")

    parser.add_option("-l", "--list-templates", action="store_true", help="list available templates", dest="listTemplates")
    parser.add_option("-i", "--init", action="store", dest="template", help="initialise a new document")

    (opts, args) = parser.parse_args()

    if opts.listTemplates:
        print "Templates:"
        templates = template.Templates()
        for t in templates.templates:
            print "    %s" % t
        raise SystemExit

    if len(args) != 1:
        parser.print_help()
        raise SystemExit

    doc = args[0]

    if opts.template:
        tpt = template.Templates().template(opts.template)
        conf = config.DocumentConfig(doc, tpt)
        conf.write()
    else:
        w = writer.Writer(doc)
        w.write()
