const API_KEY = "bf5bc438-5a14-45ca-8ed2-36ec76cb66bf";

const API_VIDEO_UNOFFICIAL_KP = "https://kinopoiskapiunofficial.tech/api/v2.2/films/"
const API_URL_POPULAR =
  "https://kinopoiskapiunofficial.tech/api/v2.2/films/top?type=TOP_100_POPULAR_FILMS&page=1";


const movie_list = document.querySelector('.movies');



movieEl.innerHTML = `
    <a 
    class='movie-preview-link'
    onclick="getVideo(${movie.filmId})"
     target="_blank"
     title="${movie.filmId}"
     >
    <div class="movie__cover-inner">
    <img
          src="${movie.posterUrlPreview}"
          class="movie__cover"
          alt="${movie.nameRu}"
        />
      
        <div class="movie__cover--darkened"></div>
      </div>
     
      <div class="movie__info">
        <div class="movie__title">${movie.nameRu}</div>
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

    async function getMovies(url) {
        const resp = await fetch(url, {
            headers: {
            "Content-Type": "application/json",
            "X-API-KEY": API_KEY,
            },
        });
        const respData = await resp.json();
        showMovies(respData);
        console.log(respData);
        }
        