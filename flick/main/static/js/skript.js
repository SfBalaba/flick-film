const API_KEY = "bf5bc438-5a14-45ca-8ed2-36ec76cb66bf";

const API_VIDEO_UNOFFICIAL_KP = "https://kinopoiskapiunofficial.tech/api/v2.2/films/"
const API_URL_POPULAR =
  "https://kinopoiskapiunofficial.tech/api/v2.2/films/top?type=TOP_100_POPULAR_FILMS&page=1";
const API_URL_SEARCH =
  "https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword=";

const API_KEY_OMDB = '6e33deaa'
const API_URL_OMDB_SEARCH = 'http://www.omdbapi.com/?apikey=6e33dea&plot=full&t='
// tt3896198

getMovies(API_URL_POPULAR); 



async function getMovies(url) {
  const resp = await fetch(url, {
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": API_KEY,
    },
  });
  const respData = await resp.json();
  showMovies(respData);
  console.log(respData.films);
  console.log(respData.films[0])
}


getFacts("https://kinopoiskapiunofficial.tech/api/v2.2/films/435/facts");

async function getFacts(url) {
    const resp = await fetch(url, {
      headers: {
        "Content-Type": "application/json",
        "X-API-KEY": API_KEY,
      },
    });
    const respData = await resp.json();

    console.log(respData);
  }

async function getPreviewMovie(url) {

        const response = await fetch(url); // Generate the Response object
    if (response.ok) {
        const jsonValue = await response.json(); // Get JSON value from the response body
        return jsonValue;
    } else {
        return Promise.reject("*** PHP file not found");
    }

  }

function getClassByRate(vote) {
  if (vote >= 7) {
    return "green";
  } else if (vote > 5) {
    return "orange";
  } else {
    return "red";
  }
}


function showMovies(data) {
  const moviesEl = document.querySelector(".movies");

  // Очищаем предыдущие фильмы
  document.querySelector(".movies").innerHTML = "";

  data.films.forEach((movie) => {
    const movieEl = document.createElement("div");
    const PREW_MOVIE = API_URL_OMDB_SEARCH + movie.nameEn; //--

    movieEl.classList.add("movie");
    movieEl.innerHTML = `
    <a 
    class='movie-preview-link'
       href="bio/${movie.filmId}"
     target="_self"
     title="${movie.filmId}"
     >
    <div class="movie__cover-inner">
    <img
          src="${movie.posterUrlPreview}"
          class="movie__cover"
          alt="${getName(movie)}"
        />
      
        <div class="movie__cover--darkened"></div>
      </div>
     
      <div class="movie__info">
        <div class="movie__title">${getName(movie)}</div>
        <div class="movie__category">${movie.genres.map(
          (genre) => ` ${genre.genre}`
        )}</div>
        ${
          movie.rating &&
          `
        <div class="movie__average movie__average--${getClassByRate(
          movie.rating
        )}">${movie.rating}</div>
        `
        }
      </div>
      </a>
        `;
    moviesEl.appendChild(movieEl);
  });
}

const form = document.querySelector("form");
const search = document.querySelector(".header__search");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const apiSearchUrl = `${API_URL_SEARCH}${search.value}`;
  if (search.value) {
    getMovies(apiSearchUrl);

    search.value = "";
  }
});

const link_movie = document.querySelector("a");

function getVideo(id) {
    const url = API_VIDEO_UNOFFICIAL_KP + id + "/videos"
    getFacts(url);
    console.log(url);
}

function getName(movie) {
  if (typeof movie.nameRu === 'undefined') {
    return movie.nameEn
  } else return movie.nameRu
}


