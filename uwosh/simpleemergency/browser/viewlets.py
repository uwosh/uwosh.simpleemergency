from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter
from Products.CMFCore.utils import getToolByName
from DateTime import DateTime

class SimpleEmergencyViewlet(ViewletBase):
    render = ViewPageTemplateFile('simpleemergency.pt')

    def update(self):
        super(SimpleEmergencyViewlet, self).update()
        context_state = getMultiAdapter((self.context, self.request), name=u'plone_context_state')
        portal_props = getToolByName(self.context, 'portal_properties')
        props = portal_props.uwosh_simpleemergency_properties
        
        self.should_display = True
        
        if not props.getProperty('show_on_all_pages', False):
            #check if they only want it to be shown on the root of the site
            self.should_display = context_state.is_portal_root()
            
        if self.should_display:
            self.message = props.getProperty('emergency_message', '')
        
            last_updated = props.getProperty('last_updated', None)
            try:
                dt = DateTime(last_updated)
                self.last_updated = dt
                self.last_updated_formatted = dt.strftime('%I:%M%p %b %d, %Y')
            except DateTime.DateTimeError:
                self.last_updated = self.last_updated_formatted = last_updated