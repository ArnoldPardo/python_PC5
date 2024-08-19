import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

def send_email(fromaddr, toaddr, subject, body, filename):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "tu_contraseña")  # Reemplaza con tu contraseña
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

# Configurar el correo
fromaddr = "tu_email@gmail.com"  # Reemplaza con tu email
toaddr = "destinatario@gmail.com"  # Reemplaza con el email del destinatario
subject = "Reporte de Vinos"
body = "Adjunto el reporte de vinos por país en formato Excel."

# Enviar el reporte
send_email(fromaddr, toaddr, subject, body, 'resumen_pais.xlsx')

print("Reporte enviado por correo.")
