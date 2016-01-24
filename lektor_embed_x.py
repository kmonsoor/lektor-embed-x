# -*- coding: utf-8 -*-
"""
    lektor-embed-x
    ~~~~~~~~~~~~~~
    Simply embed rich contents from popular sites in Lektor-generated pages
    :copyright: (c) 2016 by Khaled Monsoor
    :license: The MIT License
"""

from embedx import OnlineContent
from lektor.pluginsystem import Plugin
from markupsafe import Markup

__version__ = '0.1.2'
__author__ = 'Khaled Monsoor <k@kmonsoor.com>'


class EmbedXMixin(object):
    def autolink(self, link, is_email):
        if is_email:
            return super(EmbedXMixin, self).autolink(link, True)
        else:
            try:
                content = OnlineContent(link)
                # print content.get_embed_code()
                return Markup(content.get_embed_code())
            except (NotImplementedError, ValueError):
                print 'This host or this specific content is not supported yet. link: {0}'.format(link)
                return super(EmbedXMixin, self).autolink(link, False)


class EmbedXPlugin(Plugin):
    name = u'lektor-embed-x'
    description = u'Simply embed rich content from popular sites in Lektor-generated pages'

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(EmbedXMixin)
