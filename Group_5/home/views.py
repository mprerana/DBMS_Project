from django.shortcuts import render,HttpResponse,redirect
import boto3
from boto3.dynamodb.conditions import Key, Attr
import random

# Create your views here.
def explore(request):
    uid=request.session['uid']
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('recipe')
    names=[]
    imglinks=[]
    rids=[]
    response = dynamoTable.scan()
    for i in response['Items']:
        names+=[i['name']]
        imglinks+=[i['Imglink']]
        rids+=[i['R_id']]
    name=[]
    imglink=[]
    rid=[]
    for x in range(0,4):
        rand=random.randint(1,100)
        name.append(names[rand])
        imglink.append(imglinks[rand])
        rid.append(rids[rand])

    return render(request, 'home/explore.html',{'data':zip(name,imglink,rid),'uid':uid})


def tryout(request):
    uid=request.session['uid']
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('recipe')
    names=[]
    imglinks=[]
    rids=[]
    response = dynamoTable.scan()
    for i in response['Items']:
        names+=[i['name']]
        imglinks+=[i['Imglink']]
        rids+=[i['R_id']]
    name=[]
    imglink=[]
    rid=[]
    for x in range(0,4):
        rand=random.randint(1,100)
        name.append(names[rand])
        imglink.append(imglinks[rand])
        rid.append(rids[rand])


    #### RECOMMENDOR SYSTEMS ####

    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('Users')
    scan=dynamoTable.scan()
    count=len(scan['Items'])
    u=[]

    for i in range(1,count+1):
        u.append(i)

    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('Recommend')
    scan=dynamoTable.scan()

    rvu=[]
    r=[]

    for i in scan['Items']:
        rvu.append(i['U_id'])
        r.append(i['R_id'])

    rvu_t = [list(i) for i in zip(*rvu)]

    ### FAMOUS ###
    top_recipes = [sum(i) for i in zip(*rvu_t)]

    n = len(top_recipes)
    temp_r = r

    for a in range(0, n):
        for j in range(0, n-a-1):
            if top_recipes[j] > top_recipes[j+1]:
                top_recipes[j], top_recipes[j+1] = top_recipes[j+1], top_recipes[j]
                temp_r[j], temp_r[j+1] = temp_r[j+1], temp_r[j]


    most_famous = []
    trending = []

    for i in range(0, 8):
        most_famous.append(temp_r[i])

    print(most_famous)

    for i in range(6, 10):
        trending.append(temp_r[i])

    print(trending)
    ################

    uid = request.session['uid']
    print(uid)
    sim = []
    i = u.index(uid)
    print(i)
    print(len(rvu_t))
    user_table = rvu_t[i]
    for user in rvu_t:
        sim.append(sum(user or user_table))

    n = len(u)
    temp_r = u

    for a in range(0, n):
        for j in range(0, n-a-1):
            if sim[j] > sim[j+1]:
                sim[j], sim[j+1] = sim[j+1], sim[j]
                temp_r[j], temp_r[j+1] = temp_r[j+1], temp_r[j]

    match_rps = []

    for k in range(0,5):
        match_rps.append(rvu_t[u.index(temp_r[k])])

    recom_rps = [sum(i) for i in zip(*match_rps)]

    n = len(top_recipes)
    temp_r = r

    for a in range(0, n):
        for j in range(0, n-a-1):
            if recom_rps[j] > recom_rps[j+1]:
                recom_rps[j], recom_rps[j+1] = recom_rps[j+1], recom_rps[j]
                temp_r[j], temp_r[j+1] = temp_r[j+1], temp_r[j]


    recommended_recipes = []

    for r in range(0,8):
        recommended_recipes.append(temp_r[r])

    print(recommended_recipes)

    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('recipe')

    fst_spl = [178, 155, 169, 152]
    a=[]#8
    b=[]#8
    c=[]#4
    d=[]#4

    for i in recommended_recipes:
        response = dynamoTable.scan(
            FilterExpression=Attr('R_id').eq(int(i))
        )
        tp = []
        img =response['Items'][0]['Imglink']
        name =response['Items'][0]['name']
        rr = response['Items'][0]['R_id']
        tp.append(img)
        tp.append(name)
        tp.append(rr)
        a.append(tp)

    for i in most_famous:
        response = dynamoTable.scan(
            FilterExpression=Attr('R_id').eq(int(i))
        )
        tp = []
        img =response['Items'][0]['Imglink']
        name =response['Items'][0]['name']
        rr = response['Items'][0]['R_id']
        tp.append(img)
        tp.append(name)
        tp.append(rr)
        b.append(tp)

    for i in trending:
        response = dynamoTable.scan(
            FilterExpression=Attr('R_id').eq(int(i))
        )
        tp = []
        img =response['Items'][0]['Imglink']
        name =response['Items'][0]['name']
        rr = response['Items'][0]['R_id']
        tp.append(img)
        tp.append(name)
        tp.append(rr)
        c.append(tp)

    for i in fst_spl:
        response = dynamoTable.scan(
            FilterExpression=Attr('R_id').eq(int(i))
        )
        tp = []
        img =response['Items'][0]['Imglink']
        name =response['Items'][0]['name']
        rr = response['Items'][0]['R_id']
        tp.append(img)
        tp.append(name)
        tp.append(rr)
        d.append(tp)

    a1=[]
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('recipe')
    scan=dynamoTable.scan()
    for i in scan["Items"]:
        a1.append(i['name'])

    d1 = []
    for x in range(len(a1)):
        b1 = {}
        b1['id'] = x
        b1['value'] = a1[x]
        d1.append(b1)

    ### ACROSS FORUMS ###
    data = {'data':zip(name,imglink,rid),
            'trending':c,
            'recommended_recipes':a,
            'most_famous':b,
            'festival_splecial':d,
            'names':d1
            }

    return render(request, 'home/tryout.html', data)


