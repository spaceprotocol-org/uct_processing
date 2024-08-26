# Dataset for UCT matching over successive observation -- SpaceProtocol


## Problem Statement
Given a track, find previously seen tracks that originated from obseving the same object.

## Dataset
Using one month's worth of data from cloudstone, we have taken "associated" tracks, removed their identiy and pretend that they are uncorrelated tracks (ucts). This gives us access to known correspondence across time between observed tracks.

We have split this list by objects into a `train` and `test` set. This is the dataset contained here. 

We have preserved all the information from the original observations and added a `UCT_CLASS_LABEL` field that assoicated the tracks from the same object across time. 

The dataset consists of 
- train.json
- test.json
- train_associations.json
- test_associations.json

The last two are used to automate evaluation of developed methods.

The dataset has been shared using a separate link on rocket chat. Please contact `@yasir_spaceprotocol` on rocket chat if you haven't seen it yet.

## Code examples

A notebook contains the code for viewing and evaluating the dataset can be found at [https://github.com/spaceprotocol-org/uct_processing]()


## Setting up 

```bash
git clone https://github.com/spaceprotocol-org/uct_processing
cd uct_processing
pip install -r requirements.txt
```

Download data from the google drive link.
Run view_dataset.ipyb to visualize the dataset and look at how benchmarking it done.


# Planned updates to the dataset
- More data
- More difficult data scenarios











