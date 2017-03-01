'''
Observer pattern lab
"Lab: Watching a File Change Size"
'''

import os
import time

class FileWatcher:
    def __init__(self, path_of_file_to_watch):
        self.path = path_of_file_to_watch
        self.observers = set()
        self._last_size = 0

    def register(self, observer):
        self.observers.add(observer)
    def unregister(self, observer):
        self.observers.discard(observer)

    def check_forever(self):
        while True:
            self.check_file()
            time.sleep(0.1)

    def check_file(self):
        size = os.stat(self.path).st_size
        if size != self._last_size:
            self._last_size = size
            self.dispatch(size)

    def dispatch(self, size):
        for observer in self.observers:
            observer.update(size)

class FileObserver:
    def __init__(self, name):
        self.name = name
    def update(self, size):
        print('{} noticed that the file is now {} bytes'.format(self.name, size))

bob = FileObserver('Bob')
john = FileObserver('John')
stacy = FileObserver('Stacy')

watcher = FileWatcher('watched.txt')
watcher.register(bob)
watcher.register(john)
watcher.register(stacy)

watcher.check_forever()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
