# Creating a Digital Clock Application and Converting it to an Executable

This README will guide you through the steps to:

1. Install the required dependencies.
2. Run the digital clock application.
3. Convert the Python script to a standalone executable file.

## Prerequisites

Before you start, ensure that you have Python installed on your system. You can download the latest version of Python from [python.org](https://www.python.org/). Make sure to add Python to your system's PATH during installation.

---

## Step 1: Install Required Libraries

The script uses `customtkinter` for the user interface and `time` for retrieving the current time.

### Install `customtkinter`

To install the `customtkinter` library, open your terminal or command prompt and run the following command:

```bash
pip install customtkinter
```

### Install `PyInstaller`

To convert the Python script to an executable, you need `PyInstaller`. Install it using:

```bash
pip install pyinstaller
```

---

## Step 2: Run the Digital Clock Application

Save the provided Python code into a file named `watch.py`.

To run the digital clock, simply execute the script in your terminal or command prompt:

```bash
python watch.py
```

You should see a window displaying the current time.

---

## Step 3: Convert the Python Script to an Executable

Follow these steps to convert the `watch.py` file to a standalone `.exe` file:

1. Open a terminal or command prompt and navigate to the folder containing `watch.py`.
2. Run the following command to create an executable file:

   ```bash
   python -m PyInstaller watch.py --onefile --noconsole
   ```

   This will generate several folders and files:

   ```
   dotpytoexe/
   ├── build/
   ├── dist/
   │   ├── ...
   │   └── watch.exe
   └── watch.spec
   ```

3. Navigate to the `dist/` folder to find the `watch.exe` file.

---

## Step 4: Running the Executable

Double-click `watch.exe` in the `dist/` folder to run your digital clock as a standalone application. The console will not appear because of the `--noconsole` flag used during the conversion process.

---

## Cloning the Repository

You can clone the repository for this project from GitHub to get started:

```bash
git clone https://github.com/whistlink/dotpytoexe.git
```

This will download the project files, including the `watch.py` script and additional resources.

---

Congratulations! You have successfully created a digital clock and converted it to an executable file. Share your `watch.exe` with others, and they'll be able to run the digital clock without needing Python installed on their system.
