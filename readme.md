# Proyecto de Conversión de Divisas

## Juan Camilo Ramírez Rátiva - 20181020089
### Universidad Distrital Francisco José de Caldas

Este proyecto es un servicio de conversión de divisas construido con Flask, SQLAlchemy y SQLite.

- Sustentación en video - [aquí](https://youtu.be/wgvkPq1hAvo).

## Cómo ejecutar el proyecto

1. **Clonar el repositorio**
    ```
    git clone https://github.com/wthoutjc/currency-ud-backend
    ```

2. **Crear un entorno virtual (opcional)**
    ```
    python3 -m venv venv
    source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
    ```

3. **Instalar las dependencias**
    ```
    pip install -r requirements.txt
    ```

4. **Ejecutar la aplicación**
    ```
    python app.py
    ```

Ahora puedes acceder a la aplicación en tu navegador en `http://localhost:5000`.

## Endpoints

- `/currency`: Permite añadir una nueva moneda a la base de datos o obtener los detalles de una moneda específica.
- `/exchange_rate`: Permite añadir una nueva tasa de cambio a la base de datos o obtener los detalles de una tasa de cambio específica.
- `/convert`: Convierte una cantidad de una moneda a varias otras monedas.

Para más detalles sobre estos endpoints, consulta la documentación de la API en Swagger UI en `http://localhost:5000/api/docs`.

¡Espero que disfrutes del proyecto! Si tienes alguna pregunta o sugerencia, no dudes en ponerse en contacto.

## Extras

1. Frontend

Se utilizó Next.js 13+ con Typescript para poder crear una UI interactiva que consuma los servicios de esta API.

Puedes acceder a los recursos en:

- Accede al repositorio Frontend [aquí](https://github.com/wthoutjc/currency-ud-frontend).

- Accede al stage de producción [aquí](https://currency-ud-wthoutjc.vercel.app/)
- Link secundario stage prod [aquí](https://main.d31ipbj5l777pl.amplifyapp.com/)

2. AWS

Se utilizó AWS (Lambda, CodePipeline & CodeBuild, S3) para poder crear un entorno de despligue a producción con CI/CD.

Puedes acceder a los recursos en:

- Accede al endpoint en stage de producción  [aquí](https://o69lfswzia.execute-api.sa-east-1.amazonaws.com/Prod/currency).

3. Swagger & Pytest

Se utilizó Swagger para documentar los diferentes endpoints y pytest para realizar unitesting a los diferentes endpoints.

Nota: Por el momento solo está disponible los endpoints documentados en Swagger, root-endpoint no disponible.
