from mockito import mock, verify

import unittest

from src.main.python.main_start import EsparkWorld


class HelloWorldTest(unittest.TestCase):

    def test_should_issue_hello_world_message(self):
        out = mock()
        espark_world = EsparkWorld()
        espark_world.helloworld(out)
        verify(out).write("Hello world of Python\n")

