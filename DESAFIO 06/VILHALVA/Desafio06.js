const { readFileSync } = require('fs');
const file = process.argv[2];
const wordsFileContent = readFileSync(file, 'utf-8');

const validWords = wordsFileContent.split('\n').filter((word) => {
  return word;
});

const userInput = process.argv[3];

function validateUserInput(userWord) {
  const pattern = /^[A-Za-z_]+$/;

  if (pattern.test(userWord)) {
    userWord = userWord.toUpperCase().split('').filter((char) => {
      return char !== '_';
    });
    if (userWord.length <= 16) {
      return userWord;
    } 
    else {
      console.log('ERRO! Palavra inválida: limite de caracteres excedido!');
    }

  } 
  else {
    console.log('ERRO: Palavra inválida: contém caracteres não permitidos!');
    return false;
  }
}

function removeInvalidWords(userWord, wordsList) {
  let validWordsList = wordsList.filter((word) => {
    let newUserWord = [...userWord];
    if (typeof word === 'string') {
      word = word.split('');
    }

    for (const letter of word) {
      if (!newUserWord.includes(letter)) {
        return false;
      }
      else {
        newUserWord.splice(newUserWord.indexOf(letter), 1);
      }
    }
    return word;
  });

  return validWordsList;
}

function removeWordFromUserInput(userWord, word) {
  for (const letter of word) {
    userWord.splice(userWord.indexOf(letter), 1);
  }
}

function buildAnagrams(userWord, wordsList, anagram) {
  let word = wordsList.shift();

  anagram = [...anagram, word];
  let newWordsList = [...wordsList];
  let newUserWord = [...userWord];

  removeWordFromUserInput(newUserWord, word);
  newWordsList = removeInvalidWords(newUserWord, newWordsList);

  if (newUserWord.length === 0) {
    return anagram;
  }
  else {
    let sizeWordsList = newWordsList.length;
    for (let i = 0; i < sizeWordsList; i++) {
      let isAnagram = buildAnagrams(newUserWord, newWordsList, anagram);
      if (isAnagram) {
        isAnagram = isAnagram.join(' ');
        console.log(isAnagram);
      }
    }
  }
}

function solveAnagrams(userWord, wordsList) {
  wordsList = removeInvalidWords(userWord, wordsList);

  let sizeWordsList = wordsList.length;
  for (let i = 0; i < sizeWordsList; i++) {
    let anagram = [];
    buildAnagrams(userWord, wordsList, anagram);
  }
}

function main() {
  const userWord = validateUserInput(userInput);
  if (userWord) {
    solveAnagrams(userWord, validWords);
  }
}

main();
