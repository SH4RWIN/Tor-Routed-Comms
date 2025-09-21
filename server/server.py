"""
Dark Comm Chat Server
Main server application using the socket handler module
"""

import os
from dotenv import load_dotenv
from socket_handler import ServerSocketHandler

# Load environment variables
load_dotenv()

server_ip = os.getenv("SERVER_IP")
port = int(os.getenv("PORT"))

def display_server_info(socket_handler):
    """Display server startup information"""
    print(f"{'='*60}")
    print(f"🌐 Dark Comm Chat Server")
    print(f"{'='*60}")
    print(f"Server IP: {server_ip}")
    print(f"Port: {port}")
    print(f"Status: Running")
    print(f"Connected Clients: {socket_handler.get_connected_clients_count()}")
    print(f"{'='*60}")
    print()

def main():
    """Main server function"""
    # Create socket handler
    socket_handler = ServerSocketHandler(server_ip, port)
    
    try:
        # Start the server
        if not socket_handler.start_server():
            print("Failed to start server")
            return
        
        # Display server info
        display_server_info(socket_handler)
        
        # Run the server loop
        socket_handler.run_server_loop()
        
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, shutting down server...")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        socket_handler.cleanup()
        print("Server stopped")

if __name__ == "__main__":
    main()