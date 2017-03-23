# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

# response.logo = A(B('PawaLab'),XML('&nbsp;'),
                  # _class="navbar-brand",
                  # _id="PawaLab-logo")
# response.logo = IMG(_src=URL('static','images/imperial_white.png'), _height='70px')

response.title = 'FrEE Symposium 2017'
response.subtitle = A('Frontiers in Ecology & Evolution 4-7 September', _style="color: white;")
    
## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Sofia Sal <soflysb@gmail.com>'
response.meta.description = 'FrEE Symposium website'
response.meta.keywords = 'Conservation, Ecology, Evolution, Symposyum'
# response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################
# app = request.application

response.menu = [
    (T('HOME'), False, URL('default', 'index'), []),
    (T('REGISTRATION'), False, URL('display_your_form'), []),
    (T('ACTIVITIES'), False, URL('activities'), []),
    (T('PROGRAM & AGENDA'), False, 'program'),
    (T('FOR PRESENTERS'), False, URL('presenters'), []),
    (T('ORGANIZATION'), False, '#', [
       (T('Presenters'), False,URL('all_records'), [])
        ])
]
