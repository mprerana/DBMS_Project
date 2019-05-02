from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import boto3
from boto3.dynamodb.conditions import Key, Attr
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
import datetime

# Create your views here.

def search(request):
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('ingredients')

    pe="#na"
    ean = { "#na": "name", }

    scan=dynamoTable.scan(
            ProjectionExpression=pe,
            ExpressionAttributeNames=ean
    )
    a=[]
    for i in scan['Items']:
        a.append(i['name'])

    d = []
    for x in range(len(a)):
        b = {}
        b['id'] = x
        b['value'] = a[x]
        d.append(b)
    return render(request, 'uploadforum/search.html',{'names':d})

def insert1(request):
    if request.method == "POST":
        ingredients = request.POST.getlist('ingredient')
        print("\ningredients:",ingredients)


        dynamoDB=boto3.resource('dynamodb')
        dynamoTable=dynamoDB.Table('recipe')
        # print(dynamoTable.item_count)

        fe = Attr('ingreditents').contains(ingredients[0])


        response = dynamoTable.scan(
             FilterExpression=fe,
             )

        # print(ingredients[0])
        # print(ingredients[1])

        ing=[]
        recipe=[]
        names=[]
        imglinks=[]
        for i in response["Items"]:
            # print(i['R_id'])
            ing.append(i['ingreditents'])
            recipe.append(i['R_id'])
            names.append(i['name'])
            imglinks.append(i['Imglink'])
        # print(ing)
        #
        print(len(ing))
        print(recipe)
        for j in ing:
            for h in ingredients[1:]:
                if(h in j):
                    continue
                else:
                    index=ing.index(j)
                    ing.remove(j)
                    recipe.pop(index)
                    names.pop(index)
                    imglinks.pop(index)
                    break
        print(ing)
        print(recipe)
        print(names)
        print(imglinks)

    return render(request,'uploadforum/complected.html',{'data':zip(names,imglinks,recipe)})



#@login_required
def insert(request):
    if request.method == "POST":
        Rname = request.POST['Rname']
        ingredients = request.POST.getlist('ingredient')
        ingredients=str(ingredients)
        quantity = request.POST.getlist('quantity')
        option = request.POST.getlist('option')
        Steps = request.POST.getlist('Steps')
        Steps=str(Steps)
        Servings = request.POST['Servings']
        Description = request.POST['Description']
        Maketime = request.POST['Maketime']
        myfile = request.FILES['sentFile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        f = request.FILES['sentFile']
        f="./media/"+str(myfile)
        s3 = boto3.client('s3')
        bucket = 'dbms2019'

        file_name = str(f)
        key_name = str(myfile)
        ###

        s3.upload_file(file_name, bucket, key_name)

        bucket_location = boto3.client('s3').get_bucket_location(Bucket=bucket)
        link = "https://s3-ap-south-1.amazonaws.com/{0}/{1}".format(
             bucket,
             key_name)

        x=request.session['uid']
        print(x)
        dynamoDB=boto3.resource('dynamodb')
        dynamoTable=dynamoDB.Table('Users')
        fe = Attr('U_id').eq(x)
        response=dynamoTable.scan(FilterExpression=fe)
        print(response['Items'])
        chefname=response['Items'][0]['uname']

        dynamoDB = boto3.resource('dynamodb')
        dynamoTable = dynamoDB.Table('recipe')

        scan = dynamoTable.scan()
        count = len(scan['Items'])

        dynamoTable.put_item(
            Item={
                'R_id':int(count + 1),
                'name': Rname,
                'servings': Servings,
                'ingreditents': ingredients,
                'steps': Steps,
                'Region': 'Indian',
                'Maketime': Maketime,
                'Imglink': link,
                'Chefname': chefname ,
                'Description': Description,
                }
        )

        dynamoTable = dynamoDB.Table('forum')
        scan = dynamoTable.scan()
        count2 = len(scan['Items'])
        now = datetime.datetime.now()


        dynamoTable.put_item(
            Item={

                'P_id': int(count2 + 1),
                'U_id': int(1),
                'R_id': int(count + 1),
                'date': str(str(now.day) + '/' + str(now.month) + '/' + str(now.year)),
                }
        )

    return redirect('forum:forum')


#@login_required
def home(request):
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('ingredients')

    pe="#na"
    ean = { "#na": "name", }

    scan=dynamoTable.scan(
            ProjectionExpression=pe,
            ExpressionAttributeNames=ean
    )
    a=[]
    for i in scan['Items']:
        a.append(i['name'])

    d = []
    for x in range(len(a)):
        b = {}
        b['id'] = x
        b['value'] = a[x]
        d.append(b)
    return render(request,'uploadforum/fo.html',{'names':d})
