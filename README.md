


<a name="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br>
<div align="center">
  <a href="https://github.com/Johnny-FTW/Django-Profile-Viewer">
    <img src="https://raw.githubusercontent.com/Johnny-FTW/Django-Profile-Viewer/main/static/images/favicon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Profile Viewer</h3>

  <p align="center">
    Introducing Profile Viewer, a new social site that lets you create your own profile, follow other people, 
and connect with them through real time chat. With Profile Viewer, you can easily stay updated on your friends'
and family's latest news, statuses, and activities.

  </p>
</div>

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
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## About The Project




Main system features:
* User registration and login.
* Creating and editing events by organizers (user with a special role).
* Commenting on events by a logged in users.
* Signing up for events.
* Events search engine.
* API for other websites / services that want to present events.

### Built With

* [![Python][Python.org]][Python-url]
* [![Django][Django.com]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

General Guidelines:
* Website development using Django and Django REST Framework as an API.
* Introducing the division into models, views and controllers in the application and placing the appropriate logic in each of them.
* Securing access to the application and functionality by using django.contrib.auth

Screenshots:

![image](https://raw.githubusercontent.com/Johnny-FTW/EventAggregationService/main/imgs/Screenshot_1.png)
<br>
![image](https://raw.githubusercontent.com/Johnny-FTW/EventAggregationService/main/imgs/Screenshot_2.png)
<br>
![image](https://raw.githubusercontent.com/Johnny-FTW/EventAggregationService/main/imgs/Screenshot_3.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running follow these simple example steps.

### Requirements

List of requirements:
* Django==4.1.6


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

Below is an example of how to install and set up this app.

1. Clone the repo
   ```sh
   git clone https://github.com/Johnny-FTW/EventAggregationService.git
   ```
2. Install project dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Then simply apply the migrations
   ```sh
   python manage.py migrate
   ```
4. You can now run the development server
   ```sh
   python manage.py runserver
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

- Jan Hatapka - [Linkedin](https://www.linkedin.com/in/jan-hatapka-6b970b205/) - mail: jan.hatapka@gmail.com 


Project Link: [https://github.com/Johnny-FTW/Django-Profile-Viewer](https://github.com/Johnny-FTW/Django-Profile-Viewer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




[Python.org]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Django.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/


[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 


[contributors-shield]: https://img.shields.io/github/contributors/Johnny-FTW/Django-Profile-Viewer.svg?style=for-the-badge
[contributors-url]: https://github.com/Johnny-FTW/Django-Profile-Viewer/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Johnny-FTW/Django-Profile-Viewer.svg?style=for-the-badge
[forks-url]: https://github.com/Johnny-FTW/Django-Profile-Viewer/network/members

[stars-shield]: https://img.shields.io/github/stars/Johnny-FTW/Django-Profile-Viewer.svg?style=for-the-badge
[stars-url]: https://github.com/Johnny-FTW/Django-Profile-Viewer/stargazers

[issues-shield]: https://img.shields.io/github/issues/Johnny-FTW/Django-Profile-Viewer.svg?style=for-the-badge
[issues-url]: https://github.com/Johnny-FTW/Django-Profile-Viewer/issues

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/Johnny-FTW/Django-Profile-Viewer/blob/main/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jan-hatapka-6b970b205/
