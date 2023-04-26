import smtplib
import ssl


de = 'vmaxbh@gmail.com'
para = 'vmaxbh@gmail.com'
senha = '0704349193'
msg = """Ola, mensagem de teste"""


context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(de, senha)
    conexao.sendmail(de, para, msg)
