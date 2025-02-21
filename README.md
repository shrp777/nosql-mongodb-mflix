# Mflix

Node.js + MongoDB + Docker

## Variables d'environnement à adapter

### MongoDB

```env
MONGO_INITDB_ROOT_USERNAME=superadmin
MONGO_INITDB_ROOT_PASSWORD=superpassword
MONGO_INITDB_USERNAME=johndoe
MONGO_INITDB_PASSWORD=azerty
MONGO_INITDB_DATABASE=mflix
MONGO_INITDB_COLLECTION=movies
MONGO_INITDB_HOST=db
MONGO_INITDB_PORT=27017
```

### MONGO EXPRESS

```env
ME_CONFIG_MONGODB_ADMINUSERNAME="${MONGO_INITDB_ROOT_USERNAME}"
ME_CONFIG_MONGODB_ADMINPASSWORD="${MONGO_INITDB_ROOT_PASSWORD}"
ME_CONFIG_MONGODB_SERVER="${MONGO_INITDB_HOST}"
ME_CONFIG_BASICAUTH_USERNAME="${MONGO_INITDB_USERNAME}"
ME_CONFIG_BASICAUTH_PASSWORD="${MONGO_INITDB_PASSWORD}"
ME_CONFIG_MONGODB_PORT="${MONGO_INITDB_PORT}"
```

### APP

```env
MONGODB_URL="mongodb://${MONGO_INITDB_ROOT_USERNAME}:${MONGO_INITDB_ROOT_PASSWORD}@${MONGO_INITDB_HOST}:${MONGO_INITDB_PORT}/${MONGO_INITDB_DATABASE}?authSource=admin"
```

## Import automatique des données

Données JSON : `./db/import/data.json` (il est possible de remplacer les données JSON, mais le fichier doit être nommé data.json).

Les données JSON de test proviennent de <https://www.mongodb.com/docs/atlas/sample-data/sample-mflix/>.

Attention, si les données du `./db/import/data.json` sont incorrectes, l'import échouera et le service __db__ ne pourra pas se démarrer.

## Connexion à la base de données MongoDB depuis la machine hôte

```SH
mongosh admin --username <user> --password <password> --port <port>
```

- Exemple :

```SH
mongosh admin --username superadmin --password superpassword --port 27018
```

## Connection String URI depuis la machine hôte

`mongodb://<root-user>:<root-password>@localhost:<port>/<db-name>?authSource=admin`

- Exemple : `mongodb://superadmin:superpassword@localhost:27018/mflix?authSource=admin`

## Connection String URI depuis un container au sein du réseau Docker

`mongodb://<user>:<password>@<host>:<port>/<db-name>?authSource=admin`

- Exemple : `mongodb://superadmin:superpassword@db:27017/mflix?authSource=admin`

--

!["Logotype Shrp"](https://sherpa.one/images/sherpa-logotype.png)

__Alexandre Leroux__  
_Enseignant / Formateur_  
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

<https://shrp.dev>
