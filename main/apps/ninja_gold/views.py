from django.shortcuts import render, redirect, HttpResponse
from random import randint

def index(request):
	if 'money' not in request.session:
		request.session['money'] = 0
	if 'transactions' not in request.session:
		request.session['transactions'] = []
	return render(request, "index.html")

def farm(request):
	cash = randint(10, 21)
	request.session['money'] += cash
	temp_list = request.session['transactions']
	temp_list.append("You won: $" + str(cash))
	request.session['transactions'] = temp_list
	print (request.session['transactions'])
	return redirect(index)

def cave(request):
	cash = randint(5, 11)
	request.session['money'] += cash
	temp_list = request.session['transactions']
	temp_list.append("You won: $" + str(cash))
	request.session['transactions'] = temp_list
	return redirect(index)

def house(request):
	cash = randint(2, 6)
	request.session['money'] += cash
	temp_list = request.session['transactions']
	temp_list.append("You won: $" + str(cash))
	request.session['transactions'] = temp_list
	return redirect(index)

def casino(request):
	cash = randint(-50, 51)
	request.session['money'] += cash
	temp_list = request.session['transactions']
	if cash < 0:
		temp_list.append("You lost: $" + str(cash))
	else:
		temp_list.append("You won: $" + str(cash))
	request.session['transactions'] = temp_list
	return redirect(index)