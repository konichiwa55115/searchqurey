echo "Cloning Repo...."
git clone https://github.com/konichiwa55115/searchqurey /kony
cd /kony
pip3 install -r requirements.txt
wget https://archive.org/compress/booksbot48525x
unzip booksbot48525x
echo "Starting Bot...."
gunicorn app:app & python3 bot.py
