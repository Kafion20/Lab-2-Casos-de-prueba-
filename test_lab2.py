import ecommerce_form
import logging
import pytest

logging.basicConfig(
    level = logging.DEBUG,
    filemode = "w",
    filename = "test.log"
)


@pytest.fixture 
def system():
    return ecommerce_form.OnlinePurchase()


@pytest.mark.parametrize('quantity,expected',[
(8,True),
(0,False),
(-1,False),
(0.25,False)
])
@pytest.mark.unit
def test_validate_quantity_components(system,quantity,expected):
    result = system.validate_quantity(quantity)
    assert result == expected
    



@pytest.mark.parametrize('coupon,expected',[
('DISCOUNT10',True),
('DISCOUNT20',True),
('DISCOUNT30',False),
('DISCOUNT40',False)
])
@pytest.mark.unit
def test_validate_quantity_components(system,coupon,expected):
    result = system.validate_coupon(coupon)
    assert result == expected




@pytest.mark.parametrize('address,expected',[
('Av patria',True),
('dos',False),
('12345678',False)
])
@pytest.mark.wip
def test_validate_quantity_components(system,address,expected):
    result = system.validate_address(address)
    assert result == expected






@pytest.mark.system
def test_purchase_itemzero(system):
    logging.info("test case 1")
    #system = ecommerce_form.OnlinePurchase()
    cart ={
        'Laptop': 0,
        'Mouse' : 2
    }
    coupon = 'DISCOUNT10'
    address = 'Av patria'
    result = system.process_purchase(cart, coupon, address)
    logging.info(f'The result of purchase is :{result}')
    assert 'integer greater than 0' in result
    logging.info('test case finished ')


@pytest.mark.system
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

@pytest.mark.system
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
    test_invalid_coupon()
    
    logging.info(f'The purchase result: ' )