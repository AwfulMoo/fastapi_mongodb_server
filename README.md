<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">fastapi_mongodb_server</h3>

  <p align="center">
    Template for a simple python FastAPI connecting to mongodb 
    <br />
    <br />
    <a href="https://github.com/AwfulMoo/fastapi_mongodb_server/issues">Report Bug</a>
    ·
    <a href="https://github.com/AwfulMoo/fastapi_mongodb_server/issues">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a blank template for a Python based asynchronous API. This project makes use of FastAPI, Pydantc and includes Motor as an asynchronous Python driver for MongoDB.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![FastAPI][FastAPI.tiangolo.com]][FastAPI-url]
* [![Pydantic][Pydantic.dev]][Pydantic-url]
* [![Motor][Motor.readthedocs.io]][Motor-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Some basic installation and setup details can be found below.

### Prerequisites

I'd recommend using Poetry to manage the dependecy installation/ virtual environment setup.
* Poetry
  ```sh
  curl -sSL https://install.python-poetry.org | python3 -
  ```
* MongoDB  
  See the [the download page](https://www.mongodb.com/try/download/community/) or the [docker image](https://hub.docker.com/_/mongo)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AwfulMoo/fastapi_mongodb_server.git
   ```
2. Install Python packages (from inside the cloned repo)
   ```sh
   poetry install
   ```
3. Select the Python intpreter (use the path to the poetry virtual env created in the last step)
   ```sh
   poetry install
   ```
4. Update the config.py file to include database connection settings as needed

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Edit and expand on the application as needed.

You can debug the application by pressing *F5* in [Visual Studio Code](https://code.visualstudio.com/) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Stage your changes (`git add yourChangedFile.filetype`)
5. Commit your changes (`git commit -m 'Added an AmazingFeature!'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a pull request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/AwfulMoo/fastapi_mongodb_server](https://github.com/AwfulMoo/fastapi_mongodb_server)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AwfulMoo/fastapi_mongodb_server.svg?style=for-the-badge
[contributors-url]: https://github.com/AwfulMoo/fastapi_mongodb_server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AwfulMoo/fastapi_mongodb_server.svg?style=for-the-badge
[forks-url]: https://github.com/AwfulMoo/fastapi_mongodb_server/network/members
[stars-shield]: https://img.shields.io/github/stars/AwfulMoo/fastapi_mongodb_server.svg?style=for-the-badge
[stars-url]: https://github.com/AwfulMoo/fastapi_mongodb_server/stargazers
[issues-shield]: https://img.shields.io/github/issues/AwfulMoo/fastapi_mongodb_server.svg?style=for-the-badge
[issues-url]: https://github.com/AwfulMoo/fastapi_mongodb_server/issues
[license-shield]: https://img.shields.io/badge/LICENSE-MIT-yellow?style=for-the-badge
[license-url]: https://github.com/AwfulMoo/fastapi_mongodb_server/blob/master/LICENSE
[Pydantic.dev]: https://img.shields.io/badge/Pydantic-E92063.svg?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjAgMTIwIj4KICA8cGF0aAogICAgIGZpbGw9IiNmZmYiCiAgICAgZD0iTSAxMTkuMTgsODYuNjQgOTguMDIsNTcuMyBjIDAsMCAwLDAgMCwwIEwgNjMuNzcsOS44IGMgLTEuNzQsLTIuNCAtNS43NiwtMi40IC03LjQ5LDAgbCAtMzQuMjQsNDcuNDkgYyAwLDAgMCwwIDAsMCBMIDAuODcsODYuNjQgYyAtMC44NiwxLjIgLTEuMSwyLjczIC0wLjY1LDQuMTMgMC40NiwxLjQgMS41NSwyLjUgMi45NSwyLjk2IGwgNTUuNDEsMTguMTQgYyAwLDAgMCwwIDAuMDEsOWUtNCAwLjQ2LDAuMTUgMC45NCwwLjIzIDEuNDMsMC4yMyAwLjQ5LDAgMC45NywtMC4wOCAxLjQzLC0wLjIzIDAsMCAwLDAgMC4wMSwwIEwgMTE2Ljg3LDkzLjczIGMgMS40LC0wLjQ2IDIuNSwtMS41NSAyLjk1LC0yLjk2IDAuNDYsLTEuNCAwLjIyLC0yLjkzIC0wLjY1LC00LjEzIHogbSAtNTkuMTUsLTY2LjI1IDIyLjIxLDMwLjggLTIwLjc3LC02LjggYyAtMC4xNiwtMC4wNSAtMC4zMywtMC4wNCAtMC40OSwtMC4wOCAtMC4xNiwtMC4wNCAtMC4zMiwtMC4wNiAtMC40OCwtMC4wOCAtMC4xNiwtMC4wMiAtMC4zMSwtMC4wOCAtMC40NywtMC4wOCAtMC4xNiwwIC0wLjMxLDAuMDYgLTAuNDcsMC4wOCAtMC4xNywwLjAyIC0wLjMyLDAuMDQgLTAuNDgsMC4wOCAtMC4xNiwwLjAzIC0wLjMzLDAuMDMgLTAuNDgsMC4wOCBoIDAgbCAtMjAuNjQsNi43NiAtMC4xMywwLjA0IDIyLjIxLC0zMC44IHogbSAtMzEuMzgsNDMuNTIgMjQuMTgsLTcuOTIgMi41OCwtMC44NCBWIDEwMS4xMiBMIDEyLjA2LDg2LjkyIFogbSAzNiwzNy4yIFYgNTUuMTUgbCAyNi43Niw4Ljc2IDE2LjU5LDIzIHoiLz4KPC9zdmc+Cg==
[Pydantic-url]: https://docs.pydantic.dev/latest/
[FastAPI.tiangolo.com]: https://img.shields.io/badge/FastAPI-grey?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
[Motor.readthedocs.io]: https://img.shields.io/badge/Motor-FFF467.svg?style=for-the-badge&logo=data:image/x-icon;base64,AAABAAEAICAQAAEABADoAgAAFgAAACgAAAAgAAAAQAAAAAEABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtJyAAXlAyAC9L1ACAcVgAKXvHAJ2PdwCLjJEAuKiPAEmotABVyNYAVL3+AOrWswB86/EAY/L/AP///wAAAAAA7N3d3d3d3d3d3d3d3d3dzs3d3d3d3d3d3d3d3d3Nzdzd3d2dnJmZ3c3ZnZ2d3d3d3d3YMzNTU93dY1MzM23d3d3d2RERERDd3YERERGd3d3d3d3BETETPdgREREY3c3d3d3N2DMzMRiBMzMzjd3d3d3d3d0zE1V1VVMzM53d3d3d3d3dk1d3EQF3cxnd3d3d1lbN2VV3cRMQN1dWzdlnjde7XZNSZ1d3d1V2JY3Xu33Lu72HJCd3VVd3ckI527u52btpVohld3d3d3aIZtd7zd252HRId+t1N7Z3giPNa93dtpZ3Zne3d3W7W2Z1iHvd3Hu1dnd1dXd3V1d3Z1u23d3cxl7mczdxV1M3budtzd3d3dh+DlV1d3dXV+Dnbd3d3d3YfgtXvld161dg523d3d3d2V7ud3uzW7d37uWN3d3c3dxXZ1d1c1dXd3Z1zdzd3d3dZzEXd3d3d3ETdt3d3d3d3ZUVV3ImaEdzMTzd3d3d3d3Yd3d0RJRGd3eM3d3d3c3dzYd3ZEgiRndY3d3N3d3d3d3YV2hCJGZ1nd3d3d3d3d3d3dgzVVMznd3d3d3d3d3d3aqqgzMzOJot3d3d3d3dzdzcrYMzMziq3N3N3N3d3d3d3d3IiIiM3d3d3d3dzd3d3d3d3d3d3d3d3d3d3Ozd3d3d3d3d3d3d3d3d3c4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
[Motor-url]: https://rich.readthedocs.io/