const itemsPerPage = 3;
const url = new URL("contacts/", window.location.origin);
const filterInput = document.getElementById("search");
const preloader = document.getElementById("preloader");
const contactSection = document.getElementById("contacts-section");
const props = ["name", "email", "globalLocationNumber", "image", "jobTitle"];
const tags = ["h3", "h3", "h3", "img", "pre"];
const inputs = ["name", "email", "phone", "image", "cv", "description"];
let totalPages = 0;
let currentPage = 0;
let bonusList = [];

function createElement(name, className, id, type, value) {
  const el = document.createElement(name);
  el.innerHTML = "";
  if (className) className.forEach((val) => el.classList.add(val));
  if (id) el.id = id;
  if (type) el.type = type;
  if (value) el.value = value;
  return el;
}

function createPagination() {
  const pagination = document.getElementById("pagination");
  pagination.style.marginTop = "20px";
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

function createCell(info, type, idx, tag, itemprop) {
  const data = createElement("td", [`${type}_data_${idx}`]);
  const innerTag = createElement(tag);
  innerTag.itemprop = itemprop;
  if (tag === "img") {
    innerTag.src = info;
    innerTag.width = 150;
    innerTag.height = 150;
    innerTag.alt = "";
  } else innerTag.textContent = info;
  data.appendChild(innerTag);
  return data;
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function updateInfo(form) {
  fetch(url, {
    method: "POST",
    body: form,
    credentials: "same-origin",
  });
}

function handleCheck(checkbox) {
  if (checkbox.checked) bonusList.push(checkbox.value);
  else bonusList = bonusList.filter((val) => val != checkbox.value);
}

function createRow(data, idx, role) {
  const row = createElement("tr");
  let cell = createElement("td", [`choose_data_${idx}`]);
  const checkBox = createElement(
    "input",
    ["bonus-check"],
    undefined,
    "checkbox",
    `${data.id}`
  );
  checkBox.addEventListener("change", (e) => handleCheck(e.target));
  if (bonusList.includes(String(data.id))) checkBox.checked = true;
  else checkBox.checked = false;
  cell.appendChild(checkBox);
  row.appendChild(cell);
  const keys = Object.keys(data).slice(1);
  for (let i = 0; i < 5; i++) {
    const key = keys[i];
    row.appendChild(createCell(data[key], key, idx, tags[i], props[i]));
  }
  if (role === "adm") {
    form = createElement("form");
    form.method = "POST";
    const csrfInput = createElement(
      "input",
      undefined,
      undefined,
      "hidden",
      getCookie("csrftoken")
    );
    csrfInput.name = "csrfmiddlewaretoken";
    form.appendChild(csrfInput);
    updBtn = createElement(
      "button",
      ["btn", "btn-admin"],
      undefined,
      "submit",
      `upd_${data.id}`
    );
    updBtn.name = "action";
    updBtn.textContent = "update";
    form.addEventListener("sumbit", (e) => {
      e.preventDefault();
      updateInfo(new FormData(e.target));
    });
    form.appendChild(updBtn);
    cell = createElement("td", [`update_data_${idx}`]);
    cell.appendChild(form);
    row.appendChild(cell);
  }
  return row;
}

function rowClick(e) {
  const row = String(e.target.classList.value).split("_");
  if (!row.includes("data")) return;
  const rowData = document
    .getElementById("info-cont")
    .getElementsByTagName("tr")
    .item(row[2])
    .getElementsByTagName("td");
  document.getElementById("row-info-cont").style.display = "block";
  const footer = document.getElementById("row-info");
  footer.innerHTML = "";
  for (let i = 0; i < 5; i++) {
    const innerDiv = createElement("div");
    innerDiv.innerHTML = rowData.item(i + 1).innerHTML;
    footer.appendChild(innerDiv);
  }
}

function generateText(emp) {
  const reasons = [
    "outstanding performance",
    "successful completion of a crucial project",
    "innovative ideas and their implementation",
    "excellent fulfillment of job responsibilities",
    "significant contribution to the company's growth",
  ];
  const randomReason = reasons[Math.floor(Math.random() * reasons.length)];
  return `Based on the CEO's order dated ${new Date().toLocaleDateString(
    "en-US"
  )}, 
for ${randomReason}, ${emp["name"]} (${emp["post"]}), 
is to be awarded a bonus of 50% of their base salary.
Reason: recommendation from the immediate supervisor.\n\n`;
}

function displayBonusText(dataList) {
  document.getElementById("bonus-cont").style.display = "block";
  let text = "";
  dataList.forEach((val, idx) => {
    text += `${idx + 1}. ` + generateText(val);
  });
  document.getElementById("bonus-info").textContent = text;
}

function bonusEmployees() {
  if (bonusList.length == 0) return;
  const preloader = document.getElementById("preloader-bonus");
  const btn = document.getElementById("bonus-emp");
  preloader.style.display = "block";
  btn.style.display = "none";
  url.search = "";
  url.searchParams.append("ids", bonusList.toString());
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      displayBonusText(data["data"]);
    })
    .catch((error) => console.log("Error", error));

  bonusList = [];
  document
    .querySelectorAll('input[type="checkbox"].bonus-check')
    .forEach((box) => (box.checked = false));
  setTimeout(() => {
    preloader.style.display = "none";
    btn.style.display = "block";
  }, 300);
}

