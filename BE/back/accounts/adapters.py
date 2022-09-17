from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data

        user = super().save_user(request, user, form, False)
        # phone_number = data.get('phone_number')
        # user.phone_number = phone_number

        # addr = data.get('addr')
        # user.addr = addr

        # zip_code = data.get('zip_code')
        # user.zip_code = zip_code

        nickname = data.get('nickname')
        user.nickname = nickname

        email = data.get('email')
        user.email = email

        user.save()
        return user

