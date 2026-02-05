import sys
import os
import pytest

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from festival.bar import Bar
from festival.exceptions import BarValueError

def test_bar_draw():
    bar = Bar(current=45)
    assert bar.draw() == "Progress: [#############-----------------] 45.0%"
    bar = Bar(current=16)
    assert bar.draw() == "Progress: [####--------------------------] 16.0%"
    bar = Bar(current=45, prefix="Hi")
    assert bar.draw() == "Hi: [#############-----------------] 45.0%"

def test_bar_len():
    bar = Bar()
    assert len(bar) == 30
    bar = Bar(current=23)
    assert len(bar) == 23

def test_bar_eq():
    b1 = Bar(current=50)
    b2 = Bar(current=35)
    assert b1 == b2

def test_bar_compare():
    b1 = Bar(current=50)
    b2 = Bar(current=35)
    assert b1 > b2

def test_bar_repr():
    br = Bar(current=40)
    assert repr(br) == "Bar(current=40, total=100, prefix='Progress', width=30, fill_char='#', empty_char='-')"

def test_bar_error():
    with pytest.raises(BarValueError):
        be = Bar(current=-1)
        
