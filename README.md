# Network Monitor Lite

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Build Status](https://img.shields.io/badge/Status-Active-brightgreen)

Outil Python éducatif pour surveiller l’activité réseau locale.
Affiche les connexions actives, la bande passante utilisée et enregistre les résultats dans un fichier log.
Aucune capture de paquets ni privilèges administrateur nécessaires.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

1. Clone le dépôt :
```bash
git clone https://github.com/BlueT0m/network-monitor-lite.git
cd network-monitor-lite
```

2. Installe la dépendance :
```bash
pip install psutil
```

---

## Usage

Lance le programme :
```bash
python monitor.py
```

L’application :

- Affiche ton nom d’hôte et ton adresse IP locale.

- Liste les connexions réseau actives (IP, port, PID, état).

- Mesure la bande passante utilisée sur une période donnée.

- Enregistre les résultats dans un fichier :
```bash
network_log.txt
```

---

## Features

- Suivi des connexions réseau locales.

- Calcul de la bande passante (upload/download).

- Historique enregistré dans un fichier texte.

- Fonctionne sans privilèges administrateur.

- Code simple et pédagogique.

---

## Contributing

1. Fork le dépôt.

2. Crée une nouvelle branche :
```bash
git checkout -b feature-name
```

3. Apporte tes modifications.

4. Pousse ta branche :
```bash
git push origin feature-name
```

5. Ouvre une pull request.

---

## License

Ce projet est sous licence [MIT License](LICENSE).
