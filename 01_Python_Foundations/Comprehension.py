'''
[expression for item in iterable if condition]
'''
#used to gen iterables with iterables in a pytonic way
#List Comprehension
users = ['Goku','Jotaro','Kaneki','Guts']
active_users = [user.upper() for user in users if 'admin' not in user]
print(active_users)

Guns = ['AK47','ScarL','AWP','UZI','Kar98k']
auto_guns = [gun.lower() for gun in Guns if len(Guns)>0]
print(auto_guns)

#Dictinoary Comprehension
model_metrics = [("accuracy",0.92),("loss",0.15),("f1_score",0.88)]
metric_dict = {metric[0]:metric[1] for metric in model_metrics if len(metric)>0}
print(metric_dict)

Set Comprehensions
raw_ids = [101,102,103,104,105]
unique_ids = {id_num for id_num in raw_ids}
print(unique_ids)


