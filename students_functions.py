import pymongo
import dotenv
import os


    
def insert_userprofile(user_id , stu_name , stu_gender , stu_id , stu_subject , mail, activation_code , status , level , identity):
    ## 學生的基本資料 ##
    mycol.insert_one({"user_id":user_id ,"stu_name":stu_name , "stu_gender":stu_gender , "stu_id":stu_id , "stu_subject":stu_subject , 
                      "mail":mail , "activation_code":activation_code , "status":status , "level":level , "identity":identity})
    

def find_information_by_userid(user_id,information=["stu_name","stu_gender","stu_gender","stu_id","stu_subject","mail","activation_code","status","level","identity"]):
    ## level屬性為int,其餘為string ##

    ## 鎖定想查詢的學生id ##
    query = {"user_id": {"$in": [user_id]}}
    ## 找尋鎖定學生的資料 ##
    results = mycol.find(query)
    classes = []
    for result in results:
        classes.append(result[information])
    return classes


def update_attributes(user_id,new_attribute,attributes=["stu_name","stu_gender","stu_gender","stu_id","stu_subject","mail","activation_code","status","level","identity"]):
    mycol.update_one({"user_id":user_id},{"$set":{attributes:new_attribute}})
    
    ## 更新level需要轉成int ##