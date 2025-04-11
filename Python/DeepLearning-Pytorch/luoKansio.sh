#!/bin/bash

# Määritellään pääkansion nimi
PAKAN_NIMI="nimeaKansio"

# Luodaan pääkansio
mkdir -p "$PAKAN_NIMI"

# Luodaan alikansiot
mkdir -p "$PAKAN_NIMI/Lectures"
mkdir -p "$PAKAN_NIMI/Tasks"
mkdir -p "$PAKAN_NIMI/Projects"
mkdir -p "$PAKAN_NIMI/Slides"

# Ilmoitetaan käyttäjälle, että kansiot on luotu
echo "Kansio '$PAKAN_NIMI' ja sen alikansiot luotu onnistuneesti!"

