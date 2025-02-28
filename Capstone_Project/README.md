
## Codes - for the modeling 
```bash

├── 01_train.ipynb
├── 02_feature_extraction.ipynb
├── 03_retrieval.ipynb
│   
├── config.py
├── data.py
├── net.py
├── utils.py
│   
└── requirements.txt

```

## App - for deployment on Heroku with Flask

Check out the [web app](https://deepfashion-finder.herokuapp.com/)

```bash

├── app.py
├── config.py
├── file.py
├── retrieval.py
├── Procfile
├── requirements.txt
│   
├── feats_pca
│   ├── all_color_feat.npy
│   ├── all_feat_pca.npy
│   └── all_feat.list
├── list
│   └── Anno
│   │   └── list_category_img.txt
│   └── Eval
│       └── list_eval_partition.txt
├── static
│   └── clothing.jpg
└── templates
    ├── input_page.html
    ├── output_styling.html
    └── query_styling.html  

```

