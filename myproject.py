import numpy as np

# arr1 = np.array([23,25,27,28,29])
# arr2 = np.array([[23,26,27],[28,25,23]])

# print("Abade Arraye arr1 : ", arr1.shape)
# print("Abade Arraye arr2 : ", arr2.shape)

# list=[10,'Ali',20,30]

# list.remove('Ali')

# # list.append('AmirHoseinAlizadeh')
# list.insert(1,'AmirHoseinAlizadeh')

# print(list)

# dictionary1={'Name': 'AmirHosein','Lastname':'Alizadeh', 'Nationality': 'Iranian', 'Age':23}

# for key,value in dictionary1.items():

#     print(key, ':', value)

# key_list = [key for key in dictionary1]

# print(key_list)

# key_value_list =[(key,value) for key,value in dictionary1.items()]

# print(key_value_list)

# dictionary1['EyeColor'] = 'Ghahvei'

# print(dictionary1)

# def F(shmareAkhar_Daneshjooei,Shomare_Ghabl_Akhar_daneshjooei):
#     result = shmareAkhar_Daneshjooei + Shomare_Ghabl_Akhar_daneshjooei
#     print("Natije Jame : ",result)

# adad1 = int(input("Adad Aval Ra Vared konid : "))
# adad2 = int(input("Adad dovom Ra Vared konid : "))

# F(adad1,adad2)

# string = "Hello World"
# index_to_remove = 4
# new_string = string[:index_to_remove] + string[index_to_remove+1:]
# print(new_string)

# name = input("Name Khodetan Ra Vared Konid : ")
# family = input("Famil Khodetan Ra Vared Konid : ")
# string1 = "I am " + name + "  " + family
# print(string1)

# substring = string1[2:5]
# print("Substring : ", substring)

# index_A = string1.find('A')
# print("Khode Index 'a' : ", index_A)

# capitailaize_string = string1.capitalize()
# print("capitalize String : ", capitailaize_string)

# strip_string = string1.strip()
# print("Straip String : ",strip_string)

# sting2 = string1.split(' ')
# print("split string",sting2)

# join_str = '*'.join(string1)
# print('join string : ',join_str)



# Str1="I am Ali-mohamadi,in&Mashhad-I am student"

# Str1 = Str1.replace('-',' ')
# Str1 = Str1.replace(',',' ')
# Str1 = Str1.replace('&',' ')

# list_word = Str1.split()

# print(list_word)


# class AmirHoseinAlizadeh:
#     def __init__(self,age,height,weight):
#         self.age = age
#         self.height = height
#         self.weight = weight

# a = AmirHoseinAlizadeh(age =23,height=175,weight=70)

# print("SEN : ",a.age)
# print("GADE : ",a.height)
# print("VAZNE : ",a.weight)

# n = 3 

# p_between = [0.2,0.5,0.3]
# p_service = [0.1,0.2,0.4,0.3]

# betweenTime = np.zeros(n)
# enterTime = np.zeros(n)
# serviceTime = np.zeros(n)
# startTime = np.zeros(n)
# endTime = np.zeros(n)
# waitTime = np.zeros(n)

# for i in range(n):
#     betweenTime[i]= np.random.choice([5,2,1], p=p_between)
#     enterTime[i] = np.random.rand() * betweenTime[i]

#     serviceTime[i] = np.random.choice([6,7,5,4], p=p_service)

#     if i == 0:
#         startTime[i] = enterTime[i]
#     else:
#         startTime[i] = max(enterTime[i],endTime[i - 1])

#     endTime[i] = startTime[i] + serviceTime[i]

#     waitTime[i] = startTime[i] - enterTime[i]

#     print("   Customer   |     Between Time   |    Enter Time    |     Service Time     |      Start Time     |      End Time       |    Wait Time")
# for i in range(n):
#     print(f"   {i + 1}          |        {betweenTime[i]}         |      {enterTime[i]:.2f}        |        {serviceTime[i]}           |        {startTime[i]:.2f}         |         {endTime[i]:.2f}        |        {waitTime[i]:.2f}")

# p = [0.1,0.5,0.4]

# number = np.random.choice([20,30,40],p=p)

# print("Adad Bar Asase Ehtemal : ",number)
    
