function Pack (name, questions, paisons) {
	this.name = name;
	this.questions = questions;
	this.paisons = paisons;
}

function TestQuestion (question, answers, index_of_correct){
	this.question = question;
	this.answers = answers;
	this.index_of_correct = index_of_correct;
}


var packs = [];
var variables_pack = new Pack("Variables", 
						  [new TestQuestion("Що поверне наступна програма?<br/>a = 3<br/>print(a + a * a)",
						  					["3", "5", '12', "18"], 2),
						   new TestQuestion("Що поверне наступна програма?<br/>a = 1<br/>b = 2<br/>print(a + b + 1)",
						   					["2", "4", "1", "3"], 1),
						   new TestQuestion("Що поверне наступна програма?<br/>a = 'lol'<br/>b = 'kek'<br/>print(a + 'b' + '1')",
						   					["lolkek1", "lolkek", "Error", "lolb1", "ab1"], 3),
						  ],
						  30
						  );
packs.push(variables_pack);


function set_nth_pack(packs, n){
	var pack = packs[n];
	set_nth_question(pack, 0);
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

var index_of_pack = 0;
var question_index_ob = {index: 0};
var user_answers = []
set_nth_pack(packs, index_of_pack);


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
		var pack = packs[index_of_pack];
		question_index_ob.index ++;
		if (! set_nth_question(pack, question_index_ob.index)){
			print_result(pack, user_answers);
		}
	} else {
		console.log('Nope. Answer please');
	}
}
