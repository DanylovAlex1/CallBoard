<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	let subject='';
	let message='';
	$: test=subject+' '+message
	function sendForm(){
		dispatch('formMess',{
			subject:'Тестовый сабдж',
			message:'Тестовое месс'
		});
	}

</script>


<form>
	<input type="text" name='subject' bind:value={subject}>
	<input type="text" name='message' bind:value={message}>
	<button type="button" on:click="{sendForm}">send</button>
</form>

<p>{test}</p>


<style>
	main {
		text-align: center;
    	padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
        color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
