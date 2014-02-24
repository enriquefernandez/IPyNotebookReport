
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from __future__ import print_function, absolute_import
import os
from IPython.nbconvert.preprocessors.base import Preprocessor

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

class EfernanPreprocessor(Preprocessor):
    
    def preprocess(self, nb, resources):
        
        # Global notebook metadata
        # print ("Global notebook metadata:")
        # for element in resources['metadata']:
        #     print(str(element)+" : "+ resources['metadata'][element])

        # Individual Cell Metadata
        print ("Global individual cell metadata:")
        for worksheet in nb.worksheets:
            remove_cells = []
            for index, cell in enumerate(worksheet.cells):
                if 'homeworkReport' in cell.metadata and 'showCell' in cell.metadata['homeworkReport']:
                    if cell.metadata['homeworkReport']['showCell'] == 'nothing':
                        # Mark cell for removal
                        remove_cells.append(index)

                # if len(cell.metadata)>0:
                #     print("Cell {} metadata:".format(index))
                #     for element in cell.metadata:
                #         print(str(element) + ":" + str(cell.metadata[element]))
            # Remove cells tagged for removal
            for index in remove_cells[::-1]:
                del worksheet.cells[index]
            print('{} cells removed from worksheet.'.format(len(remove_cells)))

        # resources["enrique"]["author"] = "Enrique PY"
        return nb, resources 
