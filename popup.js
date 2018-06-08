document.addEventListener('DOMContentLoaded', function (dcle) {
    var getin_date = document.getElementById('getin_date');
    var today = new Date();

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

    var person_id = document.getElementById('person_id');
    var saveButton = document.getElementById('saveBtn');

    saveButton.addEventListener('click', function (e) {
        chrome.storage.sync.set({ 'person_id': person_id.value }, function () {
            console.log('person id is ' + person_id.value);
        });
    });




    function paddingLeft(str, lenght) {
        if (str.length >= lenght)
            return str;
        else
            return paddingLeft("0" + str, lenght);
    }

});
