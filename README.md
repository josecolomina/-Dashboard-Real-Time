# 📈 Dashboard Financiero en Tiempo Real

Este proyecto es un **panel de control interactivo** diseñado para visualizar métricas financieras en tiempo real. Simula la ingesta continua de datos de mercado (precios de acciones, volumen) y los presenta en un dashboard dinámico y moderno.

El objetivo principal es demostrar la implementación de una arquitectura de datos completa, desde la generación y almacenamiento de datos hasta su visualización en vivo.

## 🚀 Características Principales

*   **Ingesta de Datos en Tiempo Real (ETL)**: Un script de Python (`etl/ingestion.py`) genera datos simulados de mercado y los carga continuamente en una base de datos.
*   **Almacenamiento Persistente**: Uso de **SQLite** para almacenar el historial de transacciones, permitiendo análisis históricos y persistencia de datos.
*   **Visualización Interactiva**: Dashboard construido con **Streamlit** que se actualiza automáticamente para mostrar los últimos movimientos del mercado.
*   **Métricas Clave**: Visualización de KPIs instantáneos, gráficos de líneas para tendencias de precios y gráficos de barras para análisis de volumen.

## 🛠️ Tecnologías Utilizadas

*   **Python**: Lenguaje principal del proyecto.
*   **Streamlit**: Framework para la creación del dashboard web interactivo.
*   **SQLite**: Base de datos SQL ligera y eficiente para el almacenamiento de datos.
*   **Pandas**: Manipulación y análisis de datos.
*   **Plotly**: Librería de gráficos interactivos para las visualizaciones.

## 📂 Estructura del Proyecto

```
Dashboard-Real-Time/
├── dashboard/
│   └── app.py            # Aplicación principal de Streamlit (Frontend)
├── data/
│   └── finance.db        # Base de datos SQLite (generada automáticamente)
├── etl/
│   └── ingestion.py      # Script de ingesta de datos (ETL Backend)
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Documentación en Español
└── README_en.md          # Documentation in English
```

## ⚙️ Instalación y Uso

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.  **Clonar el repositorio**:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd Dashboard-Real-Time
    ```

2.  **Instalar las dependencias**:
    Asegúrate de tener Python instalado. Se recomienda usar un entorno virtual.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Iniciar el proceso de Ingesta de Datos (ETL)**:
    Abre una terminal y ejecuta el script de ingestión. Este script debe mantenerse en ejecución para simular el flujo de datos en tiempo real.
    ```bash
    python etl/ingestion.py
    ```
    *Verás logs en la consola indicando que los datos se están insertando.*

4.  **Iniciar el Dashboard**:
    Abre una **segunda terminal** y ejecuta la aplicación de Streamlit.
    ```bash
    streamlit run dashboard/app.py
    ```

5.  **Explorar**:
    El dashboard se abrirá automáticamente en tu navegador (usualmente en `http://localhost:8501`). Verás cómo los gráficos y métricas se actualizan en tiempo real a medida que el script ETL inserta nuevos datos.

## 🔍 Cómo Funciona

1.  **Generación**: `etl/ingestion.py` crea registros aleatorios de acciones (Símbolo, Precio, Volumen) cada segundo.
2.  **Almacenamiento**: Estos registros se guardan en la tabla `stock_prices` dentro de `data/finance.db`.
3.  **Lectura**: `dashboard/app.py` consulta la base de datos periódicamente para obtener los últimos 1000 registros.
4.  **Visualización**: Streamlit procesa los datos con Pandas y actualiza los gráficos de Plotly y las métricas en la interfaz de usuario.

---
*Este proyecto es parte de mi portafolio profesional, demostrando habilidades en Ingeniería de Datos y Desarrollo Full Stack con Python.*
