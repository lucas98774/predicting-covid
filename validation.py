import numpy as np

# TODO: look at inheriting from sklearn's abstraction to get benefit of error checking as well
# TimeSeriesSplit from sklearn inherits from _BaseKFold
# inheriting from this class would give us error checking
class BlockingTimeSeriesSplit():
    """
    Class for implementing a blocked time series split (to reduce data leakage...)

    See: https://medium.com/sci-net/cross-validation-strategies-for-time-series-forecasting-9e6cfab91f60 for more info
    
    """
    def __init__(self, n_splits):
        # TODO: add in param to control gaps between train-val splits
        # TODO: add in param to control gap between folds ...
        self.n_splits = n_splits
    
    def get_n_splits(self, X, y, groups):
        return self.n_splits
    
    def split(self, X, y=None, groups=None):
        n_samples = len(X)
        k_fold_size = n_samples // self.n_splits
        indices = np.arange(n_samples)

        margin = 0
        # see if there is a more efficient way to do this than a loop
        for i in range(self.n_splits):
            start = i * k_fold_size
            stop = start + k_fold_size
            # FIXME: move this hardcoded float to be a parameter ...
            mid = int(0.8 * (stop - start)) + start
            yield indices[start: mid], indices[mid + margin: stop]