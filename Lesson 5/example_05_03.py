#using return statement in functions
def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'Bonjour'
    elif lang == 'br' :
        return 'Olá!'
    else :
        return 'Hello'
print(greet('es'),'Glenn')
print(greet('br'),'Sally')
print(greet('jp'),'Michael')
print(greet('fr'),'Daniel')
print(greet('cn'),'Gabriel')