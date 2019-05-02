from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.db import connection
import json
from collections import OrderedDict
import datetime
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser, FileUploadParser
import os.path
from django.core.files.base import ContentFile
import base64
import six
import uuid


class WorkViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM literature_work where uploader_id= %s", [pk])
            tupleofuploads = cursor.fetchall()

            listofworks = []

            for tupleofworks in tupleofuploads:
                listofworks.append(OrderedDict(
                    [('id', tupleofworks[0]),
                     ('work_title', tupleofworks[1]),
                     ('author', tupleofworks[2]),
                     ('description', tupleofworks[3]),
                     ('timestamp', tupleofworks[4]),
                     ('genre', tupleofworks[5]),
                     ('thumbnail', 'http://127.0.0.1:8000/media/' +
                      tupleofworks[6]),
                     ('file', 'http://127.0.0.1:8000/media/' + tupleofworks[7]),
                     ('uploader_id', tupleofworks[8])
                     ]))

        return Response(listofworks)


class WorkDetailsViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM literature_work where id = %s", [pk]
            )
            tupleofworkdetails = cursor.fetchone()

            cursor.execute(
                "SELECT username, first_name, last_name, email FROM auth_user where id= %s", [tupleofworkdetails[8]])

            user = cursor.fetchone()

            workdetails = OrderedDict(
                [('id', tupleofworkdetails[0]),
                 ('work_title', tupleofworkdetails[1]),
                 ('author', tupleofworkdetails[2]),
                 ('description', tupleofworkdetails[3]),
                 ('timestamp', tupleofworkdetails[4]),
                 ('genre', tupleofworkdetails[5]),
                 ('thumbnail', 'http://127.0.0.1:8000/media/' +
                  tupleofworkdetails[6]),
                 ('file', 'http://127.0.0.1:8000/media/' +
                  tupleofworkdetails[7]),
                 ('uploader_id', tupleofworkdetails[8]),
                 ('username', user[0]),
                 ('first_name', user[1]),
                 ('last_name', user[2]),
                 ('email', user[3])
                 ])

            # Rating

            cursor.execute(
                "SELECT * FROM opinion_rating WHERE book_id = %s", [pk])
            tupleofratings = cursor.fetchall()

            allratings = []

            for i in tupleofratings:
                cursor.execute(
                    "SELECT username FROM auth_user WHERE id = %s", [i[4]])
                username = cursor.fetchone()

                rating = OrderedDict(
                    [('id', i[0]),
                     ('rating', i[1]),
                     ('timestamp', i[2]),
                     ('user', username[0]),

                     ])

                allratings.append(rating)

            workdetails.update({"allratings": allratings})

            # Review

            cursor.execute(
                "SELECT * FROM opinion_review WHERE book_id = %s", [pk])
            tupleofreviews = cursor.fetchall()

            allreviews = []

            for i in tupleofreviews:
                cursor.execute(
                    "SELECT username FROM auth_user WHERE id = %s", [i[4]])
                username = cursor.fetchone()

                review = OrderedDict(
                    [('id', i[0]),
                     ('timestamp', i[1]),
                     ('content', i[2]),
                     ('user', username[0]),
                     ])

                allreviews.append(review)

            workdetails.update({"allreviews": allreviews})

        return Response(workdetails)


class GetAllWorks(APIView):
    def get(self, request, ):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM literature_work")
            tupleofuploads = cursor.fetchall()

            print(tupleofuploads)

            listofworks = []

            for tupleofworks in tupleofuploads:
                cursor.execute(
                    "SELECT username FROM auth_user where id=%s", str(tupleofworks[8]))
                user = cursor.fetchone()

                print(user)

                listofworks.append(OrderedDict(
                    [('id', tupleofworks[0]),
                     ('work_title', tupleofworks[1]),
                     ('author', tupleofworks[2]),
                     ('description', tupleofworks[3]),
                     ('timestamp', tupleofworks[4]),
                     ('genre', tupleofworks[5]),
                     ('thumbnail', 'http://127.0.0.1:8000/media/' + tupleofworks[6]),
                     ('file', 'http://127.0.0.1:8000/media/' + tupleofworks[7]),
                     ('uploader_id', tupleofworks[8]),
                     ("username", user[0])

                     ]))

        return Response(listofworks)


