from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from .models import Member, Group, Event, Attendance, CommunicationLog


@login_required
def dashboard(request):
    # Key stats
    total_members = Member.objects.count()
    active_members = Member.objects.filter(category='Member').count()
    inactive_members = total_members - active_members
    total_groups = Group.objects.count()
    group_sizes = Group.objects.annotate(member_count=Count('members')).values('name', 'member_count')
    communication_stats = CommunicationLog.objects.values('communication_type').annotate(count=Count('id'))

    # Search and filter
    query = request.GET.get('q', '')
    group_filter = request.GET.get('group', '')
    category_filter = request.GET.get('category', '')

    members = Member.objects.all()
    if query:
        members = members.filter(
            Q(full_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(home_address__icontains=query)
        )
    if group_filter:
        members = members.filter(ministry_group__id=group_filter)
    if category_filter:
        members = members.filter(category=category_filter)

    context = {
        'total_members': total_members,
        'active_members': active_members,
        'inactive_members': inactive_members,
        'total_groups': total_groups,
        'group_sizes': group_sizes,
        'communication_stats': communication_stats,
        'members': members[:50],  # Limit for performance
        'groups': Group.objects.all(),
        'query': query,
        'group_filter': group_filter,
        'category_filter': category_filter,
    }
    return render(request, 'app/dashboard.html', context)


@login_required
def attendance_report(request):
    event_id = request.GET.get('event')
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')

    attendances = Attendance.objects.all()
    if event_id:
        attendances = attendances.filter(event__id=event_id)
    if date_from:
        attendances = attendances.filter(event__date__gte=date_from)
    if date_to:
        attendances = attendances.filter(event__date__lte=date_to)

    # Group by event and status
    report = attendances.values('event__title', 'status').annotate(count=Count('id')).order_by('event__title', 'status')

    context = {
        'report': report,
        'events': Event.objects.all(),
        'event_id': event_id,
        'date_from': date_from,
        'date_to': date_to,
    }
    return render(request, 'app/attendance_report.html', context)
