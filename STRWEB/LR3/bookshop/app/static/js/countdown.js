const countdownDuration = 60 * 60;

function updateCountdown(endTime) {
  const now = Math.floor(Date.now() / 1000);
  const timeLeft = Math.max(0, endTime - now);

  if (timeLeft > 0) {
    const hours = Math.floor(timeLeft / 3600);
    const minutes = Math.floor((timeLeft % 3600) / 60);
    const seconds = timeLeft % 60;

    document.getElementById("countdown").textContent = `${hours
      .toString()
      .padStart(2, "0")}:${minutes.toString().padStart(2, "0")}:${seconds
      .toString()
      .padStart(2, "0")}`;

    setTimeout(() => updateCountdown(endTime), 1000);
  } else {
    document.getElementById("countdown").textContent = "Timer expired!";
    localStorage.removeItem("countdownEndTime");
  }
}

document.addEventListener("DOMContentLoaded", async () => {
  try {
    // Проверяем, есть ли сохраненное время окончания в localStorage
    let endTime = localStorage.getItem("countdownEndTime");

    if (!endTime) {
      // Вычисляем время окончания и сохраняем его
      const now = Math.floor(Date.now() / 1000);
      endTime = now + countdownDuration;
      localStorage.setItem("countdownEndTime", endTime.toString());
    } else {
      endTime = parseInt(endTime);
    }

    updateCountdown(endTime);
  } catch (error) {
    console.error("Error:", error);
  }
});
