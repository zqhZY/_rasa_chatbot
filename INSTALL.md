
## install dependency

#### install chinese version of rasa nlu
```
git clone https://github.com/crownpku/Rasa_NLU_Chi.git
cd rasa_nlu
pip install -r requirements.txt
python setup.py install
```

#### install sklearn and MITIE

```
pip install -U scikit-learn sklearn-crfsuite
pip install git+https://github.com/mit-nlp/MITIE.git
```

#### install rasa_core

```
pip install rasa_core
```
