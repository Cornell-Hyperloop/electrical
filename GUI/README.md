## Setup
1. Clone the Hyperloop repository (use SSH)
    * [Generate SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    * [Add new SSH key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

2. Switch to the UI branch, pull any recent changes, and navigate to GUI folder
    ```
    git checkout UI
    git pull
    cd GUI
    ```

3. Create a virtual environment
    `python -m venv <environment_name>`
    * Example: `python -m venv gui_env`

4. Activate the virtual environment
    * MacOS/Linux: `source <environment_name>/bin/activate`
        * Example: `source gui_env/bin/activate`
    * Windows: `<environment_name>\Scripts\activate`
        * Example: `gui_env\Scripts\activate`

5. Install the required dependencies: `python -m pip install -r requirements.txt`

6. Run the GUI: `python main.py`

7. Deactivate the virtual environment (when finished working): `deactivate`


## Widget Choices & Reasoning
1. Window : MainWindow
2. Sensor tabs: QTabWidget
- Fits nicely accordingly to the Figma design
- Alternative QStackWidget did not work because it does not allow multiple widgets appear on the same stack, thus not able to layout widgets as shown in the design
3. Window Layout : QSplitter
- QSplitter splits the main window into different sections and allows layout embedding within the sections
- Alternative QLayout does not allow embedding of the sensor tabs
4. Plotting Graph : PlotWidget
- Embedded in the layouts of sensor tabs (on the left)
- Currently displaying data from dummy arrays
- But, can extract sample data from a txt file of the same file directory instead by replacing `second` and `temperature` with `xs` and `ys`
