const fulImgBox = document.getElementById("zoomImgBox");
const fulImg = document.getElementById("zoomImg");
const thumbnails = document.querySelectorAll(".img-photo");




fulImgBox.addEventListener('click', () => {
    fulImgBox.style.display = "none";
})

for (let thumbnail of thumbnails) {
    thumbnail.addEventListener("click", () => {
      fulImgBox.style.display = "flex";
      fulImg.setAttribute("src", thumbnail.getAttribute("src"));
    });
  }

