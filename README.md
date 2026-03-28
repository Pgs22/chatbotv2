# Práctica Final RA3 Análisis predictivo de la información

## Descripción
Proyecto **Generación Aumentada por Recuperación (RAG)**. El objetivo es permitir que un usuario realice preguntas en inglés sobre una base de conocimiento específica (almacenada en `documentos.json`). 

Resumen de funciones:
1.  **Recuperación**: Encuentra los documentos más similares a la consulta del usuario utilizando embeddings de `sentence-transformers`.
2.  **Aumentación**: Inyecta los documentos relevantes en un prompt diseñado para el modelo de lenguaje.
3.  **Generación**: Un modelo de lenguaje (LLM) genera una respuesta precisa basada exclusivamente en el contexto proporcionado.

## Estructura de Archivos
* `rag_engine.py`: Motor lógico que contiene las funciones de recuperación y generación.
* `app.py`: Interfaz gráfica de usuario construida con Gradio.
* `documents.json`: Base de datos de conocimiento en formato JSON.
* `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

## Subir a Github
cambia el fichero .gitognore.txt a .gitignore antes de subirlo al repositorio
### Desde la PowerShell
```bash
mv .\.gitignore.txt .\.gitignore
```
### Terminal Linux o Git Bash
```bash
mv .gitignore.txt .gitignore
```

# Limpiar la caché de Git para aplicar cambios .gitignore
```bash
git rm -r --cached .
git add .
git commit -m "Fix: renamed gitignore and cleared cache"
```

## Instrucciones de Instalación y Ejecución

### 1. Requisitos Previos
Tener instalado Python 3.9 o superior.

### 2. Instalación de Dependencias
Ejecuta el siguiente comando en tu terminal para instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

### 3. Ejecución del Proyecto
```bash
python app.py
```
