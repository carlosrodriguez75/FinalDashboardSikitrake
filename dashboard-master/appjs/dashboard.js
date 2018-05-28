/**
 * Created by manuel on 5/8/18.
 */

// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages': ['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

//MESSAGES BY DATE
function reformatData(jsonData){
    var temp= jsonData.Messages;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        console.log(row.count);
        console.log(row.mdate);
        dataElement.push(row.mdate);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}


//MESSAGES BY DATE
function drawChart() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/SikitrakeChat/Messages/countbymessagesperday",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'mdate');
    data.addColumn('number', 'Messages');
    data.addRows(reformatData(JSON.parse(jsonData)));

    var options = {
        title: 'Messages By Day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Messages',
            minValue: 0
        },
        vAxis: {
            title: 'Date'
        }
    };



    var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
    chart.draw(data, options);


}



google.charts.setOnLoadCallback(drawChartLikes);

//LIKES PER DATE
function reformatDataLikes(jsonData){
    var temp= jsonData.LikesPerDay;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        console.log(row.count);
        console.log(row.mdate);
        dataElement.push(row.mdate);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}


//LIKES PER DATE
function drawChartLikes() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/SikitrakeChat/Messages/countlikesperday",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'mdate');
    data.addColumn('number', 'Likes');
    data.addRows(reformatDataLikes(JSON.parse(jsonData)));

    var options = {
        title: 'Likes By Day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Likes',
            minValue: 0
        },
        vAxis: {
            title: 'Date'
        }
    };



    var chart = new google.visualization.BarChart(document.getElementById('chart_div2'));
    chart.draw(data, options);


}



google.charts.setOnLoadCallback(drawChartDisLikes);

//DISLIKES PER DATE
function reformatDataDisLikes(jsonData){
    var temp= jsonData.DisLikesPerDay;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        console.log(row.count);
        console.log(row.mdate);
        dataElement.push(row.mdate);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}


//DISLIKES PER DATE
function drawChartDisLikes() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/SikitrakeChat/Messages/countdislikesperday",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'mdate');
    data.addColumn('number', 'Dislikes');
    data.addRows(reformatDataDisLikes(JSON.parse(jsonData)));

    var options = {
        title: 'Dislikes By Day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Disikes',
            minValue: 0
        },
        vAxis: {
            title: 'Date'
        }
    };



    var chart = new google.visualization.BarChart(document.getElementById('chart_div3'));
    chart.draw(data, options);


}


google.charts.setOnLoadCallback(drawChartReplies);

//REPLIES PER DATE
function reformatDataReplies(jsonData){
    var temp= jsonData.RepliesPerDay;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        console.log(row.count);
        console.log(row.mdate);
        dataElement.push(row.mdate);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}


//REPLIES PER DATE
function drawChartReplies() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/SikitrakeChat/Messages/countrepliesperday",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'mdate');
    data.addColumn('number', 'Replies');
    data.addRows(reformatDataReplies(JSON.parse(jsonData)));

    var options = {
        title: 'Replies By Day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Replies',
            minValue: 0
        },
        vAxis: {
            title: 'Date'
        }
    };



    var chart = new google.visualization.BarChart(document.getElementById('chart_div4'));
    chart.draw(data, options);


}


google.charts.setOnLoadCallback(drawChartUsers);

//USER POSTING MSG OR REPLIES  PER DAY
function reformatDataUsers(jsonData){
    var temp= jsonData.UserPost;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        console.log(row.count);
        console.log(row.mdate);
        console.log(row.uid);
        dataElement.push(row.mdate + ' - ' + row.uid);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}



//USER POSTING MSG OR REPLIES  PER DAY
function drawChartUsers() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/SikitrakeChat/Messages/countuserpostperday",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'mdate');
    data.addColumn('number', 'Msg and Replies');
    data.addRows(reformatDataUsers(JSON.parse(jsonData)));

    var options = {
        title: 'Msg and Replies By Day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total User Msg and Replies',
            minValue: 0
        },
        vAxis: {
            title: 'Date'
        }
    };



    var chart = new google.visualization.BarChart(document.getElementById('chart_div5'));
    chart.draw(data, options);


}



google.charts.setOnLoadCallback(drawChartHashtags);

//USER POSTING MSG OR REPLIES  PER DAY
function reformatDataHashtags(jsonData){
    var temp= jsonData.HashtagPosts;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        console.log(row.count);
        console.log(row.mdate);
        dataElement.push(row.mdate);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}


//USER POSTING MSG OR REPLIES  PER DAY
function drawChartHashtags() {
    var jsonData = $.ajax({
        url: "http://localhost:5000/SikitrakeChat/Messages/counthashtagsperday",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'mdate');
    data.addColumn('number', 'Msg and Replies');
    data.addRows(reformatDataHashtags(JSON.parse(jsonData)));

    var options = {
        title: 'Hashtags By Day',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Hashtags',
            minValue: 0
        },
        vAxis: {
            title: 'Date'
        }
    };



    var chart = new google.visualization.BarChart(document.getElementById('chart_div6'));
    chart.draw(data, options);


}



















