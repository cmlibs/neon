'''
   Copyright 2015 University of Auckland

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
from PySide import QtGui


class BaseSimulationView(QtGui.QWidget):

    def __init__(self, parent=None):
        super(BaseSimulationView, self).__init__(parent)
        self._problem = None
        self._preferences = None
        self._simulation = None

    def setProblem(self, problem):
        self._problem = problem

    def setPreferences(self, preferences):
        self._preferences = preferences

    def getSimulation(self):
        return self._simulation

    def run(self):
        self.setup()
        self.execute()
        self.cleanup()
