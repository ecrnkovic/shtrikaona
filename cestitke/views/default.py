from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError

from ..models.meta import Session
from ..models.ecard import Ecard


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    ecards = Session.query(Ecard).filter(
        Ecard.deleted == False,
        Ecard.public == 1).order_by(Ecard.last_change_date.desc()).all()
    return {"ecards": ecards}




