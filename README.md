# Installation
Assurez-vous que vous avez Python et pip installé sur votre système.  

Ensuite, clonez le projet depuis GitHub :  
```git clone https://github.com/nom_utilisateur/nom_projet.git```

Ensuite, accédez au répertoire du projet :  
```cd nom_projet```

Créez et activer un environnement virtuel :  
```python -m venv env```  
```source env/bin/activate```

Installez les dépendances :  
```pip install -r requirements.txt```

# Configuration
Copiez le fichier example.env et renommez-le .env :  
```cp example.env .env```

Modifiez les variables d'environnement dans le fichier .env en fonction de votre configuration.

# Utilisation
Exécutez les migrations :  
```python manage.py migrate```

Créez un superutilisateur :  
```python manage.py createsuperuser```

Exécutez le serveur de développement :  
```python manage.py runserver```

Accédez à l'interface d'administration dans votre navigateur à l'adresse http://127.0.0.1:8000/admin  
Le nom d'utilisateur et le mot de passe sont ceux définis lors de la création du superuser

Accédez au site web dans votre navigateur à l'adresse http://127.0.0.1:8000/