Metrics for Model evaluation
==============================

Methods commonly used to evaluate model performance, include:

* Mean absolute error (MAE)

.. math::

    \mathrm{MAE}=\frac{1}{N} \sum_{i=1}^{N}\left|y_{i}-\hat{y}_{i}\right|

where `N` is number of observations, `y_i` the actual expected output
and `\hat{y}_{i}` the model’s prediction
(same notations below if not indicated otherwise).

* Mean bias error (MBE)

.. math::

    \mathrm{MBE}=\frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\hat{y}_{i}\right)

* Mean square error (MSE)

.. math::

    \mathrm{MSE}=\frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\hat{y}_{i}\right)^{2}


* Root mean square error (RMSE)

.. math::

    \mathrm{MBE}=\frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\hat{y}_{i}\right)


* Coefficient of determination (`R^2`)

.. math::

    R^{2}=
    1-\frac{\mathrm{MSE}(\text { model })}
    {\mathrm{MSE}(\text { baseline })}

    \mathrm{MSE}(\text { baseline })=
    \frac{1}{N} \sum_{i=1}^{N}\left(y_{i}-\overline{y}\right)^{2}

where `\overline{y}` is mean of observed `y_i`.

These presented with plots (e.g. scatter, time series)
allow identification of periods
where model perform well/poorly relative to observations.
It should be remembered that both the model (e.g. parameters, forcing data)
and the evaluation observations have errors.
