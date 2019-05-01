import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled.settings')

import django

django.setup()

##fake population script

import random
from django.db import connection
from faker import Faker

fakegen =Faker()
area_available=[1000,1200,1500]
available=['rent','buy','shop']
value=125
cursor=connection.cursor()
def add_plot(pid,floor):
    area=random.choice(area_available)
    available_for=random.choice(available)
    cost=0
    if available_for=="rent":
        cost=area*value
    else:
        cost=area*value*30
    sql="INSERT INTO plot_details (p_id,floor,area,tenant_id,admin_id,cost,Available_for) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val=(pid,floor,area,None,3,cost,available_for)
    cursor.execute(sql,val)





if __name__ == '__main__':
    print("populating script!")
    for i in range(6):
        if i == 0:
            continue
        else:
            floor = i
            for j in range(21):
                if j == 0:
                    continue
                else:

                    pid = floor * 100 + j
                    add_plot(pid, floor)

    print("population complete")


