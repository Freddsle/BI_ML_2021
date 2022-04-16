# BI_ML_2021

1. Two tasks about KNN in `./l01_knn/code/KNN.ipynb`:
    - [Fashion-MNIST dataset](https://www.kaggle.com/zalando-research/fashionmnist)
    - [Diabetes dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset)


2. Practice with linear models and gradient descent (LinearRegression, LogisticRegression, Pipeline from sklearn) in `l2_linmodels_GD/code/Linear_models.ipynb`. 
    
    load_boston dataset from sklearn and [pokemon](https://www.kaggle.com/abcsds/pokemon) dataset used.


3. Practice with clustering (KMeans, AgglomerativeClustering, DBSCAN, OPTICS, SpectralClustering, MiniBatchKMeans, Birch) in `l3_clustering/code/Cluster_tSNE.ipynb`. 
    
    load_digits dataset from sklearn and flow cytometry dataset (in `l3_clustering/data_folder/flow_c_data.csv`) used.


# Install requirements with pip 

Install requirements: `pip install -r ./01_knn/code/requirements.txt`

# Install and run with poetry
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project
git clone https://github.com/Freddsle/BI_ML_2021
cd ./code


# create env
poetry env use python3.10
poetry install

# Run
poetry run python code/file.py

## or for run .ipynb files
poetry run jupyter notebook
```
