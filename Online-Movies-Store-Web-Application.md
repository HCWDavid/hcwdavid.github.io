This project is the 122B project class, called "Project in Databases and Web Applications". 

I also had a awesome partner who has helped me to develop this project along the way and was able to make it work! 

This project introduces the modern data management techniques, such as database connectivity, web application development, extending database functions, database administration, and XML.

In addition, I have been explosed to cloud services, such as Amazon AWS and Google Cloud Platform. Launched instances on AWS to deploy the project, I was able to use my application through cloud and did some modification through it.

Here is a picture of my AMIs/used instances on AWS. P.S.: I have deleted my instances because of the monthly payment that I had to pay, so I created an image as a backup in case I want to have it back.
<!-- ![1 AWS](/assets/Online-Movies-Store-Web-Application/1.png) -->

<img src="/assets/Online-Movies-Store-Web-Application/1.png" alt="drawing" width="400">

This is our front-end pages look like (we also implemented fuzzy search and autocomplete in the main search bar):

<!-- ![2 Main Page](/assets/Online-Movies-Store-Web-Application/2.png) -->
<img src="/assets/Online-Movies-Store-Web-Application/2.png" alt="drawing" width="400">

Of course, it is the most simple and static web page we first created: 

<img src="/assets/Online-Movies-Store-Web-Application/3.png" alt="drawing" width="400">


Lastly, because it is a shopping website, there is a simple cart page to check out your products that you want to purchase!

<!-- ![4 Cart Page](/assets/Online-Movies-Store-Web-Application/4.png) -->
<img src="/assets/Online-Movies-Store-Web-Application/4.png" alt="drawing" width="400">

Databases connectivity (initialized in java backend to connect with the database):
```java
@Resource(name = "jdbc/readDB")
private DataSource dataSource;
```
POST:
```java
protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{
    response.setContentType("application/json");
    ...
}
```
GET:
```java
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	response.setContentType("application/json");
```

PreparedStatement in java to prevent SQL injection (what you need to do is to set the variable with the correct type into the question mark starting index of 1):
```java
String q = "SELECT ___FROM___WHERE___?___?___" ;
Connection  dbcon = dataSource.getConnection();
PreparedStatement statement = dbcon.prepareStatement(q);
statement.setString(1, somestring1);
statement.setString(2, somestring2);
ResultSet set = statement.executeQuery();
```

#FunPart (We also implemented ReCaptcha for checking robots as a security check):

```java
URL verifyUrl = new URL(SITE_VERIFY_URL);
// Open Connection to URL
HttpsURLConnection conn = (HttpsURLConnection) verifyUrl.openConnection();
// Add Request Header
conn.setRequestMethod("POST");
conn.setRequestProperty("User-Agent", "Mozilla/5.0");
conn.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
// Data will be sent to the server.
String postParams = "secret=" + RecaptchaConstants.SECRET_KEY + "&response=" + gRecaptchaResponse;
// Send Request
conn.setDoOutput(true);
```

Efficiency Improvement:

We implemented Master-slave replication servers and connection pooling to improve the speed of the web application: 

```java
# web.xml 
# Master/Slave replication, one for read-only, one for read/write
<resource-ref>
    <description>MySQL DataSource</description>
    <res-ref-name>jdbc/readDB</res-ref-name>
    <res-type>javax.sql.DataSource</res-type>
    <res-auth>Container</res-auth>
  </resource-ref>

...

# context.xml
# connection pooling
<Resource name="jdbc/readDB" auth="Container" type="javax.sql.DataSource"
              maxTotal="100" maxIdle="30" maxWaitMillis="10000" username="SomeUser"
              password="SomePassword" driverClassName="someDriverClass"
              url="someurl?autoReconnect=true&amp;useSSL=false&amp;cachePrepStmts=true"/>

<Resource name="jdbc/writeDB" auth="Container" type="javax.sql.DataSource"
            maxTotal="100" maxIdle="30" maxWaitMillis="10000" username="SomeUser"
            password="SomePassword" driverClassName="someDriverClass"
            url="someurl?autoReconnect=true&amp;useSSL=false&amp;cachePrepStmts=true"/>
```

Reference:
- Check out the class [web page][web-page] on how we did this project in detail with more instructions

[web-page]: https://grape.ics.uci.edu/wiki/public/wiki/cs122b-2019-winter

