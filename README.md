# stackstats app

stackstats is a simple command line app that can retrieve data from the StackExchange API and calculate some simple statistics, within a time interval, provided by the User.

## Instructions for User to use

In order to run the app, first make sure you have Python 3.6.8 already installed on your machine. Then, follow the instructions:

- Open terminal (command line) in project directory and run the following command, in order to create a virtual environment:
```bash
python3 -m venv venv
```
- Activate the virtual environment:

    - If you are on **Windows** environment run:
    ```bash
    .\venv\Scripts\activate
    ```
    - If you are on **Linux** environment run:
    ```bash
    source venv/bin/activate
    ```
- Then install the app by running the command:
```bash
pip install .
```
- Then you can run the application: On the terminal (with your virtual environment active) you may type:
```bash
stats "YYYYMMDD HH:MM:SS" "YYYYMMDD HH:MM:SS" --output-format xxxx
```
  **Additional Information**
  - The format in which you should pass the arguments must be in the specified form indicated as above. First argument indicates 'since' and second indicates 'until'
  - The first 2 arguments are positional arguments, which means that you **must** provide them, else you will get an error
  - The third argument is an optional argument and you can avoid it. By default, the statistics are returned in json. The different format options
    are **json, csv and html**

## Instructions for Development

This app is written in Python 3.6.8. All required dependent libraries (along with their versions) can be found into the requirements.txt file. To open the project for development purposes you should run:
```bash
pip install -r requirements.txt
```
and then (for testing)

```bash
pip install -r requirements.tests.txt
```
Then you could run ```bash pytest``` to run the tests

  **Additional Information**:
  -  Depending on what OS you are on (Linux or Windows), the test "test_convert_string_to_epoch_succeeded()" may not pass because the underlying C libraries for time.mktime used by the Python implementations for Windows and Linux are different.
     [source](https://docs.python.org/3/library/time.html#time.mktime)
