sudo systemctl stop gothic_lowcost_armada.service
git stash
git pull
sudo cp *.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl restart craftfromsilentpond.service