def recipe(request, id):
    print(id)
    print(type(id))
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('recipe')
    response = dynamoTable.scan(
        FilterExpression=Attr('R_id').eq(int(id))
    )
    #data extraction
    servings    =response['Items'][0]['servings']
    ingredients =response['Items'][0]['ingreditents']
    chefname    =response['Items'][0]['Chefname']
    img         =response['Items'][0]['Imglink']
    maketime    =response['Items'][0]['Maketime']
    region      =response['Items'][0]['Region']
    steps       =response['Items'][0]['steps']
    name        =response['Items'][0]['name']
    description = response['Items'][0]['Description']

    print(description)
    x = [x.strip() for x in eval(steps)]
    del x[-1]

    n = len(x)

    x1 = [x1.strip() for x1 in eval(ingredients)]
    del x1[-1]

    n1 = len(x1)


    data = {'servings':servings,
            'ingredients':zip([x1+1 for x1 in list(range(n1))], x1),
            'chefname':chefname,
            'img':img,
            'maketime':maketime,
            'region':region,
            'steps':zip([x+1 for x in list(range(n))], x),
            'name':name,
            'n':n,
            'description':description[1:-1],
            'l':[x+1 for x in list(range(n))]}

    return render( request, 'home/recipe.html', data)

def base(request):
    return render(request, 'home/base.html')

def register(request):
    return render(request, 'register/login.html')

def findchefs(request):

    dynamoDB = boto3.resource('dynamodb')
    dynamoTable = dynamoDB.Table('Users')


    fe = Attr('email').contains('yashukikkuri@gmail.com')

    response = dynamoTable.scan(
         FilterExpression = fe,
         )

    following = response['Items'][0]['following']

    scan = dynamoTable.scan()
    top5 = []
    followers5=[]
    count = 0

    for i in scan['Items']:
        if(i['U_id'] in following):
            continue
        else:
            count+=1
            if(count>5):

                if(i['followers']>min(followers5)):
                    index=followers5.index(min(followers5))

                    a = []
                    response2 = dynamoTable.scan(
                        FilterExpression = Attr('U_id').eq(int(i['U_id']))
                    )
                    fname = response2['Items'][0]['fname']
                    uname = response2['Items'][0]['uname']
                    lname = response2['Items'][0]['lname']
                    followers = response2['Items'][0]['followers']

                    a.append(i['U_id'])
                    a.append(fname)
                    a.append(lname)
                    a.append(uname)
                    a.append(followers)

                    top5[index] = a

                    print(followers5)
                    print("\n\n")
                    print(top5)
                    print("\n\n")

            else:
                a = []
                response2 = dynamoTable.scan(
                    FilterExpression = Attr('U_id').eq(int(i['U_id']))
                )
                fname = response2['Items'][0]['fname']
                uname = response2['Items'][0]['uname']
                lname = response2['Items'][0]['lname']
                followers = response2['Items'][0]['followers']

                a.append(i['U_id'])
                a.append(fname)
                a.append(lname)
                a.append(uname)
                a.append(followers)

                top5.append(a)
                followers5.append(i['followers'])


    user_details = {'data': top5}

    return render(request, 'home/findchefs.html', user_details)


def registered(request):
    first = request.POST['First']
    last = request.POST['Last']
    email = request.POST['email']
    password = request.POST['password']
    uname=request.POST['username']
    dynamoDB = boto3.resource('dynamodb')
    dynamoTable = dynamoDB.Table('Users')
    fe = Attr('email').eq(email)
    response = dynamoTable.scan(FilterExpression = fe)

    if (response['Items']==[]):
        response=dynamoTable.scan()
        if (response['Items']==[]):
            sno = 1
        else:
            sno = len(response['Items'])+1
        dynamoTable.put_item(
        Item={
        'U_id':sno,
        'fname':first,
        'lname':last,
        'uname':uname,
        'email':email,
        'password':password,
        'lat':'80',
        'long':'35',
        'followers':0,
        'following':[],
        'D_id':0
        }
        )

    else:
        # sno=len(response['Items'])+1
        print('email already exists')

    return render(request, 'home/index.html')

