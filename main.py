from Tiktok_uploader import uploadVideo


if __name__ == '__main__':
    session_id = "35e9dfdb17b7c871f5fcfa943995eb7b"
    file = "data/twitch_clip.mp4"
    title = "TEST TEST"
    tags = ["Funny", "Joke", "fyp"]

    uploadVideo(session_id, file, title, tags, verbose=True)
