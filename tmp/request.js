/**
 * Created by xvhuanlin on 16/10/5.
 */
/*
function _post(URL, json, _success, _error, targetURL) {

    $.ajax({
        async:false,
        contentType: "application/json; charset=utf-8",
        type: "POST",
        url: URL,
        data: JSON.stringify(json),
        dataType : "json",
        error: function(data) {
            _error(data);
        },
        success: function(data) {
            _success(data, targetURL);
        }
    });

}
*/
function _login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "") {
        alert("用户名不能为空");
        return false;
    }
    if (password == "") {
        alert("密码不能为空");
        return false;
    }
    var json = {
        username : username,
        password : password
    };
    var obj=_post("http://121.201.68.42:8000/user/login/",json);
	alert(obj.msg);
    return false;
}
function _register() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "") {
        alert("用户名不能为空");
        return false;
    }
    if (password == "") {
        alert("密码不能为空");
        return false;
    }
    var json = {
        username : username,
        password : password
    };
    var obj=_post("http://121.201.68.42:8000/user/register/",json);
	alert(obj.msg);
    return false;
}
/*
function _get(URL, json) {
	var obj=[];
    $.ajax({
        async:false,
        contentType: "application/json; charset=utf-8",
        type: "GET",
        url: URL,
        data:JSON.stringify(json),
		error: function(data) {
            obj=JSON.parse(data);
			return obj;
        },
        success: function(data) {
            obj=JSON.parse(data);
			return obj;
        },
        dataType : "JSONP"
    });
	return obj;
	
}
*/
function _post(URL, json) {
	var obj=[];
    $.ajax({
        async:false,
        contentType: "application/json; charset=utf-8",
        type: "POST",
        url: URL,
        data:JSON.stringify(json),
		error: function(data) {
            alert("Server error");
			return [];
        },
        success: function(data) {
            obj=JSON.parse(data);
			return obj;
        },
        dataType : "JSONP"
    });
	return obj;
}