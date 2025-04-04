#!/bin/bash

# Tarkistetaan, onko käyttäjä antanut kansion nimen
if [ -z "$1" ]; then
  echo "Käyttö: $0 [kansion_nimi]"
  exit 1
fi

# Luodaan pääkansio
mkdir -p "$1"

# Luodaan alikansiot
mkdir -p "$1/Lectures"
mkdir -p "$1/Tasks"
mkdir -p "$1/Projects"
mkdir -p "$1/Slides"

# Ilmoitetaan käyttäjälle, että kansiot on luotu
echo "Kansio '$1' ja sen alikansiot luotu onnistuneesti!"
