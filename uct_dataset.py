import pandas as pd
import numpy as np


class UCT_Dataset:
    def __init__(self, dataset : str) -> None:
        self.data = pd.read_json(dataset)
        self.class_ids = self.data.UCT_CLASS_LABEL.unique()

    def stats(self):
        print("Stats :")
        track_lengths = np.array([len(self.get_tracks(c)) for c in self.class_ids])
        print(f"Number of classes : {len(self.class_ids)}")
        print(f"Avg. number of tracks per class : {track_lengths.mean()}")
        print(f"Most Tracks : {track_lengths.max()}  (class_id {self.class_ids[track_lengths.argmax()]})")

    def num_classes(self):
        return len(self.class_ids)
    
    
    def get_class_labels(self):
        return self.data.UCT_CLASS_LABEL.unique()
    
    def get_tracks(self, class_id):

        if not class_id in self.class_ids:
            raise KeyError(f"{class_id} not in dataset")
        
        this_class = self.data[self.data.UCT_CLASS_LABEL == class_id]

        tracks = this_class.groupby('trackId')
        return [tracks.get_group(track).copy() for track in tracks.groups.keys()]


# How does evalution work?
# For a given track, find all the tracks in the dataset that are related to it.
# This is evalued per track


class Evaluate:
    def __init__(self, associations):
        self.associations = pd.read_json(associations)

    # expects a df with columns 'trackId' and 'UCT_CLASS_LABEL_PREDICTED'
    def  compare(self, results):

        GT = self.associations

        #result is of the form 
        # trackid : list of matching track ids

        x_predicted = []
        x_gt = []

        nTP = 0
        nFP = 0
        nFN = 0


        for result in results:
            query = result['query']
            matches = result['matches']

            true_class = GT[GT.trackId == query].UCT_CLASS_LABEL.values[0]
            true_matches = GT[GT.UCT_CLASS_LABEL == true_class].trackId.values

            TP = len(set(matches).intersection(set(true_matches)))
            FP = len(matches) - TP
            FN = len(true_matches) - TP

            # print(set(matches).intersection(set(true_matches)))

            nTP += TP
            nFP += FP
            nFN += FN

        
        precision = nTP / (nTP + nFP)
        recall = nTP / (nTP + nFN)

        return precision, recall



        

