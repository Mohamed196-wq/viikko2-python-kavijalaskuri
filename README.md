# Week 2 – Python Web Application and Database

## Project Description

This project was created for Week 2 of the Linux course at Oamk.

The web application runs on an Ubuntu 24.04 server hosted on CSC cPouta.

**Website:** http://195.148.20.80/viikko2/

## Technologies Used

- **Python and Flask:** Web application development.
- **Nginx:** Forwards HTTP requests to the Python application.
- **Gunicorn:** Runs the Python application.
- **SQLite:** Stores the visitor counter.
- **systemd:** Starts the application automatically when the server boots.

## Visitor Counter

The website displays a visitor counter that increases by one every time the page is loaded.

The counter is stored in an SQLite database called `visits.db`.

The database keeps the previous counter value, so the visitor count is not reset when the application or server restarts.

## Testing

The following tests were completed:

- The Python application returned HTTP status code **200**.
- The visitor counter increased from **2 to 3** after refreshing the webpage.
- The Python service showed **active** status.
- The SQLite database stored the visitor count correctly.
- After reconnecting to the restarted server, the Python service was active and the database still contained the previous count of **3**.

## Project Structure

- `app.py` – Flask application, HTML webpage, and SQLite visitor counter.
- `visits.db` – SQLite database stored on the server, not published on GitHub.

## Security

Passwords, private keys, access tokens, and database files are not included in the public GitHub repository.
