import requests
import json
import random
import time

tokens=['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUxNiwiaWF0IjoxNTU2NzQ3MjIzLCJleHAiOjE1NTY4MzM2MjN9.hjMNVXSxGMpPgaVqzVkaEIO8LV8t702nJGSO4_PkXqA', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUxNywiaWF0IjoxNTU2NzQ3MjIzLCJleHAiOjE1NTY4MzM2MjN9.07Tn3t8CRPH5rbNO5vWCWzNbw7UVAY1XeDoxKyO5VBU', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUxOCwiaWF0IjoxNTU2NzQ3MjIzLCJleHAiOjE1NTY4MzM2MjN9.Kp_CuMreg7hfZ3uErZlcKdpBfFUv-KBZaLyeLBm-GBE', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUxOSwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.gxxaTGFTxqUajxfO_l-tPFLJq5O2DHWaQHocEqsKRT8', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyMCwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.blwAAzRRbmCu6NqjABJamj1-yEpyVlh94k8Y3xaJQSM', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyMSwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.B8lZ3qRccTKB8qkfpihvBD2zKAMzKQ1fcQgrfRDnQ3A', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyMiwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.njm1IMlmB-BCuHBgTdwKglL1Z3d78QgieJiu3p8hj9c', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyMywiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.WMlkV2-n6uJjUUuXJmNBPIwpN-PUeExwzS_eW93H4J0', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyNCwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.ojCj8jCJr7Bj5P-b91isM6FHLnS6kVXoZ6-Y8HrlrOo', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyNSwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.yppnGrUzbIL8x20ipvGowtgK2MCBS8nILKI1V4f4jqs', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyNiwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.BD3EnA852wvXwV6b3QoJTtfaWyM8thnl1pnkqiix0J4', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyNywiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.0qBZWC6gmjhnTgn-WTl7kU-R-Kk4_DrG4TOnPMm7Keg', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyOCwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.CnfYgcop1wh176hy_CfQQ3Q75Qqcyz8eGJCXkc-V09Y', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUyOSwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.rsEo9RtZd3ScmFTl2Y_lF72NUHtBb4RVLTTIHTSdlnU', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzMCwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.8XS7kg2WonFF6Brk4PCr3vElgljn8vLCWTJ5DHEyqtg', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzMSwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.HeGqbJ2n5gBwKAQr1lYqkELRIMrFzmsn3KLXdjxbQvM', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzMiwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.fS8HMv_iy9kcWWc6B8DNOMm5IiMco6X5j3ig3uuVfso', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzMywiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.Xia5xrVrNmCfc8FZ3RANszpe8AR9-lOeAqCPCasM7RA', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzNCwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.JRrron04vcmVL6qbpsQd5-NERm7E5C40bn7qSnqQyhg', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzNSwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.E-cNH9mOeADNd9fS9iTp5y86w4bseKSjsLkFY-_4n6M', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzNiwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.0qA3YuZMMlyolBKCpZeEjGiZWw7WJ4IKq1iExaAPvfM', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzNywiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.r7Off698ebLk2h2JSSya_-JxNoDwvvI1b5LnQa0k_9I', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzOCwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.wpFb68bsFv3lkMD3_ZxTnI5ltlN6_ORhKfkMEfsefp4', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjUzOSwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.o4Ir5TWQclhH2qZW8MMyDhhWSUgpBWreWJiQii7_h4w', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0MCwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.F4yHiZJPbPZoF7RP0H72HtxLbVNQ_LSfuswxqf93HeI', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0MSwiaWF0IjoxNTU2NzQ3MjI0LCJleHAiOjE1NTY4MzM2MjR9.ioMWlPmPAkXr8h1BxdFRk8drAEZ8npm1kT7XYrBSF8o', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0MiwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.yKNGCu9kU53oXpLklTPIWzAlYyMkFYpxVsRCXy-R7II', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0MywiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.1xKhN51BpA8M0eRv8EdOLVGJWD4tthEkyvdmjChUdxo', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0NCwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.wbD1AlvAqIoPumVlCRRzMImodj7tLQ7JMVVRnWxVEgA', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0NSwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.g37Ajq1bE-Qp9ESb1dRS99BMd2CZuCMe3Y8eLsqkKU0', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0NiwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.Nl4uzjGvj10D-m3qcNnPBpoPqtknBDKf8hV1YOgpOEQ', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0NywiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.VNKfF02KBD1XujiU6fPWGdujCgCy9MLMnoFqWYEyEnw', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0OCwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.o_GxR8mv9cXlqIzZeGyX0wIPQiNVDmhS2JVL9yj-k-E', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU0OSwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.I0eYZdYIrKbdEvc-82ErcYjZgr9KhpciboNlVpZ6snA', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1MCwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.6AHrkApgINVhC66OXOTxiJX9-cHaRkwnQSFqvMYYk0o', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1MSwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.Lujuw7-kNu3iVtuHWLAsfEYdOagQEV5Hw_tztO_P0GA', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1MiwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.ICEXg52jGv-XpCfX7X3-FjTbeo7LadzdjEtwyx9oZj4', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1MywiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.lpT1vnr3D16a8lxBu9rmhnN6551RlOHAH5Zcf76ML1o', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1NCwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.Pj6JhGy8NsDRnF3CWt0yrmh5m5goPdIv6EvnPzDcScU', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1NSwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.WqjgllyD3zpSv0d9QKGfVx4WfaZaZUBUDtVAl8WlELM', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1NiwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.VegEpqVEXfaiAC-XZCnSbmNARNPLSp6JfRYEPAl89hQ', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1NywiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.N5JDt2oZLwQLOvqoXpbrGpPgzmeFIzRrZjGoYKNhexQ', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1OCwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.e2PbxzrzFDPHWJWesTl7StOHP-XoteD9mKfJoQ8PeOQ', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU1OSwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.j7inCl1zpL2RkvjbGCX87fyoDhEEaXlrcUun0WYRmkw', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU2MCwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.99xrXT2lw8nyZm7gL7AhxLRgZUy_bD7Y5qvbpQUEgy0', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU2MSwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.9i9HQOn1EhVpCG7u0Ei5QNaaKbzFeeOIv_enaNBVWOc', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU2MiwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.UU-HsZyzLb1vA2Dp0rSSzXa6z6PZztqLt5wgduH-3BI', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU2MywiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.Lnvuxq3MwuyvEmbW6vgb0m-HTVrlyVMpXeSbSxV8pqQ', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjU2NCwiaWF0IjoxNTU2NzQ3MjI1LCJleHAiOjE1NTY4MzM2MjV9.g23zCN4yq7p1743fC6_qGZ_RtfiaGuQu-HL0ZKb-GD8']


