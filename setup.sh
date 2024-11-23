mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = False\n\
headless=True\n\
\n\
" > ~/.streamlit/config.toml