# Run this in `pipenv shell`
pip install -r requirements.txt
pip install -U unstructured
pip install -U unstructured[pdf]
pip install -U jupyterlab
pip install -U pandas
pip freeze > requirements.txt
