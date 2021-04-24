import pytest
from app.controllers.hello import *

def test_hello():
    hello = Hello()
    assert hello.get() == {"message": "hello!"}