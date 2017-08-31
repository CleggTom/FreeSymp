# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to the FrEE Symposyum website")
    return dict(message=T('Welcome to the FrEE Symposyum website'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def display_your_form():
    update = db.register(request.args(0))
    form = SQLFORM(db.register, update)
    if form.accepts(request,session):
        session.flash = 'Thanks! Your data has been succesfully update' #session object redirects message to people page
        redirect(URL('presenters'))
    elif form.errors:
        response.flash = 'Please correct the error(s) in the form'
    
    return dict(form=form)


def schedule():
    db.schedule.id.readable=False
    grid = SQLFORM.grid(db.schedule,
                        csv=False,
                        deletable=False,
                        create=False,
                        details=False,
                        maxtextlength=50,
                        maxtextlengths={'schedule.Speaker':30,'schedule.Title':120,'schedule.Date':50},
                        formstyle="divs",
                        paginate=100,
                        editable=False)
    return dict(form=grid)
 

@auth.requires_login()
def all_records():
     grid = SQLFORM.grid(db.register,
			  csv=True,
              create=True,
              editable=True,
              deletable=True)
     return dict(form=grid)

def activities():
    return locals()

def program():
    return locals()

def sessions():
    return locals()
    
def presenters():
    return locals()
