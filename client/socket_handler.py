"""
Client Socket Handler Module
Handles all socket connections and message communication for the chat client
"""

import socket
import threading
import json
import time
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

class ClientSocketHandler:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False
        self.running = False
        self.message_callback = None
        self.error_callback = None
        self.lock = threading.Lock()
        
    def set_message_callback(self, callback):
        """Set callback function for received messages"""
        self.message_callback = callback
    
    def set_error_callback(self, callback):
        """Set callback function for errors"""
        self.error_callback = callback
    
    def log_message(self, message, level="INFO"):
        """Log messages with timestamp and color coding"""
        timestamp = time.strftime("%H:%M:%S")
        color = Fore.GREEN if level == "INFO" else Fore.RED if level == "ERROR" else Fore.YELLOW
        print(f"{color}[{timestamp}] {level}: {message}{Style.RESET_ALL}")
    
    def connect(self):
        """Connect to the server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.connected = True
            self.running = True
            self.log_message(f"Connected to {self.host}:{self.port}")
            return True
        except Exception as e:
            self.log_message(f"Failed to connect to server: {e}", "ERROR")
            if self.error_callback:
                self.error_callback(f"Connection failed: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from the server"""
        self.running = False
        self.connected = False
        
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
            self.socket = None
        
        self.log_message("Disconnected from server")
    
    def send_message(self, message_data):
        """Send a message to the server"""
        if not self.connected or not self.socket:
            self.log_message("Not connected to server", "ERROR")
            return False
        
        try:
            message_json = json.dumps(message_data) + "\n"
            self.socket.send(message_json.encode())
            return True
        except Exception as e:
            self.log_message(f"Failed to send message: {e}", "ERROR")
            if self.error_callback:
                self.error_callback(f"Send failed: {e}")
            return False
    
    def receive_messages(self):
        """Handle incoming messages from server"""
        buffer = ""
        while self.running and self.connected:
            try:
                data = self.socket.recv(1024)
                if not data:
                    break
                    
                buffer += data.decode()
                
                # Process newline-delimited JSON messages
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    if not line.strip():
                        continue
                    
                    try:
                        message_data = json.loads(line)
                        if self.message_callback:
                            self.message_callback(message_data)
                    except json.JSONDecodeError:
                        self.log_message(f"Received invalid JSON: {line}", "ERROR")
                        continue
                        
            except Exception as e:
                if self.running:
                    self.log_message(f"Error receiving messages: {e}", "ERROR")
                    if self.error_callback:
                        self.error_callback(f"Receive error: {e}")
                break
        
        # Connection lost
        self.connected = False
        if self.error_callback:
            self.error_callback("Connection lost")
    
    def start_receiving(self):
        """Start the message receiving thread"""
        if not self.connected:
            self.log_message("Not connected to server", "ERROR")
            return False
        
        receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
        receive_thread.start()
        return True
    
    def is_connected(self):
        """Check if client is connected to server"""
        return self.connected and self.socket is not None
    
    def get_connection_info(self):
        """Get connection information"""
        if self.connected:
            return f"{self.host}:{self.port}"
        return "Not connected"
    
    def cleanup(self):
        """Clean up resources"""
        self.disconnect()
    
    def run_client(self, message_callback=None, error_callback=None):
        """Run the client with callbacks"""
        if message_callback:
            self.set_message_callback(message_callback)
        if error_callback:
            self.set_error_callback(error_callback)
        
        if not self.connect():
            return False
        
        if not self.start_receiving():
            return False
        
        return True
