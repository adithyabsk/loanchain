# Loanchain
## A Dynamic Smart Contract Generator for Loans to be Securely Deployed on the Blockchain
Loanchain is a lending system embedded in the Ethereum blockchain which offers unparalleled transparency of and control over loan agreements for both financial institutions and borrowers.
Loanchain leverages the power of decentralized computing to allow consumers and banks to hold each other accountable in a publicly available ledger.
## Inspiration
In the Summer of 2017, Well's Fargo illegally changed the terms of many of its customers' loans.
This is just one of many cases of consumers' being tricked by the inaccessability of information on their loans and financial instruments.
Loanchain seeks to remedy this problem by creating a ledger of loan terms available to both parties.
## What is Blockchain?
Blockchain is a decentralized ledger which records data in a publicly available unalterable format.
Information stored in blockchain can be viewed by anyone, and cannot be changed.
## What is Ethereum?
Unlike its predecessors, such as bitcoin, Ethereum allows users to store complex financial agreements, called Smart Contracts, in the blockchain.
This allows institutions to publish financial instruments which are fully transparent and cryptographically secure.
## What It Does
Our project publishes the terms of financial agreements between banks and consumers to the blockchain.
This allows both parties to view all of the terms of their agreement in an explicit, easy to read format.
This would make financial fraud significantly more difficult for major institutions, protecting average consumers.
## How We Built It
Our project is divided into several parts, at its core, it is a system for generating smart contracts which conform to standard financial practices.
These smart contracts are deployed by banks onto the blockchain using the web3py library.
These smart contracts were deployed for testing purposs on a local ethereum network, hosted on an Amazon AWS server. 
These smart contracts are accessed by an easy to use wrapper which is accessible to the average consumer using CapitalOne's loan access API.
## Future Work
We would like to expand the financial instruments which can be encoded into the blockchain through our system.
