#!/usr/bin/env python

__version__ = '0.1.1'

# standard library imports

# third party related imports

# local library imports
from context import Context


class Interactor(object):

    @classmethod
    def call(cls, **context):

        instance = cls(**context)
        instance.run()
        return instance.context

    def __init__(self, **context):

        self.context = Context.build(**context)

    def run(self):

        raise NotImplementedError()
