# HousePricePredictor
a machine learning model for predicting prices of the house trained on keras's Boston houses prices dataset.

### Dataset:
Samples contain 13 features of houses at different locations around the Boston suburbs in the late 1970s. Targets are the median values of the houses at a location (in k$).

This is the list of 14 columns and their dexription in Boston houses prices dataset:
| column | Description |
| --- | --- |
| CRIM | per capita crime rate by town |
| ZN | proportion of residential land zoned for lots over 25,000 sq.ft. |
| INDUS | proportion of non-retail business acres per town. |
| CHAS | Charles River dummy variable (1 if tract bounds river; 0 otherwise) |
| NOX | nitric oxides concentration (parts per 10 million) |
| RM | average number of rooms per dwelling |
| AGE | proportion of owner-occupied units built prior to 1940 |
| DIS | weighted distances to five Boston employment centres |
| RAD | index of accessibility to radial highways |
| TAX | full-value property-tax rate per $10,000 |
| PTRATIO | pupil-teacher ratio by town |
| B | 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town |
| LSTAT | % lower status of the population |
| MEDV | Median value of owner-occupied homes in $1000's |

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
This will create a number input, if you enter any number, it will be printed on the page.
