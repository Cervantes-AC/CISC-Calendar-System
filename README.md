# CISC-Calendar-System
cisc_vhub/
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
│   │   │   ├── serializers.py      # if using DRF later
│   │   │   └── templates/users/    # Optional if using Django templates
│   │   │
│   │   └── calendar_app/           # Calendar management
│   │       ├── __init__.py
│   │       ├── admin.py
│   │       ├── apps.py
│   │       ├── models.py
│   │       ├── views.py
│   │       ├── urls.py
│   │       └── templates/calendar_app/
│   │
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/                       # Optional: static HTML templates / SPA
│   ├── css/
│   ├── js/
│   └── index.html
│
└── README.md
