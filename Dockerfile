# Usa un'immagine Python ufficiale come base
FROM python:3.11-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia il file requirements.txt
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia l'intero progetto
COPY . .

# Espone la porta di Bokeh (default: 5006)
EXPOSE 5006

# Comando per avviare l'applicazione con Bokeh server
CMD ["bokeh", "serve", "main.py", "--show", "--allow-websocket-origin", "*"]
