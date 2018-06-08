document.addEventListener('DOMContentLoaded', function (dcle) {

    var person_id = document.getElementById('person_id');
    var getin_date = document.getElementById('getin_date');
    var from_station = document.getElementById('from_station');
    var to_station = document.getElementById('to_station');
    var train_no = document.getElementById('train_no');
    var order_qty_str = document.getElementById('order_qty_str');

    var today = new Date();
    //產生日期選單
    for (var i = 0; i < 17; i++) {
        let formatDay = today.getFullYear() + "/" + paddingLeft((today.getMonth() + 1).toString(), 2) + "/" + paddingLeft(today.getDate().toString(), 2);
        let date_value = formatDay + '-' + paddingLeft(i.toString(), 2);
        let theOption = document.createElement("OPTION");
        theOption.setAttribute("value", date_value);
        let text = document.createTextNode(formatDay);
        theOption.appendChild(text);
        getin_date.appendChild(theOption);

        today.setDate(today.getDate() + 1);
    }

    //放入儲存值
    chrome.storage.sync.get(['person_id', 'getin_date', 'from_station', 'to_station', 'train_no', 'order_qty_str',], function (data) {
        if (data) {
            console.log('有東西!');
            person_id.value = data.person_id;
            getin_date.value = data.getin_date;
            from_station.value = data.from_station;
            to_station.value = data.to_station;
            train_no.value = data.train_no;
            order_qty_str.value = data.order_qty_str;
        } else {
            console.log('空的!');
        }
    });

    var saveButton = document.getElementById('saveBtn');

    saveButton.addEventListener('click', function () {
        chrome.storage.sync.set({
            'person_id': person_id.value,
            'getin_date': getin_date.value,
            'from_station': from_station.value,
            'to_station': to_station.value,
            'train_no': train_no.value,
            'order_qty_str': order_qty_str.value
        }, function () {
            console.log('person id is ' + person_id.value);
            var feedbackTag = document.createElement('span');
            feedbackTag.style.color = '#ff0000';
            feedbackTag.innerHTML = '儲存成功!';
            var btnDiv = document.getElementById('btnDiv');
            btnDiv.appendChild(feedbackTag);
        });
    });


    /**
     * 左側補0
     * @param {*} str 
     * @param {*} lenght 
     */
    function paddingLeft(str, lenght) {
        if (str.length >= lenght)
            return str;
        else
            return paddingLeft("0" + str, lenght);
    }

});
