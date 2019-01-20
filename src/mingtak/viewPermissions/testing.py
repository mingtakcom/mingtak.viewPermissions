# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mingtak.viewPermissions


class MingtakViewpermissionsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=mingtak.viewPermissions)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mingtak.viewPermissions:default')


MINGTAK_VIEWPERMISSIONS_FIXTURE = MingtakViewpermissionsLayer()


MINGTAK_VIEWPERMISSIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MINGTAK_VIEWPERMISSIONS_FIXTURE,),
    name='MingtakViewpermissionsLayer:IntegrationTesting',
)


MINGTAK_VIEWPERMISSIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MINGTAK_VIEWPERMISSIONS_FIXTURE,),
    name='MingtakViewpermissionsLayer:FunctionalTesting',
)


MINGTAK_VIEWPERMISSIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MINGTAK_VIEWPERMISSIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MingtakViewpermissionsLayer:AcceptanceTesting',
)
