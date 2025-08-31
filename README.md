# CISC-Calendar-System
CISC-Calendar-System/
├── backend/
│   ├── cisc_vhub/                  # Django project folder (config)
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── apps/
│   │   ├── users/                  # User authentication and roles
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   ├── forms.py
│   │   │   └── serializers.py
│   │   │
│   │   └── calendar_app/           # Calendar management
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── models.py
│   │       ├── views.py
│   │       └── urls.py
│   │
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/                       # HTML templates for the apps
│   ├── users/                      # All HTML for users
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── profile.html
│   │   ├── manage_users.html
│   │   └── ...                     # other user templates
│   │
│   └── calendar/                   # All HTML for calendar_app
│       ├── add_event.html
│       ├── approve_events.html
│       ├── view_events.html
│       └── calendar_home.html
│
└── README.md

