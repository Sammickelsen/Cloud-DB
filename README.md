# Overview

A basic program that connects to Google Firebase's Firestore Database.  The program gives the user a simple space to save user information.  The user can add first and last name, as well as an email.  The program runs in the user's terminal and allows them to Read, Write, Update, and Delete data as necessary.

This project was a chance for me to learn to use cloud databases as an option for data management in the future.  Having a simple cloud database allows me to understand how I can better apply one to a larger scale project

[Software Demo Video](https://youtu.be/3KzIFXI2e3Y)

# Cloud Database

The database that I decided to go with is Google Firebase's Firestore.  It is a simple cloud database that allows the user to save information in various formats, but is often shown in a JSON format, which is super useful when programming.

My database is relatively simple.  I am using one collection (Basically a table) called User Info, which only holds three "columns" of data.  Those columns are "First Name", "Last Name", and "Email".

# Development Environment

I used python to create my program in vscode.  I used the firebase_admin library in order to easily access the data saved in Firestore.

# Useful Websites

- [YouTube Tutorial](https://www.youtube.com/watch?v=-jWD-vIyirw&t=126s)
- [Firebase Python Docs](https://firebase.google.com/docs/reference/admin/python)
- [Importing data into Firestore using Python](https://medium.com/@cbrannen/importing-data-into-firestore-using-python-dce2d6d3cd51)

# Future Work

- I want to work on creating a GUI for easier use
- I need to increase the scale of my database, adding additional tables and data sets
- I want to continue to add additional query functions, allowing the user to have a better control on what they are filtering.