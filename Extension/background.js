chrome.contextMenus.create({
  id: "nudeDetection",
  title: "Detectar Nudez na Imagem",
  contexts: ["image"]
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId === "nudeDetection") {
    const imageUrl = info.srcUrl;

    try {
      const response = await fetch("http://localhost:5000/detect_nude", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: imageUrl })
      });

      const data = await response.json();
      const message = data.error ? "Erro ao processar a imagem." :
                        (data.detections.some(d => d.improper) ? "Nudez detectada!" : "Nenhuma nudez detectada.");

      // Use `scripting.executeScript` to show an alert in the tab
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: (msg) => alert(msg),
        args: [message]
      });
    } catch (error) {
      console.error("Erro:", error);
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: (msg) => alert(msg),
        args: ["Falha ao conectar com o servidor de detecção."]
      });
    }
  }
});
