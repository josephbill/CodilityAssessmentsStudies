const assert = require('chai').assert;
const calculator = require('../calculator');

describe('Calculator', function () {
    it('should calculate expressions in alternative notation', function () {
        // Test cases
        assert.equal(calculator.calculate('+ 3 4'), 7);
        assert.equal(calculator.calculate('- 3 * 4 5'), -17);
        assert.equal(calculator.calculate('* + 3 4 5'), 35);
        assert.equal(calculator.calculate('/ - 3 4 + 5 2'), -1);
    });

    // Add more test cases as needed
});
