import ecommerce_form
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filemode = "w",
    filename = "test.log"
)

def test_purchase_itemzero():
    logging.info("test case 1")
    system = ecommerce_form.OnlinePurchase()
    cart ={
        'Laptop': 0,
        'Mouse' : 2
    }
    coupon = 'DISCOUNT10'
    address = 'Av patria'
    result = system.process_purchase(cart, coupon, address)
        
    assert 'integer greater than 0' in result
    logging.info('test case finished ')


def test_invalid_coupon():
    logging.info('test case 2')
    system = ecommerce_form.OnlinePurchase()
    cart ={
            'Laptop': 1,
            'Mouse' : 2
        }
    coupon = 'DISCOUNT30'
    address = 'Av patria'
    result = system.process_purchase(cart, coupon, address)
    assert 'coupon code is not valid' in result
    logging.info(f'The result of purchase is :{result}')
    logging.info('test case finished')

def test_coupon_valid():
    logging.info('test case 9')
    system = ecommerce_form.OnlinePurchase()
    cart ={
                'Laptop': 1,
                'Mouse' : 2
            }
    coupon = 'DISCOUNT10'
    address = 'Av patria'
    result = system.process_purchase(cart, coupon, address)
    assert 'DISCOUNT10' in result
    assert '990' in result
    logging.info(f'The result of purchase is :{result}')
    logging.info('test case finished')
    
    
if __name__ == "__main__":
    test_coupon_valid()
    
    logging.info(f'The purchase result: ' )