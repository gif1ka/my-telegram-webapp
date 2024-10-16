bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    const url = "https://gif1ka.github.io/my-telegram-webapp/";  // Ваш GitHub Pages URL
  
    bot.sendMessage(chatId, "Запустите Web App:", {
      reply_markup: {
        inline_keyboard: [
          [{ text: "Открыть приложение", web_app: { url: url } }]
        ]
      }
    });
  });
  