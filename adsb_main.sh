#!/bin/bash

python -m ensurepip --upgrade

pip install -r requirements.txt

<<<<<<< HEAD
npm install

npm run build
=======
python -c "import app; app.run()" 
>>>>>>> parent of 11f59b2 (doc update)

if [ $? -eq 0 ]; then
    echo "Started, check log for more info on runtime events"
else
    echo "Failed to run, check if there is a requirements.txt file in the same directory as this script"
    exit 1
fi