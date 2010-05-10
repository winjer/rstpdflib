import os
from rstpdflib import template

here = os.path.realpath(os.path.join(__file__, os.path.pardir))
template.templatedirs['rstpdflib.plugins.isotoma'] = os.path.join(here, "templates")

