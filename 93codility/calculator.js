const operators = ['+', '-', '*', '/'];

function calculate(expression) {
  const operands = [];
  let currentOperand = '';
  let isNegative = false;

  for (const char of expression) {
    if (operators.includes(char) && char !== '-') {
      operands.push(parseFloat(currentOperand));
      currentOperand = '';

      if (isNegative) {
        isNegative = false;
        operators.unshift('-');
      }
    } else if (char === '-') {
      if (currentOperand === '') {
        isNegative = true;
      } else {
        operands.push(parseFloat(currentOperand));
        currentOperand = '-';
      }
    } else {
      currentOperand += char;
    }
  }

  operands.push(parseFloat(currentOperand));

  const mainStack = [];
  const multiplicationDivisionStack = [];

  for (let i = 0; i < operands.length; i++) {
    const operand = operands[i];
    const operator = operators[i];

    if (operator === '+' || operator === '-') {
      mainStack.push(operand);
    } else if (operator === '*' || operator === '/') {
      // Handle multiplication operations within the stack
      if (operator === '*') {
        while (multiplicationDivisionStack.length > 1 &&
              operators.indexOf(multiplicationDivisionStack[multiplicationDivisionStack.length-2]) === operators.indexOf('*')) {
          const rightOperand = multiplicationDivisionStack.pop();
          const leftOperand = multiplicationDivisionStack.pop();
          const operator = operators.shift();

          const result = evaluateOperation(leftOperand, operator, rightOperand);
          multiplicationDivisionStack.push(result);
        }
      }

      // Handle division operations within the stack
      if (operator === '/') {
        while (multiplicationDivisionStack.length > 1 &&
              operators.indexOf(multiplicationDivisionStack[multiplicationDivisionStack.length-2]) === operators.indexOf('/')) {
          const rightOperand = multiplicationDivisionStack.pop();
          const leftOperand = multiplicationDivisionStack.pop();
          const operator = operators.shift();

          const result = evaluateOperation(leftOperand, operator, rightOperand);
          multiplicationDivisionStack.push(result);
        }
      }

      // Push the operand onto the main stack
      mainStack.push(operand);
    } else {
      // Perform multiplication or division operations within the stack
      if (multiplicationDivisionStack.length > 1) {
        const rightOperand = multiplicationDivisionStack.pop();
        const leftOperand = multiplicationDivisionStack.pop();
        const operator = operators.shift();

        const result = evaluateOperation(leftOperand, operator, rightOperand);
        multiplicationDivisionStack.push(result);
      }

      // Push the operand onto the main stack
      multiplicationDivisionStack.push(operand);
    }
  }

  // Handle any remaining multiplication or division operations
  while (multiplicationDivisionStack.length > 1) {
    const rightOperand = multiplicationDivisionStack.pop();
    const leftOperand = multiplicationDivisionStack.pop();
    const operator = operators.shift();

    const result = evaluateOperation(leftOperand, operator, rightOperand);
    multiplicationDivisionStack.push(result);
  }

  // Handle any remaining addition or subtraction
  while (mainStack.length > 1) {
    const rightOperand = mainStack.pop();
    const leftOperand = mainStack.pop();
    const operator = operators.shift();

    const result = evaluateOperation(leftOperand, operator, rightOperand);
    mainStack.push(result);
  }

  // Return the final result
  return mainStack.pop();
}

function evaluateOperation(leftOperand, operator, rightOperand) {
  switch (operator) {
    case '+':
      return leftOperand + rightOperand;
    case '-':
      return leftOperand - rightOperand;
    case '*':
      return leftOperand * rightOperand;
    case '/':
      return leftOperand / rightOperand;
  }
}

console.log(calculate('+ 3 4')); // Output: 7
console.log(calculate('- 3 * 4 5')); // Output: -7
console.log(calculate('* + 3 4 5')); // Output: 35
console.log(calculate('/ - 3 4 + 5 2')); // Output: -2.5
