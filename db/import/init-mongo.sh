#!/bin/bash
set -e

mongoimport /tmp/import/data.json -d $MONGO_INITDB_DATABASE -c $MONGO_INITDB_COLLECTION --drop