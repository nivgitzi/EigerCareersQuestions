products = ['eggs', 'milk', 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold = ['eggs', 'eggs', 'cheese', 'milk']
soldPrice = [2.89, 2.99, 5.97, 3.29]


def priceCheck(products, productPrices, productSold, soldPrice):

    dictOfProductPrices = dict(zip(products, productPrices))
    amountOfErrors = 0

    for i in range(len(productSold)):
        if dictOfProductPrices[productSold[i]] != soldPrice[i]:
            amountOfErrors += 1

    return amountOfErrors




print(priceCheck(products, productPrices, productSold, soldPrice))


