from plyer import notification

notification.notify(
    title="Test Notification",
    message="Your reminder system is working!",
    timeout=10
)

print("Notification Sent")