<h3 align="center">Flask Controller (w AJAX)</h3>
<p align="center">
  Control your GPIO pins using a flask backend, with room for a video feed (now with AJAX!)
<p>

<!-- TABLE OF CONTENTS -->
<details open="open"> <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This is a template for remote control of a Rpi. It is built on flask and has corrsponding up/down/left/right buttons and an iframe for you to put your video feed in.
This project uses AJAX to remove reloading of the webpage on every input. 
####IF YOU ARE USING THIS TEMPLATE, DO AT LEAST HAVE SOME FAMILIARITY WITH THE LANGUAGES/LIBRARIES THAT IT WAS BUILT WITH.

### Built With

* python==3.8.10
* flask==2.0.1
* Javascript
* jQuery 

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
Flask should be bundled with python on Rpi, just run the command
```sh
python3 -m pip freeze
```
to confirm it's installed, if it isn't just install it with
```sh
python3 -m pip install flask
```
jQuery is loaded from Google's CDN, however in the absence of internet access, it is also bundled with this project.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/makingandtinkering/flaskcontrollerwajax.git
   ```
2. Modify the template for your project
3. Run index_page.py script and direct your browser to Rpi's_IP_ADDRESS:5000 to see the page

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
If you are using this, just head down to the lab if you got any questions

Project Link: [https://github.com/makingandtinkering/flaskcontrollerwajax](https://github.com/makingandtinkering/flaskcontrollerwajax)
