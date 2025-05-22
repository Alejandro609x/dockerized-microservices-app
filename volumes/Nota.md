# Directorio `volumes`

El directorio `volumes` es un espacio **dedicado a almacenar datos persistentes** que necesitan sobrevivir a la detención o eliminación de contenedores Docker.  

---

## ¿Qué es un volumen en Docker?

Un volumen es un método para **guardar datos fuera del contenedor**, permitiendo que la información:

- Se conserve aun cuando el contenedor se elimine o reinicie.
- Sea compartida entre varios contenedores.
- Se administre y respalde fácilmente desde el sistema anfitrión.

---

## ¿Por qué usamos un directorio `volumes` en este proyecto?

Dentro del proyecto, `volumes` es el lugar donde se guardan:

- Bases de datos (por ejemplo, datos de MySQL o PostgreSQL).
- Archivos compartidos entre servicios (como archivos CSV).
- Cualquier otro dato que debe mantenerse disponible a pesar de la vida efímera del contenedor.

Esto garantiza que **la información no se pierda** al actualizar o reiniciar los contenedores.

---

## Ejemplo de estructura común

```plaintext
volumes/
├── mysql_data/       # Datos persistentes para la base MySQL
├── postgres_data/    # Datos persistentes para la base PostgreSQL
├── shared_csv/       # Archivos CSV compartidos entre microservicios

