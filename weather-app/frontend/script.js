document
  .getElementById("weatherForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault(); // Evita o recarregamento da página
    const city = document.getElementById("cityInput").value;
    const resultDiv = document.getElementById("result");
    const errorDiv = document.getElementById("error");

    // Limpar mensagens anteriores
    resultDiv.classList.add("hidden");
    errorDiv.classList.add("hidden");

    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/weather?city=${encodeURIComponent(city)}`
      );
      if (!response.ok) {
        throw new Error("Não foi possível obter os dados.");
      }
      const data = await response.json();
      console.log(data);
      // Exibir os dados
      document.getElementById("cityName").textContent = data.city;
      document.getElementById("temperature").textContent = data.temperature;
      document.getElementById("description").textContent = data.description;
      document.getElementById("humidity").textContent = data.humidity;
      resultDiv.classList.remove("hidden");
    } catch (error) {
      errorDiv.textContent =
        "Erro ao obter os dados do clima. Verifique o nome da cidade.";
      errorDiv.classList.remove("hidden");
    }
  });
