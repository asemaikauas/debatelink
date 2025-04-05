document.addEventListener("DOMContentLoaded", function () {
  const texts = document.querySelectorAll(".fade-text");
  if (texts.length > 0) {
    let index = 0;
    setInterval(() => {
      texts.forEach((text) => text.classList.remove("active"));
      texts[index].classList.add("active");
      index = (index + 1) % texts.length;
    }, 1500);
  }

  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    link.addEventListener('mouseenter', () => {
      const tab = new bootstrap.Tab(link);
      tab.show();
    });
  });

  const telegramBtn = document.getElementById('telegramBtn');
  if (telegramBtn) {
    telegramBtn.addEventListener('click', function () {
      window.open('https://t.me/debatelinkbot', '_blank');
    });
  }

  const form = document.getElementById("interestForm");
  const successMessage = document.getElementById("successMessage");

  if (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();
      const formData = new FormData(this);

      const response = await fetch("/submit", {
        method: "POST",
        body: formData
      });

      if (response.ok) {
        successMessage.style.display = "block";
        this.reset();
      }
    });
  }

});



