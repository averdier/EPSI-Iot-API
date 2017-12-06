# -*- coding: utf-8 -*-

from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app
from elasticsearch_dsl import DocType, Date, Text, Integer
from .utils import hash_sha256

class MyDocType(DocType):
    created_at = Date()
    updated_at = Date()

    def to_dict(self, include_id=False, include_meta=False):
        base = super().to_dict(include_meta)

        if include_id and not include_meta:
            base['id'] = self.meta.id

        return base

    def save(self, **kwargs):
        self.created_at = datetime.utcnow()
        return super().save(**kwargs)

    def update(self, using=None, index=None, **fields):
        self.updated_at = datetime.utcnow()
        return super().update(using, index, **fields)


class Sensor(MyDocType):
    pos_x = Integer()
    pos_y = Integer()
    radius = Integer()
    mqtt_token = Text()
    key = Text()

    class Meta:
        index = 'bluetooth'

    def verify_key(self, key):
        return self.key == hash_sha256(key)