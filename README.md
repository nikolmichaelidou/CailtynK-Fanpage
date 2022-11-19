# Caitlyn Kirraman Fan-Website

## Description

This a fan-website for the fictional character Caitlyn Kiramman from the popular game League Of Legends and the award winning show Arcane!

## UX

## Features

- Home page
  - The home page features a header with an animated background
  ![](imgs/Screenshot_20221119_112809.png)
  - Along with a welcome message
    ![](imgs/Screenshot_20221119_112901.png)
- Contact page
  - in this page user will be able to provide feedback and ideas on how imporve the website
    ![screenshot](imgs/Screenshot_20221119_112338.png)  

## Bugs & Fixes

- Cannot deploy to Heroku due to "App not compatible with buildpack" error.
  - Have not found a way to resolve this error
- IP missmatch error from Heroku CLI.
  - According to their website, the platform requires that the IP address of both the CLI and web browser align. This means that you will need to have the same proxy setup for both the CLI and the browser used to authenticate. You'll need to configure the web proxy in the CLI with the 'https_proxy option'.
    - So far that has not worked and the deployment has been difficult.
