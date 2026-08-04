from winotify import Notification, audio

toast = Notification( 
    app_id="Python Application",
    title="New Message",
    msg="This is a Windows notification.",
    launch = "https://www.youtube.com",
    duration="short"
)
toast.set_audio(audio.Default, loop=False)
toast.show()