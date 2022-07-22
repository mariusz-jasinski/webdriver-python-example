# PDF Demo of Selenium WebDriver 
Tests in Docker container. Chrome Browser runs in Docker too.  
This Python's example is generating PDF File or Screenshot File (PNG Image) from any webPage.


 
Helper commands:
```
docker-compose build && docker-compose up -d pytest
docker logs -f sample_pytest_1
docker cp sample_pytest_1:/tmp/file.pdf .
docker cp sample_pytest_1:/tmp/page.png .
```

Helper links:
- https://www.rokpoto.com/selenium-tests-in-docker/
- https://www.selenium.dev/selenium/docs/api/py/api.html
- https://www.smashingmagazine.com/2021/12/headers-https-requests-ui-automation-testing/
- https://github.com/wkeeling/selenium-wire
