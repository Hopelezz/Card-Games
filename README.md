<div id="top"></div>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
 <h3 align="center">Card Games</h3>

  <p align="center">
    Games you can play against the computer.
    <br />
    <br />
    <a href="https://github.com/Hopelezz/Card-Games"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Hopelezz/Card-Games">View Demo</a>
    ·
    <a href="https://github.com/Hopelezz/Card-Games/issues">Report Bug</a>
    ·
    <a href="https://github.com/Hopelezz/Card-Games/issues">Request Feature</a>
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

[![Product Name Screen Shot][product-screenshot]]()

  Was working through the projects in a book called The Big Book of Small Python Projects. Landed on a bit of code called Blackjack. As a challenge I decided to alter to code to break out things that could be usuable between different card games. Talking with my son we came up with a game called War using similar concepts. To prove the game before even starting my girlfriend and I sat down and played a few rounds with an actual deck. We came to realize that based on the amount of your bets towards the end you could be close to wiping out your account. So we decided might be best to add a bonus payout.  


### Lessons Learned:
  In war I kept running into an issue where the Deck wasn't generating the Cards. This was a good leason on iterative loops. Found out that my "getDeck()" function wasn't outputting to proper values. 

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

Optimizations:
- [x] Added a Deck Module to use between different games.
- [x] Added Score Win/Lose ratio
- [x] Added rounds, when rounds hit 26 (Half of a deck) Based on the W/L ratio it'll award you a bonus payout.

<!-- ROADMAP -->
## Roadmap

- [ ] Selection menu where the user can call up which card game they'd wish to play.
- [ ] Player profile that collects game stats.
- [ ] FAdding new games like Go Fish, Old Maid (Need to learn this one), Poker 5-Card Draw, ect..
- [ ] Adding a UI

See the [open issues](https://github.com/Hopelezz/Card-Games/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

  


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Twitter: [@Icillz](https://twitter.com/Icillz)

GitHub: [@Hopelezz](https://github.com/Hopelezz)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>
  
  
  
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/Hopelezz/Card-Games
[forks-url]: https://github.com/Hopelezz/Card-Games/network/members
[stars-shield]: https://img.shields.io/github/stars/Hopelezz/Card-Games
[stars-url]: https://github.com/Hopelezz/Card-Games/stargazers
[issues-shield]: https://img.shields.io/github/issues/Hopelezz/Card-Games
[issues-url]: https://github.com/Hopelezz/Card-Games/issues
[license-shield]: https://img.shields.io/github/license/Hopelezz/Card-Games.svg?style=for-the-badge
[license-url]: https://github.com/Hopelezz/Card-Games/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mark-spratt/
[product-screenshot]: https://user-images.githubusercontent.com/72772558/167760329-90ad0328-8dcf-4100-aaea-c995bfcebdfd.png
