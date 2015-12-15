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

from opencmiss.neon.ui.views.base import BaseView

from opencmiss.neon.ui.views.ui_problemview import Ui_ProblemView


class ProblemView(BaseView):

    def __init__(self, parent=None):
        super(ProblemView, self).__init__(parent)
        self._name = 'Problem'

        self._ui = Ui_ProblemView()
        self._ui.setupUi(self)

        self._makeConnections()

    def _makeConnections(self):
        pass

    def setContext(self, context):
        pass