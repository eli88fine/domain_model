#! python2
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

sys.dont_write_bytecode = True

import copy

class DomainModel(object):
    def __init__(self):
        self.persisters = []

    def addPersister(self, persister):
        self.persisters.append(persister)

    def persist(self):
        for p in self.persisters:
            p.persist(self)

class Persister(object):
    def persist(self, thing):
        raise NotImplementedError

class SingleObjectCreationPersister(Persister):
    _isNew = False

    def createObject(self):
        obj = self.createBaseObject()
        obj.addPersister(self)
        return obj

    def createBaseObject(self):
        raise NotImplementedError

    @classmethod
    def createNewObject(cls):
        newPersister = cls()
        newPersister._isNew = True
        newObject = newPersister.createObject()
        return newObject


class CreationPersister(SingleObjectCreationPersister):

    @classmethod
    def createAllObjects(cls):
        persisters = cls.createAllPersisters()
        objects = []
        for p in persisters:
            objects.append(p.createObject())
        return objects

    @classmethod
    def createAllPersisters(cls):
        raise NotImplementedError


class PeeweeCreationPersister(CreationPersister):
    @classmethod
    def createAllPersisters(cls):
        return cls.select()

    def persist(self, toSave):
        if not self._isNew:
            self.saveOptimistic()
        else:
            self.save(force_insert=True)
            self._isNew = False

class MemoryPersister(Persister):
    def __init__(self):
        self.savedStates = list()

    def persist(self, thing):
        print('Saving %s!' % thing)
        self.savedStates.append(copy.deepcopy(thing))
        print(self.savedStates)

