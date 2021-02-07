<!-- ABOUT THE PROJECT -->
## About The Project

There are many great YouTube Video Downloaders available online. However, every downloader (atleast the ones I could find) when video is downloaded above 720p gives video without
any audio.
This is because of something called streaming technique. YouTube basically divides it's videos in two types of streams.
* Progressive
* DASH (also referred to as “adaptive”)

The later one is the challange, as the audio is seperated from the video in this one.

This projects checks whether the video is DASH or not. If not then user can download the video right away. On the other hand if the video is DASH then it will download the video
and audio seperately, merge them together and send you the link to the final file to your e-mail id.


### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Pytube](https://python-pytube.readthedocs.io/en/latest)
* [MoviePy](https://zulko.github.io/moviepy/)
* [Bootstrap](https://getbootstrap.com/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Python](https://www.python.org/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/sourcenaman/YouTube_Downloader.git
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Run Server
   ```sh
   python manage.py runserver
   ```



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/sourcenaman/YouTube_Downloader/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact

Naman Vashishth - namanvashishth12@gmail.com

Project Link: [https://github.com/sourcenaman/YouTube_Downloader](https://github.com/sourcenaman/YouTube_Downloader)
