@shared_task
def rpi_capture_image(project, number):
    """
    capture image from camera
    """
    import picamera
    #now = datetime.datetime.now()
    #now_str = now.strftime('%Y%m%d:%H:%M:%S')
    #print now_str
    name = project.name
    #print name
    if not os.path.exists(IMAGE_PATH):
        call(["mkdir", IMAGE_PATH])
    image_number = str(number).zfill(7)
    path = "%s%s/" % (IMAGE_PATH, name)
    call(["mkdir", path])
    filename = "%s_%s.jpg" % (name, image_number)
    #call(["fswebcam", "-r", "1280x720", "--no-banner", "%s%s" % (path, filename)])
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.start_preview()
        camera.exposure_compensation = 2
        camera.exposure_mode = 'spotlight'
        camera.meter_mode = 'matrix'
        camera.image_effect = 'gpen'
        # Give the camera some time to adjust to conditions
        time.sleep(2)
        camera.capture("%s%s" % (path, filename))
        camera.stop_preview()
    image = File(open('%s%s' % (path, filename), 'r'))
    ti = TimelapseImage(name=name, image=image, timelapse=project)
    ti.save()
    print "photo taken"
