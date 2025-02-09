('app', [ # Корень
    ('dist', [ # Внутренний узел
        ('index.html'), # Лист
        ('main.py') # Лист
    ]),
    ('index.py'), # Лист
    ('assets', [ # Внутренний узел
        ('favicon.ico'), # Лист
        ('app.css'), # Лист #
    ]),
])

#                  app
#          /        |         \
#        dist    index.py   assets
#       /    \             /     \
# index.html main.py   favicon.ico app.css