class WorkDeleteViewSet(APIView):
    def delete(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM literature_readinglist_books WHERE work_id = %s", [pk]
            )
            cursor.execute(
                "DELETE FROM opinion_rating WHERE book_id = %s", [pk]
            )
            cursor.execute(
                "DELETE FROM opinion_review WHERE book_id = %s", [pk]
            )
            cursor.execute(
                "DELETE FROM literature_work WHERE id = %s", [pk]
            )

        response = pk

        return Response(response)


class WorkPostViewSet(APIView):

    # parser_classes = (JSONParser, FormParser, MultiPartParser)
    def post(self, request, pk):
        time = datetime.datetime.now()
        time = str(time)
        # data = request.data.get('work')
        data = request.data
        print(data)

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT username FROM auth_user where id= %s", [pk])

            user = cursor.fetchone()

        thumbnail = data['thumbnail']
        # print('*******')
        # print(data.get('file'))

        # def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(thumbnail, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in thumbnail and ';base64,' in thumbnail:
                # Break out the header from the base64 content
                header, thumbnail = thumbnail.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(thumbnail)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            # file_extension = self.get_file_extension(file_name, decoded_file)
            file_extension = header.split('/')[-1]
            complete_file_name1 = "%s.%s" % (file_name, file_extension,)
            dir_path = os.path.dirname(os.path.realpath(__file__))
            if dir_path.endswith('\Literature'):
                dir_path = dir_path[:-11]
                dir_path.replace('\\', '/')
            # save_path = dir_path+ 'Project/media/thumbnails/'+user[0]+'/'+data.get('work_title')+'/'+complete_file_name

            save_path = os.path.join(dir_path, 'Project', 'media', 'thumbnails', user[0], data['work_title'], )
            if not os.path.isdir(save_path):
                os.makedirs(save_path)

            # thumbnail = ContentFile(decoded_file, name=complete_file_name)

            image_result = open(save_path + '/' + complete_file_name1, 'wb')
            image_result.write(decoded_file)

        file = data['file']

        if isinstance(file, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in file and ';base64,' in file:
                # Break out the header from the base64 content
                header, file = file.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(file)
            except TypeError:
                self.fail('invalid_file')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            # file_extension = self.get_file_extension(file_name, decoded_file)
            file_extension = header.split('/')[-1]
            complete_file_name = "%s.%s" % (file_name, file_extension,)
            dir_path = os.path.dirname(os.path.realpath(__file__))
            if dir_path.endswith('\Literature'):
                dir_path = dir_path[:-11]
                dir_path.replace('\\', '/')
            # save_path = dir_path+ 'Project/media/thumbnails/'+user[0]+'/'+data.get('work_title')+'/'+complete_file_name

            save_path = os.path.join(dir_path, 'Project', 'media', 'files', user[0], data['work_title'], )
            if not os.path.isdir(save_path):
                os.makedirs(save_path)

            # thumbnail = ContentFile(decoded_file, name=complete_file_name)

            file_result = open(save_path + '/' + complete_file_name, 'wb')
            file_result.write(decoded_file)

            thumbnail = 'thumbnails/' + user[0] + '/' + data.get('work_title') + '/' + complete_file_name1
            file = 'files/' + user[0] + '/' + data.get('work_title') + '/' + complete_file_name

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO literature_work (work_title, author, uploader_id, timestamp, description, genre, thumbnail, file) VALUES( %s, %s, %s, %s, %s, %s, %s, %s)",
                [data['work_title'], data['author'], pk, time, data['description'], data['genre'], thumbnail, file])

            cursor.execute(
                "SELECT * FROM literature_work WHERE uploader_id = %s and work_title = %s", [pk, data['work_title']])

            work = cursor.fetchone()

            insertedwork = OrderedDict(
                [('id', work[0]),
                 ('work_title', work[1]),
                 ('author', work[2]),
                 ('description', work[3]),
                 ('timestamp', work[4]),
                 ('genre', work[5]),
                 ('thumbnail', work[6]),
                 ('file', work[7]),
                 ('uploader_id', work[8]),
                 ])

        return Response(insertedwork)


