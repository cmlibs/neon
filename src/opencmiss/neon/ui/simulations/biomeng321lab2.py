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

from opencmiss.neon.ui.simulations.base import BaseSimulationView
from opencmiss.neon.core.simulations.biomeng321lab2 import Biomeng321Lab2 as Biomeng321Lab2Simulation

from opencmiss.neon.ui.simulations.ui_biomeng321lab2 import Ui_Biomeng321Lab2
from opencmiss.neon.ui.misc.utils import set_wait_cursor
from opencmiss.neon.core.problems.biomeng321lab2 import BOUNDARY_CONDITIONS


class Biomeng321Lab2(BaseSimulationView):

    def __init__(self, parent=None):
        super(Biomeng321Lab2, self).__init__(parent)
        self._ui = Ui_Biomeng321Lab2()
        self._ui.setupUi(self)
        self._ui.groupBox_4.setVisible(False)

        self._map_name_ui = self._createNameUiMap()

        self._simulation = Biomeng321Lab2Simulation()

    def _createNameUiMap(self):
        map_name_ui = {}
        map_name_ui['Cauchy stress tensor (fibre coordinate system)'] = self._ui.tableWidgetCauchyStress
        map_name_ui['Deformation gradient tensor'] = self._ui.tableWidgetDeformationGradient
        map_name_ui['Green-Lagrange strain tensor (reference coordinate system)'] = self._ui.tableWidgetGreenLagrangeStrainReference
        map_name_ui['Green-Lagrange strain tensor (fibre coordinate system)'] = self._ui.tableWidgetGreenLagrangeStrainFibre
        map_name_ui['Right Cauchy-Green deformation tensor'] = self._ui.tableWidgetRightCauchyGreenDeformation
        map_name_ui['Second Piola-Kirchhoff stress tensor (reference coordinate system)'] = self._ui.tableWidgetSecondPiolaKirchoffStressReference
        map_name_ui['Second Piola-Kirchhoff stress tensor (fibre coordinate system)'] = self._ui.tableWidgetSecondPiolaKirchoffStressFibre

        return map_name_ui

    def _displayResults(self, r):
        self._ui.lineEditHydrostaticPressure.setText("{0:.4f}".format(r['Hydrostatic pressure']))
        self._ui.lineEditInvariant1.setText("{0:.4f}".format(r['Invariants'][0]))
        self._ui.lineEditInvariant2.setText("{0:.4f}".format(r['Invariants'][1]))
        self._ui.lineEditInvariant3.setText("{0:.4f}".format(r['Invariants'][2]))

        for key in self._map_name_ui:
            a = r[key]
            ui = self._map_name_ui[key]
            ui.setColumnCount(3)
            ui.setRowCount(3)
            for i in range(3):
                for j in range(3):
                    ui.setItem(i, j, QtGui.QTableWidgetItem("{0:.4f}".format(a[i][j])))

            ui.resizeColumnsToContents()
            ui.resizeRowsToContents()

    def setZincContext(self, context):
        self._ui.widgetSceneviewer.setContext(context)

    def setup(self):
        parameters = {}
        parameters['name'] = self._problem.getName()
        bc = self._problem.getBoundaryCondition()
        parameters['boundary_condition'] = BOUNDARY_CONDITIONS.index(bc) + 1 if bc else 1

        self._simulation.setParameters(parameters)
        self._simulation.setup()

    @set_wait_cursor
    def execute(self):
        r = self._simulation.execute()
        self._displayResults(r)

    def cleanup(self):
        self._simulation.cleanup()

    def validate(self):
        return True
