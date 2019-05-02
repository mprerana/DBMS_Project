# REFERENCE
# latest_review_list = rate.objects.order_by('-published_date')
#         form = ReviewForm()
#         a = rate.objects.values('rating')
#         t=len(a)
#         avg,one,two,three,four,five=0,0,0,0,0,0
#         for i in range(len(a)):
#             avg+=a[i]['rating']
#             if (a[i]['rating'] == 5):
#                 five += 1
#             if (a[i]['rating'] == 4):
#                 four += 1
#             if (a[i]['rating'] == 3):
#                 three += 1
#             if (a[i]['rating'] == 2):
#                 two += 1
#             if (a[i]['rating'] == 1):
#                 one += 1
#         avg = round(avg/(len(a)),2)


# transaction.commit()
# # service.objects.create(service_name=org)
#
# #
# # inst = rate()
# # inst.service_type = type
# # inst.service_name = org
# # inst.user_name = user_name
# # inst.rating = rating
# # inst.comment = comment
# # inst.published_date = datetime.datetime.now()
# #
# # inst.save()
# return redirect('review_list')
# # else:
# #     form = ReviewForm()
# # context = {'form': form, }
# # return render(request,'user_reviews/rev    # else:iew_list.html',context)
# return HttpResponse('invalid!!!')





# cursor.execute("SELECT * FROM user_reviews_rate ORDER BY rating DESC")
            # latest_review_list=cursor.fetchall()

# cursor = connection.cursor()
            # cursor.execute("SELECT * FROM user_reviews_rate ORDER BY rating")
            # latest_review_list = cursor.fetchall()
            #
            # form = ReviewForm()
            # avg, one, two, three, four, five = 0, 0, 0, 0, 0, 0
            # cursor.execute("SELECT AVG(rating) FROM user_reviews_rate")
            # avg = cursor.fetchone()
            # avg = avg[0]
            #
            # cursor.execute("SELECT COUNT(rating) FROM user_reviews_rate WHERE rating=1")
            # one = cursor.fetchone()
            # one = one[0]
            #
            # cursor.execute("SELECT COUNT(rating) FROM user_reviews_rate WHERE rating=2")
            # two = cursor.fetchone()
            # two = two[0]
            #
            # cursor.execute("SELECT COUNT(rating) FROM user_reviews_rate WHERE rating=3")
            # three = cursor.fetchone()
            # three = three[0]
            #
            # cursor.execute("SELECT COUNT(rating) FROM user_reviews_rate WHERE rating=4")
            # four = cursor.fetchone()
            # four = four[0]
            #
            # cursor.execute("SELECT COUNT(rating) FROM user_reviews_rate WHERE rating=5")
            # five = cursor.fetchone()
            # five = five[0]

# body
# < !-- Fixed
# navbar -->
# < nav
#
#
# class ="navbar navbar-default navbar-fixed-top" >
#
# < div
#
#
# class ="container" >
#
# < div
#
#
# class ="navbar-header" >
#
# < button
# type = "button"
#
#
# class ="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar" >
#
# < span
#
#
# class ="sr-only" > Toggle navigation < / span >
#
# < span
#
#
# class ="icon-bar" > < / span >
#
# < span
#
#
# class ="icon-bar" > < / span >
#
# < span
#
#
# class ="icon-bar" > < / span >
#
# < / button >
# < a
#
#
# class ="navbar-brand" href="#" > Demo < / a >
#
# < / div >
# < div
# id = "navbar"
#
#
# class ="navbar-collapse collapse" >
#
# < ul
#
#
# class ="nav navbar-nav navbar-right" >
#
# < li > < a
# href = "../navbar/" > Default < / a > < / li >
# < / ul >
# < / div > <!-- /.nav - collapse -->
# < / div >
# < / nav >
"""
<form action="{% url 'add_review'%}" method="POST", autocomplete="off">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Add" />
</form>
"""