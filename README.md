# CML Streamlit

A minimal example of a [Streamlit](https://www.streamlit.io/) application running as a CML or CDSW Application.
We'll refer only to CML from here on out, but the instructions are exactly the same for CDSW.

## Instructions

Create a new CML project from git, or otherwise clone this repo into a CML project.

Open a Python 3 session in CML.

Install Streamlit by running `!pip3 install -r requirements.txt` in the Python REPL to the right.

There are two scripts relevant to running Streamlit as a CML Application:

```bash
app.py        # this is the streamlit app itself
launcher.py   # this is the script we pass to the CML Application to launch our app
```

Create a new Application by navigating to the Applications pane on the left.
Fill in the details similarly to the screenshot below.

![Creating a new streamlit application](https://user-images.githubusercontent.com/6513950/99111374-e71a5a80-25e3-11eb-8fe1-ac93ce7d1869.png)

Once the Application has been created, you can launch it from the Applications pane.
This should open a browser window, with a Streamlit application running at a URL something like `streamlit-demo.cml.your-organization.com`.

If everything worked, you should see something like this:

![A working streamlit app](https://user-images.githubusercontent.com/6513950/99112467-9e63a100-25e5-11eb-9932-778ef5309e7a.png)

To develop the Streamlit app, return to the Python 3 session, and hack away.
Hot reloading of the app on save should work.

Happy hacking!
