supermilai
==========

A initial of auth based on django.auth module on version 1.7


build-in permissions:

`
("change_other_userprofile", "Can Change others Profile"),
("stop_userprofile", "Can userprofile"),
("read_first_menu_account", "Can See the first menu of user management"),
("read_second_menu_user", "Can See the second menu of user management"),
("read_second_menu_group", "Can See the second menu of group"),
("read_second_menu_permission", "Can See the second menu of permission"),
`

├── account
│   ├── admin.py
│   ├── ajax.py
│   ├── backend_manage.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-34.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-34.pyc
│   │   ├── __init__.cpython-34.pyc
│   │   └── models.cpython-34.pyc
│   ├── templates
│   │   ├── base_account.html
│   │   ├── change_password.html
│   │   ├── group_add.html
│   │   ├── group_form.html
│   │   ├── group_list.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── perm_add.html
│   │   ├── perm_form.html
│   │   ├── perm_list.html
│   │   ├── user_add.html
│   │   ├── user_form.html
│   │   ├── user_list.html
│   │   └── view_profile.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── doc.yaml
├── LICENSE
├── manage.py
├── README.md
├── static
│   ├── css
│   │   └── fdv.css
│   ├── img
│   │   ├── input-spinner.gif
│   │   └── loading.gif
│   ├── js
│   │   └── maskcover.js
│   └── plugins
│       └── bootstrap-select
│           ├── js
│           │   ├── bootstrap-select.js
│           │   └── i18n
│           └── less
│               ├── bootstrap-select.less
│               └── variables.less
├── supermilai
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-34.pyc
│   │   └── settings.cpython-34.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
└── templates
    ├── base_proj.html
    ├── footer.html
    ├── home_page.html
    ├── navibar.html
    └── sidebar.html
