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

```python
import house_prices
...

# predictions
predictions = house_prices.make_predictions(data)
```

Please refer to the specific function docstrings for more detailed usage examples.

Dependencies:
--------------
The package requires the following Python libraries:

- numpy
- pandas
- joblib
- scikit-learn
