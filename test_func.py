import sys
import filemanager
import main
from filemanager import author_info
from filemanager import quit
from main import separator





assert author_info() == 'Leonid Orlov'
assert filemanager.author_info() == 'Leonid Orlov'

assert quit() == sys.exit(0)