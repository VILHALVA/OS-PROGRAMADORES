const baseChars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const inputFile = process.argv[2];

if (!inputFile) {
    console.log('Você precisa fornecer um arquivo como argumento, utilize o arquivo teste "baseconv.txt"');
    process.exit(1);
}

const readline = require("readline");
const fs = require("fs");

const lineReader = readline.createInterface({
    input: fs.createReadStream(inputFile)
});

lineReader.on("line", function (line) {
    return console.log(convertFromBaseToBase(line));
});

function convertFromBaseToBase(element) {
    const params = element.split(" ").splice(0, 3);
    const inputBase = params[0];
    const outputBase = params[1];
    const inputNumber = params[2];
    const validationResult = validateInput(inputBase, outputBase, inputNumber);

    if (validationResult === "valid") {
        const numberInDecimal = convertToDecimal(inputBase, inputNumber);
        return convertDecimalToBase(outputBase, numberInDecimal);
    } 
    else {
        return validationResult;
    }
}

function validateInput(inputBase, outputBase, inputNumber) {
    const maxBase = 62;
    const minBase = 2;
    const invalidBases =
        inputBase < minBase || inputBase > maxBase || outputBase < minBase || outputBase > maxBase;
    const negativeNumber = parseInt(inputNumber) < 0;
    let invalidInputNumber = false;
    const validDigitsForInputBase = [...baseChars.slice(0, inputBase)];

    for (let index = 0; index < inputNumber.length; index++) {
        const digit = inputNumber[index];
        const digitBelongsToBase = validDigitsForInputBase.includes(digit);
        if (!digitBelongsToBase) {
            invalidInputNumber = true;
            break;
        }
    }

    if (invalidBases || negativeNumber || invalidInputNumber) {
        return "???";
    }

    const numberInDecimal = convertToDecimal(inputBase, inputNumber);
    const limit = BigInt(
        convertToDecimal(maxBase, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    );

    if (numberInDecimal > limit) {
        return "???";
    }

    if (numberInDecimal === 0n) {
        return "0";
    }

    return "valid";
}

function convertDecimalToBase(outputBase, numberInDecimal) {
    let result = "";
    while (numberInDecimal > 0) {
        const remainder = numberInDecimal % BigInt(outputBase);
        result = baseChars[remainder] + result;
        numberInDecimal = (numberInDecimal - remainder) / BigInt(outputBase);
    }
    return result;
}

function convertToDecimal(inputBase, inputNumber) {
    const baseCharsArray = baseChars.split("");
    let numberInDecimal = 0n;
    let exponent = BigInt(inputNumber.length - 1);

    for (let index = 0; index < inputNumber.length; index++) {
        const digit = inputNumber[index];
        let exponentiatedBase = 1n;

        for (let j = 0; j < exponent; j++) {
            exponentiatedBase *= BigInt(inputBase);
        }

        const digitInDecimal = BigInt(
            baseCharsArray.findIndex((char) => char === digit)
        );

        numberInDecimal += digitInDecimal * exponentiatedBase;
        exponent--;
    }

    return numberInDecimal;
}
