from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    if request.user.role.lower() != 'admin':
        messages.error(request, "Access denied")
        return redirect('users:dashboard_view')

    # Get all pending events
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
# Redirect based on role
# ---------------------------
@login_required
def calendar_home(request):
    role = request.user.role.lower()
    if role == 'officer':
        return redirect('calendar:add_event')
    elif role == 'admin':
        return redirect('calendar:approval')  # ✅ fixed
    else:  # student/faculty
        return redirect('calendar:view_events')
