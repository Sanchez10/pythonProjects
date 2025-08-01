from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm


# Create your views here.
def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, "livros/listar.html", {"livros": livros})


def adicionar_livros(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_livros")
    else:
        form = LivroForm()

    return render(request, "livros/form.html", {"form": form})


def editar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)

    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect("listar_livros")
    else:
        form = LivroForm(instance=livro)

    return render(request, "livros/form.html", {"form": form})


def excluir_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()
    return redirect("listar_livros")