# class WorkViewSet(viewsets.ModelViewSet):
#     queryset = Work.objects.all()
#     serializer_class = WorkSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# class ReadingListViewSet(viewsets.ModelViewSet):
#     queryset = ReadingList.objects.all()
#     serializer_class = ReadingListSerializer


class BlogListViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM literature_blog WHERE uploader_id= %s", [pk])

            tupleofblogs = cursor.fetchall()

            listofblogs = []

            for tupleofblog in tupleofblogs:
                listofblogs.append(OrderedDict(
                    [('id', tupleofblog[0]),
                     ('blog_title', tupleofblog[1]),
                     ('blog_content', tupleofblog[2]),
                     ('timestamp', tupleofblog[3]),
                     ('uploder_id', tupleofblog[4]), ]
                ))

        return Response(listofblogs)


class BlogPostViewSet(APIView):

    def post(self, request, pk):
        time = datetime.datetime.now()
        time = str(time)

        data = request.data.get('addblog')

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO literature_blog (blog_title, blog_content, timestamp, uploader_id) VALUES( %s,%s,%s,%s )",
                [data['blog_title'], data['blog_content'], time, pk])

            cursor.execute(
                "SELECT * FROM literature_blog WHERE uploader_id = %s and timestamp=%s", [pk, time])

            tupleofblog = cursor.fetchone()

            listofblogs = OrderedDict(
                [('id', tupleofblog[0]),
                 ('blog_title', tupleofblog[1]),
                 ('blog_content', tupleofblog[2]),
                 ('timestamp', tupleofblog[3]),
                 ('uploader_id', tupleofblog[4]), ]
            )
        return Response(listofblogs)


class BlogDeleteViewSet(APIView):

    def delete(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM literature_blog WHERE id=%s", [pk])

        response = pk

        return Response(response)


class ReadingListViewSet(APIView):
    def get(self, request, pk):
        print("pk= %s" % pk)
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM literature_readinglist where related_user_id= %s", [pk])
            tupleofreadlists = cursor.fetchall()

            listoflists = []

            for tupleoflists in tupleofreadlists:
                listoflists.append(OrderedDict(
                    [('id', tupleoflists[0]),
                     ('r_list_name', tupleoflists[1]),
                     ('related_user_id', tupleoflists[2])
                     ]))

                length = len(listoflists)

        return Response(listoflists)


class ReadingListPostViewSet(APIView):

    def post(self, request, pk):
        data = request.data.get('addlist')
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO literature_readinglist ( r_list_name,related_user_id ) VALUES( %s,%s )",
                [data['r_list_name'], pk])

            cursor.execute(
                "SELECT * FROM literature_readinglist WHERE related_user_id = %s AND r_list_name= %s",
                [pk, data['r_list_name']])

            readlist = cursor.fetchone()

            insertedlist = OrderedDict(
                [('id', readlist[0]),
                 ('r_list_name', readlist[1]),
                 ('related_user_id', readlist[2]),
                 ])

        return Response(insertedlist)


class ReadingListDeleteViewSet(APIView):
    def delete(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM literature_readinglist_books WHERE readinglist_id = %s", [pk]
            )
            cursor.execute(
                "DELETE FROM literature_readinglist WHERE id = %s", [pk])

        response = pk

        return Response(response)


# class ReadingListWorksPostViewSet(APIView):
#     def post(self, request, pk):
#         data = request.data.get('addwork')
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "INSERT INTO literature_readinglist_books (work_title, )"
#             )


