import os
import smtplib


def connect_smtp_server(smtp_server: smtplib.SMTP_SSL) -> None:
    smtp_server.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
