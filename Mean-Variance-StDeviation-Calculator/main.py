import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    list = np.array(list).reshape(3, 3)


    nam = ["mean", "variance", "standard deviation", "max", "min", "sum"]
    fun = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    ax = [0, 1, None]
    calculations = {}
    for i in range(len(nam)):
        data = []
        for j in ax:
            data.append(fun[i](list, axis=j).tolist() if type(fun[i](list, axis=j)) == np.ndarray else fun[i](list, axis=j))
        calculations[nam[i]] = data

    return calculations
