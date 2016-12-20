# trivia
Small Flask, SQLite3, Bootstrap application that collected the submissions for ACE's Hacker Movie Still-Frame Trivia

## Development Installation Instructions

    git clone git@github.com:LaTechACE/trivia.git
    cd trivia
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cp trivia.config.default trivia.config
    nano trivia.config
    export FLASK_APP=trivia
    flask initdb

0. Clone Git Repository
0. Move into Application Directory
0. Create Virtualenv
0. Activate Virtualenv
0. Install Application Dependencies
0. Copy the default configuration to your own file
0. Modify the copy of the default configuration
   * database: The Database file to store submissions
   * secret_key: Key to secure Admin authentication
   * admin_user: Username to log in to the Admin page
   * admin_pass: Password to log in to the Admin page
0. Export FLASK_APP variable for flask command
0. Initialize the Database

## Execution Instructions

    export FLASK_APP=trivia
    export FLASK_DEBUG=1
    flask run

0. Export FLASK_APP variable with application name
0. Export FLASK_DEBUG variable to turn debug on
0. Run the app with flask
