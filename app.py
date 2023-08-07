
import pandas as pd
import numpy as np
import pickle
import streamlit
from sklearn import decomposition
from sklearn import preprocessing


with open(r'C:\Users\chouc\openclassrooms\projet3\model\scaler_transform.pickle','rb') as handle:
#     model= pickle.load(handle)
#      pickle.dump(scaler,handle)
       scaler_transform = pickle.load(handle)
       
with open(r'C:\Users\chouc\openclassrooms\projet3\model\cluster_model.pickle', 'rb') as handle:
#     scaler_model= pickle.load(handle)
#       pickle.dump(model,handle)
       cluster_model = pickle.load(handle)
with open(r'C:\Users\chouc\openclassrooms\projet3\model\df_dict.pkl','rb') as handle:
#     clusters_list= pickle.load(handle)
      df_dict = pickle.load(handle)
def get_key(my_dict,K):
    for key,value in df_dict.items():
        if K == key:
            return value

    return "key doesn't exist "+str(val)  
def cluster_prediction(fat_100g,carbohydrates_100g,fiber_100g,proteins_100g):
    
    pred_args=[fat_100g,carbohydrates_100g,fiber_100g,proteins_100g]
    pred_arr=np.array(pred_args)
    preds=pred_arr.reshape(1,-1)
    preds=scaler_transform.transform(preds)
#   preds=preds.astype(int)
    model_prediction=cluster_model.predict(preds)
    print(model_prediction[0])
    return get_key(df_dict,model_prediction[0])
def run():
    streamlit.title("Keto_app")
    html_temp="""
    """
    streamlit.markdown(html_temp)
fat_100g=streamlit.text_input('Lipides pour 100g')
carbohydrates_100g=streamlit.text_input('Glucides pour 100g')
fiber_100g=streamlit.text_input('Fibres pour 100g')
proteins_100g=streamlit.text_input('Proteines pour 100g')

prediction=" "
if streamlit.button("Predict"):
    prediction=cluster_prediction(fat_100g,carbohydrates_100g,fiber_100g,proteins_100g)
streamlit.success("Résultat: {}".format(prediction))

if __name__=='__main__':
    run()

