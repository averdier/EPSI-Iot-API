# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restplus import Api


authorizations = {
    'basicAuth': {
        'type': 'basic',
        'in': 'header'
    }
}

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint,
          title='EPSI Iot API',
          version='0.1',
          description='EPSI Iot API',
          authorizations=authorizations,
          security='basicAuth'
          )

from .endpoints.config import ns as config_namespace

api.add_namespace(config_namespace)