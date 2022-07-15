from django.shortcuts import render, redirect # importa o redirecionamento
from django.contrib import messages, auth # mensagems e a auntenticacao
from django.core.validators import validate_email # valida o email
from django.contrib.auth.models import User # usado pra criar super usuario
from django.contrib.auth.decorators import login_required # autentica para ser liberado para a pagina principal
from .models import FormContato # puxa a classe formcontato do django

# funcao de login
def login(request):

    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuario ou senha invalidos!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso!')
        return redirect('dashboard')
    
    
# funcao de logout
def logout(request):
    auth.logout(request)
    return redirect('index')

# funcao de cadastro
def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode ficar vazio!')
        return render(request, 'accounts/cadastro.html')


    try:
        validate_email(email)
    
    except:
        messages.error(request, 'Email invalido!')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter ao menos 6 digitos!')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuario precisa ter ao menos 6 digitos!')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não estão iguais!!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuario já existe!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'accounts/cadastro.html')
    
    messages.success(request, 'Cadastrado com sucesso!, Agora faça login.')
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')

# verifica e funcao principal
@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form' : form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulario.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form' : form})
    
    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Precisa de mais caracteres.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form' : form})

    
    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    return redirect('dashboard')