pragma solidity ^0.4.0;
contract rewardusers
{
    address lender = 0xE2836fB7Ad6f59B90CDa462AD277DCc6c880a4f5; //account 1 private key = cf8f826c581699b821738c91fd4918b1041324c0832f2759b7806205da0ff813
    address client = 0x4F9019B3325468D51835A9EB67Cb70877f135a52; //account 2 private key = 6d16fc5815d7086765b823087a962e013093bfcbc8cad50546b0c442b12132ef
    uint total;
    uint min_payment;
    uint payed;
    uint rate;
    uint time_init;
    uint time_last_calc;
    uint hasbeeninitted = 0;

    function initloan(uint _total, uint _min_payment,uint _rate) public
    {
        if((msg.sender == lender) && (hasbeeninitted == 0))
        {
            total = _total;
            min_payment = _min_payment;
            rate = _rate;
            payed = 0;
            time_init = now;
            time_last_calc = time_init;
            hasbeeninitted = 1;
        }
    }
    function makepayment() public payable
    {
        calcinterest();
        total -= msg.value;
        payed += msg.value;
    }
    function calcinterest() public
    {
        uint time_of_calc = now;
        uint time_since_last_payed = time_of_calc - time_last_calc;
        total += (1+rate)**time_since_last_payed;
        time_last_calc = time_of_calc;
    }
    function withdraw() public
    {
        lender.transfer(this.balance);
    }
}
