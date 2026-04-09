#!/bin/bash
INSTALL_DIR="$(cd "$(dirname "$0")" && pwd)"

if command -v apt &> /dev/null; then
    sudo apt install -y python3-venv
elif command -v dnf &> /dev/null; then
    sudo dnf install -y python3-virtualenv
elif command -v pacman &> /dev/null; then
    sudo pacman -S --noconfirm python-virtualenv
fi

python3 -m venv "$INSTALL_DIR/venv"
"$INSTALL_DIR/venv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"

echo "#!/bin/bash
$INSTALL_DIR/venv/bin/python $INSTALL_DIR/app.py" | sudo tee /usr/local/bin/vdb-clock

sudo chmod +x /usr/local/bin/vdb-clock
echo "Done. Run 'vdb-clock' to start."