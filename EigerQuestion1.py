

def priceCheck(products, productPrices, productSold, soldPrice):

    dictOfProductPrices = dict(zip(products, productPrices))
    amountOfErrors = 0

    for i in range(len(productSold)):
        if dictOfProductPrices[productSold[i]] != soldPrice[i]:
            amountOfErrors += 1

    return amountOfErrors





