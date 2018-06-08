
//接受快捷鍵觸發事件
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    // console.log(message); //取得message {greeting: "hello"}
    // console.log(sender); // {id: "hojcoebfmdnijbojfkjpmhcdmoejgakn"}
    sendResponse({ res: "來自內容腳本的回覆" });


    //取得popup html儲存的訊息
    chrome.storage.sync.get('trainId', function (data) {
        console.log('popup html儲存的trainId----->' + data.trainId);
        //changeColor.setAttribute('value', data.color);
        addInput(data);
    });
});

var addInput = function(data){
    console.log('addInput function內:');
    console.log(data);
    var searchInput = document.getElementById('lst-ib');
    searchInput.value = data.trainId;
    var searchButton = document.getElementById('mKlEF');
    searchButton.click();
}


