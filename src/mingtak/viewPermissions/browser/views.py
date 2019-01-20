# -*- coding: utf-8 -*-
from mingtak.viewPermissions import _
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from Products.CMFPlone.utils import safe_unicode

from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

import json
import logging

logger = logging.getLogger("mingtak.viewPermissions")


class PermissionsTableView(BrowserView):

    template = ViewPageTemplateFile("template/permissions_table_view.pt")

    def __call__(self):


        self.view_name_list = api.portal.get_registry_record('mingtak.viewPermissions.browser.configlet.IViewPermissions.view_name_list')
        self.view_name_list = json.loads(self.view_name_list)
        self.users = api.user.get_users()

        return self.template()
