  function showhideSignup()
	{
		if(document.getElementById("signup").style.display==='none')
		{
			document.getElementById('signup').style.display = 'block';
			document.getElementById('login').style.display = 'none';
			document.getElementById('foo').innerHTML="Log In";
		}
		else
		{
			document.getElementById('signup').style.display = 'none';
			document.getElementById('login').style.display = 'block';
			document.getElementById('foo').innerHTML="Sign Up";
			}	
	}