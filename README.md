# Privacy and Data Sovereignty Component
## Description

The Privacy and Data Sovereignty (PDS) component provides mechanisms that allow actors to better control their data, as well as mechanisms that protect clients’ privacy.

In its present form, this component extends the IAA component in the following ways: (i) it enables flexible authorisation server delegation, and (ii) it enables client authentication and authorisation using verifiable credentials (VCs).

### Architecture Overview

The PDS component is composed of 5 sub-scomponents: Client, Smart contracts, IAA blockchain agent, Authorization Server, and IoT platform.

#### Client
This this sub-component includes libraries that can be used by an external client application in order to access a platform using the PDS component. 

#### PDS blockchain agent
Similarly to the [IAA component](https://github.com/SOFIE-project/IAA), this sub-component includes a blockchain agent entity that mediates the communication between the authorisation server (see next), the authorisation delegation smart contract, and the Hyperledger Indy pool

#### Authorization server
This entity is an enhanced version of the [OAuth2 php server](https://github.com/bshaffer/oauth2-server-php). It supports verfiable credentials and access control delegation. 

#### Setup script
The setup script creates configurations that can be used for testing with Hyperledger Indy docker-based testing pool


### Relation with SOFIE

Nore information about this compoment and its relation to the SOFIE project can be found in [D2.5 Federation Framework, SOFIE deliverable](https://media.voog.com/0000/0042/0957/files/SOFIE_D2.5-Federation_Framework%2C_2nd_version.pdf)


### Key Technologies

The following table includes the key technologies used for each sub-component

| Sub-component | Technologies |
| ------------- | ------------- |
| Client  | Hyper Ledger Indy python SDK |
| Smart contracts  | Solidity  |
| PDS blockchain agent  | Hyper Ledger Indy pyhton SDK   |
| Authorization server  | php compatilbe web server, OAuth2 |


## Usage


## Installation
The following instruction have been tested for Ubuntu 18.04
### Prerequisites

#### Client
Python 3 is required

#### PDS blockchain agent
Python 3, Hyperledger Indy SDK, and the python wrapper are required 
* sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE7709D068DB5E88
* sudo add-apt-repository "deb https://repo.sovrin.org/sdk/deb bionic stable"
* sudo apt-get update
* sudo apt-get install -y libindy
* pip3 install install python3-indy


#### Authorization server
The Authorization-server folder should be stored in a web server that supports php and python 3, so it can be accessed over HTTP(s) (NOTE accessing the Authorization server is not secure). For testing purposes the php build-in server can be used. 

#### Setup script


### Configuration



## Testing

To be provided 


## Integration

To be provided.

## Deployment

To be provided.

## Known/Open Issues

No known issues

## Contact info

Please contact Nikos Fotiou or Dimitris Dimopoulos (AUEB) in case of any questions.

***