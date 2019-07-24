from crate.theme.rtd.conf.standalone import *

# crate.theme sets html_favicon to favicon.png which causes a warning because
# it should be a .ico and in addition there is no favicon.png in this project
# so it can't find the file
html_favicon = None

source_suffix = '.rst'

exclude_patterns = ['.*', '*.lint']

master_doc = 'index'

site_url = 'https://crate.io/docs/cloud/getting-started/en/latest/'

extensions = ['sphinx_sitemap']

