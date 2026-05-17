from win10toast import ToastNotifier

toaster = ToastNotifier()


def show_notification(title, message):

    toaster.show_toast(
        title,
        message,
        duration=10,
        threaded=True
    )