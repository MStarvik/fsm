#!/usr/bin/env python2
from . import State

class StateMachine(object):
    def __init__(self):
        self.state = None
        self.states = dict()

        self.debug = 0

    def __del__(self):
        if self.state:
            self.state.exit()

    def transition(self, state):
        if self.state:
            self.state.exit()

        if state in self.states:
            self.state = self.states[state]
        elif self.debug > 0:
            print('debug: {} has no state named "{state}"'.format(self.__name__, state))

        if self.state:
            self.state.entry()

    def signal(self, signal):
        if self.state:
            self.state.signal(signal)