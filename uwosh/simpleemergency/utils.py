from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from zope.component import getUtility

viewlet = "uwosh.simpleemergency"
manager = "plone.portaltop"


def get_viewlet(storage, skinname):
    # enable different viewlets to be registered
    # this is to support uwosh.emergency.*
    for vlet in storage.getOrder(manager, skinname):
        if vlet.startswith(viewlet):
            return vlet
            
    for vlet in storage.getHidden(manager, skinname):
        if vlet.startswith(viewlet):
            return vlet
    
def get_viewlet_info(context):
    storage = getUtility(IViewletSettingsStorage)
    skinname = context.getCurrentSkinName()
    hidden = storage.getHidden(manager, skinname)    
    return storage, skinname, hidden

def emergency_enabled(context):
    storage, skinname, hidden = get_viewlet_info(context)
    viewlet = get_viewlet(storage, skinname)
    return viewlet not in hidden
    
    
def disable_emergency(context):
    storage, skinname, hidden = get_viewlet_info(context)
    viewlet = get_viewlet(storage, skinname)
    hidden = hidden + (viewlet,)
    storage.setHidden(manager, skinname, hidden)
    
def enable_emergency(context):
    storage, skinname, hidden = get_viewlet_info(context)
    viewlet = get_viewlet(storage, skinname)
    hidden = tuple(x for x in hidden if x != viewlet)
    storage.setHidden(manager, skinname, hidden)
    