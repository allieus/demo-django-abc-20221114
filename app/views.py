from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from app.forms import CommentForm
from app.models import Movie, Comment


def index(request):
    return render(request, "app/index.html", {
        "movie_list": Movie.objects.all(),
    })


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comment_list = movie.comment_set.all()
    comment_form = CommentForm()
    # comment_list = Comment.objects.filter(movie=movie)

    return render(request, "app/movie_detail.html", {
        "movie": movie,
        "comment_list": comment_list,
        "comment_form": comment_form,
    })


@login_required
def comment_new(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():  # <= message 필드에 대해서만 유효성 검사
            comment = form.save(commit=False)  # 내부적으로 comment.save()가 호출 X
            comment.author = request.user
            comment.movie = movie
            comment.save()
            redirect_url = f"/{comment.movie.pk}/"  # Ugly
            return redirect(redirect_url)
    else:
        form = CommentForm()
    return render(request, "app/comment_form.html", {
        "form": form,
    })



@login_required
def comment_edit(request, movie_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            redirect_url = f"/{comment.movie.pk}/"  # Ugly
            return redirect(redirect_url)
    else:
        form = CommentForm(instance=comment)
    return render(request, "app/comment_form.html", {
        "form": form,
    })

