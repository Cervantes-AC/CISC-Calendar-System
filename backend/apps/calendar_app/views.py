from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Event
from .forms import EventForm

# ---------------------------
# Org Officer: Add Event
# ---------------------------
@login_required
def add_event(request):
    if request.user.role.lower() != 'officer':
        messages.error(request, "Access denied")
        return redirect('users:dashboard_view')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            # For immediate visibility in JSON, set approved; otherwise use 'pending'
            event.status = 'pending'  
            event.save()
            messages.success(request, "Event submitted for approval")
            return redirect('calendar:add_event')
    else:
        form = EventForm()

    return render(request, 'calendar/add_event.html', {'form': form})


# ---------------------------
# Org Officer: Manage own events
# ---------------------------
@login_required
def manage_calendar(request):
    if request.user.role.lower() != 'officer':
        messages.error(request, "Access denied")
        return redirect('users:dashboard_view')

    # Fixed: order by existing fields
    events = Event.objects.filter(created_by=request.user).order_by('date', 'time')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.status = 'pending'
            event.save()
            messages.success(request, "Event submitted for approval")
            return redirect('calendar:manage_calendar')
    else:
        form = EventForm()

    return render(request, 'calendar/manage_calendar.html', {
        'events': events,
        'form': form
    })


# ---------------------------
# Admin: Event Approval
# ---------------------------
@login_required
def approval(request):
    events = Event.objects.filter(status='pending').order_by('date', 'time')
    return render(request, 'calendar/approval.html', {'events': events})


@login_required
def update_event_status(request, event_id, status):
    if request.user.role.lower() != 'admin':
        messages.error(request, "Access denied")
        return redirect('users:dashboard_view')

    event = get_object_or_404(Event, id=event_id)
    if status.lower() in ['approved', 'rejected']:
        event.status = status.lower()
        event.is_approved = True if status.lower() == 'approved' else False
        event.save()
        messages.success(request, f"Event {status.lower()}")
    return redirect('calendar:approval')


# ---------------------------
# Students/Faculty: View Calendar
# ---------------------------
@login_required
def view_events(request):
    events = Event.objects.filter(status='approved').order_by('date', 'time')
    return render(request, 'calendar/view_events.html', {'events': events})


# ---------------------------
# Calendar JSON endpoint
# ---------------------------
def events_json(request):
    """
    Public JSON endpoint for events (e.g., FullCalendar).
    Returns only approved events for students/faculty/public.
    """
    # Return only approved events
    events = Event.objects.filter(status='approved').order_by('date', 'time')

    data = []
    for e in events:
        data.append({
            'id': e.id,
            'title': e.title,
            'start': e.start_datetime.isoformat(),  # combines date + time
            'description': e.description,
            'status': e.status,
            'created_by': e.created_by.username
        })
    return JsonResponse(data, safe=False)


# ---------------------------
# Redirect based on role
# ---------------------------
@login_required
def calendar_home(request):
    role = request.user.role.lower()
    if role == 'officer':
        return redirect('calendar:add_event')
    elif role == 'admin':
        return redirect('calendar:admin_calendar')
    else:  # student/faculty
        return redirect('calendar:view_events')


# ---------------------------
# Admin: View full calendar
# ---------------------------
@login_required
def admin_calendar(request):
    if request.user.role.lower() != 'admin':
        messages.error(request, "Access denied")
        return redirect('users:dashboard_view')

    return render(request, 'calendar/admin_calendar.html')
