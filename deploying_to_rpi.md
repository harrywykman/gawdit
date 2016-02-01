# Deploying to Rpi

`sudo apt-get install python-dev python-setuptools`

`sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk`

* change locale to en_US.UTF-8
* restart


`cd /usr/local/src`
`wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz`
`tar xzf noip-duc-linux.tar.gz`
`cd noip-2.1.9-1`
`make`
`make install`

`vim /etc/init.d/noip2`

    #! /bin/sh
    # /etc/init.d/noip

    ### BEGIN INIT INFO
    # Provides:          noip
    # Required-Start:    $remote_fs $syslog
    # Required-Stop:     $remote_fs $syslog
    # Default-Start:     2 3 4 5
    # Default-Stop:      0 1 6
    # Short-Description: Simple script to start a program at boot
    # Description:       A simple script from www.stuffaboutcode.com which will start / stop a program a boot / shutdown.                                           l
    ### END INIT INFO
    # If you want a command to always run, put it here
    # Carry out specific functions when asked to by the system
    case "$1" in
      start)
        echo "Starting noip"
        # run application you want to start
        /usr/local/bin/noip2
        ;;
      stop)
        echo "Stopping noip"
        # kill application you want to stop
        killall noip2
        ;;
      *)
        echo "Usage: /etc/init.d/noip {start|stop}"
        exit 1
        ;;
    esac

    exit 0



`fab all`  # in mezzanine app virtualenv


`sudo apt-get install rabbitmq-server`
