import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import festival.version as v

def test_version():
    assert type(v.__version__) == str

def test_license():
    assert v.__license__ == "MIT"

def test_author():
    assert v.__author__ == "aiwonderland"

def test_copyright():
    assert v.__copyright__ == "(C) 2026 aiwonderland and festival team"

def test_description():
    assert v.__description__ == "fun and enjoyment of terminal output"

def test_email():
    assert v.__email__ == "quantbit@126.com"

def test_url():
    assert v.__url__ == "https://github.com/aiwonderland/festival"