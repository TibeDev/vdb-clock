#!/bin/bash
INSTALL_DIR="$(cd "$(dirname "$0")" && pwd)"

python3 -m venv "$INSTALL_DIR/venv"
"$INSTALL_DIR/venv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"

echo "#!/bin/bash
$INSTALL_DIR/venv/bin/python $INSTALL_DIR/app.py" | sudo tee /usr/local/bin/vdb-clock

sudo chmod +x /usr/local/bin/vdb-clock
echo "Done. Run 'vdb-clock' to start."