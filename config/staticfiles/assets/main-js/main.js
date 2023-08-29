// ! Filter
const filterSection = document.querySelectorAll(".filter-section");
const filterBtn = document.querySelectorAll(".filter");

function clickedBtn() {
  filterSection.forEach((x) => x.classList.toggle("active"));
}

filterBtn.forEach(
  (x) =>
    (x.onclick = () => {
      clickedBtn();
    })
);

const hb = document.querySelectorAll(".mb-second");
const gh = document.querySelectorAll(".nav-pills");
const we = document.querySelectorAll(".nav-item");

function df() {
  gh.forEach((x) => x.classList.toggle("active"));
}

hb.forEach(
  (x) =>
    (x.onclick = () => {
      df();
    })
);

we.forEach(
  (x) =>
    (x.onclick = () => {
      df();
    })
);
