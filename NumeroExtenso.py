print ("PROGRAMA PARA ESCREVER POR EXTENSO DINHEIRO DE -999,99 À 999.99\n") 

while True:
    try:
        digitacao=input("Digite o número: ")
        valor    =float(digitacao)
    except ValueError:
        print ("Deve-se digitar um número monetário entre -999,99 e 999.99!")
    else:
        parte=digitacao.split(".")
        if parte[0]=="":
            parte[0]="0"
        elif parte[0]=="-":
            parte[0]="0"
        
        if len(parte)==1:
            parte.append("00")
        elif parte[1]=="":
            parte[1]="00"
        elif len(parte[1])==1:
            parte[1]=parte[1]+"0"
            
        if len(parte[1])>2:
            print ("Deve-se digitar um número monetário entre -999,99 e 999.99!")
        else:
            reais   =int(parte[0])
            centavos=int(parte[1])
            
            if reais<-999 or reais>999:
                print("O número digitado está fora da faixa solicitada!")
            elif reais==0 and centavos==0:
                print("zero reais")
            elif valor<0:
                print("menos ",end="")
                reais=-reais
        
            dig1centavos=centavos//10
            dig2centavos=centavos%10
            
            compreais = int(len(parte[0]))

            unidade = True
            if compreais == 3:
                centena = int(parte[0][0])
                dezena = int(parte[0][1])
                unidade = int(parte[0][2])

                #print(centena)
                if centena==1:
                    if dezena != 0 or unidade != 0:
                        print("cento ", end="")
                    else:
                        print("cem ",end="")
                elif centena==2:
                    print("duzentos ",end="")
                elif centena==3:
                    print("trezentos ",end="")
                elif centena==4:
                    print("quatroscentos ",end="")
                elif centena==5:
                    print("quinhentos ",end="")
                elif centena==6:
                    print("seiscentos ",end="")
                elif centena==7:
                    print("setescentos ",end="")
                elif centena==8:
                    print("oitoscentos ",end="")
                elif centena==9:
                    print("novescentos ",end="")

                if dezena != 0 or unidade != 0:
                    print("e ",end="")

                if dezena==1:
                    if unidade == 0:
                        print("dez ",end="")
                        unidade = True
                    elif unidade == 1:
                        print("onze ", end="")
                        unidade = False
                    elif unidade == 2:
                        print("doze ", end="")
                    elif unidade == 3:
                        unidade = False
                        print("treze ", end="")
                    elif unidade == 4:
                        unidade = False
                        print("quatorze ", end="")
                    elif unidade == 5:
                        unidade = False
                        print("quinze ", end="")
                    elif unidade == 6:
                        unidade = False
                        print("dezesseis ", end="")
                    elif unidade == 7:
                        unidade = False
                        print("edzessete ", end="")
                    elif unidade == 8:
                        unidade = False
                        print("dezoito ", end="")
                    elif unidade == 9:
                        unidade = False
                        print("dezenove ", end="")
          
                elif dezena==2:
                    print("vinte ",end="")
                elif dezena==3:
                    print("trinta ",end="")
                elif dezena==4:
                    print("quarenta ",end="")
                elif dezena==5:
                    print("cinquenta ",end="")
                elif dezena==6:
                    print("sessenta ",end="")
                elif dezena==7:
                    print("setenta ",end="")
                elif dezena==8:
                    print("oitenta ",end="")
                elif dezena==9:
                    print("noventa ",end="")
                if unidade != 0:
                    print("e ",end="")

                if unidade==1:
                    print("um ",end="")
                elif unidade==2:
                    print("dois ",end="")
                elif unidade==3:
                    print("três ",end="")
                elif unidade==4:
                    print("quatro ",end="")
                elif unidade==5:
                    print("cinco ",end="")
                elif unidade==6:
                    print("seis ",end="")
                elif unidade==7:
                    print("sete ",end="")
                elif unidade==8:
                    print("oito ",end="")
                elif unidade==9:
                    print("nove ",end="")

            
            if compreais == 2:
                dezena = int(parte[0][0])
                unidade = int(parte[0][1])
                #print(dezena)
                if dezena==1:
                    if unidade == 0:
                        print("dez ",end="")
                        unidade = True
                    elif unidade == 1:
                        print("onze ", end="")
                        unidade = False
                    elif unidade == 2:
                        print("doze ", end="")
                    elif unidade == 3:
                        unidade = False
                        print("treze ", end="")
                    elif unidade == 4:
                        unidade = False
                        print("quatorze ", end="")
                    elif unidade == 5:
                        unidade = False
                        print("quinze ", end="")
                    elif unidade == 6:
                        unidade = False
                        print("dezesseis ", end="")
                    elif unidade == 7:
                        unidade = False
                        print("edzessete ", end="")
                    elif unidade == 8:
                        unidade = False
                        print("dezoito ", end="")
                    elif unidade == 9:
                        unidade = False
                        print("dezenove ", end="")
          
                elif dezena==2:
                    print("vinte ",end="")
                elif dezena==3:
                    print("trinta ",end="")
                elif dezena==4:
                    print("quarenta ",end="")
                elif dezena==5:
                    print("cinquenta ",end="")
                elif dezena==6:
                    print("sessenta ",end="")
                elif dezena==7:
                    print("setenta ",end="")
                elif dezena==8:
                    print("oitenta ",end="")
                elif dezena==9:
                    print("noventa ",end="")
                if unidade != 0:
                    print("e ",end="")

                if unidade == 1 and dezena != 1:
                    print("um ",end="")
                elif unidade == 2 and dezena != 1:
                    print("dois ",end="")
                elif unidade == 3 and dezena != 1:
                    print("três ",end="")
                elif unidade == 4 and dezena != 1:
                    print("quatro ",end="")
                elif unidade == 5 and dezena != 1:
                    print("cinco ",end="")
                elif unidade == 6 and dezena != 1:
                    print("seis ",end="")
                elif unidade == 7 and dezena != 1:
                    print("sete ",end="")
                elif unidade == 8 and dezena != 1:
                    print("oito ",end="")
                elif unidade == 9 and dezena != 1:
                    print("nove ",end="")

            
            if compreais == 1:
                unidade = int(parte[0][0])
               # print (unidade)
                if unidade==1:
                    print("um ",end="")
                elif unidade==2:
                    print("dois ",end="")
                elif unidade==3:
                    print("três ",end="")
                elif unidade==4:
                    print("quatro ",end="")
                elif unidade==5:
                    print("cinco ",end="")
                elif unidade==6:
                    print("seis ",end="")
                elif unidade==7:
                    print("sete ",end="")
                elif unidade==8:
                    print("oito ",end="")
                elif unidade==9:
                    print("nove ",end="")
                
            if reais==1:
                print("real ",end="")
            elif reais!=0:
                print("reais ",end="")
                
            if reais!=0 and centavos!=0:
                print("e ",end="")
                
            if centavos==10:
                print("dez ",end="")
            elif centavos==11:
                print("onze ",end="")
            elif centavos==12:
                print("doze ",end="")
            elif centavos==13:
                print("treze ",end="")
            elif centavos==14:
                print("quatorze ",end="")
            elif centavos==15:
                print("quinze ",end="")
            elif centavos==16:
                print("dezesseis ",end="")
            elif centavos==17:
                print("dezessete ",end="")
            elif centavos==18:
                print("dezoito ",end="")
            elif centavos==19:
                print("dezenove ",end="")
            elif dig1centavos==2:
                print("vinte ",end="")
            elif dig1centavos==3:
                print("trinta ",end="")
            elif dig1centavos==4:
                print("quarenta ",end="")
            elif dig1centavos==5:
                print("cinquenta ",end="")
            elif dig1centavos==6:
                print("sessenta ",end="")
            elif dig1centavos==7:
                print("setenta ",end="")
            elif dig1centavos==8:
                print("oitenta ",end="")
            elif dig1centavos==9:
                print("noventa ",end="")
                
            if dig1centavos!=1 and dig2centavos!=0:
                if dig1centavos!=0:
                    print("e ",end="")
                
                if dig2centavos==1:
                    print("um ",end="")
                elif dig2centavos==2:
                    print("dois ",end="")
                elif dig2centavos==3:
                    print("três ",end="")
                elif dig2centavos==4:
                    print("quatro ",end="")
                elif dig2centavos==5:
                    print("cinco ",end="")
                elif dig2centavos==6:
                    print("seis ",end="")
                elif dig2centavos==7:
                    print("sete ",end="")
                elif dig2centavos==8:
                    print("oito ",end="")
                elif dig2centavos==9:
                    print("nove ",end="")
                    
            if centavos==1:
                print("centavo")
            elif centavos!=0:
                print("centavos")
                
    while True:
        resposta=input("\n\nDeseja escrever por extenso outro valor monetário entre -999.99 e 999.99? (S/N): ").upper()
        if resposta!="S" and resposta!="N":
            print("Você deve responder ou S, ou N; tente novamente!")
        else:
            break
    
    if resposta=="N":
        break

print("\nOBRIGADO POR USAR ESTE PROGRAMA!")