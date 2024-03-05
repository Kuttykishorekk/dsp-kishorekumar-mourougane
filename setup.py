from setuptools import setup, find_packages

setup(
    name="house_prices",
    version="0.3",
    packages=find_packages(),
    package_data={'': ['*.joblib']},
    install_requires=[
        'numpy',
        'pandas',
        'joblib',
        'scikit-learn'
    ],
    entry_points={
        "console_scripts": [
            "house_prices_build_model = house_price:build_model",
            "house_prices_make_prediction = house_price:make_prediction",
            "house_prices_preprocess = house_price:preprocess"
        ],
    },
    author="kishorekumar",
    author_email="kishorekumar.mourougane@epita.fr",
    description="A package for predicting house prices",
    license="MIT",
    keywords="House_price Package"
)
