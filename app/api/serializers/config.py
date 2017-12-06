# -*- coding: utf-8 -*-

from flask_restplus import fields
from .. import api


config_minimal = api.model('Sensor Configuration', {
    'id': fields.String(required=True, description='Sensor unique id'),
    'pos_x': fields.Integer(required=True, description='Sensor X position'),
    'pos_y': fields.Integer(required=True, description='Sensor Y position'),
    'radius': fields.Integer(required=True, exclusiveMin=0, description='Sensor radius')
})
