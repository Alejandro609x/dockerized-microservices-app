# 🚀 Dockerized Microservices Application

Este proyecto implementa una arquitectura de microservicios contenerizada con Docker. Está compuesta por:

- 🧍‍♂️ Microservicio de Usuarios (Python + MySQL)
- 📦 Microservicio de Productos (Python + PostgreSQL)
- 🌐 API Gateway (FastAPI)
- 🗃️ Bases de datos independientes para usuarios y productos
- 📂 Volúmenes para persistencia de datos y compartición de archivos

> ⚠️ **Estado actual**: Todos los contenedores se crean correctamente, incluidos los de MySQL y PostgreSQL. Sin embargo, los microservicios de usuarios y productos aún no están conectados a sus respectivas bases de datos en contenedores (MySQL y PostgreSQL). Actualmente, ambos microservicios utilizan bases de datos locales en memoria, lo que significa que los datos se pierden al reiniciar los servicios.

---

## 📁 Estructura del Proyecto

Al descomprimir el archivo Microservicios.zip, se generará un directorio llamado Microservicios, dentro del cual encontrarás la carpeta API. Esta carpeta contiene la estructura del proyecto, la cual se muestra a continuación:

```
API
├── api_gateway                            # Punto de entrada a los servicios
│   ├── Dockerfile
│   ├── main.py
│   ├── _pycache_
│   │   └── main.cpython-311.pyc
│   └── requirements.txt
├── docker-compose.yml                      # Orquestador de todos los servicios
├── products_service                        # Servicio de productos (CRUD) con PostgreSQL — conexión a la base de datos no disponible actualmente
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src
│       ├── controllers
│       │   ├── products_controller.py
│       │   └── _pycache_
│       │       └── products_controller.cpython-311.pyc
│       ├── dtos
│       │   ├── product_dto.py
│       │   └── _pycache_
│       │       └── product_dto.cpython-311.pyc
│       ├── main.py
│       └── _pycache_
│           └── main.cpython-311.pyc
├── users_service                              # Servicio de usuarios (CRUD) con MySQL — conexión a la base de datos no disponible actualmente
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src
│       ├── controllers
│       │   ├── _pycache_
│       │   │   └── users_controller.cpython-311.pyc
│       │   └── users_controller.py
│       ├── dtos
│       │   ├── _pycache_
│       │   │   └── user_dto.cpython-311.pyc
│       │   └── user_dto.py
│       ├── main.py
│       └── _pycache_
│           └── main.cpython-311.pyc
└── volumes                                     # Volúmenes persistentes y compartidos
    ├── mysql_data
    ├── postgres_data
    ├── shared_csv
    │   └── users.csv
    └── users.csv
````
🔹 Nota: CRUD es el acrónimo de Create (Crear), Read (Leer), Update (Actualizar) y Delete (Eliminar), que representan las operaciones básicas para gestionar datos en una aplicación.

Create (Crear): Añadir nuevos registros o datos.

Read (Leer): Consultar o recuperar información existente.

Update (Actualizar): Modificar datos existentes.

Delete (Eliminar): Borrar registros.

---
Por ejemplo, en un sistema de gestión de usuarios como el nuestro:

Crear un usuario nuevo → POST /usuarios

Consultar un usuario → GET /usuarios/{id}

Actualizar los datos de un usuario → PUT /usuarios/{id}

Eliminar un usuario → DELETE /usuarios/{id}

---

## 🔧 Servicios

### 🧍‍♂️ Microservicio de Usuarios
- CRUD completo de usuarios (nombre, apellido, correo)
- Destinado a conectarse con una base de datos **MySQL**
- Escribe un archivo CSV (`users.csv`)
- Actualmente usa una base local (no persistente)
- Expuesto internamente al API Gateway

### 📦 Microservicio de Productos
- CRUD completo de productos (nombre, precio, descripción)
- Destinado a conectarse con una base de datos **PostgreSQL**
- Actualmente usa una base local (no persistente)
- Expuesto internamente al API Gateway

### 🌐 API Gateway
- Basado en **FastAPI**
- Único punto de acceso para clientes externos
- Lee el archivo `users.csv` desde volumen compartido
- Expone Swagger UI en `http://localhost:8000/docs`

### 🗃️ Bases de Datos
- MySQL: Almacena usuarios con persistencia (aún no conectada)
- PostgreSQL: Almacena productos con persistencia (aún no conectada)

---

## 🌐 Endpoints Disponibles

Actualmente disponibles a través del API Gateway en `http://localhost:8000`:

### Usuarios (5 endpoints)
- `GET /users` — Obtener todos los usuarios
- `GET /users/{id}` — Obtener un usuario por ID
- `POST /users` — Crear usuario
- `PUT /users/{id}` — Actualizar usuario
- `DELETE /users/{id}` — Eliminar usuario

### Productos (5 endpoints)
- `GET /products` — Obtener todos los productos
- `GET /products/{id}` — Obtener un producto por ID
- `POST /products` — Crear producto
- `PUT /products/{id}` — Actualizar producto
- `DELETE /products/{id}` — Eliminar producto

🔟 **Total: 10 endpoints REST disponibles**

---

## 📄 Archivos CSV

- 📝 `users.csv`: generado automáticamente por el microservicio de usuarios.
- 📂 Volumen compartido `volumes/shared_csv` permite que el API Gateway lea este archivo.

---

## 📦 Volúmenes Usados

| Servicio     | Volumen                              | Ruta interna en contenedor                   |
|--------------|---------------------------------------|----------------------------------------------|
| MySQL        | `mysql_data`                         | `/var/lib/mysql`                             |
| PostgreSQL   | `postgres_data`                      | `/var/lib/postgresql/data`                   |
| Compartido   | `shared_csv`                         | `/shared_csv`                                |

---

## 🐳 Docker Compose

Orquesta los cinco servicios:

```bash
docker-compose up --build
````

Contenedores que levanta:

* `usuarios`
* `productos`
* `api-gateway`
* `db-mysql`
* `db-postgresql`

---

## 🧪 Ejemplos de uso con `curl`

### Crear usuario

```bash
curl -X POST http://localhost:8000/users \
-H "Content-Type: application/json" \
-d '{"nombre": "Ana", "apellido": "López", "correo": "ana@example.com"}'
```

### Crear producto

```bash
curl -X POST http://localhost:8000/products \
-H "Content-Type: application/json" \
-d '{"nombre": "Teclado", "precio": 49.99, "descripcion": "Mecánico retroiluminado"}'
```

---

## 🛠️ Requisitos

* Docker
* Docker Compose

---

## 🧹 Limpieza

Para detener y eliminar todos los contenedores, redes, y volúmenes:

```bash
docker-compose down -v
```

---

## ⚠️ Pendientes

* [ ] Conectar el microservicio de usuarios a la base de datos MySQL
* [ ] Conectar el microservicio de productos a la base de datos PostgreSQL
* [ ] Persistencia de datos confirmada tras reinicios
* [ ] Validación de lectura del archivo `users.csv` desde API Gateway

---

## 👨‍💻 Autor

Desarrollado por **Alejandro** como parte de un proyecto de arquitectura de microservicios contenerizados con Docker y FastAPI realizado en un curso de Madrid-España.
¡Se agradecen ideas, mejoras y pull requests!

