
import os

print(os.getcwd())
os.chdir(os.getcwd()+'/water_pollution/')
print(os.getcwd())
print(os.listdir('./2022-01-10 Tests'))
print([x for x in os.listdir('./2022-01-10 Tests') if x[-3:].lower() == 'jpg'])

dir = os.path.dirname(os.path.abspath(__file__))
print(dir)
