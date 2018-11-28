from django.shortcuts import redirect

def login_auth(func):
    """
    登录验证
    """
    def login_fun(request, *args, **kwargs):
        if request.COOKIES.get('user') != None:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login')

    return login_fun