def gendata(start, end):
  for i in range(start, end):
    response = requests.post(
        'http://localhost:8000/api/auth/register',
        data = {
          "name": "student" + str(i),
          "email": "student" + str(i) + "@asd.com",
          "age": "20",
          "password": "asdasd",
          "username": "student" + str(i),
          "isTeacher": False
        }
    )

    tokens.append(response.json()['token'])

  print(tokens)

def change_tokens():
    for token in tokens:
        print(token)

def readtokens():
  with open('tokens.txt') as f:
    for line in f:
      tokens.append(line.rstrip())

def joincourse(course=1):
  for t in tokens:
    response = requests.post(
      'http://localhost:8000/course/joincourse',
      data = {
        "joinKey": "4bf5a2de367d8fc9a38c4ccbb4c7469d"
      },
      headers={
        'x-access-token': t
      }
    )

    print(response.json())

t_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiaWF0IjoxNTU2NzQ3NDc2LCJleHAiOjE1NTY4MzM4NzZ9.wheb9OjzrDK_ZORUVy-QVPF1FJZM3p9wKgmY6aW0GjQ"
def createquiz(course=2, token=t_token, qname="DBMS_ENDSEM"):
  response = requests.post(
    "http://localhost:8000/quiz/createquiz",
    headers={'x-access-token': token, "Content-Type": "application/json"},
    data=json.dumps(json.loads("""
      {
        "accesskey":"DBMS",
        "quizname":""" + f"\"{qname}\"" + """,
        "qdata":[
            {
              "questiontext":"""+ f"\"{qname}" + """Question 1",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 2",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 3",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 4",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 5",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 6",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 7",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 8",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 9",
              "options":["Option1","Option2","Option3","Option4"]
            },
            {
              "questiontext":"""+ f"\"{qname}" + """Question 10",
              "options":["Option1","Option2","Option3","Option4"]
            }
          ],
        "answers":[2,2,1,4,1,2,3,3,1,4,4],
        "coursecid":2,
        "starttime":"2019-05-01T23:21:00.782Z",
        "endtime":"2019-05-02T00:17:00.782Z"
      }"""))
  )
  print(response.json())
  return response.json()[0]['quizid']

def startquiz(qid):
  for t in tokens:
    response = requests.post(
      'http://localhost:8000/quiz/startquiz',
      headers = {
        'x-access-token': t
      },
      data={'accesskey': 'DBMS', 'quizid': qid}
    )
    print(response.json())
answers = [2,2,1,4,1,2,3,3,1,4,4]
def randomresponses(quiz):
  for idx, t in enumerate(tokens):
    intelligence = intelligence_arr[idx]
    for i in range(10):
      response = requests.post(
        'http://localhost:8000/quiz/sendAnswer',
        data={'quizid':quiz, 'question': i, 'answer': answers[i] if random.randint(1,10) <= intelligence else random.randint(1, 4)},
        headers={'x-access-token': t}
      )

quizids = []
#readtokens()
for i in range(5):
  quizids.append(createquiz(qname="Quiz"+str(i)))
#joincourse(course=2)
intelligence_arr = []
for i in tokens:
    intelligence_arr.append(random.randint(1,10))

for q in quizids:
  startquiz(q)
  randomresponses(q)