function fillTable(contacts, role) {
  const body = document.getElementById("info-cont");
  body.innerHTML = "";
  contacts.forEach((emp, idx) => {
    const row = createRow(emp, idx, role);
    row.addEventListener("click", (e) => rowClick(e));
    body.appendChild(row);
  });
}

function displayPage(contacts, role) {
  const message = document.getElementById("no-msg");
  const hasData = contacts && contacts.length > 0;
  message.style.display = hasData ? "none" : "block";
  if (hasData) {
    fillTable(contacts, role);
    createPagination();
    updateButtons();
  }
  contactSection.style.display = hasData ? "block" : "none";
}

function fetchData(url) {
  preloader.style.display = "block";
  contactSection.style.display = "none";
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      totalPages = Math.ceil(data["total"] / itemsPerPage);
      setTimeout(() => {
        preloader.style.display = "none";
        displayPage(data["contacts"], data["role"]);
      }, 500);
    })
    .catch((error) => console.error("Error fetching contacts:", error));
}

function updateButtons() {
  document.getElementById("prev").disabled = currentPage === 0;
  document.getElementById("next").disabled = currentPage === totalPages - 1;
}

function getContactsByPage() {
  url.searchParams.delete("page");
  url.searchParams.append("page", `${currentPage}`);
  fetchData(url);
}

function sortContacts(e) {
  if (String(e.target.classList.value).includes("sort-dir")) return;
  const col = String(e.target.value);
  const prev = url.searchParams.get("sort");
  let dir;
  let arrow;
  if (prev) {
    dir = prev[0] === "-";
    arrow = document
      .getElementsByClassName(`sort-dir ${dir ? prev.substring(1) : prev}`)
      .item(0);
    if (arrow) {
      arrow.style.transform = `rotateX(${dir ? "0" : "0.5turn"})`;
      arrow.style.display = "none";
    }
  } else
    document.getElementsByClassName(`sort-dir name`).item(0).style.display =
      "none";
  url.searchParams.delete("sort");
  dir = col[0] === "-";
  e.target.value = dir ? col.substring(1) : "-" + col;
  arrow = document
    .getElementsByClassName(`sort-dir ${dir ? col.substring(1) : col}`)
    .item(0);
  arrow.style.transform = `rotateX(${dir ? "0" : "0.5turn"})`;
  arrow.style.display = "inline";
  url.searchParams.append("sort", e.target.value);
  fetchData(url);
}

function filterContacts() {
  currentPage = 0;
  url.searchParams.delete("page");
  url.searchParams.append("page", `${currentPage}`);
  url.searchParams.delete("filter");
  url.searchParams.append("filter", `${filterInput.value}`);
  filterInput.value = "";
  fetchData(url);
}

function prevPage() {
  if (currentPage > 0) {
    currentPage--;
    getContactsByPage();
  }
}

function nextPage() {
  if (currentPage == totalPages) return;
  currentPage++;
  getContactsByPage();
}

