#nombreArchivo = input("Dame el nombre del archivo: ");
try:
    nombreArchivo = "instance_3SAT_example2.txt"
    archivo = open(nombreArchivo,"r");
    lineas = archivo.read();
    lineas = lineas.split("\n");
    archivo.close()

    salida = open("output.txt","w")

    numVariables = 0
    numClausulas = 0
    numDummy = 0

    for linea in lineas:
        valores = linea.split();
        # COMENTARIO
        if linea[:1] == 'c':
            salida.write("Esta es la descripcion del problema:\n"+linea+"\n")

        # VARIABLES
        elif linea[:1] == 'p':
            numVariables = int(valores[2])
            numClausulas = int(valores[3])
            numDummy = numVariables + 1
            print("Numero de variables: ",numVariables,"\nNumero de clausulas: ",numClausulas)

        #CLAUSULAS
        else:
            salida.write("\nClausula original: "+linea+"\n")
            valores.remove('0')
            numVariablesClaus = len(valores)
            nuevaClausula =""

            # UNA SOLA VARIABLE
            if (numVariablesClaus == 1):
                nuevaClausula = valores[0]+" "+valores[0]+" "+valores[0]+" 0\n"
                salida.write(nuevaClausula)

            # DOS VARIABLES
            elif (numVariablesClaus == 2):
                strDummy = str(numDummy)
                nuevaClausula = valores[0] + " " + valores[1] + " "+strDummy+" 0\n"
                salida.write(nuevaClausula)

                numDummy*=-1
                strDummy = str(numDummy)
                nuevaClausula = strDummy+" "+valores[0] + " " + valores[1] + " 0\n"
                salida.write(nuevaClausula)

                numDummy *=-1
                numDummy+=1

            #TRES VARIABLES
            elif (numVariablesClaus == 3):
                nuevaClausula = valores[0] + " " + valores[1] +" " + valores[2] + " 0\n"
                salida.write(nuevaClausula)

            # MAS DE TRES VARIABLES
            else:
                print ("mas de rees")
                strDummy = str(numDummy)

                # PRIMERAS DOS VARIABLES Xn
                nuevaClausula = valores[0] + " " + valores[1] + " " + strDummy + " 0\n"
                print(nuevaClausula)
                salida.write(nuevaClausula)

                # VARIABLES X3 A Xi-2
                Xn = 2
                numVarTemp = len(valores) - 2
                print(valores)
                # MIENTRAS QUEDEN TRES O MÁS VARIABLES
                while numVarTemp > 2:
                    # print("dummy antes ",numDummy)
                    # print("xn ",Xn)
                    # print("numvartemp ", numVarTemp)
                    # print ("valorVariable ",str(valores[Xn]))
                    numDummySig = numDummy + 1
                    numDummy *= -1
                    strDummy = str(numDummy)

                    nuevaClausula = strDummy + " " + str(valores[Xn]) + " " + str(numDummySig) + " 0\n"
                    print(nuevaClausula)
                    salida.write(nuevaClausula)
                    numDummy = numDummySig
                    print("dummy depsues ", numDummy)

                    numVarTemp -=1
                    Xn +=1

                # ULTIMAS DOS VARIABLES
                print("ultimas 2")
                print("dummy antes ",numDummy)
                print("xn ",Xn)
                print ("valorVariable ",str(valores[Xn]))
                numDummy *= -1
                strDummy = str(numDummy)
                nuevaClausula = strDummy+ " "+valores[Xn] + " " + valores[Xn + 1] + " 0\n"
                print(nuevaClausula)
                numDummy *= -1
                numDummy += 1
                #salida.write(nuevaClausula)


            # FIN DE LA LINEA/CLAUSULA
            nuevaClausula = ""
    salida.close()

except FileNotFoundError:
        print("No encuentro el archivo");
