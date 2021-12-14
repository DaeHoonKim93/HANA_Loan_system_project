from django.shortcuts import redirect


def is_login(func):  #데코레이터 명명
    def decorated(request, *args, **kwargs):

        session = request.session.get('user')  # 로그인시 저장한 사용자 아이디 session 부름

        # 세션 여부 체크
        if (session != None or session == ''):  # 있다면 통과
            return func(request, *args, **kwargs)
        else:  # 세션 없다면, 로그인 창으로 return
            return redirect('/')

    return decorated