from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='uwosh.simpleemergency',
      version=version,
      description="This product creates a viewlet that can be configured to show emergency noticiations",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Nathan Van Gheem',
      author_email='vangheem@gmail.com',
      url='https://svn.it.uwosh.edu/svn/plone/Projects/uwosh.simpleemergency/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      
      [zc.buildout]
      default = uwosh.simpleemergency.recipe:Recipe
      
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
