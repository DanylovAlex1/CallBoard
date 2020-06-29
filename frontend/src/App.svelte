<script>
	import FormApp from './FormApp.svelte'

	let subject2='';
	let message2='';
	function print(event){
		subject2 =event.detail.subject;
		message2 =event.detail.message;
	}

</script>

<FormApp on:formMess="{print}"/>

<hr>
<h2>{subject2}</h2>
<p>{message2}</p>