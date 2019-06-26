from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_pombos(request):
    return render(request, 'pombos.html')

def mostrar_rolezinho(request):
    roles = ['Bailão', 'Shopping União', 'Quermesse da Paróquia de São João', 'Calçadão de Osasco', 'SESC','Risca faca das 40']
    bairro = 'Rochdale'
    return render(request, 'rolezinho.html',{'roles':roles,'bairro':bairro})

def mostrar_cachorroquente(request):
    return render(request, 'cachorroquente.html')

def mostrar_assalto(request):
    return render(request, 'assalto.html')