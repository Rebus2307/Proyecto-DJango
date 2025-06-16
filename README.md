
# Proyecto-DJango

Backend RESTful desarrollado en Django + PostgreSQL, completamente dockerizado. Este proyecto forma parte de la **Práctica 4 de Ingeniería de Software** (ESCOM - IPN).

---

## 🛠️ Tecnologías Utilizadas

- Python 3.12
- Django 5.2.3
- Django REST Framework
- PostgreSQL 15
- Docker & Docker Compose

---

## 🧱 Estructura del Proyecto

```
Proyecto-DJango/
├── backend/                   # Proyecto Django
├── recomendaciones/          # Aplicación principal
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── wait-for.sh               # Script para esperar a PostgreSQL
└── README.md
```

---

## ⚙️ Instalación Manual (modo local)

### 1. Crear entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install django djangorestframework psycopg2-binary
pip freeze > requirements.txt
```

### 3. Crear proyecto y app
```bash
django-admin startproject backend .
python manage.py startapp recomendaciones
```

### 4. Configurar base de datos y registrar la app en `INSTALLED_APPS`

### 5. Ejecutar migraciones y levantar el servidor
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🐳 Ejecución con Docker

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd Proyecto-DJango
```

### 2. Descargar el script `wait-for.sh`
```bash
curl -o wait-for.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
chmod +x wait-for.sh
```

### 3. Levantar los servicios
```bash
docker-compose build
docker-compose up
```

Esto construye la imagen, levanta PostgreSQL y el backend Django en:
👉 [http://localhost:8000](http://localhost:8000)

---

## 🔐 Crear superusuario (admin)

```bash
docker exec -it django_backend bash
python manage.py createsuperuser
```

Luego accede a:  
👉 [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 📡 Endpoints disponibles

| Método | Ruta                                | Descripción                     |
|--------|-------------------------------------|---------------------------------|
| POST   | /api/usuarios/registro/             | Registrar nuevo usuario         |
| GET    | /api/libros/                        | Listar libros                   |
| GET    | /api/recomendaciones/<id_usuario>/  | Ver recomendaciones del usuario |

---

## 📝 Notas

- Este backend fue construido desde cero con enfoque modular y dockerizado.
- Se puede conectar con una aplicación Flutter (por crear) para consumir los endpoints REST.
- Compatible con despliegue local o en servidores cloud.

---

## 📄 Licencia

Proyecto académico realizado para la materia de **Ingeniería de Software**  
Escuela Superior de Cómputo — Instituto Politécnico Nacional