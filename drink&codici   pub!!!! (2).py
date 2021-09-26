print('''       BENVENUTI AL
                          PUB
                              DRINK&CODICI  ''')

print('\nCiao sono Giangengiuarola cosa posso servirti????')
alcolici={'moyto':5,'margarita':6,'daiquiri':4,'birra':3}
analcolici={'moyto analcolico':4.50,'analcolico alla frutta':4.50,'tè al limone':2,
            'tè alla pesca':2,'coca cola':3}
print('prima  però mi servirebbe sabere:'+' come ti chiami')
nome_cliente=input()
print('quanti anni hai '+ nome_cliente+' ???')
anni_cliente=int(input())
#bgrngr    list
bibite=list(alcolici.keys())+list(analcolici.keys())
if anni_cliente <= 18:
    print('sei minorenne '+nome_cliente+' non posso servirti alcolici')
    print('possiamo offrirti queste bibite:')
    for analcolico in analcolici:
        #ye5h '%s:%d'
        print('%s:%d euro ' % (analcolico,analcolici [analcolico]))
else:
    print('sei maggiorenne '+nome_cliente+' quindi possiamo servirvi:')
    for bibita in bibite:
        print(bibita)


bibita_scelta=input()
while bibita_scelta not in bibite:
    print('abbiamo finito questa  bibita,riscegliete  tra la lista')
    
    bibita_scelta= input()
if anni_cliente <= 18:
    if bibita_scelta in alcolici:
        # cicloooooooooooooooooooooooooooooooooo
        print('non possiamo servirvi bibite alcoliche '+nome_cliente) 
        while bibita_scelta not in analcolici:
            print(nome_cliente+'scegli un'' altra bibita')
            bibita_scelta=input()
                
                
            
            
print('\necco lo scontrino, e alla prossima spero ')
print('\nindovinello:cosa fa un uccellino su phiton???')

while True:
    risposta=input()
    if risposta == 'chip':
        print('COMPLIMENTI RISPOSTA ESATTA!!!!')
        print('\nHAHAHAHAHAHA che bravo che sono nelle battute!!!!')
        break

    else:
        print('\nrisposta non esatta ritenta')
    
        
    
