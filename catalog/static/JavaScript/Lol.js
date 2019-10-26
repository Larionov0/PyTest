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
	if (n >= pack.questions.length) {
		return false;
	}
	document.getElementById('question').innerHTML = pack.questions[n].question;
	var html_code = "";
	var answers = pack.questions[n].answers;
	for (i in answers){
		html_code += `<input type="radio" name="answers">${answers[i]}`;
	}
	var form = document.getElementById('answer_form');
	form.innerHTML = "";
	form.insertAdjacentHTML('afterbegin', html_code);
	return true
}


function print_result(pack, answers){

    end_test(answers);
    return true;

	var result_array = [];
	var test_passed = true
	var res = false;
	for (var i = 0; i < answers.length; i ++){
		res = answers[i] == pack.questions[i].index_of_correct
		result_array.push(res);
		if (! res) {
			test_passed = false;
		}
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
	html_code += "<div class = 'center'><button id='PassTest_button' onclick='toPage(\"MyCabinet_page.html\", \"_self\")'>До Мого Кабінету</button></div>"
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

var index_of_pack = 0;
var question_index_ob = {index: 0};
var user_answers = []



function next_question(){
	var answers = document.getElementsByName("answers");
	var result = false;
	for (var i = 0; i < answers.length; i ++){
		if (answers[i].checked) {
			user_answers.push(i);
			result = true;
			break;
		}
	}
	if (result) {
		question_index_ob.index ++;
		if (! set_nth_question(current_pack, question_index_ob.index)){
			print_result(current_pack, user_answers);
		}
	} else {
		console.log('Nope. Answer please');
	}
}

function Pupa(pack){
    alert(pack);
}

function set_pack(name, paisons) {
    pack = new Pack(name, [], paisons)
}


