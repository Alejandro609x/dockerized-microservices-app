# Configuración de Conexiones entre Servicios

Este documento explica cómo se configuran y gestionan las **conexiones** entre los diferentes microservicios y bases de datos dentro del proyecto contenerizado.

---

## ¿Qué es una conexión en este contexto?

Una conexión es el vínculo que permite a un microservicio comunicarse con otro servicio o con una base de datos para intercambiar datos, hacer consultas o enviar información.

---

## Conexiones comunes en el proyecto

1. **Microservicio ↔ Base de datos**

   Cada microservicio debe conectarse a su base de datos correspondiente para almacenar y recuperar datos. Por ejemplo:

   - Microservicio de usuarios → Base de datos MySQL
   - Microservicio de productos → Base de datos PostgreSQL

2. **API Gateway ↔ Microservicios**

   El API Gateway actúa como intermediario, redirigiendo las peticiones externas a los microservicios adecuados (usuarios, productos, etc.).

3. **Microservicios ↔ Archivos compartidos**

   Algunos servicios pueden necesitar acceder a archivos compartidos, por ejemplo, CSV ubicados en volúmenes.

---

## ¿Qué falta configurar?

- **Variables de entorno:**  
  Se deben definir las variables necesarias para que los servicios conozcan la dirección, puerto, usuario y contraseña de la base de datos.  
  Ejemplo:
  ```env
  DB_HOST=mysql_service
  DB_PORT=3306
  DB_USER=root
  DB_PASSWORD=secret
  DB_NAME=users_db
