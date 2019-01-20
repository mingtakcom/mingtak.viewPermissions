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

    def checkPermission(self, userId, viewName):
        permissions_table = api.portal.get_registry_record('mingtak.viewPermissions.browser.configlet.IViewPermissions.permissions_table')
        permissions_table = json.loads(permissions_table)
        userList = permissions_table.get(viewName, [])
        if userId in userList:
            return True
        else:
            return False


    def updatePermissionsTable(self):

        request = self.request
        permissions_table = {}

        for key in request.form.keys():
            if '--' not in key:
                continue
            viewName, userId = key.split('--')
            if not permissions_table.has_key(viewName):
                permissions_table[viewName] = [userId]
            else:
                permissions_table[viewName].append(userId)

        api.portal.set_registry_record('mingtak.viewPermissions.browser.configlet.IViewPermissions.permissions_table',
                                       safe_unicode(json.dumps(permissions_table)),
        )


    def __call__(self):

        request = self.request

        if request.has_key('submit'):
            self.updatePermissionsTable()
            api.portal.show_message(message=_(u'Permissions Table Already Update.'), request=request)

        self.view_name_list = api.portal.get_registry_record('mingtak.viewPermissions.browser.configlet.IViewPermissions.view_name_list')
        self.view_name_list = json.loads(self.view_name_list)
        self.users = api.user.get_users()

        return self.template()
