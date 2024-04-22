import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

ok = True

while ok:
    print("1 - Cadastrar Usuário")
    print("2 - Verificar Email")
    print("3 - Autenticar Usuário")

    opcao = input("Selecione uma das opções:")

    if opcao == "1":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        print("Email cadastrado: ",user)

    if opcao == "2":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        print("Email de verificação enviado: ", user)

    if opcao == "3":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        

        print("Usuário Autenticado!!!")
