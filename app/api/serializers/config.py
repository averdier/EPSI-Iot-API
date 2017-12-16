# -*- coding: utf-8 -*-

from flask_restplus import fields
from .. import api

mqtt_account = api.model('MQTT account', {
    'username': fields.String(required=True, description='MQTT username'),
    'password': fields.String(required=True, description='MQTT password'),
    'server': fields.String(required=True, description='MQTT server address'),
    'port': fields.Integer(required=True, description='MQTT server port'),
    'keep_alive': fields.Integer(required=True, description='MQTT keep alive'),
    'clients_topic': fields.String(required=True, description='Clients topic'),
    'device_topic': fields.String(required=True, description='Device topic')
})

config_minimal = api.model('Sensor Configuration', {
    'id': fields.String(required=True, description='Sensor unique id'),
    'pos_x': fields.Integer(required=True, description='Sensor X position'),
    'pos_y': fields.Integer(required=True, description='Sensor Y position'),
    'radius': fields.Integer(required=True, exclusiveMin=0, description='Sensor radius'),
    'mqtt_account': fields.Nested(mqtt_account, required=True, description='Mqtt account')
})
