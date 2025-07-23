echo "Installing Required Dependecies. . ."
sudo apt install python3-pip -y
pip install subprocess webbrowser random requests time
sudo apt-get install apache2-utils
sudo apt-get install siege
mkdir BlackEye
git clone https://github.com/EricksonAtHome/blackeye BlackEye
cd BlackEye
chmod +x blackeye.sh
RED="\033[31m"

MESSAGE=" Required Packages Installed, you may proceed to run the software "
echo -e "${RED}${MESSAGE}"
