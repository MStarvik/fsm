#!/usr/bin/env python2
from weakref import proxy

class State(object):
    def __init__(self, state_machine):
        self.state_machine = proxy(state_machine);

        self.signals = dict()

        self.debug = 0

    def entry(self):
        pass

    def exit(self):
        pass

    def transition(self, state):
        if self.state_machine:
            self.state_machine.transition(state)
        elif self.debug > 0:
            print("debug: {} has no state machine".format(self.__name__))

    def signal(self, signal):
        if signal in self.signals:
            return self.signals[signal]()
        elif self.debug > 2:
            print("debug: {} has no signal named {}".format(self.__name__, signal))