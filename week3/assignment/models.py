import matplotlib.pyplot as plt
from matplotlib import rc
from itertools import product
import pandas as pd

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor

# 한글 폰트 깨지지 않게 하기
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

def generate_param_combinations(param_grid):
    param_names = list(param_grid.keys())
    param_values = list(param_grid.values())
    
    combinations = list(product(*param_values))
    
    param_combinations = []
    for combination in combinations:
        param_combinations.append(dict(zip(param_names, combination)))
    
    return param_combinations

def run_models(params, train_x, train_y, test_x, test_y, model_name, param_name, plt_mode = 0):
    train_score = []
    test_score = []

    params_comb = generate_param_combinations(params)
    for i in params_comb:
        if model_name == 'dt':
            model = DecisionTreeRegressor(random_state = 777,  
                                              min_samples_leaf= i['min_samples_leaf'], 
                                              min_samples_split= i['min_samples_split'],
                                              max_depth= i['max_depth'])
        elif model_name == 'rf':
            model = RandomForestRegressor(random_state = 777, 
                                              n_estimators= i['n_estimators'], 
                                              min_samples_leaf= i['min_samples_leaf'], 
                                              min_samples_split= i['min_samples_split'],
                                              max_depth= i['max_depth'])
        elif model_name == 'gb':
            model = GradientBoostingRegressor(random_state = 777, 
                                              n_estimators= i['n_estimators'], 
                                              min_samples_leaf= i['min_samples_leaf'], 
                                              min_samples_split= i['min_samples_split'],
                                              max_depth= i['max_depth'],
                                              learning_rate= i['lr'])
        model.fit(train_x, train_y)
        train_score.append(model.score(train_x, train_y))
        test_score.append(model.score(test_x, test_y))
    df_score = pd.DataFrame()
    df_score[param_name] = params[param_name]
    df_score["TrainScore"] = train_score
    df_score["TestScore"] = test_score
    if plt_mode == 1:
        plt.plot(params[param_name], train_score, label = "Train score")
        plt.plot(params[param_name], test_score, label = "Test score")
        plt.legend()
        plt.show()
    
    return df_score