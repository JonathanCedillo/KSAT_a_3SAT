#EQUIPO
# ALEJANDRO CÁMARA MARTÍNEZ - A01370909
# JONATHAN SAMUEL CEDILLO BELMÁN - A01377844

nombreArchivo = input("Dame el nombre del archivo: ");
try:
    #nombreArchivo = "instance_3SAT_example2.txt"
    archivo = open(nombreArchivo,"r");
    lineas = archivo.read();
    lineas = lineas.split("\n");
    archivo.close()

    salidaTemp = open("outputTemp.txt", "w")

    numVariables = 0
    numClausulas = 0
    numDummy = 0
    totalClausulas = 0

    #LECTURA LINEA POR LINEA DEL ARCHIVO DEL USUARIO
    for linea in lineas:
        clausula = linea.split();
        # # COMENTARIO
        if linea[:1] == 'c':
            continue

        # VARIABLES
        if linea[:1] == 'p':
            numVariables = int(clausula[2])
            numClausulas = int(clausula[3])
            numDummy = numVariables + 1

        #CLAUSULAS
        else:
            clausula.remove('0')
            numVariablesClaus = len(clausula)
            nuevaClausula =""

            # UNA SOLA VARIABLE
            if (numVariablesClaus == 1):
                nuevaClausula = clausula[0] + " " + clausula[0] + " " + clausula[0] + " 0\n"
                salidaTemp.write(nuevaClausula)
                totalClausulas += 1

            # DOS VARIABLES
            elif (numVariablesClaus == 2):
                nuevaClausula = clausula[0] + " " + clausula[1] + " " + str(numDummy) + " 0\n"
                salidaTemp.write(nuevaClausula)
                totalClausulas += 1

                numDummy*=-1
                nuevaClausula = str(numDummy)+" " + clausula[0] + " " + clausula[1] + " 0\n"
                salidaTemp.write(nuevaClausula)
                totalClausulas += 1

                numDummy *=-1
                numDummy+=1

            #TRES VARIABLES
            elif (numVariablesClaus == 3):
                nuevaClausula = clausula[0] + " " + clausula[1] + " " + clausula[2] + " 0\n"
                salidaTemp.write(nuevaClausula)
                totalClausulas += 1

            # MAS DE TRES VARIABLES
            else:
                # PRIMERAS DOS VARIABLES Xn
                nuevaClausula = clausula[0] + " " + clausula[1] + " " + str(numDummy) + " 0\n"
                salidaTemp.write(nuevaClausula)
                totalClausulas += 1

                # VARIABLES X3 A Xi-2
                Xn = 2
                numVarTemp = len(clausula) - 2
                # MIENTRAS QUEDEN TRES O MÁS VARIABLES
                while numVarTemp > 2:
                    numDummySig = numDummy + 1
                    numDummy *= -1

                    nuevaClausula = str(numDummy) + " " + str(clausula[Xn]) + " " + str(numDummySig) + " 0\n"
                    salidaTemp.write(nuevaClausula)
                    totalClausulas += 1
                    numDummy = numDummySig

                    numVarTemp -=1
                    Xn +=1

                # ULTIMAS DOS VARIABLES
                numDummy *= -1
                nuevaClausula = str(numDummy)+ " " + clausula[Xn] + " " + clausula[Xn + 1] + " 0\n"
                salidaTemp.write(nuevaClausula)
                totalClausulas += 1
                numDummy *= -1
                numDummy += 1

            # FIN DE LA LINEA/CLAUSULA
            nuevaClausula = ""
    salidaTemp.close()

    # GUARDAR SALIDAS EN UN OUTPUT.TXT
    salidaTemp = open("outputTemp.txt", "r");
    cnf = open("instance_3SAT_Output.txt","w");

    cnf.write("c A SAT instance generated from a 3-CNF formula that had "+str(totalClausulas)+
              " clauses and "+ str(numDummy-1) +" variables\n")
    cnf.write("p cnf "+str(numDummy-1)+" "+str(totalClausulas)+"\n")

    final = salidaTemp.read()
    final = final.split("\n")

    for x in range(0,len(final)-1):
        if (x == len(final)-2):
            cnf.write(final[x])
        else:
            cnf.write(final[x] + "\n")

    salidaTemp.close()
    cnf.close()

except FileNotFoundError:
        print("No encuentro el archivo");
