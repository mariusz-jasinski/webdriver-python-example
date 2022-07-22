from seleniumwire import webdriver  # Import from seleniumwire

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        wire_options = {
            'addr': hostname
        }

        # Create a request interceptor
        def header_interceptor(request):
            del request.headers['Authorization']
            request.headers['Authorization'] = TOKEN_JWT


        # Set the interceptor on the driver
        browserDriver.request_interceptor = header_interceptor
        print (wire_options)

        browserDriver = webdriver.Remote(command_executor=BROWSER_URL, options=chrome_options, seleniumwire_options=wire_options)
