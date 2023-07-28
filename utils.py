import pickle
import json
import numpy as np
import config


class BankChurn():
    def __init__(self,credit_score,gender,age,tenure,balance,products_number,
                 credit_card,active_member,estimated_salary,country):
        print("****** INIT Function *********")
        self.credit_score = credit_score
        print(self.credit_score)
        self.gender = gender
        self.age = age
        self.tenure = tenure
        self.balance = balance
        self.products_number = products_number
        self.credit_card = credit_card
        self.active_member = active_member
        self.estimated_salary = estimated_salary
        self.country = country

       
    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

        with open(config.SCALING_FILE_PATH, 'rb') as f:
            self.std_scaler = pickle.load(f)

    def get_churn(self):
        self.__load_saved_data()

        
        gender = self.json_data['Gender'][self.gender]
        country = 'country_'+ self.country

        country_index = self.json_data["Column Names"].index(country)

        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.credit_score
        test_array[0,1] = gender
        test_array[0,2] = self.age
        test_array[0,3] = self.tenure
        test_array[0,4] = self.balance
        test_array[0,5] = self.products_number
        test_array[0,6] = self.credit_card
        test_array[0,7] = self.active_member
        test_array[0,8] = self.estimated_salary
        test_array[0,country_index] = 1

        std_test_array = self.std_scaler.transform(test_array)


        predicted_churn =  self.model.predict(std_test_array)[0]
        return predicted_churn
            