Package Name: house_prices
Version: 0.3
Author: kishorekumar
Email: kishore.mourougane@epita.fr

Description:
-------------
"house_prices" is a Python package for predicting house prices. This package uses machine learning models trained with specific parameters and pre-processing strategy to predict the cost of a house given several features.

Installation:
-------------

You can install the package using pip:

```bash
pip install .
```

Usage:
------
After installing the package, you can import it in your script as follows:

**Model building:**

```python
import pandas as pd
from house_prices.train import build_model

training_data_df = pd.read_csv('your_path_train.csv')
model_performance_dict = build_model(training_data_df)
print(model_performance_dict)
```
**Model inference:**

```python
import pandas as pd
from house_prices.inference import make_predictions

user_data_df = pd.read_csv('your_path_test.csv')
predictions = make_predictions(user_data_df)
predictions
```

Please refer to the specific function docstrings for more detailed usage examples.

Dependencies:
--------------
The package requires the following Python libraries:

- numpy
- pandas
- joblib
- scikit-learn
