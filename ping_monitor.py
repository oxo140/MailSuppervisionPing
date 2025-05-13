import os
import subprocess
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Paramètres e-mail
from_email = "votre_email@gmail.com"
to_email = "destinataire@exemple.com"
app_password = "votre_mot_de_passe_application"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Chemin du fichier hosts.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
hosts_file = os.path.join(script_dir, "hosts.txt")

# Lire les hôtes et descriptions depuis le fichier
if not os.path.isfile(hosts_file):
    print(f"Fichier hosts.txt introuvable à {hosts_file}")
    exit(1)

hosts = []
with open(hosts_file, "r") as f:
    for line in f:
        parts = line.strip().split(maxsplit=1)
        if parts:
            ip_or_host = parts[0]
            description = parts[1] if len(parts) > 1 else ""
            hosts.append((ip_or_host, description))

# Fonction ping
def ping(host):
    try:
        subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", host],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

# Vérifier les hôtes
unreachable_hosts = []
for host, description in hosts:
    if not ping(host):
        unreachable_hosts.append(f"{host} - {description}")

# Envoi du mail si au moins un hôte est injoignable
if unreachable_hosts:
    hostname = socket.gethostname()
    subject = f"⚠️ Hôtes inaccessibles depuis {hostname}"
    body = "Les hôtes suivants ne répondent pas au ping :\n\n"
    body += "\n".join(unreachable_hosts)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, app_password)
        server.sendmail(from_email, to_email, msg.as_string())
        print("Alerte e-mail envoyée.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail : {e}")
    finally:
        server.quit()
else:
    print("Toutes les machines sont accessibles.")
