After building the model on local machine and integrating with FastAPI with code.<br>

We can run FastAPI at the backend using following code in terminal: <br>

```uvicorn main:app --reload```

and use streamlit to open web app: <br>

```streamlit run \path\to\streamlit.py```

This will open a web app on the default browser where we can place the HTML block within the text area and click on `Parse HTML` to view the response.