#!/usr/bin/env python2
from . import State
from threading import Thread

class StateMachine(object):
    def __init__(self):
        self.state = None
        self.states = dict()
        self.worker = None

        self.debug = 0

    def __del__(self):
        if self.state:
            if self.worker:
                self.state.running = False
                self.worker.join()
                self.worker = None
            self.state.exit()

    def transition(self, state):
        if self.state:
            if self.worker:
                self.state.running = False
                self.worker.join()
                self.worker = None
            self.state.exit()

        if state in self.states:
            self.state = self.states[state]
        elif self.debug > 0:
            print('debug: {} has no state named "{state}"'.format(self.__name__, state))

        if self.state:
            self.state.entry()
            self.state.running = True
            self.worker = Thread(target=self.state.main)
            self.worker.start()

    def signal(self, signal):
        if self.state:
            return self.state.signal(signal)
