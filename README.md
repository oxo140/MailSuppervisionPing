# 📡 Ping Monitor

**Ping Monitor** est un outil de surveillance réseau simple et efficace permettant de vérifier régulièrement la connectivité d'une liste de machines (serveurs, routeurs, services, etc.). En cas d'inaccessibilité, le script envoie automatiquement une **alerte par e-mail** listant les hôtes concernés, avec leur description.

---

## 📋 Prérequis

* ✅ **Debian 11.8 ou supérieure** (Ubuntu compatible)
* ✅ **Python 3** (installé par défaut sur la plupart des distributions)
* ✅ Connexion Internet pour l’envoi d’e-mails (SMTP)
* ✅ Un compte Gmail avec mot de passe d’application (recommandé)

---

## 🚀 Installation

Installez les dépendances requises :

```bash
sudo apt update && sudo apt install -y python3 python3-pip curl
```

Téléchargez le script et préparez le fichier des hôtes :

```bash
sudo apt install curl
curl -O https://raw.githubusercontent.com/oxo140/MailSuppervisionPing/main/ping_monitor.py
curl -O https://raw.githubusercontent.com/oxo140/MailSuppervisionPing/main/hosts.txt
```

> 📁 Placez le fichier `hosts.txt` dans le **même dossier** que `ping_monitor.py`.

---

## 🗂️ Format du fichier `hosts.txt`

Chaque ligne du fichier `hosts.txt` contient un hôte à surveiller suivi d’une brève description :

```
192.168.0.1 Routeur principal
192.168.0.2 Serveur fichiers
8.8.8.8 DNS Google
```

---

## ✉️ Configuration de l'e-mail

Dans le fichier `ping_monitor.py`, modifiez les lignes suivantes :

```python
from_email = "votre_email@gmail.com"
to_email = "destinataire@example.com"
app_password = "votre_mot_de_passe_application"
```

💡 Activez l’**authentification à deux facteurs sur Gmail** et créez un **mot de passe d’application** pour sécuriser l’envoi.

---

## 🔁 Automatisation

Pour exécuter le script automatiquement toutes les 10 minutes, ajoutez une tâche cron :

```bash
crontab -e
```

Ajoutez la ligne suivante :

```bash
*/10 * * * * /usr/bin/python3 /chemin/vers/ping_monitor.py
```

> 📌 Remplacez `/chemin/vers/` par le chemin réel du script.

---

## 🛠️ Conseils d’usage

* Désactivez la mise en veille automatique de la machine de surveillance.
* Activez le démarrage automatique et l'ouverture de session automatique si utilisé au boot.
* Ajoutez le script à un service `systemd` pour une intégration plus robuste.

---

## 📬 Exemple d'alerte e-mail

Objet : `⚠️ Hôtes inaccessibles depuis nom-machine`

Contenu :

```
Les hôtes suivants ne répondent pas au ping :

192.168.0.2 - Serveur fichiers
8.8.8.8 - DNS Google
```

---

## 📄 Fichiers du projet

* `ping_monitor.py` : script principal de surveillance
* `hosts.txt` : liste des hôtes à surveiller
* (optionnel) `ping_monitor.service` : service `systemd` si besoin

---
