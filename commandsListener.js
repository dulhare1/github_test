console.log("commandsListener.js running...");

chrome.commands.onCommand.addListener(function (command) {
	console.debug('command is : ' + command);

	// Develop use : reload extension.
	if (command == 'reload_extension') {
		chrome.runtime.reload();
	}
	//按下ctrl+shift+z觸發事件給content page
	if (command == 'trigger_page') {
		chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
			chrome.tabs.sendMessage(tabs[0].id, { greeting: "hello" }, function (response) {
				console.log(response.res); //(來自內容腳本的回覆)
			});
		});
	}
});
