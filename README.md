# Credential

You will need the credential to access our data. Please email Simon Peter at sp@xerberus.io . 
If you have any questions about the data please email tv@xerberus.io 

# Tables 

## polygon.erc20_network_raw 
This table contains all the ERC20 contracts before the decimal.
However, we only use the subset of the data for our risk ratings. 

### Schemas 
| Columns | Data Type | Desceription                                 | Is_Partition |
| --- | --- |----------------------------------------------|------------|
|token_address | string | ERC20 token address                          | no |
|from_address|string| Address of the sender                        |no|
|to_address|string| Address of the receiver                      |no|
|value|string| Amount of tokens transferred                 |no|
|transaction_hash| string |                                              |no|
|block_timestamp|timestamp| Timestamp of the block where transfer was in |no|
|partition_date|date|                                              |yes|
|last_updated|timestamp| When the data was last created               |no|

## polygon.polygon_network
This is the transaction data
### Schemas
| Columns                     | Data Type | Desceription                                                                                        | Is_Partition |
|-----------------------------|--------|-----------------------------------------------------------------------------------------------------|------------|
| transaction_hash            | string |                                                                                                     |no|
| from_address                | string | Address of sender                                                                                   |no|
| to_address                  | string | Address of receiver                                                                                 |no|
| value                       | NUMERIC| Value transferred in Wei                                                                            |no|
| block_timestamp             | timestamp | Block number where this transaction was in                                                          |no|
| receipt_status              |integer| Either 1 (success) or 0 (failure) (post Byzantium)                                                  |no|
| transaction_type            |integer| Transaction type. One of 0 (Legacy), 1 (Legacy), 2 (EIP-1559)                                       |no|
| receipt_gas_used            |integer| The amount of gas used by this specific transaction alone                                           |no|
| receipt_cumulative_gas_used |integer| The total amount of gas used when this transaction was executed in the block                        |no|
| receipt_effective_gas_price |inteer| The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559 |no|
| gas_price                   |integer| Gas price provided by the sender in Wei                                                             |no|
| address_edge_hash           |bytes| hash address from/to address                                                                        |no|
| transaction_fee             |BIGNUMERIC |                                                                                                     |no|
| partition_date              | date   |                                                                                                     |yes|
| created_dt                  | timestamp | When the data was last created                                                                      |no|
