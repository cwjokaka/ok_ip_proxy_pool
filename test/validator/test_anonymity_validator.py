import unittest

from src.database.sqlite_opt import sqlite_opt
from src.validator.anonymity_validator import anonymity_validator


class TestAnonymityValidator(unittest.TestCase):

    def setUp(self) -> None:
        self._opt = sqlite_opt
        self._validator = anonymity_validator

        # self._opt.clean()

    def test_valid_proxy(self):
        self._validator.run()
        pass

