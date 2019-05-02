from django.shortcuts import render
import boto3
from boto3.dynamodb.conditions import Key, Attr

# Create your views here.
def forum(request):
    x=request.session['uid']
    print(x)
    dynamoDB=boto3.resource('dynamodb')
    dynamoTable=dynamoDB.Table('forum')
    scan=dynamoTable.scan()
    print(scan['Items'])
    rid=[]
    date=[]
    for i in scan['Items']:
        rid.append(i['R_id'])
        date.append(i['date'])
    name=[]
    chefname=[]
    desc=[]
    imglink=[]
    for i in rid:
        dynamoDB=boto3.resource('dynamodb')
        dynamoTable=dynamoDB.Table('recipe')
        fe = Attr('R_id').eq(i)
        scan=dynamoTable.scan(FilterExpression=fe)
        name.append(scan['Items'][0]['name'])
        chefname.append(scan['Items'][0]['Chefname'])
        imglink.append(scan['Items'][0]['Imglink'])
        desc.append(scan['Items'][0]['Description'])

    data=[]

    for index in range(0, len(name)):
        tp = {}
        tp.update({'rid':rid[index]})
        tp.update({'date':date[index]})
        tp.update({'name':name[index]})
        tp.update({'chefname':chefname[index]})
        tp.update({'imglink':imglink[index]})
        tp.update({'desc':desc[index]})

        data.append(tp)

    print(data)

    return render(request, 'forum/forum.html', {'data':data})
