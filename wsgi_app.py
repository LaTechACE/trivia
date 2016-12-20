#-*- coding: utf-8 -*-
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

activate_this = os.path.join(dir_path,'venv-trivia/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, dir_path)

from trivia import app as application
