# -*- coding: utf-8 -*-
from plone import api
from sc.photogallery.config import PROJECTNAME

import logging


logger = logging.getLogger(PROJECTNAME)


def cook_css_resources(context):
    """Cook css resources."""
    css_tool = api.portal.get_tool('portal_css')
    css_tool.cookResources()
    logger.info('CSS resources were cooked')


def cook_javascript_resources(context):
    """Cook JS resources."""
    js_tool = api.portal.get_tool('portal_javascripts')
    js_tool.cookResources()
    logger.info('JS resources were cooked')
