Introduction
============


This package is a Plone product that enables you to provide a simple emergency message to a Plone site.

It provides mechanisms for WYSIWYG editing of the emergency message and it allows the manager to display 
the message only on the front page or on all pages.


Why
===

Because we need to be able to display emergency messages to our users.

How
===

Go into the site setup and click on the `Emergency Config` button or just append `uwosh.simpleemergency.configuration` 
onto the portal url. Then enter the emergency message and enable it.


Upgrading
=========

to 1.0*
-------

Run the upgrade step to 1.0.1 to convert times over to the better format



Uninstall
---------

To uninstall deactivate the product in the plone control panel and also run the import step `Simple Emergency Uninstall Profile` in the zmi -> portal_setup -> Import tab.


Compatibility
-------------

Plone 3 and 4