portfolioEntity={
    "ticker":str,
    "quantity":int,
}
order={
    "ticker": str,
    "atPrice": float,
    "change":int
}
trade={
    "date": str,
    "orders":[
        order   
    ]
}
money={
        "allotedFunds":int,
        "currency":str,
    }
schema={
    "username":str,
    "name": str,
    "password": str,
    "email":str,
    #"role": str,
    "netProfits":[money],
    "funds":[money],
    "portfolio":
        [
        portfolioEntity
    ],
    "trades":
        [
            trade
        ]
    
        
}