
// const API_KEY = `PFVMN7W-69KMSHQ-NHXCYME-DWN0FDH`
// const API_KEY = `YJKWE1C-8WSMSY3-PB0XDGX-2JN8N8N`
// const API_KEY = "YJKWE1C-8WSMSY3-PB0XDGX-2JN8N8N"
const API_KEY = `61556GR-YSY47YS-JBK7JE0-M9FJ4EA`

function showMovies(data) {
  const moviesEl = document.querySelector(".movies");

  // Очищаем предыдущие фильмы
  document.querySelector(".movies").innerHTML = "";

  data.docs.forEach((movie) => {
    const movieEl = document.createElement("div");
    // const PREW_MOVIE = API_URL_OMDB_SEARCH + movie.nameEn; //--

    movieEl.classList.add("movie");
    movieEl.innerHTML = `
    <a 
    class='movie-preview-link'
       href="bio/${movie.id}"
     target="_self"
     title="${movie.id}"
     >
    <div class="movie__cover-inner">
    <img
          src="${movie.poster.previewUrl}"
          class="movie__cover"
          alt="${movie.name}"
        />
      
        <div class="movie__cover--darkened"></div>
      </div>
     
      <div class="movie__info">
        <div class="movie__title">${movie.name}</div>
        <div class="movie__category">${movie.genres.map(
          (genre) => ` ${genre.name}`
        )}</div>
        ${
          movie.rating &&
          `
        <div class="movie__average movie__average--grren"
        )}">${movie.rating.kp}</div>
        `
        }
      </div>
      </a>
        `;
    moviesEl.appendChild(movieEl);
  });
}
async function getMovies(url) {

  const resp = await fetch(url, {
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": API_KEY,
    },
  });
  const respData = await resp.json();
  alert(respData);
  showMovies(respData);
}



var button = document.getElementById("but");
var form = document.querySelector(".form-year");
button.addEventListener("click", function (evnt) {
      event.preventDefault();
      var url = `https://api.kinopoisk.dev/v1.3/movie?page=1&limit=10`

      var from = form.from;
      var to = form.to;
      var from_value = from.options[from.selectedIndex].text;
      var to_value = to.options[to.selectedIndex].text;
      url += `&year=${Math.min(parseInt(from_value), parseInt(to_value))}
      -${Math.max(parseInt(from_value), parseInt(to_value))}`;
      $.each($(".form-select-genre option:selected"), function(){
      url += `&genres.name=${$(this).val()}`
      });
      $.each($(".country option:selected"), function(){
      url += `&countries.name=${$(this).val()}`
      });
      alert(url);
      getMovies(url);
});

