# -*- coding: utf-8 -*-
from mingtak.viewPermissions import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from zope import schema
from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form


class IViewPermissions(Form.Schema):

    view_name_list = schema.Text(
        title=_(u'View Name List'),
        description=_(u"JSON format, [(view_1, description_1), (view_2, description_2), ...]"),
        default=u"[]",
        required=True,
    )

    permissions_table = schema.Text(
        title=_(u'Permissions Table'),
        description=_(u"JSON format, {'view_1':['user_1', 'user_3',...], 'view_2':['user_2', 'user_5',...], ... }"),
        default=u"{}",
        required=True,
    )


class ViewPermissionsControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IViewPermissions

ViewPermissionsControlPanelView = layout.wrap_form(ViewPermissionsControlPanelForm, ControlPanelFormWrapper)
ViewPermissionsControlPanelView.label = _(u"BrowserView Permissions Control Table Related Setting")
