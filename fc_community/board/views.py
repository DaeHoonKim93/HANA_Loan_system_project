from django.shortcuts import redirect, render
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_write(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        print(form)
        if form.is_valid():
            print("b")
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})
    # return redirect('/board/list')


def board_list(request):
    # boards = Board.objects.all().order_by('-id')

    # return render(request, 'board_list.html', {'boards': boards})
    return render(request, 'board_list.html')


def work_registration(request):
    # boards = Board.objects.all().order_by('-id')

    # return render(request, 'board_list.html', {'boards': boards})
    return render(request, 'work_registration.html')
