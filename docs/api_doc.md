After model deployment on local machine using FastAPI with code: <br>

```uvicorn main:app --reload```

the Fast API documentation can be viewed from http://localhost:8000/docs where we can send the html block within `html_input` and click on `Execute` to view response. <br>

Or,

We can run FastAPI at the backend using following code in terminal: <br>

```uvicorn main:app --reload```

and use streamlit to open web app: <br>

```streamlit run \path\to\streamlit.py```

This will open a web app on the default browser where we can place the HTML block within the text area and click on `Parse HTML` to view the response.

*P.S: For better UI experience and prevent errors, it's suggested to use streamlit rather than using FastAPI documentation because it may throw errors.* 