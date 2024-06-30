import speedtest

def bandwidth_meter():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    st.results.share()
    results = st.results.dict()
    print(f"Download: {results['download'] / 1_000_000:.2f} Mbit/s")
    print(f"Upload: {results['upload'] / 1_000_000:.2f} Mbit/s")
    print(f"Ping: {results['ping']} ms")
