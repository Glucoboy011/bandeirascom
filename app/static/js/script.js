let slideIndex = 1;

document.addEventListener("DOMContentLoaded", function() {
  console.log("DOM carregado!");
  showSlides(slideIndex);
});

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");

  // Verifica se existem slides
  if (slides.length === 0) {
    console.error("Nenhum slide encontrado com a classe 'mySlides'.");
    return;
  }

  // Ajusta slideIndex ao intervalo válido
  if (n > slides.length) { slideIndex = 1; }
  if (n < 1) { slideIndex = slides.length; }

  // Oculta todos os slides
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  // Remove a classe "active" de todos os pontos
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  // Exibe o slide atual e destaca o ponto correspondente
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}
