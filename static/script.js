console.log('hello world');

function timelock(){
    document.getElementById('donebtn').disabled = false;
}

// apply to every model
$(document).ready(function() {
    $('.modal_appear').click(function() {
        $('#exampleModalCenter').modal({
            backdrop: 'static',
            keyboard: false
        });
    });
});

// setting default attribute of minus
document.querySelector('.minus_btn').setAttribute('disabled','disabled'); 
// increment / decrement Work
// complete flow
// starting by declaring variable
var valueCount 

var price = document.getElementById('price').innerText = 0;
// social condition
function amountTotal() {
    var total = valueCount * 1.20;
    document.getElementById('price').innerText = total 
}
// view condition
function amountTotal2() {
  var total = valueCount * 2;
  document.getElementById('price').innerText = total 
}

var accValue = socialAcc(x);    //social account
var amount = changeAmount(y);   // amount selected

function changeAmount(y) {
  var count = y.value;
  if(count != null){
    var getAccount = accValue;

    if(getAccount == "Youtube Views"){
      var parseCount = Number(count);
      var calTotal = parseCount * 2;
      document.getElementById('amount').innerText = calTotal;
      console.log("hurray");
      console.log(calTotal);
    }
    else if(getAccount == "Instagram Likes"){
     var parseCount = Number(count);
     var calTotal = parseCount * 1.20;
     console.log(calTotal);
     document.getElementById('amount').innerText = calTotal;
    }
    else if(getAccount == "Facebook Likes"){
      var parseCount = Number(count);
      var calTotal  = parseCount * 1.20;
      console.log(calTotal);
      document.getElementById('amount').innerText = calTotal;
    }
    else if(getAccount == "Instagram Followers"){
      var parseCount = Number(count);
      var calTotal  = parseCount * 1.20;
      console.log(calTotal);
      document.getElementById('amount').innerText = calTotal;
    }
    else if(getAccount == "Youtube Subscribers"){
      var parseCount = Number(count);
      var calTotal  = parseCount * 1.20;
      console.log(calTotal);
      document.getElementById('amount').innerText = calTotal;
    }

  }
  
}

function socialAcc(x) {
  accValue = x.value;
  var getAmount = amount;
  if(getAmount == null){
    console.log("value not selected yet");
    document.getElementById('amount').innerText = "";
  }
}

//condition check to apply
function yesnoCheck1() {
  if (document.getElementById("yesCheck1").selected) { 
    amountTotal2()
    } else {
    amountTotal()
  }
}
// increment value
document.querySelector('.plus_btn').addEventListener('click', function() {
  valueCount = document.getElementById('quantity').value;
  var test = parseInt(valueCount);
  test+=5;
  document.getElementById('quantity').value = test;

  if(test >= 1000) {
      document.querySelector('.plus_btn').setAttribute('disabled','disabled');
  }
  if (test >= 50) {
      document.querySelector('.minus_btn').removeAttribute('disabled');
      document.querySelector('.minus_btn').classList.remove('disabled');
  }
  // calling amount function
  yesnoCheck1()
})

// increment value 50
  document.querySelector('.btn_plus50').addEventListener('click', function() {
  valueCount = document.getElementById('quantity').value;
  var test = parseInt(valueCount);
  test+=50;
  document.getElementById('quantity').value = test;

  if(test > 950 && test <= 1000) {
      document.querySelector('.btn_plus50').setAttribute('disabled','disabled');
  }
  if (test >= 100) {
      document.querySelector('.minus_btn50').removeAttribute('disabled');
      document.querySelector('.minus_btn50').classList.remove('disabled');
  }
  // calling amount function
  yesnoCheck1()
})

// decrement value
document.querySelector('.minus_btn').addEventListener('click',function() {
  valueCount = document.getElementById('quantity').value;
  var test= parseInt(valueCount);
  test-=5;
  document.getElementById('quantity').value = test;

  if(test <=50){
    test=50;
    console.log(test);
    valueCount=test
     console.log(valueCount)
     document.querySelector('.minus_btn').setAttribute('disabled','disabled');
  }
  if (test < 1000) {
      document.querySelector('.plus_btn').removeAttribute('disabled');
      document.querySelector('.plus_btn').classList.remove('disabled')
  }
  // calling amount function
  yesnoCheck1()
})
