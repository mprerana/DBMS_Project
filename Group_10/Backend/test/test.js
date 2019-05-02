var assert = require('assert')
var token2id = require('../auth/token2id')
const chai = require('chai')
const expect = chai.expect
chai.use(require('chai-as-promised'))


describe("Auth", function () {
  describe("#token2id", function () {
    it('Should give the correct id from JWT token', async function () {
      let token = await token2id("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNTU2Njk0MTMyLCJleHAiOjE1NTY3ODA1MzJ9.HiQ8W8gmYLEb6dsclFGtKyQcEzbR_rWDuiTZEi8IqBA")
      assert.equal(token, 1)
    })
    it('Should throw error on incorrect JWT', async function () {
      let token = "jidasdasdas"
      await expect(token2id(token)).to.be.rejectedWith(Error)
    })
  })
})