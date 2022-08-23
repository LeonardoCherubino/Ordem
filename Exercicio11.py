# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

NumeroUm = int(input('Entre com um número: '))
NumeroDois = int(input('Entre com outro número: '))
NumeroTres = int(input('Entre com mais um número: '))

if NumeroUm > NumeroDois and NumeroUm > NumeroTres:
    
    print('O primeiro número maior é {}'.format(NumeroUm))
        
    if NumeroDois > NumeroTres:
        print('O segundo número maior é {}'.format(NumeroDois))
        print('O terceiro número maior: {}'.format(NumeroTres))

    else:

        print('O segundo número maior é {}'.format(NumeroTres))
        print('O terceiro número maior: {}'.format(NumeroDois))

elif NumeroDois > NumeroUm and NumeroDois > NumeroTres:

    print('O primeiro número maior é {}.'.format(NumeroDois))
    
    if NumeroUm > NumeroTres:
        print('O segundo número maior é {}'.format(NumeroUm))
        print('O terceiro maior número é {}'.format(NumeroTres))

    else:
        print('O segundo número maior é {}'.format(NumeroTres))
        print('O terceiro maior número é {}'.format(NumeroUm))


elif NumeroTres > NumeroUm and NumeroTres > NumeroDois:

    print('O primeiro maior número é {}'.format(NumeroTres))

    if NumeroUm > NumeroDois:

        print('O segundo número maior é {}'.format(NumeroUm))
        print('O terceiro maior número é {}'.format(NumeroDois))

    else:
        print('O segundo número maior é {}'.format(NumeroDois))
        print('O terceiro maior número é {}'.format(NumeroUm))