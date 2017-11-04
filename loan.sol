contract loanterms
{
    address lender = 0xE2836fB7Ad6f59B90CDa462AD277DCc6c880a4f5; //account 1 private key = cf8f826c581699b821738c91fd4918b1041324c0832f2759b7806205da0ff813
    address client = 0x4F9019B3325468D51835A9EB67Cb70877f135a52; //account 2 private key = 6d16fc5815d7086765b823087a962e013093bfcbc8cad50546b0c442b12132ef
    uint total; //total balance of loan
    uint min_payment; //minimum payment per payment cycle
    uint payed; //total amount which the client has payed
    uint rate; //interest rate of the loan
    uint time_init; //time when contract was initiated
    uint time_last_calc; //time when interest was calculated last
    uint hasbeeninitted = 0; //flag for loan having terms set
    bool is_defunct; //flag for delinquent loans
    bool fullypaid; //flag for fully paid
    address swapaddresslender; //address of loan with new terms approved by lender
    address swapaddressclient; //address of loan with new terms approved by client
    bool stillactive = 0;
    function initloan(uint _total, uint _min_payment,uint _rate) public
    {//initialize loan
        if((msg.sender == lender) && (hasbeeninitted == 0))
        {
            total = _total;
            min_payment = _min_payment;
            rate = _rate;
            payed = 0;
            time_init = now;
            time_last_calc = time_init;
            hasbeeninitted = 1;
            is_defunct = 0;
            fullypaid = 0;
            swapaddresslender = this;
            swapaddressclient = this;
            stillactive = 1;
        }
    }
    function makepayment() public payable
    {//function for the client to approve the payment
        calcoverdue()
        calcinterest();
        total -= msg.value;
        payed += msg.value;
        if (total <= 0)
        {
            msg.sender.transfer(-1*total);//shoot any extra ethereum back to the payer
            fullypaid = 1;
            stillactive = 0;
        }
    }
    function calcinterest() public
    {//determine the interest which has accrued and add it to the total value of the loan
        uint time_since_last_payed = now - time_last_calc;
        total += (1+rate)**time_since_last_payed; //TODO: make noninteger shit work
        time_last_calc = now;
    }
    function withdraw() public
    {//transfer the paid balance of the loan to the bank
        lender.transfer(this.balance);
    }
    function calcoverdue() public
    {//determine whether the  loan is overdue
        uint time_active = now - time_init
        if (payed/time_active < min_payment)
        {//if they have averaged less than the required payment, fuck them up
            is_defunct = 1;
        }
    }
    function swapterms()//if both lender and client approve switching the terms, do it
    {//TODO: set up functions for lender and client to switch their approval
        if ((swapaddresslender == swapaddressclient) && (swapaddresslender != this))
        {
            active = 0;
        }   
    }
}
