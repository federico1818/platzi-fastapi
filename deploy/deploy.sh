#!/bin/sh

VERSION="$1"
FILENAME="platzi-fastapi-$VERSION.tar"

mkdir -p dist

tar --exclude-from=./deploy/.tarignore -cf "dist/$FILENAME" .