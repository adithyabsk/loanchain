pragma solidity ^0.4.0;
contract loanterms
{
    address lender;
    address ratesource; 
    uint total; //total balance of loan
    uint min_payment; //minimum payment per payment cycle
    uint maturity; //time allowed to payoff loan
    uint payed; //total amount which the client has payed
    uint rate; //interest rate of the loan*1000
    uint time_init; //time when contract was initiated
    uint time_last_calc; //time when interest was calculated last
    bool hasbeeninitted = false; //flag for loan having terms set 
    //bool is_defunct; //flag for delinquent loans
    bool fullypaid; //flag for fully paid
    address swapaddresslender; //address of loan with new terms approved by lender
    address swapaddressclient; //address of loan with new terms approved by client
    bool stillactive = false;
    uint ratescale = 10000;
    mapping(address => bool) votes;
    bool needsupdate = false;
    uint Aproposed = 0;
    uint yesvotes = 0;
    uint shouldbepayed;
    function loanterms(uint _total, uint _maturity, address _ratesource)
    {
        lender = msg.sender;
        maturity = _maturity;
        total = _total;
        ratesource = _ratesource;
        determinerate ratefinder = determinerate(ratesource);
        rate = ratefinder.getrate();
        payed = 0;
        shouldbepayed = 0;
    }
    /*
    function setminpayment(uint A)
    {
        shouldbepayed += min_payment * cyclelength;
        min_payment = A;
    }
    */
    function makepayment() public payable
    {//function for the client to approve the payment
        total -= msg.value;
        payed += msg.value;
    }   
    function calcinterest() 
    {//determine the interest which has accrued and add it to the total value of the loan
        determinerate ratefinder = determinerate(ratesource);
        rate = ratefinder.getrate();
        uint time_since_last_payed = 5;
        uint256 num = (ratescale + rate)**(time_since_last_payed);
        uint256 denom = ratescale**(time_since_last_payed);
        total = (total*num)/denom;
    }   
    function withdraw()
    {//transfer the paid balance of the loan to the bank
        lender.send(this.balance);
    }   
    function viewbalance() returns (uint remainingbalance)
    {
        return total;
    }
}
contract determinerate
{
    address[] trustedbanks = [0xca35b7d915458ef540ade6068dfe2f44e8fa733c,0x8D7D242D87fb67Ad22bFCF0e4D10933d4dC8F700,0x770a05A923D2F22603CC1897660963D1B078B731];
    uint rate;
    function setrate(uint _rate)
    {
        bool trusted = false;
        for (uint i = 0; i < trustedbanks.length; i++)
        {
            if(trustedbanks[i] == msg.sender)
            {
                trusted = true;
            }
        }
        if(trusted)
        {
            rate = _rate;
        }
    }
    function getrate() returns (uint intrate)
    {
        return rate;
    }

}
