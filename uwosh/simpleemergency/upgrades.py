from Products.CMFCore.utils import getToolByName
from DateTime import DateTime

default_profile = 'profile-uwosh.simpleemergency:default'

def upgrade_to_1_0_1(context):
    """ perform upgrade to 0.7rc2 -- Some important changes. """
    portal_catalog = getToolByName(context, 'portal_catalog')
    portal_props = getToolByName(context, 'portal_properties')
    props = portal_props.uwosh_simpleemergency_properties
    last_updated = props.getProperty('last_updated')
    
    if not last_updated:
        return
    
    # old non-standard date storage was in the form of `01:07pm Apr 26, 2010`
    time, month, day, year = last_updated.split(' ')
    
    # datetime will take dates in the form of `Mar 9, 1997 01:07pm`
    dt = DateTime("%s %s %s %s" % (month, day, year, time))
    props.last_updated = dt.pCommonZ()


def upgrade_to_1_1(context):
    context.runImportStepFromProfile(default_profile, 'propertiestool')