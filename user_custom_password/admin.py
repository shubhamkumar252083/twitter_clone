from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'mobile','is_admin')
    list_filter = ('is_admin', )
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'mobile', 'password', 'raw_password')}),
        ('Personal info', {'fields': ("name", "address")}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'id', 'mobile', 'name')
    ordering = ('email', 'id')
    filter_horizontal = ()

    '''
    def save_model(self, request, obj, form, change):
        # print(f'form ==> {form}')
        print(f'obj.password ==> {obj.password}')
        print(f'change ==> {change}')
        # Your custom modification logic here
        obj.email = obj.email.lower()  # For example, convert the email to lowercase
        obj.save()
    '''


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)