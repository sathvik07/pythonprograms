

acess_key = str(input("enter the acesses key"))
secret_key = str(input("enter the secret key"))



import yaml

with open(r'')as file:
    variables = yaml.load(file,Loader=yaml.FullLoader)

    for i ,j in  variables.items():
         print(i,"=",j)


