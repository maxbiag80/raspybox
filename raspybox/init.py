from auth import auth

admin = auth.User(username='admin', admin=True, active=True)
admin.set_password('admin')
admin.email = 'admin@localhost.it'
admin.save()

