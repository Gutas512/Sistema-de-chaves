from django.shortcuts import render
from django.shortcuts import render, redirect
from tcc_keylink.models import *

def index(request):
    return render(request, 'index.html')


def funcionario_list(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario_list.html', {'funcionarios': funcionarios})

def funcionario_detail(request, id_funcionario):
    # Fetch the Funcionario object based on the id
    funcionario = get_object_or_404(Funcionario, id_funcionario=id_funcionario)
    return render(request, 'funcionario_detail.html', {'funcionario': funcionario})

def funcionario_create(request):
    if request.method == 'POST':
        # Coleta dados do formulário
        nome = request.POST['nome_funcionario']
        telefone = request.POST['telefone_funcionario']
        endereco = request.POST['endereco_funcionario']
        funcao = request.POST['funcao_funcionario']
        cpf = request.POST['cpf_funcionario']
        senha = request.POST['senha']
        tipo = request.POST['tipo_funcionario']

        # Cria o funcionário
        funcionario = Funcionario.objects.create(
            nome_funcionario=nome,
            telefone_funcionario=telefone,
            endereco_funcionario=endereco,
            funcao_funcionario=funcao,
            cpf_funcionario=cpf,
            senha=senha,
            tipo_funcionario=tipo
        )

        # Redireciona para a página de sucesso ou lista de funcionários
        return redirect('funcionario_list')  # Alterar para o nome da URL de sua lista de funcionários

    return render(request, 'funcionario_create.html')


def funcionario_edit(request, id_funcionario):
    funcionario = get_object_or_404(Funcionario, id_funcionario=id_funcionario)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')  # Redirect to the list after saving
    else:
        form = FuncionarioForm(instance=funcionario)

    return render(request, 'funcionario_form.html', {'form': form})

def funcionario_delete(request, id_funcionario):
    funcionario = get_object_or_404(Funcionario, id_funcionario=id_funcionario)

    if request.method == 'POST':
        funcionario.delete()
        messages.success(request, "Funcionário excluído com sucesso!")
        return redirect('funcionario_list')  # Redirect to the list after deletion

    return render(request, 'funcionario_confirm_delete.html', {'funcionario': funcionario})

def sala_list(request):
    return render(request, 'sala_list.html')

def registro_list(request):
    return render(request, 'registro_list.html')
