Deployment Instructions
-----

1. Run `pip install -r requirements.txt` to install the required dependencies (you may want to run this within an virtualenv)
2. Run `python _get_access_token.py` to generate your personal Access Token Keys and Access Token Secret, and place it into the `config.py` file
3. Place our Consumer Key and Consumer Secret into the `config.py` file as well
4. Run `python main.py` and the application will run on port `5000`


>###Please do not commit the `config.py` file as it contains your private keys. Committing them enables others to gain access to your Twitter account and do bad things.###