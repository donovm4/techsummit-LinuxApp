# techsummit-LinuxApp

## Commands for Linux VM

```bash
set -e  # Exit on error

sudo apt install python3.12-venv

python3 -m venv venv
source venv/bin/activate

echo "Installing Python ODBC package..."
pip install pyodbc

pip install -r requirements.txt

echo "Verifying pip packages..."
pip list | grep pyodbc || echo "pyodbc not found in pip list"

deactivate

echo "Installing unixODBC runtime..."
sudo apt-get update
sudo apt-get install -y unixodbc unixodbc-dev

echo "Setting up Microsoft keyring..."
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | \
  sudo tee /usr/share/keyrings/microsoft-prod.gpg > /dev/null

echo "Adding Microsoft SQL Server ODBC repository..."
echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/ubuntu/24.04/prod noble main" | \
  sudo tee /etc/apt/sources.list.d/mssql-release.list > /dev/null

echo "Updating package lists..."
sudo apt-get update

echo "Installing Microsoft ODBC Driver 18 for SQL Server..."
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18

echo "Installed ODBC drivers:"
odbcinst -q -d
```
