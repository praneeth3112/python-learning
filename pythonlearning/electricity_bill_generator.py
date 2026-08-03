name = str(input('enter the name of the customer : '))
customer_ID = str(input('enter the customer id : '))
previous_meter_reading = float(input('enter the previous meter reading : '))
current_meter_reading = float(input('enter the current meter reading : '))
if current_meter_reading > previous_meter_reading:
    total_units_consumed = current_meter_reading - previous_meter_reading
    cost_per_unit = float(input('enter the cost per unit : '))
    energy_charge = total_units_consumed * cost_per_unit
    electrical_duty = 0.05 * energy_charge
    fixed_meter_charge = 100
    net_bill = energy_charge + electrical_duty + fixed_meter_charge
    print(f'name of the customer is {name}')
    print(f'customer id is {customer_ID}')
    print(f'total units consumed are {total_units_consumed}')
    print(f'energy charge is {energy_charge}')
    print(f'electrical duty is {electrical_duty}')
    print(f'fixed meter charge is {fixed_meter_charge}')
    print(f'net bill is {net_bill}')
else :
    print('error: current meter reading should be greater than previous meter reading')