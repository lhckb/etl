import os
import json

if (os.path.isdir('./raw_data/countries-olympics-medals-since-1896/')):
    print('dataset already downloaded')
    exit(0)

# CONFIG ENV TO IMPORT KAGGLE DEPS
file_content = open('kaggle.json', 'r').read()

kaggle_file = json.loads(file_content)
os.environ["KAGGLE_USERNAME"] = kaggle_file['username']
os.environ["KAGGLE_KEY"] = kaggle_file['key']


from kaggle import KaggleApi

api = KaggleApi()
api.authenticate()

download_dir = './raw_data/'
dataset_id = 'the-guardian/olympic-games'

print('downloading dataset...')

api.dataset_download_files(dataset_id, path=download_dir, unzip=True)

print('dataset downloaded')