class ReadingListWorksViewSet(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM literature_readinglist where id=%s", [pk]
            )
            readlist = cursor.fetchone()

            worksinreadinglist = OrderedDict(
                [('id', readlist[0]),
                 ]
            )

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT literature_work.id,work_title,author,uploader_id FROM literature_work INNER JOIN literature_readinglist_books on literature_readinglist_books.work_id = literature_work.id where readinglist_id= %s",
                [pk])
            tupleofworksinreadlist = cursor.fetchall()

            listofworksinreadlist = []

            for tupleofworks in tupleofworksinreadlist:
                cursor.execute(
                    "SELECT username FROM auth_user where id=%s", str(tupleofworks[3]))
                user = cursor.fetchone()

                listofworksinreadlist.append(OrderedDict(
                    [('id', tupleofworks[0]),
                     ('work_title', tupleofworks[1]),
                     ('author', tupleofworks[2]),
                     ('uploader_id', tupleofworks[3]),
                     ('username', user[0])
                     ]))

            worksinreadinglist.update({"works": listofworksinreadlist})

        return Response(worksinreadinglist)


class ReadingListWorksPostViewSet(APIView):
    def post(self, request, pk):
        data = request.data.get('addworktolist')

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO literature_readinglist_books ( readinglist_id,work_id ) VALUES( %s,%s )",
                [pk, data['work_id']])

            cursor.execute(
                "SELECT literature_work.id,work_title,author,uploader_id FROM literature_work INNER JOIN literature_readinglist_books on literature_readinglist_books.work_id = literature_work.id where readinglist_id= %s and work_id=%s",
                [pk, data['work_id']])

            addedwork = cursor.fetchone()

            insertedwork = OrderedDict(
                [('id', addedwork[0]),
                 ('work_title', addedwork[1]),
                 ('author', addedwork[2]),
                 ('uploader_id', addedwork[2]),
                 ])

        return Response(insertedwork)


class ReadingListWorksDeleteViewSet(APIView):
    def delete(self, request, pk):
        pklist = pk.split('n')
        pk1 = pklist[0]
        pk2 = pklist[1]
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM literature_readinglist_books WHERE readinglist_id=%s and work_id=%s", [
                    pk1, pk2]
            )

        response = pk

        return Response(response)


class GetFeed(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM literature_work where uploader_id in (SELECT user_id FROM user_follow where follower_id = %s) ORDER BY timestamp DESC",
                [pk])
            tupleofuploads = cursor.fetchall()

            feed = []

            for tupleofworks in tupleofuploads:
                cursor.execute(
                    "SELECT username FROM auth_user where id= %s", [tupleofworks[8]])

                user = cursor.fetchone()

                feed.append(OrderedDict(
                    [('id', tupleofworks[0]),
                     ('work_title', tupleofworks[1]),
                     ('author', tupleofworks[2]),
                     ('description', tupleofworks[3]),
                     ('timestamp', tupleofworks[4]),
                     ('genre', tupleofworks[5]),
                     ('thumbnail', 'http://127.0.0.1:8000/media/' +
                      tupleofworks[6]),
                     ('file', 'http://127.0.0.1:8000/media/' +
                      tupleofworks[7]),
                     ('uploader_id', tupleofworks[8]),
                     ('user', user[0])
                     ]))

        return Response(feed)


class GetBlogs(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM literature_blog where uploader_id in (SELECT user_id FROM user_follow where follower_id = %s) ORDER BY timestamp DESC",
                [pk])
            tupleofblogs = cursor.fetchall()

            print(tupleofblogs)

            listofblogs = []

            for tupleofblog in tupleofblogs:
                cursor.execute(
                    "SELECT username FROM auth_user where id= %s", [tupleofblog[4]])

                user = cursor.fetchone()

                listofblogs.append(OrderedDict(
                    [('id', tupleofblog[0]),
                     ('blog_title', tupleofblog[1]),
                     ('blog_content', tupleofblog[2]),
                     ('timestamp', tupleofblog[3]),
                     ('uploader_id', tupleofblog[4]),
                     ('username', user[0])
                     ]))

        return Response(listofblogs)
