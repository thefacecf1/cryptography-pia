# cryptography-pia

## Installation
``` docker compose up --build ```
## Usage
1. Logearse en dos tabs distintas en http://localhost:8080
2. Mandarse mensajes entre las dos tabs
3. Ver la magia :3
## How works?
1. Despues de logear a un usuario y se entra al chat
2. Se establece una conexion por medio de WebSockets
3. Cuando cualquier usuario envia un mensaje,
el backend emite un evento en donde envia una lista nueva con todos los mensajes a todos sus clientes
