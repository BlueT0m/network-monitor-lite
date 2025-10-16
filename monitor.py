import psutil
import time
import socket
from datetime import datetime

LOG_FILE = "network_log.txt"


def log(message: str):
    """Écrit un message dans le fichier log avec un horodatage."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def list_connections():
    """Affiche les connexions réseau actives."""
    print("\n=== Connexions réseau actives ===")
    for conn in psutil.net_connections(kind='inet'):
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        pid = conn.pid if conn.pid else "N/A"
        status = conn.status

        print(f"Local: {laddr:<21}  Distant: {raddr:<21}  PID: {pid:<6}  État: {status}")
        log(f"Connexion - Local: {laddr}, Distant: {raddr}, PID: {pid}, État: {status}")


def monitor_bandwidth(duration=10):
    """Mesure l'utilisation de la bande passante pendant un temps donné."""
    print(f"\n=== Surveillance de la bande passante ({duration}s) ===")
    net_io_start = psutil.net_io_counters()
    time.sleep(duration)
    net_io_end = psutil.net_io_counters()

    bytes_sent = net_io_end.bytes_sent - net_io_start.bytes_sent
    bytes_recv = net_io_end.bytes_recv - net_io_start.bytes_recv

    sent_mb = bytes_sent / (1024 * 1024)
    recv_mb = bytes_recv / (1024 * 1024)

    print(f"Envoyé : {sent_mb:.2f} MB | Reçu : {recv_mb:.2f} MB")
    log(f"Bande passante - Envoyé: {sent_mb:.2f} MB, Reçu: {recv_mb:.2f} MB")


def show_hostname():
    """Affiche le nom d'hôte et l'adresse IP locale."""
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)
    print(f"Appareil : {hostname} ({ip_local})")
    log(f"Appareil détecté - Nom: {hostname}, IP: {ip_local}")


def main():
    print("=== Network Monitor Lite ===")
    print("Outil simple pour surveiller le trafic réseau local.\n")

    show_hostname()
    list_connections()
    monitor_bandwidth(duration=5)

    print(f"\nLes résultats sont enregistrés dans : {LOG_FILE}")


if __name__ == "__main__":
    main()
