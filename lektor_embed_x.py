# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from embedx import OnlineContent

embedx_marker = '#!#'

EMBED_FAILED_SCRIPT = 
'''<div class="embedx-notsupported"><p><a href="%(URL)s">%(URL)s</a></p></div>'''

class EmbedXMixin(object):

    def paragraph(self, text):
        if not strip(text).startswith(embedx_marker):
            return super(EmbedXMixin, self).paragraph(text)
        content_url = strip(strip(text)[3:])
        
        try:
            content = OnlineContent(content_url)
            return Markup(content.get_embed_code())
        except NotImplementedError:
            # should emit this msg when generating
            print 'The hosting site or the specific content is not supported yet'
            # failed to generate embeddable code, so returning plain URL
            return Markup(EMBED_FAILED_SCRIPT % {'URL': content_url})
            

class EmbedXPlugin(Plugin):
    name = u'lektor-embed-x'
    description = u'Embed rich content from popular sites in Lektor-generated pages'

#   def on_process_template_context(self, context, **extra):
#       def test_function():
#           return 'Value from plugin %s' % self.name
#       context['test_function'] = test_function
    
    
    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(EmbedXMixin)
