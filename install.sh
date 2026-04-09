INSTALL_DIR="$(cd "$(dirname "$0")" && pwd)"
DEST_DIR="/opt/vdb-clock"
START_DIR="$(cd "$(dirname "$0")" && pwd)"

sudo mkdir -p "$DEST_DIR"

INSTALL_DIR="$DEST_DIR" 

sudo cp "$START_DIR/app.py" "$DEST_DIR/"
sudo cp "$START_DIR/requirements.txt" "$DEST_DIR/"

if command -v apt &> /dev/null; then
    sudo apt install -y python3-venv
elif command -v pacman &> /dev/null; then
    sudo pacman -S --noconfirm python-virtualenv
fi

python3 -m venv "$INSTALL_DIR/venv"
"$INSTALL_DIR/venv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"
sudo python3 -m venv "$INSTALL_DIR/venv"
sudo "$INSTALL_DIR/venv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"

echo "#!/bin/bash
$INSTALL_DIR/venv/bin/python $INSTALL_DIR/app.py" | sudo tee /usr/local/bin/vdb-clock
