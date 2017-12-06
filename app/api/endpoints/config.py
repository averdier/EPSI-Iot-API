# -*- coding: utf-8 -*-

from flask import g
from flask_restplus import Namespace, Resource
from flask_httpauth import HTTPBasicAuth
from ..serializers.config import config_minimal
from app.models import Sensor

ns = Namespace('config', description='Configuration related operations')


# ================================================================================================
# AUTH
# ================================================================================================
#
#   Auth verification
#
# ================================================================================================

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """
    Verify Sensor authorization

    :param username: Sensor ID
    :type username: str

    :param password: Sensor Key
    :type password: str

    :return: True if sensor can connect, else False
    :rtype: bool
    """

    sensor = Sensor.get(id=username, ignore=404)

    if sensor is None or not sensor.verify_key(password):
        return False

    g.sensor = sensor
    return True


# ================================================================================================
# ENDPOINTS
# ================================================================================================
#
#   API config endpoints
#
# ================================================================================================


@ns.route('/')
class ConfigItem(Resource):
    decorators = [auth.login_required]

    @ns.doc(security='basicAuth')
    @ns.marshal_with(config_minimal)
    def get(self):
        """
        Return auth token
        """

        return g.sensor.to_dict(include_id=True)