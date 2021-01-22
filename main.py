from PyQt5 import uic
import PyQt5.QtWidgets as QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="sgmfinancas"
)

def gerar_total():
    default = 0
    cursor = banco.cursor()
    comando = "SELECT SUM(saldo) FROM contas"
    cursor.execute(comando)
    saldocont = cursor.fetchone()
    lsaldocont = list(saldocont)
    comando = "SELECT SUM(valor) FROM despesas"
    cursor.execute(comando)
    saldodesp = cursor.fetchone()
    lsaldodesp = list(saldodesp)
    comando = "SELECT SUM(valor) FROM lembretes"
    cursor.execute(comando)
    saldolemb = cursor.fetchone()
    lsaldolemb = list(saldolemb)
    if(lsaldocont[0] != None and lsaldodesp[0] != None and lsaldolemb[0] != None): 
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        total = lsaldocont[0] - (lsaldodesp[0] + lsaldolemb[0])
        tela_info.label_9.setText(f"{total}")
    elif(lsaldocont[0] == 0 and lsaldodesp[0] != None and lsaldolemb[0] != None):
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        tela_info.label_9.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
    elif(lsaldocont[0] == 0 and lsaldodesp[0] == None and lsaldolemb[0] != None):
        lsaldodesp[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        tela_info.label_9.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
    elif(lsaldocont[0] == 0 and lsaldodesp[0] != None and lsaldolemb[0] == None):
        lsaldolemb[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        tela_info.label_9.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
    elif(lsaldocont[0] == 0 and lsaldodesp[0] == None and lsaldolemb[0] == None):
        lsaldodesp[0] = 0
        lsaldolemb[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        tela_info.label_9.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
    elif(lsaldocont[0] == None and lsaldodesp[0] != None and lsaldolemb[0] != None):
        lsaldocont[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        tela_info.label_9.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
    elif(lsaldocont[0] == None and lsaldodesp[0] == None and lsaldolemb[0] != None):
        lsaldocont[0] = 0
        lsaldodesp[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        tela_info.label_9.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
    elif(lsaldocont[0] == None and lsaldodesp[0] != None and lsaldolemb[0] == None):
        lsaldocont[0] = 0
        lsaldolemb[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        tela_info.label_9.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
    elif(lsaldocont[0] != None and lsaldodesp[0] == None and lsaldolemb[0] != None):
        lsaldodesp[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        total = lsaldocont[0] - (lsaldodesp[0] + lsaldolemb[0])
        tela_info.label_9.setText(f"{total}")
    elif(lsaldocont[0] != None and lsaldodesp[0] != None and lsaldolemb[0] == None):
        lsaldolemb[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        total = lsaldocont[0] - (lsaldodesp[0] + lsaldolemb[0])
        tela_info.label_9.setText(f"{total}")
    elif(lsaldocont[0] != None and lsaldodesp[0] == None and lsaldolemb[0] == None):
        lsaldodesp[0] = 0
        lsaldolemb[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        total = lsaldocont[0] - (lsaldodesp[0] + lsaldolemb[0])
        tela_info.label_9.setText(f"{total}")
    else:
        lsaldocont[0] = 0
        lsaldodesp[0] = 0
        lsaldolemb[0] = 0
        tela_info.label_7.setText(f"{lsaldocont[0]}")
        tela_info.label_8.setText(f"{lsaldodesp[0] + lsaldolemb[0]}")
        total = lsaldocont[0] - (lsaldodesp[0] + lsaldolemb[0])
        tela_info.label_9.setText(f"{total}")

def abrir_reg_conta():
    tela_info.close()
    tela_add_conta.show()

def registrar_conta():
    tipo = tela_add_conta.comboBox.currentText()
    nome = tela_add_conta.lineEdit.text()
    sal = tela_add_conta.lineEdit_2.text()
    try:
        if(float(sal) > 0):
            cursor = banco.cursor()
            comando = "INSERT INTO contas (tipo, nome, saldo) VALUES (%s, %s, %s)"
            info =(str(tipo),str(nome),float(sal))
            cursor.execute(comando,info)
            banco.commit()
            tela_add_conta.label_5.setText("Conta registrada")
        else:
            tela_add_conta.label_5.setText("Saldo de conta não pode ser = 0")
    except:
        tela_add_conta.label_5.setText("Conta com nome já registrado")

def listar_contas():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM contas"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    tela_info.tableWidget.setRowCount(len(dados_lidos))
    tela_info.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_info.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def abrir_att_contas():
    tela_info.close()
    tela_att_conta.show()

def buscar_contas():
    nm = tela_att_conta.lineEdit.text()
    try:  
        cursor = banco.cursor()
        cursor.execute(f"SELECT nome,saldo FROM contas WHERE nome='{nm}'")
        dados = cursor.fetchall()
        nome = dados[0][0]
        conta = dados[0][1]
        tela_att_conta.label_6.setText(f"Conta = {nome} Saldo atual = {conta}")
    except:
        tela_att_conta.label_6.setText("Campo vazio ou conta não encontrada")

def deletar_conta():

    conta_selecionada = tela_info.tableWidget.currentRow()
    print(conta_selecionada)
    tela_info.tableWidget.removeRow(conta_selecionada)

    cursor = banco.cursor()
    cursor.execute("SELECT nome FROM contas")
    ctsel = cursor.fetchall()
    ctdel = ctsel[conta_selecionada][0]
    print(ctdel)

def atualizar_contas():
    nm = tela_att_conta.lineEdit.text()
    ct = tela_att_conta.lineEdit_2.text()
    modo = tela_att_conta.comboBox.currentText()
    try:  
        cursor = banco.cursor()
        cursor.execute(f"SELECT saldo FROM contas WHERE nome='{nm}'")
        dados = cursor.fetchall()
        conta = dados[0][0]
        if(modo == "ADICIONAR"):
            newvalor = conta + float(ct)
            cursor.execute(f"UPDATE contas SET saldo='{newvalor}' WHERE nome='{nm}'")
            tela_att_conta.label_6.setText(f"Conta: {nm} Saldo = {newvalor}")
        elif(modo == "RETIRAR"):
            if(float(ct)>conta):
                tela_att_conta.label_6.setText("Valor de retirada maior que o Saldo")
            else:
                newvalor = conta - float(ct)
                cursor.execute(f"UPDATE contas SET saldo='{newvalor}' WHERE nome='{nm}'")
                tela_att_conta.label_6.setText(f"Conta: {nm} Saldo = {newvalor}")
    except:
        tela_att_conta.label_6.setText("Campo vazio ou conta não encontrada")

def fechar_att_contas():
    tela_att_conta.close()
    tela_info.show()

def fechar_reg_conta():
    tela_add_conta.close()
    tela_info.show()

def abrir_reg_desp():
    tela_info.close()
    tela_add_desp.show()

def registrar_despesa():
    nome = tela_add_desp.lineEdit.text()
    valor = tela_add_desp.lineEdit_2.text()
    try:
        if(float(valor)>0):
            cursor = banco.cursor()
            comandoSQL = "INSERT INTO despesas (nome, valor) VALUES (%s, %s)"
            info = (str(nome),float(valor))
            cursor.execute(comandoSQL, info)
            banco.commit()
            tela_add_desp.label_4.setText("Despesa registrada")
        else:
            tela_add_desp.label_4.setText("Erro valor = ou < que 0")
    except:
        tela_add_desp.label_4.setText("Campos em nulo/Use . em ,")

def listar_despesas():
    cursor = banco.cursor()
    comandoSQL = "SELECT * FROM despesas"
    cursor.execute(comandoSQL)
    dados = cursor.fetchall()

    tela_info.tableWidget_2.setRowCount(len(dados))
    tela_info.tableWidget_2.setColumnCount(2)

    for i in range(0, len(dados)):
        for j in range(0, 2):
            tela_info.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

def fechar_reg_desp():
    tela_add_desp.close()
    tela_info.show()

def abrir_reg_lemb():
    tela_info.close()
    tela_add_lemb.show()

def registrar_lembretes():
    nome = tela_add_lemb.lineEdit.text()
    data = tela_add_lemb.dateEdit.date().toPyDate()
    valor = tela_add_lemb.lineEdit_2.text()

    try:
        if(float(valor)>0):
            cursor = banco.cursor()
            comando = "INSERT INTO lembretes (nome,data,valor) VALUES(%s,%s,%s)"
            info = (str(nome),str(data),float(valor))
            cursor.execute(comando, info)
            banco.commit()
            tela_add_lemb.label_5.setText("Lembrete registrado")
        else:
            tela_add_lemb.label_5.setText("Erro valor < ou = a 0")
    except:
        tela_add_lemb.label_5.setText("Campos em nulo/Use . em ,")

def listar_lembretes():
    cursor = banco.cursor()
    comando = "SELECT * FROM lembretes"
    cursor.execute(comando)
    dados = cursor.fetchall()

    tela_info.tableWidget_3.setRowCount(len(dados))
    tela_info.tableWidget_3.setColumnCount(3)

    for i in range(0, len(dados)):
        for j in range(0, 3):
            tela_info.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))
    
def fechar_reg_lemb():
    tela_add_lemb.close()
    tela_info.show()

def abrir_pagamento():
    tela_info.close()
    tela_pagamentos.show()

def fazer_pagamento():
    try:
        tipo = tela_pagamentos.comboBox.currentText()
        nm = tela_pagamentos.lineEdit.text()
        vlr = tela_pagamentos.lineEdit_2.text()
        conta = tela_pagamentos.lineEdit_3.text()

        if(tipo == "DESPESAS"):
            if(conta == "" or nm == "" or vlr == ""):
                tela_pagamentos.label_6.setText("Algum campo está vazio")
            else:
                cursor = banco.cursor()
                cursor.execute(f"SELECT nome,valor FROM despesas WHERE nome='{nm}' AND valor='{vlr}'")
                dados = cursor.fetchall()
                nm = dados[0][0]
                vlr = dados[0][1]
                
                cursor.execute(f"SELECT saldo FROM contas WHERE nome='{conta}'")
                info = cursor.fetchall()
                vlrconta = info[0][0]
                if(float(vlr) <= float(vlrconta)):
                    newvlrconta = float(vlrconta) - float(vlr)
                    cursor.execute(f"DELETE FROM despesas WHERE nome='{nm}' AND valor='{vlr}'")
                    cursor.execute(f"UPDATE contas SET saldo='{newvlrconta}' WHERE nome='{conta}'")
                    tela_pagamentos.label_6.setText("Pagamento feito com sucesso em sgmfinanças")
                else:
                    tela_pagamentos.label_6.setText("ERRO,valor de retirada maior que o da conta")
        elif(tipo == "LEMBRETES"):
            if(conta == "" or nm == "" or vlr == ""):
                tela_pagamentos.label_6.setText("Algum campo está vazio")
            else:
                cursor = banco.cursor()
                cursor.execute(f"SELECT nome,valor FROM lembretes WHERE nome='{nm}' AND valor='{vlr}'")
                dados = cursor.fetchall()
                nm = dados[0][0]
                vlr = dados[0][1]
                
                cursor.execute(f"SELECT saldo FROM contas WHERE nome='{conta}'")
                info = cursor.fetchall()
                vlrconta = info[0][0]
                if(float(vlr) <= float(vlrconta)):
                    newvlrconta = float(vlrconta) - float(vlr)
                    cursor.execute(f"DELETE FROM lembretes WHERE nome='{nm}' AND valor='{vlr}'")
                    cursor.execute(f"UPDATE contas SET saldo='{newvlrconta}' WHERE nome='{conta}'")
                    tela_pagamentos.label_6.setText("Pagamento feito com sucesso em sgmfinanças")
                else:
                    tela_pagamentos.label_6.setText("ERRO,valor de retirada maior que o da conta")


    except:
        tela_pagamentos.label_6.setText("Informações não encontradas!")   


def fechar_pagamento():
    tela_pagamentos.close()
    tela_info.show()

app = QtWidgets.QApplication([])

tela_info = uic.loadUi("informacoes.ui")
tela_add_conta = uic.loadUi("registrarconta.ui")
tela_att_conta = uic.loadUi("atualizarconta.ui")
tela_add_desp = uic.loadUi("registrardespesa.ui")
tela_add_lemb = uic.loadUi("registrarlembretes.ui")
tela_pagamentos = uic.loadUi("fazerpagamentos.ui")

tela_info.pushButton.clicked.connect(abrir_reg_conta)
tela_info.pushButton_2.clicked.connect(abrir_reg_desp)
tela_info.pushButton_3.clicked.connect(abrir_reg_lemb)
tela_info.pushButton_4.clicked.connect(listar_contas)
tela_info.pushButton_5.clicked.connect(listar_despesas)
tela_info.pushButton_6.clicked.connect(listar_lembretes)
tela_info.pushButton_7.clicked.connect(gerar_total)
tela_info.pushButton_8.clicked.connect(abrir_att_contas)
tela_info.pushButton_9.clicked.connect(abrir_pagamento)
tela_info.pushButton_10.clicked.connect(deletar_conta)

tela_add_conta.pushButton.clicked.connect(fechar_reg_conta)
tela_add_conta.pushButton_2.clicked.connect(registrar_conta)

tela_att_conta.pushButton.clicked.connect(fechar_att_contas)
tela_att_conta.pushButton_2.clicked.connect(buscar_contas)
tela_att_conta.pushButton_3.clicked.connect(atualizar_contas)

tela_add_desp.pushButton.clicked.connect(fechar_reg_desp)
tela_add_desp.pushButton_2.clicked.connect(registrar_despesa)

tela_add_lemb.pushButton.clicked.connect(fechar_reg_lemb)
tela_add_lemb.pushButton_2.clicked.connect(registrar_lembretes)

tela_pagamentos.pushButton.clicked.connect(fechar_pagamento)
tela_pagamentos.pushButton_2.clicked.connect(fazer_pagamento)

tela_info.show()
app.exec()
 