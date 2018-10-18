"""
<18.5                太輕
18.5~25            正常
25~30               過重
>30                   肥胖
BMI=體重(kg)/(身高(m)*身高(m))
"""
try:
    user_height = float(input("請輸入身高，單位為公分： "))
    user_body_weight = float(input("請輸入體重，單位為公斤： "))
    user_bmi = user_body_weight / ((user_height / 100) ** 2)
    if user_bmi < 25:
        if user_bmi < 18.5:
            bmi_level_of_user = "太輕"
        else :
            bmi_level_of_user = "正常"
    else :
        if user_bmi < 30:
            bmi_level_of_user = "過胖"
        else :
            bmi_level_of_user = "肥胖"
    print("your BMI is", user_bmi, "您的體重" + bmi_level_of_user)
except ValueError:
    print("請重新執行程式並輸入數字")
except (EOFError, KeyboardInterrupt):
    print("使用者中斷程式，請重新執行")
except:
    print("程式意外停止，請重新執行")
