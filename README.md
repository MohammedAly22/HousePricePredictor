# HousePricePredictor
a machine learning model for predicting prices of the house trained on keras's Boston houses' prices dataset.

### Dataset:
Samples contain 13 features of houses at different locations around the Boston suburbs in the late 1970s. Targets are the median values of the houses at a location (in k$).

This is the list of 14 columns in Boston houses's prices dataset:
CRIM - per capita crime rate by town
ZN - proportion of residential land zoned for lots over 25,000 sq.ft.
INDUS - proportion of non-retail business acres per town.
CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)
NOX - nitric oxides concentration (parts per 10 million)
RM - average number of rooms per dwelling
AGE - proportion of owner-occupied units built prior to 1940
DIS - weighted distances to five Boston employment centres
RAD - index of accessibility to radial highways
TAX - full-value property-tax rate per $10,000
PTRATIO - pupil-teacher ratio by town
B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
LSTAT - % lower status of the population
MEDV - Median value of owner-occupied homes in $1000's

you can see how to load and use it in this link:
https://keras.io/api/datasets/boston_housing/

### Deployment:
for deployment I used `streamllit` package which is a pretty easy and straight-forward package. Here is the link of its official website:
https://streamlit.io/

#### Example usage:
```python
import streamlit as st

number = st.number_input('Insert a number')
st.write('The current number is ', number)

```

```html

<!doctype html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no"/><link rel="shortcut icon" href="./favicon.png"/><title>Streamlit</title><script>window.prerenderReady=!1</script><script src="./vendor/viz/viz-1.8.0.min.js" type="javascript/worker"></script><script src="./vendor/bokeh/bokeh-2.4.3.min.js"></script><script src="./vendor/bokeh/bokeh-widgets-2.4.3.min.js"></script><script src="./vendor/bokeh/bokeh-tables-2.4.3.min.js"></script><script src="./vendor/bokeh/bokeh-api-2.4.3.min.js"></script><script src="./vendor/bokeh/bokeh-gl-2.4.3.min.js"></script><script src="./vendor/bokeh/bokeh-mathjax-2.4.3.min.js"></script><script defer="defer" src="./static/js/main.1d359564.js"></script><link href="./static/css/main.f4a8738f.css" rel="stylesheet"></head><body><noscript>You need to enable JavaScript to run this app.</noscript><div id="root"></div></body></html>

```
