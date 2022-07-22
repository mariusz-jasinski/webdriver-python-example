# Demo of Selenium WebDriver 
Tests in Docker container. Chrome Browser runs in Docker too.
Python example is generating PDF File from any webPage.


 
Helper commands:
```
docker-compose build && docker-compose up -d tests
docker logs -f sample_tests_1
docker cp sample_tests_1:/tmp/file.pdf /vagrant/
```

Helper links:
- https://www.rokpoto.com/selenium-tests-in-docker/
- https://www.selenium.dev/selenium/docs/api/py/api.html
- https://www.smashingmagazine.com/2021/12/headers-https-requests-ui-automation-testing/
- https://github.com/wkeeling/selenium-wire
