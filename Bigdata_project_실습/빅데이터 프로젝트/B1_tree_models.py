import matplotlib.pyplot as plt
from matplotlib import rc
from itertools import product
import pandas as pd

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

# 분류모델 평가 함수
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report

# 한글 폰트 깨지지 않게 하기 -맥
# rc('font', family='AppleGothic')
# plt.rcParams['axes.unicode_minus'] = False

# 한글 폰트 깨지지 않게 하기 -리눅스
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.family"] = 'NanumGothic'

# 실행결과 경고메시지 출력 제외
import warnings
warnings.filterwarnings('ignore')

def generate_param_combinations(param_grid):
    param_names = list(param_grid.keys())
    param_values = list(param_grid.values())
    
    combinations = list(product(*param_values))
    
    param_combinations = []
    for combination in combinations:
        param_combinations.append(dict(zip(param_names, combination)))
    
    return param_combinations

def run_models_classification(params, train_x, train_y, test_x, test_y, model_name, param_name, plt_mode = 0):
    train_score = []
    test_score = []

    params_comb = generate_param_combinations(params)
    for i in params_comb:
        if model_name == 'dt':
            model = DecisionTreeClassifier(random_state = 1986,  
                                              min_samples_leaf= i['min_samples_leaf'], 
                                              min_samples_split= i['min_samples_split'],
                                              max_depth= i['max_depth'])
        elif model_name == 'rf':
            model = RandomForestClassifier(random_state = 1986, 
                                              n_estimators= i['n_estimators'], 
                                              min_samples_leaf= i['min_samples_leaf'], 
                                              min_samples_split= i['min_samples_split'],
                                              max_depth= i['max_depth'])
        elif model_name == 'gb':
            model = GradientBoostingClassifier(random_state = 1986, 
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
    #print(df_score)
    #print(train_score)
    df_score["TrainScore"] = train_score
    df_score["TestScore"] = test_score
    if plt_mode == 1:
        plt.plot(params[param_name], train_score, label = "Train score")
        plt.plot(params[param_name], test_score, label = "Test score")
        plt.legend()
        plt.show()
    
    return df_score

def eval_class_model(y_test, y_pred):
    confusion = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    F1 = f1_score(y_test, y_pred)
    AUC = roc_auc_score(y_test, y_pred)
    
    print('오차행렬:\n', confusion, '\n')
    print('정확도: {:.4f}'.format(accuracy))
    print('정밀도: {:.4f}'.format(precision))
    print('재현율: {:.4f}'.format(recall))
    print('F1    : {:.4f}'.format(F1))
    print('AUC   : {:.4f}'.format(AUC))
