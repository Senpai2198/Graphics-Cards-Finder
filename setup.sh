mkdir -p ~/.streamlit/

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml

echo PORT $PORT
streamlit run  --server.port $PORT Nvidia_Graphics_Cards_Finder.py
