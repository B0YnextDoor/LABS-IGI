const itemsPerPage = 3;
const titleInput = document.getElementById("search");
const url = new URL("books/", window.location.origin);

let totalPages = 0;
let currentPage = 0;

function initAnimation() {
  const cards = document.querySelectorAll(".card-wrapper");
  cards.forEach((card_w) => {
    const card = card_w.querySelector(".book_card");
    card_w.addEventListener("mousemove", (event) => {
      const [x, y] = [event.offsetX, event.offsetY];
      const rect = card_w.getBoundingClientRect();
      const [width, height] = [rect.width, rect.height];
      const middleX = width / 2;
      const middleY = height / 2;
      const offsetX = ((x - middleX) / middleX) * 25;
      const offsetY = ((y - middleY) / middleY) * 25;
      const offX = 50 + ((x - middleX) / middleX) * 25;
      const offY = 50 - ((y - middleY) / middleY) * 20;
      card.style.setProperty("--rotateX", 1 * offsetX + "deg");
      card.style.setProperty("--rotateY", -1 * offsetY + "deg");
      card.style.setProperty("--posx", offX + "%");
      card.style.setProperty("--posy", offY + "%");
    });
    card_w.addEventListener("mouseleave", (eve) => {
      card.style.animation = "reset-card 1s ease";
      card.addEventListener(
        "animationend",
        (e) => {
          card.style.animation = "unset";
          card.style.setProperty("--rotateX", "0deg");
          card.style.setProperty("--rotateY", "0deg");
          card.style.setProperty("--posx", "50%");
          card.style.setProperty("--posy", "50%");
        },
        {
          once: true,
        }
      );
    });
  });
}

function createElement(name, className, id) {
  const el = document.createElement(name);
  el.innerHTML = "";
  if (className) el.classList.add(className);
  if (id) el.id = id;
  return el;
}

function createBookCard(book) {
  const cardWrapper = createElement("article", "card-wrapper");
  const bookCard = createElement("article", "book_card");
  const hasAmount = book.amount > 0;
  bookCard.innerHTML = `
  <a href="${book.get_absolute_url}" id="link">${book.title}</a>
  <p>Author: ${book.author_surname} ${book.author_name}</p>
  <p>Genre: ${book.genre}</p>
  <p class="${hasAmount ? "" : "col-blue"}">${
    hasAmount ? `Amount of books: ${book.amount}` : "Out of stock!"
  }</p>
  <span>Price: ${book.price} BYN</span>`;
  cardWrapper.appendChild(bookCard);
  return cardWrapper;
}

function createCatalog(books) {
  const booksGrid = document.getElementById("book-grid");
  booksGrid.innerHTML = "";
  books.forEach((book) => {
    booksGrid.appendChild(createBookCard(book));
  });
}

function createPagination(count) {
  const pagination = document.getElementById("pagination");
  if (count < 3) pagination.style.marginTop = "186px";
  else pagination.style.marginTop = "20px";
  pagination.innerHTML = "";
  const prevBtn = createElement("button", undefined, "prev");
  prevBtn.addEventListener("click", () => prevPage());
  prevBtn.innerHTML = "&laquo";
  pagination.appendChild(prevBtn);
  for (let i = 0; i < totalPages; i++) {
    const btn = createElement("button");
    if (i == currentPage) btn.classList.add("active");
    btn.addEventListener("click", () => goToPage(i));
    btn.textContent = `${i + 1}`;
    pagination.appendChild(btn);
  }
  const nextBtn = createElement("button", undefined, "next");
  nextBtn.addEventListener("click", () => nextPage());
  nextBtn.innerHTML = "&raquo";
  pagination.appendChild(nextBtn);
}

function displayPage(books) {
  const message = document.getElementById("empty-catalog");
  const bookList = document.getElementById("book-list");
  const hasBooks = books && books.length > 0;
  message.style.display = hasBooks ? "none" : "block";
  bookList.style.display = hasBooks ? "grid" : "none";
  if (hasBooks) {
    createCatalog(books);
    createPagination(books.length);
    updateButtons();
    initAnimation();
  }
}

function updateButtons() {
  document.getElementById("prev").disabled = currentPage === 0;
  document.getElementById("next").disabled = currentPage === totalPages - 1;
}

function fetchBooks(url) {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      totalPages = Math.ceil(data["total"] / itemsPerPage);
      displayPage(data["books"]);
    })
    .catch((error) => console.error("Error fetching books:", error));
}

function getBooksByPage() {
  url.searchParams.delete("page");
  url.searchParams.append("page", `${currentPage}`);
  fetchBooks(url);
}

function prevPage() {
  if (currentPage > 0) {
    currentPage--;
    getBooksByPage();
  }
}

function nextPage() {
  if (currentPage == totalPages) return;
  currentPage++;
  getBooksByPage();
}

function goToPage(index) {
  currentPage = index;
  getBooksByPage();
}

function searchBooks() {
  url.search = "";
  currentPage = 0;
  url.searchParams.append("search", `${titleInput.value}`);
  fetchBooks(url);
}

function sortBooks(type) {
  url.search = "";
  currentPage = 0;
  url.searchParams.append("sort", `${type}`);
  fetchBooks(url);
}

document.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("price")
    .addEventListener("click", () => sortBooks("price"));
  document
    .getElementById("amount")
    .addEventListener("click", () => sortBooks("amount"));
  getBooksByPage();
});
