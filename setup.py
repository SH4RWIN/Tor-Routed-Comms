#!/usr/bin/env python3
"""
Setup script for Dark Comm Terminal Chat
"""

import os

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = ".env"
    if not os.path.exists(env_file):
        with open(env_file, 'w') as f:
            f.write("SERVER_IP=localhost\n")
            f.write("PORT=12345\n")
        print("Created .env file with default settings")
    else:
        print(".env file already exists")

def main():
    print("Setting up Dark Comm Terminal Chat...")
    create_env_file()
    print("Setup complete!")
    print("\nTo start the server: python src/server.py")
    print("To start a client: python src/client.py")

if __name__ == "__main__":
    main()
