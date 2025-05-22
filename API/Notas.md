## 📂 Contenido de la Carpeta `API`

Como se mencionó anteriormente, dentro de la carpeta `API` se encuentra toda la estructura del proyecto, incluyendo los siguientes directorios:

* `api_gateway/`
* `products_service/`
* `users_service/`
* `volumes/`

Estos directorios corresponden a los microservicios y sus configuraciones, por lo que no se explicarán en esta sección. En cambio, nos enfocaremos en el archivo `docker-compose.yml`, ya que **desde esta carpeta (`API`) es donde debes ubicarte para ejecutar el orquestador y construir los contenedores.**

---

## 🚀 Construcción y Ejecución de los Contenedores

Para construir y levantar todos los servicios definidos en `docker-compose.yml`, puedes utilizar uno de los siguientes comandos desde el directorio `API`:

### ✅ Opción 1: Levantar contenedores en segundo plano

```bash
docker-compose build && docker-compose up -d
```

Este comando compila las imágenes y levanta los contenedores en segundo plano.
Puedes verificar que los cinco contenedores estén corriendo con:

```bash
docker ps
```

### 🛠️ Opción 2: Ver la salida en tiempo real

```bash
docker-compose build && docker-compose up
```

Este comando también compila y levanta los contenedores, pero **muestra en tiempo real los logs de cada servicio**. La terminal quedará ocupada, pero es útil para detectar errores durante la ejecución.
En este caso, como no se esperan errores, se recomienda usar la primera opción.

Nota: Los logs almacenan de forma secuencial los eventos o acciones que afectan a un sistema, aplicación o proceso.

---

## 🌐 Acceso a los Servicios Web

Una vez que los contenedores estén en funcionamiento, puedes acceder a la documentación interactiva de cada servicio (Swagger UI) a través de tu navegador:

* 🔹 API Gateway: [http://localhost:8000/docs](http://localhost:8000/docs)
* 🔹 Microservicio de Productos: [http://localhost:8001/docs](http://localhost:8001/docs)
* 🔹 Microservicio de Usuarios: [http://localhost:8002/docs](http://localhost:8002/docs)

---
