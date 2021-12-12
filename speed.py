from say import speak
def test():
    import speedtest
    stt = speedtest.Speedtest()
    di=stt.download()
    up=stt.upload()
    speak(f"sir! uploading speed is {up} and downloadimg speed is {di}")

        