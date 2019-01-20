# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from mingtak.viewPermissions.testing import MINGTAK_VIEWPERMISSIONS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that mingtak.viewPermissions is properly installed."""

    layer = MINGTAK_VIEWPERMISSIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if mingtak.viewPermissions is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'mingtak.viewPermissions'))

    def test_browserlayer(self):
        """Test that IMingtakViewpermissionsLayer is registered."""
        from mingtak.viewPermissions.interfaces import (
            IMingtakViewpermissionsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IMingtakViewpermissionsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MINGTAK_VIEWPERMISSIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['mingtak.viewPermissions'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if mingtak.viewPermissions is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'mingtak.viewPermissions'))

    def test_browserlayer_removed(self):
        """Test that IMingtakViewpermissionsLayer is removed."""
        from mingtak.viewPermissions.interfaces import \
            IMingtakViewpermissionsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IMingtakViewpermissionsLayer,
            utils.registered_layers())
