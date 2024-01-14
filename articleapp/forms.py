from django import forms
from .models import Signup
from uuid import uuid4

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth', 'password']
           
    def save(self, commit=True):
        uuid = str(uuid4())
        instance = super().save(commit=False)
        instance.user_uuid = uuid  # Generate uuid4 and assign it to user_uuid
        if commit:
            instance.save()
        return instance

    # You can add any additional form validation or customization here if needed
