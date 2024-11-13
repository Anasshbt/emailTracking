# 📧 emailTracking

**emailTracking** est une application dédiée aux étudiants à la recherche de stages de fin d'études (PFE). Elle permet de gérer et de suivre l'envoi de candidatures auprès de différentes entreprises en fournissant des fonctionnalités pour ajouter une liste de contacts, générer des lettres de motivation, suivre l'état des emails, et accéder à un tableau de bord intuitif.

🔗 [Lien vers le dépôt GitHub](https://github.com/Anasshbt/emailTracking.git)

## 🎯 Fonctionnalités

- **Ajout de contacts** : Importez une liste d'entreprises avec leurs informations de contact.
- **Génération de lettres de motivation** : Créez automatiquement des lettres personnalisées pour chaque entreprise.
- **Suivi des emails** : Suivez l'état des emails envoyés (ouverts, non ouverts).
- **Tableau de bord** : Visualisez une vue d'ensemble des envois et des statistiques de suivi.

## 🛠️ Prérequis

- Python 3.x
- MySQL
- Compte Gmail (pour l'envoi des emails)
- Compte Vercel pour le déploiement de l'application

## 🚀 Installation et Configuration

Suivez les étapes ci-dessous pour installer et configurer l'application **emailTracking**.

### 1. 📂 Cloner le projet

Clonez le dépôt GitHub du projet et accédez au répertoire :

```bash
git clone https://github.com/Anasshbt/emailTracking.git
cd emailTracking
```
### 2. 📄 Ajouter la liste des entreprises
Préparez un fichier CSV nommé result.csv contenant les informations des entreprises et leurs contacts. Ce fichier doit inclure les colonnes suivantes :

Nom de l'entreprise
Email
Adresse
Placez ce fichier result.csv dans le dossier racine de l'application.

### 3. 📝 Générer les lettres de motivation
Ajoutez le modèle de lettre de motivation au dossier lettres. Configurez le script pour générer des lettres personnalisées pour chaque entreprise en utilisant les données du fichier result.csv.

### 4. 🗄️ Configurer la base de données sur Aiven
Créez une base de données MySQL gratuite sur Aiven et notez les informations de connexion (URL de la base, utilisateur, mot de passe).

Accédez au fichier index.py dans le dossier api.

Mettez à jour les informations de connexion dans dbconfig comme suit :

python
Copier le code
# Exemple de configuration
db_config = {
    "host": "URL_DE_VOTRE_BD_AIVEN",
    "user": "VOTRE_UTILISATEUR",
    "password": "VOTRE_MOT_DE_PASSE",
    "database": "NOM_DE_VOTRE_BASE",
    "port":,
}
### 5. 🔒 Configurer le mot de passe et l'utilisateur pour le tableau de bord
Définissez un nom d'utilisateur et un mot de passe pour sécuriser l'accès au tableau de bord :

Ouvrez login.html dans le dossier templates.
Modifiez les champs nécessaires pour définir vos identifiants.
### 6. 🌐 Déployer sur Vercel
Déployez l'application sur Vercel en suivant les étapes ci-dessous :

Créez un compte sur Vercel.
Associez votre dépôt GitHub avec Vercel.
Suivez les instructions de Vercel pour déployer l'application.
Une fois le déploiement terminé, ajoutez le lien de suivi d’email dans template.html.
### 7. 🔐 Configurer le mot de passe de l'application Gmail
Pour envoyer les emails, vous devrez générer un mot de passe d'application pour votre compte Gmail :
Connectez-vous à votre compte Gmail.
Accédez aux paramètres de sécurité de votre compte.
Sous "Mots de passe des applications", générez un mot de passe pour cette application.

Ajoutez ce mot de passe dans le fichier mailsentwithtrack.py.

### 🖥️ Utilisation
Accéder au tableau de bord : Connectez-vous avec les identifiants définis pour visualiser les candidatures envoyées et les statistiques de suivi.
Vérifier l'état des emails : Dans le tableau de bord, vous pouvez voir si les emails ont été ouverts ou non.
### 👤 Auteur
Anass El Habti - Étudiant en Data Science et développement de logiciels, ENSIAS.
