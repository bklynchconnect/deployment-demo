# Machine Learning Model Deployment Demo

Brian Lynch 2025

This repository demonstrates a simple model built in a Jupyter notebook and saved as a pickle file. The model is then loaded in another notebook as well as a script to demonstrate loading and running the model outside of the original notebook. A Flask app and Streamlit app are also demonstrated for deployment (with the inference notebook demonstrating how to call the Flask app for prediction).

### File structure

> ```
> deployment-demo
> |--- \data (contains source data in CSV format)
> |--- \images (contains screenshots for this README)
> |--- \models (where the model pickle file is stored)
> |--- app.py (the demo Flask app)
> |--- README.md (this README)
> |--- used_cars_inference.ipynb (the demo notebook for loading and running the model as well as calling the Flask app)
> |--- used_cars_inference.py (demo of loading and running the model in a Python script)
> |--- used_cars_model.ipynb (the notebook where we first build the model)
> ```

