Single Sign-On, aka SSO, is a session and user authentication service that permits a user to use one set of login credentials to access multiple applications. A great example is Google; Google has many services, such as Google Play, Gmail, and YouTube. Once a user has successfully login into one of the applications via Google Account, it would seamlessly go into the application. The benefits of that are greater security and compliance, improvement of usability, and lower IT costs. 

SSO is mostly managed by Active Directory Federation Service, aka AD FS. First of all, before explaining AD FS, let's talk about Active Directory. It is a hierarchical structure that stores information about objects on the network. It provides the methods for storing directory data and making data to administrators and users via the network. Nextly, AD FS is the service provided by Microsoft for SSO solution using Active Directory. It provides users with authenticated access to applications. 

idP-initiated SSO:

<!-- ![idP-initiated SSO](/assets/SSO/Picture2.png =250x250) -->
<img src="/assets/SSO/Picture2.png" alt="drawing" width="400">

SP-initiated SSO:

<img src="/assets/SSO/Picture3.png" alt="drawing" width="400">

Note: the big gray/blue rectangles on both of the pictures can be interpreted as VM or on-premise. Tomcat, Pentaho, and Node.js is pre-installed in the machine and Angular application is deployed in the Tomcat. LOGIN (SecureAuth) is one identity provider that used in this senerio.

I implemented prototype idP-initiated SSO using Node.js ; more specifically I optimized parsing the SAML Assertion data by using "[samlify][samlfiy]".

Because this project was aimed to use AngularCLI with an implementation of single web application, it was a steep learning curve in the beginning. It took me quite sometimes to understand how to use Angular as well as get familiar with TypeScript.


Pro:
- Reduce password fatigue
- increases speed where it needed
- simplifies user management 

Con:
- Might need extra-strong password (because only one username and passwrod will be needed)
- If SSO is down, all connection is down
- Takes longer time to set it up

Reference:
- [Samlify][samlfiy]
- [Single Sign-On onelogin][SSO]

[samlfiy]: https://www.npmjs.com/package/samlify
[SSO]:https://www.onelogin.com/learn/how-single-sign-on-works

[back](./)