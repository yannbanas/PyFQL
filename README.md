## Prérequis

Assurez-vous d'avoir Python 3.9 ou supérieur installé sur votre système
Assurez-vous egalement avoir importer le package PyFQL
```bash
pip install PyFQL
```
url: https://pypi.org/project/PyFQL/

## Exemple

le script main.py vous permet de tester rapidement le package

```bash
python main.py

(PyFQL)>>>
```

## Commandes disponibles

Le script prend en charge les commandes suivantes :

- `creer la bdd [nom_bdd]`: Crée une nouvelle base de données fichier .json.
- `supprime la bdd [nom_bdd]`: Supprime la base de données fichier .json.

- `creer la table [nom_table]`: Crée une nouvelle table dans la base de données.
- `supprime la [nom_table] [options]`: Supprime des enregistrements ou une table entière de la base de données.

- `affiche la table [nom_table]`: Affiche le contenu d'une table.
- `exit` ou `quit`: Quitte le programme.

## Exemples de requêtes

Voici des exemples de requêtes que vous pouvez exécuter dans le script :

1. **Création d'une bdd** :
   ```bash
   creer la bdd garage
   ```

2. **Utiliser une bdd spécifique** :
   ```bash
   utilise la bdd garage
   ```

3. **Création d'une table** :
   ```bash
   creer la table voiture
   ```

4. **supprimer une bdd** :
   ```bash
   supprime la bdd garage
   ```

5. **supprimer une table** :
   ```bash
   supprime la table voiture
   ```

**Ceci est toujour en dévelopement merci de votre comprehension**

## Phrase type traiter en language naturel sans library externe
- [creer] la [table]/[bdd] [VARIABLE]       
  RESERVER IGNORE RESERVER VARIABLE
--
- [utilise] la [bdd] [VARIABLE]
  RESERVER IGNORE RESERVER VARIABLE
--
- [supprime] la [table]/[bdd] [VARIABLE]
  RESERVER IGNORE RESERVER VARIABLE
--
- [supprime] le [champ]/ [VARIABLE] de la [table] [VARIABLE]
  RESERVER IGNORE RESERVER VARIABLE IGNORE IGNORE RESERVER VARIABLE
--
- [supprime] les [enregistrements] de la [table] [VARIABLE]
  RESERVER IGNORE RESERVER IGNORE IGNORE RESERVER VARIABLE
--
-[modifie] la [table] [VARIABLE] et [renome] le [champ] [VARIABLE] par [VARIABLE]
RESERVER IGNORE RESERVER RESERVER IGNORE RESERVER IGNORE RESERVER RESERVER IGNORE VARIABLE
--
-[modifie] la [table] [VARIABLE] et [ajoute] le [champ] [VARIABLE]
RESERVER IGNORE RESERVER VARIABLE IGNORE RESERVER IGNORE RESERVER VARIABLE
--
- [modifie] la     [table] [VARIABLE] et    [ajoute]   le [champ] [VARIABLE]  a la position [VARIABLE]
  RESERVER IGNORE RESERVER VARIABLE  IGNORE RESERVER IGNORE RESERVER VARIABLE IGNORE IGNORE IGNORE VARIABLE
--
## Conclusion

Ce guide devrait vous aider à comprendre comment utiliser mon package pour interagir avec une base de données principalement (KeysDB) via des phrase en language naturel en frencais. Si vous avez des questions ou des problèmes, n'hésitez pas à demander de l'aide à ce mail yannbanas@gmail.com.

## build from source

mettez vous a la racine du projet et executer

```bash
pip install -e .
```
