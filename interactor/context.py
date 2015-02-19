#!/usr/bin/env python

# standard library imports

# third party related imports

# local library imports


class Context(object):

    @classmethod
    def build(cls, **context):

        return cls(**context)

    def __init__(self, **context):

        map(lambda key: setattr(self, key, context[key]), context)
