[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<div align="center">
    <h3 align="center">Graph Search Visualizer</h3>
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#running-the-application">Running the Application</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project

<br/>
<div align="center">
    <img src="img/graph-search.png" width="700">
</div>
<br/>

This Plotly Dash web application visualizes the path and the nodes visited by two graph search algorithms: breadth-first
search and A*. The grid is initialized with obstacles forming a maze. The obstacle cells can be added or removed by
clicking on the
grid cells. Moreover, the locations of the start and end cells can also be moved.

### Built With

* [Plotly Dash][dash-url]

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

The application assumes Python version of 3.6+

```bash
$ pip install plotly
$ pip install dash
$ pip install dash-bootstrap-components 
```

### Running the Application

```bash
$ python main.py
```

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[license-url]: LICENSE.txt

[linkedin-url]: https://www.linkedin.com/in/faerlin-pulido/

[dash-url]: https://dash.plotly.com

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555