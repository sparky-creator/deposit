import scipy.stats as stat
from sklearn.linear_model import LinearRegression

class LR_mod(LinearRegression):
    def __init__(self, fit_intercept=True, normalize =True, copy_X=True, n_jobs=1):
        super.__init__()

        self.fit_intercept = fit_intercept
        self.normalize = normalize
        self.copy_X = copy_X
        self.n_jobs = n_jobs

    def fit(self, X, y, n_jobs =1):

        self = super(LinearRegression, self).fit(X,y,n_jobs)

        sse = np.sum((self.predict(X) - y)**2, axis =0)/

