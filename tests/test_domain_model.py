#! python2
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

sys.dont_write_bytecode = True


import pytest

from domain_model import DomainModel, MemoryPersister

def test_domainModelSave():
    foo = DomainModel()
    persister = MemoryPersister()
    foo.addPersister(persister)
    foo.bar = 1
    foo.persist()
    foo.bar = 2
    foo.persist()
    foo.bar = 3
    foo.persist()
    assert persister.savedStates.pop().bar == 3
    assert persister.savedStates.pop().bar == 2
    assert persister.savedStates.pop().bar == 1
