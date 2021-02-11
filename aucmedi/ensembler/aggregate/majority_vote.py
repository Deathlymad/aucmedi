#==============================================================================#
#  Author:       Dominik Müller                                                #
#  Copyright:    2021 IT-Infrastructure for Translational Medical Research,    #
#                University of Augsburg                                        #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#==============================================================================#
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# External libraries
import numpy as np
# Internal libraries/scripts
from aucmedi.ensembler.aggregate.agg_base import Aggregate_Base

#-----------------------------------------------------#
#               Aggregate: Majority Vote              #
#-----------------------------------------------------#
""" Aggregate function based on majority vote.

    Methods:
        __init__:               Object creation function.
        aggregate:              Merge multiple class predictions into a single prediction.
"""

class Majority_Vote(Aggregate_Base):
    #---------------------------------------------#
    #                Initialization               #
    #---------------------------------------------#
    def __init__(self):
        # No hyperparameter adjustment required for this method, therefore skip
        pass

    #---------------------------------------------#
    #                  Aggregate                  #
    #---------------------------------------------#
    def aggregate(self, preds):
        # Count votes
        votes = np.argmax(preds, axis=1)
        # Identify majority
        majority_vote = np.argmax(np.bincount(votes))
        # Create prediction based on majority vote
        pred = np.zeros((preds.shape[1]))
        pred[majority_vote] = 1
        # Return prediction
        return pred


        # # Split data columns into multi level structure based on architecutre
        # data.columns = data.columns.str.split('_', expand=True)
        # # Identify argmax (vote) for each architecutre and cache n-architectures
        # data = data.groupby(level=0, axis=1).idxmax(axis=1)
        # n_architectures = len(data.columns)
        # data = data.apply(lambda entry: [tup[1] for tup in entry])
        # # Sum up votes of all architectures
        # data = data.apply(pd.Series.value_counts, axis=1).fillna(0)
        # # Compute Class Probabilities
        # pred = data.divide(n_architectures)
        # # Return prediction
        # return pred.to_numpy()