def home(request):
    request.session['uid']=0
    return render(request, 'home/index.html')

def login(request):
    flag = 0
    email=request.POST['email']
    password=request.POST['password']
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('Users')
    fe = Attr('email').eq(email)
    response=dynamoTable.scan(FilterExpression=fe)
    if (response['Items']==[]):
        res = 'You have not registered yet. Please register first to continue'
        flag = 1
        print("register first")
    else:
        print(response['Items'][0]['password'])
        id = int(response['Items'][0]['U_id'])
        request.session['uid']=id
        if(response['Items'][0]['password'] == password):
            return redirect('home:tryout')
        else:
            res = 'The password you have entered is wrong'
            flag = 1
    return render(request, 'register/login.html', {'res':res, 'flag':flag})


def search(request):
    return render(request,'search/search.html')

def contact(request):
    return render(request,'home/contact.html')

def cont(request):
    return render(request,'home/cont.html')

def diet(request):
    id=request.session['uid']
    print(id)
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('Users')
    fe = Attr('U_id').eq(id)
    scan=dynamoTable.scan(FilterExpression=fe)
    print(scan['Items'])
    d_id=scan['Items'][0]['D_id']
    print(d_id)
    d_id=int(d_id)
    d_id=0
    r_id=[]
    if(d_id==0):
        r_id=[]
    else:
        r_id=[139,140,153,155]

    name=[]
    link=[]

    rid=[]
    d_id=str(d_id)
    print('aaa')
    print(r_id)
    for id in r_id:
        dynamoDB=boto3.resource('dynamodb')
        dynamoTable=dynamoDB.Table('recipe')
        fe = Attr('R_id').eq(id)
        scan=dynamoTable.scan(FilterExpression=fe)
        print(scan['Items'])
        print('aaaa')
        name.append(scan['Items'][0]['name'])
        link.append(scan['Items'][0]['Imglink'])
        rid.append(scan['Items'][0]['R_id'])
    data=zip(name,link,rid)
    print(name)
    return render(request,'home/diet.html',{'d_id':d_id,'data':data})

def select(request,id_1):
    # id=request.session['uid']
    # dynamoDB=boto3.resource('dynamodb')
    # dynamoTable=dynamoDB.Table('Users')
    # fe = Attr('U_id').eq(id)
    # scan=dynamoTable.scan(FilterExpression=fe)
    # print(scan['Items'][0]['D_id'])
    # x=scan['Items'][0]['D_id']

    x=0
    r_id=[25,30,75]

    name=[]
    link=[]
    rid=[]
    print('aaa')
    print(r_id)
    for i in r_id:
        dynamoDB=boto3.resource('dynamodb')
        dynamoTable=dynamoDB.Table('recipe')
        fe = Attr('R_id').eq(i)
        scan=dynamoTable.scan(FilterExpression=fe)
        print(scan['Items'])
        print('aaaa')
        name.append(scan['Items'][0]['name'])
        link.append(scan['Items'][0]['Imglink'])
        rid.append(scan['Items'][0]['R_id'])
    data=zip(name,link,rid)


    if int(id_1)>3:
        d_id=5
        x=0

    elif x==id_1:
        d_id=x
    else:
        x=id_1
        d_id = x
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('Users')
    fe = Attr('U_id').eq(id)
    scan=dynamoTable.scan(FilterExpression=fe)

    dynamoTable.put_item(
    Item={
        'U_id':scan['Items'][0]['U_id'],
        'fname':scan['Items'][0]['fname'],
        'lname':scan['Items'][0]['lname'],
        'uname':scan['Items'][0]['uname'],
        'email':scan['Items'][0]['email'],
        'password':scan['Items'][0]['password'],
        'lat':scan['Items'][0]['lat'],
        'long':scan['Items'][0]['long'],
        'followers':0,
        'following':[],
        'D_id':x
    }
    )


    return render(request,'home/diet.html',{'d_id':d_id,'data':data})
def insert(request):
    if request.method == "POST":
        recipe = request.POST.getlist('recipe')
        print("\nrecipe:",recipe)
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('recipe')
    fe = Attr('name').eq(recipe[0])
    response=dynamoTable.scan(FilterExpression=fe)
    print(response['Items'])
    name=[]
    link=[]
    rid=[]
    for i in response['Items']:
        name.append(i['name'])
        link.append(i['Imglink'])
        rid.append(i['R_id'])
    data=zip(name,link,rid)
    return render(request,'home/disp.html',{'data':data})
