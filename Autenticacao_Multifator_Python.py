import pyrebase
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

firebaseConfig = {
    "apiKey": "AIzaSyCUGOVL7JRJQ1OfIDyYFNyv7ywatwaJchU",
    "authDomain": "fir-pucpr-19c95.firebaseapp.com",
    "projectId": "fir-pucpr-19c95",
    "databaseURL": "https://" + "fir-pucpr-19c95" + ".firebaseio.com",
    "storageBucket": "fir-pucpr-19c95.appspot.com",
    "messagingSenderId": "634569554769",
    "appId": "1:634569554769:web:76a6f010f89fe0de99b170",
    "measurementId": "G-9376VZGV04"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

server = "smtp.gmail.com"
port = 587
username = "glauber.jask@gmail.com"
passwordSMTP = "wqkfmxgncvvtneqc"

ok = True

while ok:
    print("1 - Cadastrar Usuário")
    print("2 - Verificar Email")
    print("3 - Autenticar Usuário")

    opcao = input("Selecione uma das opções:")

    if opcao == "1":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        status = auth.create_user_with_email_and_password(user, password)
        print("Email cadastrado: ",user)

    if opcao == "2":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        status = auth.sign_in_with_email_and_password(user, password)
        idToken = status["idToken"]
        auth.send_email_verification(idToken)
        print("Email de verificação enviado: ", user)

    if opcao == "3":
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")
        status = auth.sign_in_with_email_and_password(user, password)
        idToken = status["idToken"]
        info = auth.get_account_info(idToken)
        users = info["users"]
        verifyEmail = users[0]["emailVerified"]

        if verifyEmail:
            print("Segundo Fator de Autenticao")
            codigo = random.randint(100,1000)
            mail_body = "Código de validação: %d "%codigo

            mensagem = MIMEMultipart()
            mensagem['From'] = username
            mensagem['To'] = user
            mensagem['Subject'] = "Código E-mail"
            mensagem.attach(MIMEText(mail_body, 'plain'))

            connection = smtplib.SMTP(server, port)
            connection.starttls()
            connection.login(username, passwordSMTP)
            connection.send_message(mensagem)
            connection.quit()

            codigoEmail = int(input("Entre com o código que foi enviado por e-mail: "))

            if codigo == codigoEmail:
                print("Usuário Autenticado!!!")
            else:
                print("Código Inválido!!")

        else:
            print("Email não verificado!")