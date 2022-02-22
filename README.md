<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://charliealgert.com/">
    <img src="https://charliealgert.com/Watchdog.png" alt="Logo" width="700" height="">
  </a>
  <p align="center">
    <strong>Monitoring, Reporting, and Logging For Your Tor Relay</strong>
    

<center> - Nightly Email Traffic Reports</center>
<center>  - mySQL Traffic Logging </center>
<center> - Utime and Connections to be Implemented Soon</center>

</p>
<br/>
    <center>
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
    </center>
    <hr/>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A utility made to monitor your tor relay through the inbuilt api. Has SQL logging capabilities and sends nightly HTML fancy email reports updating you on the status of your relay. Fully configurable for local or remote sql and smtp

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Python](https://python.org/)
* [mySQL](https://www.mysql.com/)
* [HTML](https://vuejs.org/)
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

 - Running Tor Relay with full access to operator control
 - SMTP Server
 - mySQL DB and user with read/write access
 - Python 3x

### Installation/Setup
 1. Clone the repo
	   ```sh
	   git clone https://github.com/algertc/Tor_watchdog.git
	   ```
 2. Edit config.ini (all fields are strings. Do not use quotes.

		```
		[RELAY_AUTH]
		hashPass = YOUR_RELAY_PASSWORD

		[SMTP_AUTH]
		smtpUser = 
		smtpPass = 

		[MYSQL]
		host = 
		user = 
		passwd = 

		[SMTP_OUTPUT]
		receivingAddr = Address to which the reports should be sent

 3. Run the main once for testing. 
  	   ```sh
	   cd Tor_watchdog
	   python3 main.py
	   ```

 4. If all is well, kill the script and run it in background.
  	   ```sh
	   python3 main.py &
	   ```
 6. Done!

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
