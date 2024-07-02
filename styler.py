import streamlit as st

def customize_style():
    st.markdown(
        f"""
        <style>
          .stApp {{
                background: linear-gradient(135deg, #1a237e, #6a1b9a);
                background-attachment: fixed;
                background-size: cover;
                font-family: 'Open Sans', sans-serif;
                font-size: 18px;
                color: #ffffff; /* Branco */
                padding: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                box-sizing: border-box;
            }}
          .stApp h1 {{
                font-size: 3em;
                color: #1a237e; /* Azul escuro */
                font-weight: bold;
                text-align: center;
                text-transform: uppercase;
                letter-spacing: 2px;
                margin-bottom: 20px;
            }}
          .st-expander {{
                border: 2px solid #6a1b9a; /* Roxo mais escuro */
                border-radius: 10px;
                margin-bottom: 20px;
            }}
          .timeline {{
                list-style: none;
                padding: 0;
                margin-top: 30px;
                width: 100%;
            }}
          .timeline-item {{
                display: flex;
                flex-direction: row;
                align-items: flex-start;
                margin-bottom: 40px;
                border-left: 2px solid #6a1b9a; /* Roxo mais escuro */
                padding-left: 20px;
            }}
          .timeline-item:last-child {{
                border: none;
            }}
          .timeline-item.title {{
                font-size: 24px;
                font-weight: bold;
                margin-right: 20px;
                color: #6a1b9a; /* Roxo mais escuro */
            }}
          .timeline-item.description {{
                font-size: 18px;
                color: #ffffff; /* Branco */
            }}
          .columns {{
                display: flex;
                flex-direction: row;
                justify-content: space-between;
                width: 100%;
                margin-top: 30px;
            }}
          .column {{
                width: 48%;
                background-color: rgba(255, 255, 255, 0.8);
                padding: 20px;
                border-radius: 10px;
                border-bottom: 2px solid #6a1b9a; /* Roxo mais escuro */
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5);
            }}
          .column h3 {{
                font-size: 24px;
                color: #6a1b9a; /* Roxo mais escuro */
                margin-bottom: 10px;
            }}
          .column p {{
                font-size: 18px;
                color: #ffffff; /* Branco */
            }}
          h1 > div > a, h2 > div > a, h3 > div > a, h4 > div > a, h5 > div > a, h6 > div > a {{
                display: none!important;
            }}
          .stButton > button {{
                background-color: #4adbf0; /* Azul claro */
                color: #ffffff; /* Branco */
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
          .stButton > button:hover {{
                background-color: #1a237e; /* Azul escuro */
            }}
          .stColumn {{
                flex: 1;
                margin: 10px;
                padding: 20px;
                background-color: #ffffff;
                border: 1px solid #dddddd;
                border-radius: 10px;
            }}
          .container:first-child {{
                background-image: url('https://grupodoublenet.com.br/wp-content/uploads/2023/11/Banner-Site-AZUL-1.jpg');
                background-size: cover;
                background-position: center;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                padding: 3em;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                width: 80%;
                max-width: 1245px;
                height: 150px;
                margin: auto;
                margin-top: 50px;
                background-color: rgba(255, 255, 255, 0.2); /* Ajuste da opacidade */
                border: 4px solid #cccccc; /* Borda branca grossa */
            }}
          .title {{
                text-align: center;
                font-size: 3em;
                color: #ffffff; /* Branco */
                margin-top: 20px;
                font-weight: bold;
            }}
          .banner {{
                background-image: url('https://www.rnp.br/arquivos/2020-12/internetBR.jpeg?VersionId=1GG0j9T2Xpv8LprD.6MJAqQMlDiBHUJ9');
                background-size: cover;
                background-position: center;
                padding: 2em;
                border-radius: 50px;
                text-align: center;
                margin-bottom: 2em;
                height: 300px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                border: 4px solid #cccccc; /* Borda branca grossa */
            }}
          .banner-content {{
                background-image: url('https://infoway.com.br/media/resize/1920x1080/pasta/1/64da333a03e0c.png');
                background-position: center;
                background-color: rgba(0, 0, 0, 0.6); /* Ajuste da opacidade */
                padding: 2em;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            }}
          .stTextInput > div > input {{
                background-color: #333333;
                color: #ffffff; /* Branco */
                border: 1px solid #555555;
                border-radius: 5px;
                padding: 0.5em;
                font-size: 1em;
            }}
          .stButton > button {{
                background-color: #0056b3; /* Azul escuro */
                color: #ffffff; /* Branco */
                border: none;
                border-radius: 5px;
                padding: 0.5em 1em;
                font-size: 1em;
                cursor: pointer;
            }}
          .stButton > button:hover {{
                background-color: #004080; /* Azul mais escuro */
            }}
          .col1 {{
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.5);
                border: 4px solid #cccccc; /* Borda branca grossa */
                margin-bottom: 20px;
            }}
          @media (max-width: 768px) {{
                .container {{
                    width: 95%;
                    margin-top: 20px;
                }}
                .banner {{
                    height: 300px;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
