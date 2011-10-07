"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'reseaugrappe.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            _('Base de donnees'),
            collapsible=False,
            column=1,
            exclude=('django.contrib.*',),
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Le GRAPPE !'),
            column=2,
            children=[
                {
                    'title': _('Forums du GRAPPE'),
                    'url': 'http://forums.reseaugrappe.org/',
                    'external': True,
                },
                {
                    'title': _('Wiki du GRAPPE'),
                    'url': 'http://wiki.reseaugrappe.org/',
                    'external': True,
                },
                {
                    'title': _('Reseau GRAPPE'),
                    'url': 'http://www.reseaugrappe.org',
                    'external': True,
                },
            ]
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


