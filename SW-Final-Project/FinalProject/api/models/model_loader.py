from api.dependencies.database import Base, engine

from api.models import customer
from api.models import menu
from api.models import orders
from api.models import order_details
from api.models import promotion
from api.models import recipes
from api.models import resource
from api.models import review
from api.models import sandwiches

def index():
    Base.metadata.create_all(bind=engine)