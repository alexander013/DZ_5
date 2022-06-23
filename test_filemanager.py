
import sys
import filemanager
import main
from filemanager import author_info
from filemanager import quit
from main import separator



def test_author_info():
    assert author_info() == 'Leonid Orlov'
def test_filemanager_author():
    assert filemanager.author_info() == 'Leonid Orlov'







