from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Signup
from django.contrib import messages
from .forms import SignUpForm

def homepage_f(request):
    return render(request, 'homepage.html')


def articles_f(request):
    return render(request, 'article.html')

def signup_f(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                # Save the form only if it is valid
                form.save()
                # Redirect to a success page, or you can customize this part as needed
                return redirect('/login')
            except Exception as e:
                print('Error ---- ', e)
                messages.error(request, 'Signup failed. An error occurred during form submission.')
        else:
            # Display all error messages
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f'{field.capitalize()}: {error}')
            messages.error(request, f'{" ".join(error_messages)}')
            print(form.errors)
            return redirect('signup_f')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def login_f(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Signup.objects.get(username=username, password=password)
        except Signup.DoesNotExist:
            user = None

        if user is not None:
            # Perform login logic here if needed
            # Redirect to a success page, or you can customize this part as needed
            return redirect('/')  # Change '/dashboard' to the appropriate URL
        else:
            # Display error message for invalid credentials
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
