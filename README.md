## Setup Environment - Anaconda
```
conda create --name main-ds python=3.12.6
conda activate main-ds
pip install -r requirement.txt
```

## Setup Environment - Shell/Terminal
```
mkdir lastproject
cd lastproject
pipenv install
pipenv shell
pip freeze requirements.txt
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard5.py
```
