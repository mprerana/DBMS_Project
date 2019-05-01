from django.urls import path
from group import views
from .views import ListEventView

app_name = 'group'
urlpatterns = [
    path('groups_list/<int:p_id>', views.groups_list, name='group_list'),
    path('create_group/<int:p_id>', views.create_group, name='create_group'),
    path('edit_group/<int:g_id>', views.update_group, name='update_group'),
    path('event_list/<int:g_id>', views.event_list, name='event_list'),
    path('create_event/<int:g_id>', views.create_event, name='create_event'),
    path('edit_event/<int:event_id>', views.update_event, name='update_event'),
    path('members_list/<int:g_id>', views.members_list, name='members_list'),
    path('add_group_members/<int:g_id>', views.add_group_members, name='add_group_members'),
    path('request_member/<int:g_id>/<int:u_id>', views.request_member, name='request_member'),
    path('requested_members/<int:g_id>', views.requested_members, name='requested_members'),
    path('delete_request/<int:g_id>/<int:u_id>', views.delete_request, name='delete_request'),
    path('user_groups/<int:u_id>', views.user_groups, name='user_groups'),
    path('user_requested/<int:u_id>', views.user_requested, name='user_requested'),
    path('user_accept/<int:g_id>/<int:u_id>', views.user_accept, name='user_accept'),
    path('user_decline/<int:g_id>/<int:u_id>', views.user_decline, name='user_decline'),
    path('exit_group/<int:g_id>/<int:u_id>', views.exit_group, name='exit_group'),
    path('events/', views.events_location, name='events_location'),
    path('delete_event/<int:g_id>/<int:event_id>', views.delete_event, name='delete_event'),
    path('join_event/<int:e_id>', views.join_event, name='join_event'),
    path('leave_event/<int:e_id>', views.leave_event, name='leave_event'),
    path('add_comment/<int:e_id>/', views.add_comment, name='add_comment'),
    path('events/', ListEventView.as_view(), name="events-all"),
]
