function Pack (name, questions, paisons) {
	this.name = name;
	this.questions = questions;
	this.paisons = paisons;
	this.add_question = function (question) {
	    this.questions.push(question);
	}
}

function TestQuestion (question, answers){
	this.question = question;
	this.answers = JSON.parse(answers);
}


function set_nth_question(pack, n){
	if (n >= pack.questions.length || n < 0) {
		return false;
	}
	document.getElementById('question').innerHTML = pack.questions[n].question;
	var html_code = `<p>Питання ${n+1}/${pack.questions.length}<\p><br>`;
	var answers = pack.questions[n].answers;
	for (i in answers){
		html_code += `<p><input type="radio" class='radio' name="answers">${answers[i]}</p>`;
	}
	var form = document.getElementById('answer_form');
	form.innerHTML = "";
	form.insertAdjacentHTML('afterbegin', html_code);
	if (n == pack.questions.length - 1){
	    document.getElementById('NextButton').innerHTML = "Закінчити";
	} else {
	    document.getElementById('NextButton').innerHTML = "Наступна";
	}

	if (user_answers.length != n && user_answers[n] != -1){
	    document.getElementsByName("answers")[user_answers[n]].checked = true;
	    console.log('bob');
	}
	console.log(user_answers)
	return true
}


function print_result(result_array){

	var test_passed = true;
	var res = false;
	if (result_array.indexOf(false) != -1){
	    test_passed = false;
	}
	var html_code = ""
	if (test_passed){
		html_code += "<h1 class='result'>Test passed! ヽ(・∀・)ﾉ</h1><h2 class='result1'>Congratulations!</h2>"
	} else {
		html_code += "<h2 class='result'>Test Failed ¯\\_(ツ)_/¯</h2>"
	}
	html_code += "<ol id='result_list'>";
	for (i = 0; i < result_array.length; i ++){
		html_code += `<li>${result_array[i]}</li>`;
	}
	html_code += "</ol>"
	html_code += "<div class = 'center'><button id='PassTest_button' onclick='toPage(\"" + url_to_my_cab + "\", \"_self\")'>До Мого Кабінету</button></div>"
	var base = document.getElementById("base");
	base.innerHTML = html_code;
}

function toPage(url, par){
	//par = _self
	window.open(url, par);
}

function no_questions() {
    var base = document.getElementById("base");
	base.innerHTML = "<h1>No questions:(</h1>";
}



function next_question(){
	var answers = document.getElementsByName("answers");
	var result = false;
	for (var i = 0; i < answers.length; i ++){
		if (answers[i].checked) {
			if (user_answers.length == question_index_ob.index){
			    user_answers.push(i);
			}
			else {
			    console.log(`---=${question_index_ob.index}=---`);
			    user_answers[question_index_ob.index] = i;
			}
			result = true;
			break;
		}
	}
	if (! result) {
	    if (user_answers.length == question_index_ob.index){
			    user_answers.push(-1);
			}
		else {
			user_answers[question_index_ob.index] = -1;
		}
	}
	question_index_ob.index ++;
	if (! set_nth_question(current_pack, question_index_ob.index)){
		    end_test(user_answers);
	}
}

function previous_question(){
    var answers = document.getElementsByName("answers");
	var result = false;
	for (var i = 0; i < answers.length; i ++){
		if (answers[i].checked) {
		    if (user_answers.length == question_index_ob.index){
			    user_answers.push(i);
			}
			else {
			    user_answers[question_index_ob.index] = i;
			}
			result = true;
			break;
		}
	}
	if (! result) {
	    if (user_answers.length == question_index_ob.index){
			    user_answers.push(-1);
			}
			else {
			    user_answers[question_index_ob.index] = -1;
			}
	}
	question_index_ob.index --;
	if (! set_nth_question(current_pack, question_index_ob.index)){
		    alert("Ви вперлися в початок :) Ненада далі");
	}
}

function Pupa(pack){
    alert(pack);
}

function set_pack(name, paisons) {
    pack = new Pack(name, [], paisons)
}


function end_test(array) {
    console.log("sendin...");
	console.log(array);
	$.ajax({
    url: url_end_test,
    type: "POST",
    data: {
    	csrfmiddlewaretoken: csrf_token,
        answers : JSON.stringify(array)
    	},
    success: function(response) {
            toPage(url_view_result);
	    },
    });
    console.log('sended');
}


var index_of_pack = 0;
var question_index_ob = {index: 0};
var user_answers = []
