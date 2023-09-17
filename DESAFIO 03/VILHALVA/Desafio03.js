(function(){
    console.log('Solução do Desafio 03 - imprimir todos os números palindrômicos entre dois outros!');

    Palindromo();

    function Palindromo() {
        var num1 = 1;
        var num2 = 200;

        for(let i = num1; i <= num2; i++) {
            e_Palindromo(i) ? console.log('Palindromo:', i) : null;
        }
    }

    function e_Palindromo(num) {
        if (!num)
            return false;

        let numChar = String(num);
        return numChar === numChar.split('').reverse().join('');
    }

})();