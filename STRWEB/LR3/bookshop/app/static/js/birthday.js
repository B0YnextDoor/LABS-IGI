const daysOfWeek = [
  "воскресенье",
  "понедельник",
  "вторник",
  "среда",
  "четверг",
  "пятница",
  "суббота",
];

document.getElementById("form-Up").addEventListener("submit", function (event) {
  // Получаем значение даты рождения из поля ввода
  const birthdateInput = document.getElementById("id_confirmation").value;
  if (!birthdateInput) {
    alert("Пожалуйста, введите дату рождения.");
    event.preventDefault();
    return;
  }

  // Конвертируем строку даты в объект Date
  const birthdate = new Date(birthdateInput);
  const today = new Date();

  // Рассчитываем возраст
  let age = today.getFullYear() - birthdate.getFullYear();
  const monthDiff = today.getMonth() - birthdate.getMonth();

  // Уточняем возраст, если текущий месяц и день меньше, чем месяц и день рождения
  if (
    monthDiff < 0 ||
    (monthDiff === 0 && today.getDate() < birthdate.getDate())
  ) {
    age--;
  }

  // Определяем день недели
  const birthDayOfWeek = daysOfWeek[birthdate.getDay()];

  if (age < 18) {
    alert(
      "Вы несовершеннолетний. Необходимо разрешение родителей на использование сайта."
    );
    event.preventDefault();
  } else {
    alert(`Возраст: ${age} лет. Вы родились в ${birthDayOfWeek}.`);
  }
});
