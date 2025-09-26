# Secure Communication Terminal

## Intro

Secure Communication Terminal is a secure, terminal-based chat application designed for anonymous, end-to-end encrypted communication over the Tor network. It consists of a modular Python client and server, enabling private group chats with strong privacy guarantees.

## What it is

This project is a cross-platform, terminal chat system where all traffic is routed through Tor using a SOCKS5 proxy. The server runs as a Tor hidden service, and clients connect using the server's `.onion` address.

## How it is made

- **Language:** Python 3
- **Architecture:** Modular client-server, with dedicated socket handler modules for each.
- **Transport:** All communication is routed through Tor (SOCKS5 proxy).
- **UI:** Uses `rich` and `colorama` for a modern terminal experience.
- **Configuration:** Environment variables via `.env` files.
- **Dependencies:** See `requirements.txt` for all required packages.

## Why is it for

This project is for anyone who needs a simple, private, and anonymous chat system—ideal for privacy enthusiasts, journalists, or anyone requiring secure communications over the Tor network.

---

## Installation

### Server Side

1. **Install Tor:**  
   - Linux: `sudo apt install tor`  

2. **Set up Tor Hidden Service:**  
   - Edit your `torrc` file (usually at `/etc/tor/torrc`) to add a hidden service:
     ```
     HiddenServiceDir /var/lib/tor/servicename/
     HiddenServicePort 4444 127.0.0.1:4444
     ```
   - Restart Tor: `sudo systemctl restart tor`  
   - Find your `.onion` address in `/var/lib/tor/servicename/hostname`.

3. **Install Python dependencies:**  
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment:**  
   - Copy `.env.example` to `.env` in the project root.
   - Set `SERVER_IP=localhost` and `PORT=4444` .

5. **Start the server:**  
   ```
   python start_server.py
   ```

### Client Side

1. **Install Tor:**  
   - As above, install and run Tor so the SOCKS5 proxy is available on `127.0.0.1:9050`.

2. **Install Python dependencies:**  
   ```
   pip install -r requirements.txt
   ```

3. **Configure environment:**  
   - Copy `client/.env.example` to `client/.env`.
   - Set `SERVER_IP` to the server's `.onion` address (from `/var/lib/tor/servicename/hostname` on the server).
   - Set `PORT=4444` (must match the port in `torrc`).

4. **Start the client:**  
   ```
   python start_client.py
   ```

---

## Setup TL;DR (Critical Steps)

**1. Set the same port everywhere:**
   - Use `4444` as the default port in both your `torrc` and all `.env` files (server and client).

**2. On the server:**
   - Edit `/etc/tor/torrc`:
     ```
     HiddenServiceDir /var/lib/tor/servicename/
     HiddenServicePort 4444 127.0.0.1:4444
     ```
   - Restart Tor: `sudo systemctl restart tor`
   - Get the `.onion` address from `/var/lib/tor/servicename/hostname`.
   - Set `SERVER_IP=localhost` and `PORT=4444` in `.env`.
   - Run `python start_server.py`.

**3. On the client:**
   - Set up and run Tor (SOCKS5 proxy on `127.0.0.1:9050`).
   - Set `SERVER_IP=<server_onion_address>` (from the server's hostname file) and `PORT=4444` in `client/.env`.
   - Run `python start_client.py`.

**Note:** The client must use the `.onion` address from the server, and the port must match exactly in all configs.

---

## Conclusion

This project provides a simple, robust, and private way to communicate over the Tor network. With easy setup and a modern terminal interface, it is ideal for secure, anonymous group chats. For more details, see the code and comments in each module.

---
