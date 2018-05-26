Example usage:

```sh
virtualenv -p `which python2.7` .
source bin/activate

brew install graphicsmagick
brew install boost-python

pip install -r tools/requirements.txt
```

```sh
source bin/activate
python tools/mk_thumbnails.py ~/Downloads/IMG_*.JPG
```
