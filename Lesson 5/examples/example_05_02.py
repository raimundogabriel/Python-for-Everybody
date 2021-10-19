#exemple of computing things inside a function
def greet(lang) :
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bonjour')
    elif lang == 'br' :
        print('Olá!')
    else :
        print('Hello')

greet('es')
greet('br')
greet('jp')
greet('fr')
greet('cn')