function goToPage(index) {
  currentPage = index;
  getContactsByPage();
}

function validateURL(url) {
  const urlPattern = /^https?:\/\/\S+\.(?:php|html)$/;
  return urlPattern.test(url);
}

function validatePhone(phone) {
  const phonePattern =
    /^(?:\+375|8)(?:\s*\(?0?(?:25|29|33|44)\)?)(?:\s*|-?)\d{3}(?:\s*|-?)\d{2}(?:\s*|-?)\d{2}$/;
  return phonePattern.test(phone);
}

function validateEmail(email) {
  const emailPattern = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  return emailPattern.test(email);
}

function closeForm() {
  document.getElementById("add-emp-btn").style.display = "block";
  document.getElementById("filename").textContent = "Choose file";
  const form = document.getElementById("add-emp-form");
  form.reset();
  form.style.display = "none";
  document.getElementById("table-actions").style.justifyContent = "";
}

function addEmployee() {
  document.getElementById("add-emp-form").style.display = "flex";
  document.getElementById("add-emp-btn").style.display = "none";
  document.getElementById("table-actions").style.justifyContent = "end";
}

function getInput(name) {
  return [
    document.getElementById(name),
    document.getElementById(`${name}-error`),
  ];
}

function getReqiredMessage(name) {
  return `⚠ ${name.charAt(0).toUpperCase() + name.substring(1)} is required!`;
}

function getPatternMessage(name) {
  return `⚠ Wrong ${name} pattern!`;
}

function displayError(errorCont, inputField, msg) {
  if (msg) {
    errorCont.style.display = "block";
    errorCont.textContent = msg;
    inputField.setAttribute("aria-invalid", true);
    return true;
  }
  errorCont.style.display = "none";
  inputField.removeAttribute("aria-invalid");
  return false;
}

function checkRequired(name) {
  const [inputField, errorCont] = getInput(name);
  return displayError(
    errorCont,
    inputField,
    !inputField.value || (name == "image" && !inputField.files[0])
      ? getReqiredMessage(name)
      : undefined
  );
}

function checkPattern(name, validator) {
  const [inputField, errorCont] = getInput(name);
  const patternValidation = validator(inputField.value);
  return displayError(
    errorCont,
    inputField,
    !patternValidation ? getPatternMessage(name) : undefined
  );
}

function checkInput(name, validator) {
  const requiredValidation = checkRequired(name);
  if (requiredValidation) return;
  return checkPattern(name, validator);
}

function checkForm() {
  const submitBtn = document.getElementById("submit-form-btn");
  let isValid = true;
  checkRequired("name");
  checkInput("email", validateEmail);
  checkInput("phone", validatePhone);
  checkRequired("image");
  checkInput("cv", validateURL);
  checkRequired("description");
  for (let i = 0; i < inputs.length; ++i) {
    if (document.getElementById(inputs[i]).getAttribute("aria-invalid")) {
      isValid = false;
      break;
    }
  }
  submitBtn.disabled = !isValid;
}

async function submitForm(form) {
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  const result = await fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrfToken,
    },
    body: form,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data["error"]) return false;
      totalPages = Math.ceil(data["total"] / itemsPerPage);
      displayPage(data["contacts"], data["role"]);
      return true;
    })
    .catch((error) => {
      console.error("Error:", error);
      return false;
    });
  return result;
}

document.addEventListener("DOMContentLoaded", () => {
  ["name", "email", "phone", "descr"].forEach((col) => {
    document
      .getElementById(`sort-${col}`)
      .addEventListener("click", (e) => sortContacts(e));
  });
  document.getElementsByClassName(`sort-dir name`).item(0).style.display =
    "inline";
  const form = document.getElementById("add-emp-form");
  if (form) {
    document.getElementById("image").addEventListener("change", (e) => {
      document.getElementById("filename").textContent = e.target.files[0].name;
    });
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const res = await submitForm(new FormData(e.target));
      const formError = document.getElementById("add-emp-form-error");
      if (res) {
        formError.style.display = "none";
        closeForm();
      } else {
        formError.style.display = "block";
        formError.textContent = "Creating employee error!";
      }
    });
  }
  getContactsByPage();
});
