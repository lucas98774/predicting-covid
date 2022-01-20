# Covid Predictions

This repo aims to predict covid cases as well as covid hospitalizations as cases continue to rise around the globe. Another aim of this project is to learn more about time series analysis in all its forms (forecasting, spectral analysis, anomaly detection) which are broken down further below.

# Applications:

## Feature engineering

This concept is involved in every application for time series analysis as processing time series data is pivotal for success in subsequent parts of the analysis regardless of the goal. There are also different processing techniques for different applications (ie anomaly detection vs forecasting). A big concept in classical time series forecasting techniques is stationary, how to identify it, and how to deal with nonstationary data. Other ideas that will be of interest are decomposition (classical and multivariate) and ...

## Forecasting

This is broadly defined as modeling techniques that involve temporal information with the purpose of predicting a response (or multiple). There may or not be independent variables used as well. 

### Univariate

This section is where the most simple classical theory is utilized (ma and ar models) and is vital for understanding and building to more complex time series scenarios. This involves predicting a single response variable in the future without any independent variables.

### Multivariate

This involves predicting a single response in the future with independent variables. When using independent variables with temporal information as well, feature engineering and feature processing becomes more difficult and this will be a key area to explore.

## Anomaly Detection

This involves identifying interesting events in the data that seem to be from a different process and follow a different distribution than the typical data.

### Supervised

This instance includes labels that denote anomalous samples from normal samples. In this case, the task is often training a classification model but the key obstacles are a high class imbalance and identifying anomalies ahead of time so action can be taken prior to the anomaly (sometimes a breakdown) occuring.

### Unsupervised

This instance does not involve labels and is in turn more subjective as there is no target to indicate what events are interest. The main approaches for this scenario are clustering techniques, classical methods (iqr method ...), isolation forests (random cut forest is an extension --- need to find and implementation). Some extensions to this scenarion is again identifying the anomaly in advance so proactive maintenance can be implemented. This often leads to use of forecasting models (and deep learning models) and using an error threshold where any residuals above this threshold are classified as anomalous points as the model is not able to recreate this point.

## Spectral Analysis

This technique is often used to transform data from the time domain to the signal domain where cyclical patterns and possibly acyclical patterns can be identified more easily. Applications for this family of techniques is also of interest as I do not know how these are used in conjunction with other time series methods (models or processing techniques)

## NOTES

Justin feel free to add in details and things of interest wherever you see fit.

* Cross Validation (blocked time series split and nested techniques)
* Deep Learning can always be used to lag predictors or process inputs but how much does initial processing matter then (similar to normalization)?
*  



