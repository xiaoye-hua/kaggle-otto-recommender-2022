local = False

if local:
    # from google.colab import drive
    # drive.mount('/content/drive')
    # %cd /content/drive/MyDrive/'Kaggle Otto Reccommender'/data
    # path_o_module = '/content/drive/MyDrive/Kaggle Otto Reccommender/'
    data_path = '/home/jupyter/kaggle-otto-recommender-2022/data'
    path_to_module = '/home/jupyter/kaggle-otto-recommender-2022'
else:
    data_path = '/home/jupyter/kaggle-otto-recommender-2022/data'
    path_to_module = '/home/jupyter/kaggle-otto-recommender-2022'