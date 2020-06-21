# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 03:53:12 2020
"""

import numpy as np
import random
import pandas as pd
import hiplot as hip
import optuna # import optimization tool
from optuna.samplers import TPESampler # TPE sampler

np.random.seed(777)
random.seed(777)

def objective(trial):
    x = trial.suggest_uniform('x', -10, 10)
    return x**2 # objective function

study = optuna.create_study(sampler=TPESampler(seed=777))
study.optimize(objective, n_trials=1000)

parameter = study.trials_dataframe()['params_x']
value = study.trials_dataframe()['value']

plotdata = pd.concat([parameter,value], axis=1)

data = []
for i in range(len(parameter)):
    data.append({'parameter' : parameter[i], 'value' : value[i]})

html = hip.Experiment.from_iterable(data).to_html("render.html") # or from_dataframe
