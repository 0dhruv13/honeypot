import socket
import logging
from datetime import datetime

# Configure logging to save attacker data
logging.basicConfig(
    filename="honeypot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def start_honeypot(host="0.0.0.0", port=2222):
    # Create a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((host, port))
        server.listen(5)
        print(f"[*] Honeypot active. Listening on {host}:{port}...")
        
        while True:
            # Accept incoming connection from the attacker
            client_conn, client_addr = server.accept()
            logging.info(f"CONNECTION FROM: {client_addr[0]}:{client_addr[1]}")
            print(f"[!] Alert: Connection from {client_addr[0]}:{client_addr[1]}")
            
            try:
                # Fake banner to mimic a real service (e.g., Ubuntu SSH)
                client_conn.sendall(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n")
                
                # Receive attacker's login attempt or commands
                data = client_conn.recv(1024)
                if data:
                    payload = data.decode('utf-8', errors='ignore').strip()
                    logging.info(f"PAYLOAD FROM {client_addr[0]}: {payload}")
                    print(f"[-] Data received: {payload}")
                    
                # Send a generic login failure message
                client_conn.sendall(b"Permission denied, please try again.\r\n")
                
            except Exception as e:
                print(f"[x] Error handling client: {e}")
            finally:
                client_conn.close()
                
    except KeyboardInterrupt:
        print("\n[*] Shutting down honeypot safely.")
    except Exception as e:
        print(f"[x] Bind failed: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    # Port 2222 is used to avoid needing root privileges
    start_honeypot()
