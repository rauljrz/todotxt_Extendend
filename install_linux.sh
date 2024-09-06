#!/bin/bash

# Obtener el directorio home del usuario
HOME_DIR=$(eval echo ~$USER)

# Verificar si existe el archivo .todo
TODO_CONFIG="$HOME_DIR/.todo"
if [ ! -f "$TODO_CONFIG" ]; then
    echo "Creando archivo .todo..."
    
    # Crear la carpeta Life si no existe
    LIFE_DIR="$HOME_DIR/Life"
    mkdir -p "$LIFE_DIR"
    
    # Crear la carpeta Inbox dentro de Life si no existe
    INBOX_DIR="$LIFE_DIR/Inbox"
    mkdir -p "$INBOX_DIR"
    
    # Crear el archivo .todo con las entradas correspondientes
    cat > "$TODO_CONFIG" << EOL
TODO_FILE = $LIFE_DIR/todo.txt
DONE_FILE = $LIFE_DIR/done.txt
HELP_FILE = $INBOX_DIR/todohelp.txt
EOL
    echo "Archivo .todo creado con éxito."
else
    echo "El archivo .todo ya existe."
fi

# Crear la carpeta ~/bin si no existe
BIN_DIR="$HOME_DIR/bin"
if [ ! -d "$BIN_DIR" ]; then
    echo "Creando carpeta ~/bin..."
    mkdir -p "$BIN_DIR"
fi

# Copiar archivos a ~/bin
echo "Copiando archivos a ~/bin..."
cp todo.py "$BIN_DIR/"
cp todohelp_es.txt "$BIN_DIR/"
cp todohelp.txt "$BIN_DIR/"

# Crear alias
echo "Creando alias..."
BASHRC="$HOME_DIR/.bashrc"
if ! grep -q "alias t='python ~/bin/todo.py'" "$BASHRC"; then
    echo "alias t='python ~/bin/todo.py'" >> "$BASHRC"
    echo "Alias 't' creado con éxito."
else
    echo "El alias 't' ya existe en .bashrc."
fi

# Agregar ~/bin al PATH si no está ya
if ! grep -q "export PATH=\$HOME/bin:\$PATH" "$BASHRC"; then
    echo "export PATH=\$HOME/bin:\$PATH" >> "$BASHRC"
    echo "~/bin añadido al PATH."
fi

echo "Instalación completada. Por favor, reinicia tu terminal o ejecuta 'source ~/.bashrc' para aplicar los cambios."