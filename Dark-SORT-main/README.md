# Dark-SORT

<center>
<img src="pipeline.png" width="600"/>
</center>


| Dataset          | HOTA | AssA | IDF1 | MOTA  |
| ---------------- | ---- | ---- | ---- | ---- |
| MOT17 | 65.4 | 63.8 | 78.2 | 77.9 |


| Dataset          | HOTA | AssA | DetA | MOTA  | IDF1   |
| ---------------- | ---- | ---- | ---- | ---- | ----- | 
| MINE-MOT | 67.4 | 46.8 | 80.3 | 92.6| 61.7 | 


## Installation



After cloning, install external dependencies: 
```
cd external/yolov7/
pip install -r requirements.txt && python setup.py develop
cd ../external/deep-person-reid/
pip install -r requirements.txt && python setup.py develop
cd ../external/fast_reid/
pip install -r docs/requirements.txt
```

OCSORT dependencies are included in the external dependencies. If you're unable to install `faiss-gpu` needed by `fast_reid`, 
`faiss-cpu` should be adequate. Check the external READMEs for any installation issues.


## Data

Place MOT17 AND MINE-MOT under:

```
data
|——————mot17
|        └——————train
|        └——————test
|        └——————val
|——————MINE-MOT
|        └——————train
|        └——————test
|        └——————val
```

and run:


python3 data/tools/convert_mot17_to_coco.py
python3 data/tools/convert_mine_mot_to_coco.py
```

## Evaluation


For the MOT17 and MINE-MOT baseline:

```
exp=baseline
# Flags to disable all the new changes
python3 main.py --exp_name $exp --post --emb_off --cmc_off --aw_off --new_kf_off --grid_off --dataset mot17
python3 main.py --exp_name $exp --post --emb_off --cmc_off --aw_off --new_kf_off --grid_off -dataset mine-mot 
py
```

This will cache detections under ./cache, speeding up future runs. This will create results at:

```
# For the standard results
results/trackers/<DATASET NAME>-val/$exp.
# For the results with post-processing linear interpolation
results/trackers/<DATASET NAME>-val/${exp}_post.
```

To run TrackEval for HOTA and Identity with linear post-processing on MOT17, run:

```bash
python3 external/TrackEval/scripts/run_mot_challenge.py \
  --SPLIT_TO_EVAL val \
  --METRICS HOTA Identity \
  --TRACKERS_TO_EVAL ${exp}_post \
  --GT_FOLDER results/gt/ \
  --TRACKERS_FOLDER results/trackers/ \
  --BENCHMARK MOT17
```

Replace that last argument with MOT17 / MINE to evaluate those datasets.  


You can achieve higher results on individual datasets with different parameters, but we kept them fairly consistent with round 
numbers to avoid over-tuning.

# Citation
Also see OC-SORT, which we base our work upon: 
```
@article{cao2022observation,
  title={Observation-centric sort: Rethinking sort for robust multi-object tracking},
  author={Cao, Jinkun and Weng, Xinshuo and Khirodkar, Rawal and Pang, Jiangmiao and Kitani, Kris},
  journal={arXiv preprint arXiv:2203.14360},
  year={2022}
}
```
