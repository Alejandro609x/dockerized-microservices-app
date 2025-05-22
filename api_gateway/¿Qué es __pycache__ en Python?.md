# 🧠 ¿Qué es `__pycache__` en Python?

`__pycache__` es una carpeta **automática** que crea Python para acelerar tu código 🚀

---

### 🔍 ¿Para qué sirve?

Cuando ejecutas un archivo `.py`, Python **lo traduce a bytecode** 🧾 (una forma intermedia que entiende más rápido).

🔁 Para no repetir ese trabajo cada vez, Python guarda esa "traducción" en `__pycache__` como archivos `.pyc`.

---

### 📦 ¿Qué contiene?

Archivos `.pyc` como:

```
__pycache__/
  mi_script.cpython-311.pyc  👈 Compilado con Python 3.11
```

➡️ El nombre incluye la versión de Python para evitar errores entre versiones.

---

### ❓¿Puedo borrarla?

✅ **Sí**, puedes eliminarla sin miedo.
🛠️ Se volverá a crear automáticamente la próxima vez que ejecutes tu script.

💡 Tip: En proyectos con Git, se **ignora** con esta línea en `.gitignore`:

```
__pycache__/
```

---

### 🚫 ¿Cómo evito que se genere?

Puedes evitar que se cree usando esta variable de entorno al ejecutar:

```bash
PYTHONDONTWRITEBYTECODE=1 python mi_script.py
```

🧩 *No recomendado en producción*, ya que los `.pyc` mejoran el rendimiento.

---

### ✅ Conclusión

`__pycache__` es como la **memoria cache de tu código**:

📂 guarda versiones rápidas de tus scripts

⚡ acelera el arranque

🧹 se puede eliminar

🛡️ mejor ignorarlo en Git

