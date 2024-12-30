# 걸엉가게

This repository is for the backend of the project '걸엉가게'.

- [Landing Page](https://github.com/9oormthon9th/FE)
- [Frontend Repository](https://github.com/9oormthon9th/FE/blob/main/README2.md)
- Backend: This repository.
- [Deployment Repository](https://github.com/9oormthon9th/Deployment): Deployment on DKOS.

## Installation

> [!NOTE]
> This project uses Python 3.6 as D2Hub had a Python 3.6 image available back then. <br>
> If you don't have Python 3.6 installed, you can use [pyenv](https://github.com/pyenv/pyenv) to install it.

1. Clone the git repository:
   ```bash
   git clone https://github.com/9oormthon9th/BE2.git
   cd BE2
   ```
2. Install Python 3.6 and select it:
   ```bash
   pyenv install 3.6.15
   pyenv shell 3.6.15
   ```
3. Create a virtual environment for the project:

   As python 3.6 is selected, `python3` and `pip3` commands will use python 3.6
   ```bash
   pip3 install virtualenv
   python3 -m virtualenv my_env
   # => created virtual environment CPython3.6.15.final.0-64 in 271ms
   ```
5. Activate the virtual environment and install dependencies:
   ```bash
   source my_env/bin/activate
   # In my_env environment, do following
   pip3 install -r requirements.txt
   ```

## Usage

1. Set your OpenAI API key in the `./mnt/.secret` file.

   You can rename `./mnt/.secret.template` to `./mnt/.secret` and set your OpenAI API key in it.

2. Run the server:
   ```bash
   (my_env) $ flask run
   ```
3. Test the server at [http://localhost:5000/api/ready](http://localhost:5000/api/ready)

## Endpoints

- [`/api/ready`](http://localhost:5000/api/ready): Check if the server is ready.
- [`/api/test/course?theme=xxx`](http://localhost:5000/api/test/course?theme=xxx): Get information of course six regardless of input.
- [`/api/course?theme=example`](http://localhost:5000/api/course?theme=example): Get a recommended course based on the input.
- [`/api/food?food=example`](http://localhost:5000/api/food?food=example): Get a recommended food based on the input.
