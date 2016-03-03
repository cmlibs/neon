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
from opencmiss.neon.core.visualisations.base import BaseVisualisation


class Ventilation(BaseVisualisation):

    def __init__(self):
        super(Ventilation, self).__init__()
        self.setName('Ventilation Visualisation')

    def visualise(self, document):
        filenames = self._simulation.getOutputFilenames()
        visualisation_description = default_visualisation
        visualisation_description['RootRegion']['Model']['Sources'][0]['FileName'] = filenames['tree_exnode']
        visualisation_description['RootRegion']['Model']['Sources'][1]['FileName'] = filenames['tree_exelem']
        visualisation_description['RootRegion']['Model']['Sources'][2]['FileName'] = filenames['terminal_exnode']
        visualisation_description['RootRegion']['Model']['Sources'][3]['FileName'] = filenames['radius_exelem']
#         visualisation_description['RootRegion']['Model']['Sources'][4]['FileName'] = filenames['ventilation_exelem']
        document.deserialize(default_visualisation)


default_visualisation = {
  "OpenCMISS-Neon Version": [
    0,
    1,
    0
  ],
  "RootRegion": {
    "Model": {
      "Sources": [
        {
          "FileName": "../../tmp/ventilation_tree.exnode",
          "Type": "FILE"
        },
        {
          "FileName": "../../tmp/ventilation_tree.exelem",
          "Type": "FILE"
        },
        {
          "FileName": "../../tmp/ventilation_terminal.exnode",
          "Type": "FILE"
        },
        {
          "FileName": "../../tmp/ventilation_radius.exelem",
          "Type": "FILE"
        },
#         {
#           "FileName": "../../tmp/ventilation_ventilation.exelem",
#           "Type": "FILE"
#         }
      ]
    },
    "Scene": {
      "Graphics": [
        {
          "CoordinateField": "coordinates",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "MESH1D",
          "LineAttributes": {
            "BaseSize": [
              0,
              0
            ],
            "OrientationScaleField": "radius",
            "ScaleFactors": [
              2,
              2
            ],
            "ShapeType": "CIRCLE_EXTRUSION"
          },
          "Lines": {},
          "Material": "default",
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "Scenecoordinatesystem": "LOCAL",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Tessellation": "default",
          "Type": "LINES",
          "VisibilityFlag": True
        },
        {
          "CoordinateField": "coordinates",
          "DataField": "pleural pressure",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "NODES",
          "Material": "default",
          "PointAttributes": {
            "BaseSize": [
              4,
              4,
              4
            ],
            "Font": "default",
            "Glyph": "sphere",
            "GlyphOffset": [
              0,
              0,
              0
            ],
            "GlyphRepeatMode": "NONE",
            "GlyphShapeType": "SPHERE",
            "LabelOffset": [
              0,
              0,
              0
            ],
            "LabelText": [
              "",
              "",
              ""
            ],
            "ScaleFactors": [
              1,
              1,
              1
            ]
          },
          "Points": {},
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "SamplingAttributes": {
            "ElementPointSamplingMode": "CELL_CENTRES",
            "Location": [
              0,
              0,
              0
            ]
          },
          "Scenecoordinatesystem": "LOCAL",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Spectrum": "default",
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        }
      ],
      "VisibilityFlag": True
    }
  },
  "Spectrums": {
    "DefaultSpectrum": "default",
    "Spectrums": [
      {
        "Components": [
          {
            "Active": True,
            "BandedRatio": 0.2,
            "ColourMappingType": "RAINBOW",
            "ColourMaximum": 1,
            "ColourMinimum": 0,
            "ColourReverse": True,
            "Exaggeration": 1,
            "ExtendAbove": True,
            "ExtendBelow": True,
            "FieldComponent": 1,
            "NumberOfBands": 10,
            "RangeMaximum": 1033.377319335938,
            "RangeMinimum": 266.9163513183594,
            "ScaleType": "LINEAR",
            "StepValue": 650.1468353271484
          }
        ],
        "MaterialOverwrite": True,
        "Name": "default"
      }
    ]
  },
  "Tessellations": {
    "DefaultPointsTessellation": "default_points",
    "DefaultTessellation": "default",
    "Tessellations": [
      {
        "CircleDivisions": 12,
        "MinimumDivisions": [
          1
        ],
        "Name": "default",
        "RefinementFactors": [
          4
        ]
      },
      {
        "CircleDivisions": 12,
        "MinimumDivisions": [
          1
        ],
        "Name": "default_points",
        "RefinementFactors": [
          1
        ]
      }
    ]
  }
}


default_visualisation_init = {
  "OpenCMISS-Neon Version": [
    0,
    1,
    0
  ],
  "RootRegion": {
    "Model": {
      "Sources": [
        {
          "FileName": "/tmp/ventilation_out_KQZe9U.exnode",
          "Type": "FILE"
        }
      ]
    },
    "Scene": {
      "Graphics": [
        {
          "CoordinateField": "coordinates",
          "DataField": "flow",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "NODES",
          "Material": "default",
          "PointAttributes": {
            "BaseSize": [
              2,
              2,
              2
            ],
            "Font": "default",
            "Glyph": "sphere",
            "GlyphOffset": [
              0,
              0,
              0
            ],
            "GlyphRepeatMode": "NONE",
            "GlyphShapeType": "SPHERE",
            "LabelOffset": [
              0,
              0,
              0
            ],
            "LabelText": [
              "",
              "",
              ""
            ],
            "ScaleFactors": [
              1,
              1,
              1
            ]
          },
          "Points": {},
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "SamplingAttributes": {
            "ElementPointSamplingMode": "CELL_CENTRES",
            "Location": [
              0,
              0,
              0
            ]
          },
          "Scenecoordinatesystem": "LOCAL",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Spectrum": "default",
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        }
      ],
      "VisibilityFlag": True
    }
  },
  "Spectrums": {
    "DefaultSpectrum": "default",
    "Spectrums": [
      {
        "Components": [
          {
            "Active": True,
            "BandedRatio": 0.2,
            "ColourMappingType": "RAINBOW",
            "ColourMaximum": 1,
            "ColourMinimum": 0,
            "ColourReverse": True,
            "Exaggeration": 1,
            "ExtendAbove": True,
            "ExtendBelow": True,
            "FieldComponent": 1,
            "NumberOfBands": 10,
            "RangeMaximum": 0,
            "RangeMinimum": 0,
            "ScaleType": "LINEAR",
            "StepValue": 0
          }
        ],
        "MaterialOverwrite": True,
        "Name": "default"
      }
    ]
  },
  "Tessellations": {
    "DefaultPointsTessellation": "default_points",
    "DefaultTessellation": "default",
    "Tessellations": [
      {
        "CircleDivisions": 12,
        "MinimumDivisions": [
          1
        ],
        "Name": "default",
        "RefinementFactors": [
          4
        ]
      },
      {
        "CircleDivisions": 12,
        "MinimumDivisions": [
          1
        ],
        "Name": "default_points",
        "RefinementFactors": [
          1
        ]
      }
    ]
  }
}
